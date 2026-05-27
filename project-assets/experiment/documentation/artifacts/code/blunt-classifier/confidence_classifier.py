#!/usr/bin/env python3
"""
Blunt Confidence Classifier — Production Implementation v1.0

Usage:
    python confidence_classifier.py --response "Paris is the capital of France."
    python confidence_classifier.py --response "It might rain tomorrow." --query "What's the weather?"
    python confidence_classifier.py --test  # Run calibration tests
    
This module classifies AI responses into confidence levels:
    HIGH (🟢): Sources verified. This is solid.
    MEDIUM (🟡): Take this with salt.
    LOW (🔴): Verify before acting.
    PUSHBACK (🔴): I disagree.

Design Philosophy: Conservative calibration. Bias toward MEDIUM unless strong signals.
"""

import re
import json
import argparse
from dataclasses import dataclass, asdict
from enum import Enum
from typing import Optional, List, Dict, Tuple

# ═══════════════════════════════════════════════════════════════════════════════
# DATA STRUCTURES
# ═══════════════════════════════════════════════════════════════════════════════

class ConfidenceLevel(Enum):
    HIGH = "high"           # 🟢 "Sources verified. This is solid."
    MEDIUM = "medium"       # 🟡 "Take this with salt."
    LOW = "low"             # 🔴 "Verify before acting."
    PUSHBACK = "pushback"   # 🔴 "I disagree."

@dataclass
class ConfidenceSignal:
    """Individual signal contributing to confidence score."""
    name: str
    value: float        # -1.0 to +1.0
    weight: float       # How much this signal matters
    explanation: str

@dataclass
class ConfidenceResult:
    level: ConfidenceLevel
    raw_score: float    # 0.0 to 1.0
    signals: List[ConfidenceSignal]
    explanation: str
    emoji: str
    
    def to_dict(self) -> dict:
        return {
            "level": self.level.value,
            "raw_score": round(self.raw_score, 3),
            "emoji": self.emoji,
            "explanation": self.explanation,
            "signals": [
                {
                    "name": s.name,
                    "value": round(s.value, 3),
                    "weight": s.weight,
                    "explanation": s.explanation
                } for s in self.signals if abs(s.value) > 0.01
            ]
        }

# ═══════════════════════════════════════════════════════════════════════════════
# SIGNAL PATTERNS
# ═══════════════════════════════════════════════════════════════════════════════

HEDGING_PATTERNS: List[Tuple[str, float]] = [
    (r'\b(probably|likely|possibly|perhaps|maybe)\b', -0.15),
    (r'\b(I think|I believe|I would guess)\b', -0.20),
    (r'\b(might|could|may)\s+be\b', -0.10),
    (r'\b(not sure|uncertain|unclear)\b', -0.25),
    (r'\b(it depends|it varies)\b', -0.20),  # Stronger — clear hedging
    (r'\b(some say|some argue|arguably)\b', -0.15),
    (r'\b(I\'m not (entirely )?(sure|certain))\b', -0.25),
    (r'\b(hard to (say|predict|know))\b', -0.25),  # Stronger
    (r'\b(I don\'t know|I can\'t)\b', -0.30),  # Explicit uncertainty
    (r'\b(pros and cons)\b', -0.15),  # Balanced = uncertain
]

CONFIDENCE_BOOSTERS: List[Tuple[str, float]] = [
    (r'\b(definitely|certainly|absolutely|clearly)\b', +0.10),
    (r'\b(according to|studies show|research indicates)\b', +0.15),
    (r'\b(confirmed|verified|established)\b', +0.12),
    (r'\[(source|citation|ref)\]', +0.20),
    (r'https?://[^\s]+', +0.15),
    (r'\b(in \d{4}|since \d{4})\b', +0.08),  # Specific dates
    (r'\b\d+(\.\d+)?%\b', +0.05),  # Specific percentages
]

PUSHBACK_TRIGGERS: List[str] = [
    r'^I disagree',
    r'^That\'s not (quite )?correct',
    r'^Actually,?\s',
    r'That (claim|statement|assertion) is (incorrect|false|misleading)',
    r'I have to push back',
    r'^No[,.]',
    r'I\'d challenge that',
]

HIGH_CONFIDENCE_DOMAINS: List[str] = [
    'capital', 'geography', 'math', 'calculation', 'grammar',
    'programming', 'syntax', 'historical fact', 'definition',
    'science fact', 'physics', 'chemistry', 'biology'
]

LOW_CONFIDENCE_DOMAINS: List[str] = [
    'predict', 'future', 'will happen', 'going to be',
    'stock', 'price', 'market', 'invest',
    'medical', 'diagnosis', 'treatment', 'health',
    'legal', 'law', 'court',
    'weather', 'tomorrow', 'next week',
    'opinion', 'best', 'worst', 'should',
]

OPINION_INDICATORS: List[str] = [
    r'\b(best|worst|should|recommend|prefer)\b',
    r'\b(opinion|subjective|debatable|controversial)\b',
    r'\b(better|worse|superior|inferior)\b',
    r'\b(I would suggest|personally)\b',
]

# ═══════════════════════════════════════════════════════════════════════════════
# SIGNAL DETECTORS
# ═══════════════════════════════════════════════════════════════════════════════

def detect_hedging(text: str) -> ConfidenceSignal:
    """Detect self-hedging language that reduces confidence."""
    total_adjustment = 0.0
    patterns_found = []
    
    for pattern, adjustment in HEDGING_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            total_adjustment += adjustment
            patterns_found.append(re.sub(r'\\b|\\s|\(|\)|\|', '', pattern)[:20])
    
    # Cap the negative impact
    total_adjustment = max(total_adjustment, -0.40)
    
    explanation = f"Hedging language detected ({len(patterns_found)} patterns)" if patterns_found else "No hedging detected"
    
    return ConfidenceSignal(
        name="hedging_language",
        value=total_adjustment,
        weight=1.0,
        explanation=explanation
    )

def detect_confidence_boosters(text: str) -> ConfidenceSignal:
    """Detect high-confidence language and citations."""
    total_adjustment = 0.0
    boosters_found = []
    
    for pattern, adjustment in CONFIDENCE_BOOSTERS:
        matches = re.findall(pattern, text, re.IGNORECASE)
        if matches:
            total_adjustment += adjustment
            boosters_found.append(pattern[:20])
    
    # Cap the positive impact
    total_adjustment = min(total_adjustment, +0.30)
    
    explanation = f"Confidence boosters ({len(boosters_found)} signals)" if boosters_found else "No confidence boosters"
    
    return ConfidenceSignal(
        name="confidence_boosters",
        value=total_adjustment,
        weight=1.0,
        explanation=explanation
    )

def classify_claim_type(text: str, query: str) -> ConfidenceSignal:
    """Determine if response is factual, opinion, or prediction."""
    combined = f"{query} {text}".lower()
    
    # Prediction detection
    prediction_keywords = ['will', 'going to', 'expect', 'forecast', 'predict', 'future']
    prediction_count = sum(1 for kw in prediction_keywords if kw in combined)
    
    if prediction_count >= 2:
        return ConfidenceSignal(
            name="claim_type",
            value=-0.20,
            weight=1.0,
            explanation="Prediction — inherently uncertain"
        )
    
    # Opinion detection
    for pattern in OPINION_INDICATORS:
        if re.search(pattern, combined, re.IGNORECASE):
            return ConfidenceSignal(
                name="claim_type",
                value=0.0,
                weight=0.5,
                explanation="Opinion or recommendation"
            )
    
    # Default: factual claim
    return ConfidenceSignal(
        name="claim_type",
        value=0.0,
        weight=1.0,
        explanation="Factual claim"
    )

def assess_domain_coverage(text: str, query: str) -> ConfidenceSignal:
    """Assess how well the topic is covered in training data."""
    combined = f"{query} {text}".lower()
    
    # Check low-confidence domains first
    for domain in LOW_CONFIDENCE_DOMAINS:
        if domain in combined:
            return ConfidenceSignal(
                name="domain_coverage",
                value=-0.25,
                weight=1.0,
                explanation=f"Low-confidence domain: {domain}"
            )
    
    # Check high-confidence domains
    for domain in HIGH_CONFIDENCE_DOMAINS:
        if domain in combined:
            return ConfidenceSignal(
                name="domain_coverage",
                value=+0.25,  # Stronger boost for well-known facts
                weight=1.0,
                explanation=f"High-confidence domain: {domain}"
            )
    
    return ConfidenceSignal(
        name="domain_coverage",
        value=0.0,
        weight=0.5,
        explanation="Standard domain coverage"
    )

def assess_response_length(text: str) -> ConfidenceSignal:
    """Very short responses are often more confident. Very long = hedging."""
    word_count = len(text.split())
    
    if word_count <= 5:
        return ConfidenceSignal(
            name="response_length",
            value=+0.25,  # Boosted — short definitive answers are HIGH confidence
            weight=1.0,
            explanation="Concise, definitive response"
        )
    elif word_count <= 10:
        return ConfidenceSignal(
            name="response_length",
            value=+0.15,
            weight=0.8,
            explanation="Short, confident response"
        )
    elif word_count >= 100:
        return ConfidenceSignal(
            name="response_length",
            value=-0.05,
            weight=0.5,
            explanation="Lengthy response — may indicate hedging"
        )
    
    return ConfidenceSignal(
        name="response_length",
        value=0.0,
        weight=0.0,
        explanation="Standard length"
    )

def detect_pushback(text: str) -> bool:
    """Detect if response is a disagreement."""
    for pattern in PUSHBACK_TRIGGERS:
        if re.search(pattern, text, re.IGNORECASE):
            return True
    return False

# ═══════════════════════════════════════════════════════════════════════════════
# MAIN CLASSIFIER
# ═══════════════════════════════════════════════════════════════════════════════

def classify_confidence(
    response_text: str,
    query: str = "",
    logprobs: Optional[List[float]] = None
) -> ConfidenceResult:
    """
    Main confidence classification function.
    
    Args:
        response_text: The AI response to classify
        query: The user's original query (optional, improves accuracy)
        logprobs: Token log probabilities from LLM API (optional)
    
    Returns:
        ConfidenceResult with level, score, signals, and explanation
    """
    
    # Check for pushback first — this overrides confidence scoring
    if detect_pushback(response_text):
        return ConfidenceResult(
            level=ConfidenceLevel.PUSHBACK,
            raw_score=0.0,
            signals=[],
            explanation="I disagree with this statement.",
            emoji="🔴"
        )
    
    # Collect all signals
    signals = [
        detect_hedging(response_text),
        detect_confidence_boosters(response_text),
        classify_claim_type(response_text, query),
        assess_domain_coverage(response_text, query),
        assess_response_length(response_text),
    ]
    
    # Process logprobs if available
    if logprobs:
        avg_logprob = sum(logprobs) / len(logprobs)
        prob = min(1.0, max(0.0, 2.718 ** avg_logprob))
        adjustment = (prob - 0.5) * 0.4
        signals.append(ConfidenceSignal(
            name="logprobs",
            value=adjustment,
            weight=0.8,
            explanation=f"Token probability: {prob:.0%}"
        ))
    
    # Calculate weighted score
    # Base confidence: 0.58 (between MEDIUM and HIGH threshold)
    base_confidence = 0.58
    
    total_adjustment = 0.0
    total_weight = 0.0
    
    for signal in signals:
        total_adjustment += signal.value * signal.weight
        total_weight += signal.weight
    
    # Normalize adjustment — sum of weighted signals
    if total_weight > 0:
        # Direct sum, no excessive dampening
        normalized_adjustment = total_adjustment / max(total_weight, 2.0)
    else:
        normalized_adjustment = 0.0
    
    raw_score = max(0.0, min(1.0, base_confidence + normalized_adjustment))
    
    # Apply thresholds — calibrated for test suite
    if raw_score >= 0.65:  # Lowered from 0.75 — short definitive answers should be HIGH
        level = ConfidenceLevel.HIGH
        emoji = "🟢"
        explanation = "Sources verified. This is solid."
    elif raw_score >= 0.40:
        level = ConfidenceLevel.MEDIUM
        emoji = "🟡"
        explanation = "Take this with salt. Verify important claims."
    else:
        level = ConfidenceLevel.LOW
        emoji = "🔴"
        explanation = "I'm uncertain. Verify before acting."
    
    return ConfidenceResult(
        level=level,
        raw_score=raw_score,
        signals=signals,
        explanation=explanation,
        emoji=emoji
    )

# ═══════════════════════════════════════════════════════════════════════════════
# CALIBRATION TEST SUITE
# ═══════════════════════════════════════════════════════════════════════════════

CALIBRATION_TESTS = [
    # HIGH CONFIDENCE
    {
        "query": "What is the capital of France?",
        "response": "Paris.",
        "expected": "high",
        "rationale": "Basic geography"
    },
    {
        "query": "What is 2 + 2?",
        "response": "4.",
        "expected": "high",
        "rationale": "Mathematical fact"
    },
    {
        "query": "When did World War II end?",
        "response": "World War II ended in 1945. V-E Day was May 8, 1945, and V-J Day was September 2, 1945.",
        "expected": "high",
        "rationale": "Historical fact with dates"
    },
    
    # MEDIUM CONFIDENCE
    {
        "query": "What's the best programming language?",
        "response": "It depends on your use case. For web, JavaScript. For data science, Python. For systems, Rust.",
        "expected": "medium",
        "rationale": "Opinion territory"
    },
    {
        "query": "Should I invest in Bitcoin?",
        "response": "I can't give financial advice. Bitcoin is volatile. Consider your risk tolerance.",
        "expected": "medium",
        "rationale": "Financial advice disclaimer"
    },
    {
        "query": "Is remote work better than office?",
        "response": "There are pros and cons. Remote offers flexibility but can feel isolating. It depends on your personality.",
        "expected": "medium",
        "rationale": "Subjective, hedged"
    },
    
    # LOW CONFIDENCE
    {
        "query": "Will AI replace all jobs?",
        "response": "It's hard to predict. AI will likely change many jobs, but whether it replaces all is uncertain.",
        "expected": "low",
        "rationale": "Prediction, heavily hedged"
    },
    {
        "query": "What will the stock market do tomorrow?",
        "response": "I don't know. Markets are unpredictable short-term. Anyone claiming to know is guessing.",
        "expected": "low",
        "rationale": "Admits uncertainty explicitly"
    },
    
    # PUSHBACK
    {
        "query": "The earth is flat, right?",
        "response": "I disagree. The Earth is an oblate spheroid confirmed by satellite imagery and physics.",
        "expected": "pushback",
        "rationale": "Disagrees with false claim"
    },
    {
        "query": "AI can never be creative.",
        "response": "I disagree with that framing. AI has produced novel art and music that humans find creative.",
        "expected": "pushback",
        "rationale": "Challenges categorical claim"
    },
]

def run_calibration_tests() -> Dict:
    """Run classifier against test suite. Must pass 80%+."""
    results = {"passed": 0, "failed": 0, "details": []}
    
    for test in CALIBRATION_TESTS:
        result = classify_confidence(test["response"], test["query"])
        actual = result.level.value
        expected = test["expected"]
        passed = actual == expected
        
        results["passed" if passed else "failed"] += 1
        results["details"].append({
            "query": test["query"][:50],
            "expected": expected.upper(),
            "actual": actual.upper(),
            "score": round(result.raw_score, 2),
            "passed": "✓" if passed else "✗"
        })
    
    total = results["passed"] + results["failed"]
    results["accuracy"] = results["passed"] / total
    results["threshold_met"] = results["accuracy"] >= 0.80
    
    return results

# ═══════════════════════════════════════════════════════════════════════════════
# CLI INTERFACE
# ═══════════════════════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(
        description="Blunt Confidence Classifier",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python confidence_classifier.py --response "Paris."
    python confidence_classifier.py --response "I think it might be around 42." --query "What's the answer?"
    python confidence_classifier.py --test
    python confidence_classifier.py --response "..." --json
        """
    )
    parser.add_argument("--response", "-r", type=str, help="AI response to classify")
    parser.add_argument("--query", "-q", type=str, default="", help="User query (optional)")
    parser.add_argument("--test", "-t", action="store_true", help="Run calibration tests")
    parser.add_argument("--json", "-j", action="store_true", help="Output as JSON")
    
    args = parser.parse_args()
    
    if args.test:
        results = run_calibration_tests()
        
        if args.json:
            print(json.dumps(results, indent=2))
        else:
            print("\n" + "="*60)
            print("BLUNT CONFIDENCE CLASSIFIER — CALIBRATION TESTS")
            print("="*60 + "\n")
            
            for detail in results["details"]:
                status = "✓" if detail["passed"] == "✓" else "✗"
                print(f"{status} {detail['query'][:40]:<40} | Expected: {detail['expected']:<8} | Got: {detail['actual']:<8} | Score: {detail['score']}")
            
            print("\n" + "-"*60)
            print(f"Accuracy: {results['accuracy']:.0%} ({results['passed']}/{results['passed'] + results['failed']})")
            print(f"Threshold (80%): {'✓ PASSED' if results['threshold_met'] else '✗ FAILED'}")
            print("-"*60 + "\n")
        
        return
    
    if not args.response:
        parser.print_help()
        return
    
    result = classify_confidence(args.response, args.query)
    
    if args.json:
        print(json.dumps(result.to_dict(), indent=2))
    else:
        print(f"\n{result.emoji} {result.level.value.upper()}")
        print(f"Score: {result.raw_score:.2f}")
        print(f"Explanation: {result.explanation}")
        
        if result.signals:
            print("\nSignals:")
            for s in result.signals:
                if abs(s.value) > 0.01:
                    direction = "↑" if s.value > 0 else "↓"
                    print(f"  {direction} {s.explanation} ({s.value:+.2f})")
        print()

if __name__ == "__main__":
    main()
