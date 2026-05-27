# Session 9: Technical Feasibility Assessment

**Datum:** 2026-02-09
**Fokus:** Confidence Classification — Can It Actually Work?

---

## 1. The Core Question

**Is "Visible Confidence" technically feasible for a startup-scale product?**

Blunt's entire positioning rests on showing confidence levels. If this can't be implemented reliably, the brand is an empty promise.

---

## 2. Current State of LLM Confidence Estimation

### 2.1 The Problem: LLMs Are Poorly Calibrated

**Academic Finding (CHI 2026):**
> "Many ML algorithms, especially deep-learning models, are known to provide miscalibrated confidence scores."

**What this means:**
- LLMs often express high confidence when wrong
- Self-reported confidence ("I'm 80% sure") is unreliable
- Token-level probabilities don't directly translate to "answer correctness"

### 2.2 Available Technical Approaches

| Approach | Description | Pros | Cons | Feasibility |
|----------|-------------|------|------|-------------|
| **Token Logprobs** | Use token-level probabilities from the model | Available via API, no fine-tuning | Doesn't measure "correctness", only "likelihood" | Medium |
| **Self-Assessment** | Ask the model "how confident are you?" | Easy to implement | Known to be unreliable, sycophancy bias | Low |
| **Calibration Fine-Tuning** | Train model to produce calibrated confidence | Can be accurate | Requires training data, expensive | Low (for MVP) |
| **Heuristic Rules** | "Has sources" → higher confidence | Simple, controllable | Rigid, may miss nuance | High |
| **Ensemble Methods** | Multiple models vote on confidence | More robust | Expensive, slow | Low (for MVP) |
| **Uncertainty Quantification Models** | Specialized confidence estimation | Research-grade accuracy | Complex, not production-ready | Low |

### 2.3 What's Realistic for MVP

**Approach: Hybrid Heuristics + Token Logprobs**

```
CONFIDENCE = f(
    token_logprobs,          // API-available
    source_presence,         // Can we cite?
    claim_type,              // Factual vs Opinion
    topic_domain,            // Training data coverage
    hedging_language         // Does model itself hedge?
)
```

This won't be perfect. But it can be **directionally accurate** — which is better than nothing.

---

## 3. Detailed Technical Analysis

### 3.1 Token Logprobs

**What it is:** OpenAI, Anthropic, and others provide log-probabilities for generated tokens. Higher logprob = model was more "sure" about that token.

**How to use it:**
```python
# Pseudocode
response = llm.complete(prompt, logprobs=True)
avg_logprob = mean(response.token_logprobs)
confidence_raw = exp(avg_logprob)  # Convert to probability
```

**Limitations:**
- Measures "expected token" not "correct answer"
- Short responses often have higher logprobs (fewer tokens to get wrong)
- Doesn't account for hallucination

**Assessment:** Useful as one signal, not sufficient alone.

### 3.2 Source Presence Heuristic

**Rule:** If the model cites verifiable sources → higher confidence.

```python
def source_confidence_boost(response):
    if has_citations(response):
        return +0.15  # Boost confidence
    if makes_factual_claims(response) and not has_citations(response):
        return -0.20  # Reduce confidence
    return 0
```

**Why this works:**
- Citation-capable models (Perplexity, Bing) are more accurate when citing
- Forces model to "show its work"
- User can verify

**Limitations:**
- Sources can also be wrong
- Not all valuable responses need sources

### 3.3 Claim Type Classification

**Factual claims** → Need higher bar for "high confidence"
**Opinions/Preferences** → Confidence less meaningful
**Predictions** → Inherently uncertain

```python
def claim_type_modifier(response):
    if is_factual_claim(response):
        threshold_high = 0.85
    elif is_opinion(response):
        return "N/A"  # Confidence doesn't apply
    elif is_prediction(response):
        threshold_high = 0.70  # Lower bar
```

### 3.4 Hedging Language Detection

If the model itself hedges ("probably", "might", "it's possible"), that's a signal of uncertainty.

```python
HEDGING_WORDS = [
    "probably", "might", "could be", "possibly",
    "I think", "it seems", "arguably", "potentially"
]

def detect_hedging(response):
    hedge_count = sum(1 for word in HEDGING_WORDS if word in response.lower())
    if hedge_count > 2:
        return "LOW"  # Model is uncertain
    return None
```

### 3.5 Topic Domain Coverage

Some topics are better covered in training data than others.

```python
HIGH_COVERAGE_DOMAINS = [
    "programming", "science", "history", "math",
    "well-documented events"
]

LOW_COVERAGE_DOMAINS = [
    "recent events (< 6 months)",
    "obscure topics",
    "local/regional knowledge",
    "personal advice"
]

def domain_confidence_modifier(topic):
    if topic in HIGH_COVERAGE_DOMAINS:
        return +0.10
    if topic in LOW_COVERAGE_DOMAINS:
        return -0.15
    return 0
```

---

## 4. Proposed MVP Architecture

### 4.1 Confidence Pipeline

```
User Input
    ↓
LLM Response (with logprobs)
    ↓
┌───────────────────────────────────────────────┐
│           CONFIDENCE CLASSIFIER               │
├───────────────────────────────────────────────┤
│  1. Extract avg token logprob                 │
│  2. Detect hedging language                   │
│  3. Classify claim type (factual/opinion)     │
│  4. Check source presence                     │
│  5. Assess topic domain                       │
│  6. Combine signals → RAW_CONFIDENCE          │
│  7. Apply thresholds → HIGH/MEDIUM/LOW        │
└───────────────────────────────────────────────┘
    ↓
Display Confidence Pill
```

### 4.2 Threshold Calibration

| Level | Raw Confidence | Meaning |
|-------|---------------|---------|
| HIGH | ≥ 0.75 | Multiple strong signals |
| MEDIUM | 0.45 - 0.74 | Mixed signals |
| LOW | < 0.45 | Weak signals or explicit uncertainty |

**Important:** These thresholds must be calibrated against real-world accuracy. Initial values are guesses.

### 4.3 Explanation Generation

For each confidence level, generate a brief explanation:

```
HIGH: "Sources verified, widely reported"
→ Because: has_citations = True, claim_type = factual, logprob > 0.8

MEDIUM: "Opinion territory, sources may conflict"
→ Because: claim_type = opinion OR has_citations = mixed

LOW: "I'm uncertain — use as starting point"
→ Because: hedging_detected = True OR logprob < 0.5 OR no_sources
```

---

## 5. Risk Assessment

### 5.1 Technical Risks

| Risk | Severity | Likelihood | Mitigation |
|------|----------|------------|------------|
| **Miscalibration** | Critical | High | Extensive testing, feedback loop, conservative thresholds |
| **Over-confidence on wrong answers** | Critical | Medium | Bias toward MEDIUM/LOW unless strong signals |
| **Latency** | Medium | Low | Confidence calculation is fast (< 100ms) |
| **API Dependency** | Medium | Low | Works with any logprob-capable API |

### 5.2 The Miscalibration Doom Loop

**Worst case:** Blunt shows HIGH confidence on wrong answers.

**Impact:** Users learn to distrust confidence levels → Core value proposition destroyed.

**Mitigation Strategy:**
1. **Conservative calibration:** Default to MEDIUM unless strong signals
2. **Bias LOW on risky topics:** Predictions, medical, legal, financial
3. **User feedback:** "Was this accurate?" → recalibrate thresholds
4. **Transparency:** Show calibration accuracy in dashboard
5. **Human override:** Allow users to flag miscalibration

### 5.3 The "Honest About Uncertainty" Paradox

**Research finding:** Showing uncertainty can reduce trust and increase under-reliance.

**Our bet:**
- Empowering framing ("I show you my confidence") > Warning framing ("I'm uncertain")
- Users who self-select for transparency will appreciate it
- Relationship context (companion) differs from decision-support context

**Risk if wrong:** Users feel Blunt is "less helpful" than ChatGPT.

**Mitigation:**
- Test framing with users before launch
- Offer "confidence off" mode for users who prefer it
- Position confidence as feature, not warning

---

## 6. Pushback Detection (Anti-Sycophancy)

### 6.1 The Challenge

Detecting when to disagree is harder than detecting confidence.

**Triggers for pushback:**
- Factual errors ("The earth is 6000 years old")
- Logical fallacies (strawman, false dichotomy)
- Categorical claims that are false ("All X are Y")
- Confirmation-seeking ("You agree that...")

### 6.2 Technical Approach

**Option A: Prompt Engineering**

```
SYSTEM PROMPT:
When the user makes a claim you believe is incorrect:
1. Say "I disagree."
2. Explain why with evidence.
3. Never soften or hedge the disagreement.

When the user seeks confirmation ("Right?", "You agree?"):
1. Only confirm if you actually agree.
2. If you don't agree, say so directly.
```

**Pros:** Works today, no fine-tuning.
**Cons:** Models resist disagreement. Requires careful tuning.

**Option B: Claim Verification Pipeline**

```
User Claim
    ↓
Extract Factual Claims
    ↓
Verify Against Knowledge Base / Web Search
    ↓
If FALSE → Trigger Pushback Response
If UNCERTAIN → Express uncertainty
If TRUE → Proceed normally
```

**Pros:** More reliable for factual claims.
**Cons:** Latency, complexity, limited to verifiable claims.

### 6.3 MVP Recommendation

**Start with Prompt Engineering + Claim Type Detection.**

Fine-tune prompt to:
- Recognize categorical claims ("all", "always", "never")
- Trigger pushback on factual errors where model has high confidence
- Resist sycophancy patterns ("Great question!")

V2: Add claim verification pipeline for factual claims.

---

## 7. Implementation Timeline

### Phase 1: MVP (Weeks 1-4)

| Week | Deliverable |
|------|-------------|
| 1 | Basic confidence heuristics (hedging, sources) |
| 2 | Token logprob integration |
| 3 | Threshold calibration against test set |
| 4 | Confidence UI integration |

### Phase 2: Calibration (Weeks 5-8)

| Week | Deliverable |
|------|-------------|
| 5 | User feedback collection |
| 6 | Calibration analysis |
| 7 | Threshold adjustment |
| 8 | A/B testing with/without confidence |

### Phase 3: Anti-Sycophancy (Weeks 9-12)

| Week | Deliverable |
|------|-------------|
| 9 | Pushback prompt engineering |
| 10 | Claim type classification |
| 11 | Pushback UI |
| 12 | Integration and testing |

---

## 8. Key Dependencies

| Dependency | Status | Risk |
|------------|--------|------|
| **LLM API with logprobs** | Available (OpenAI, Anthropic) | Low |
| **Citation capability** | Available (Perplexity-style) | Low |
| **Claim type classification** | Needs implementation | Medium |
| **Calibration test dataset** | Needs creation | Medium |
| **User feedback system** | Needs implementation | Low |

---

## 9. Conclusion: Is It Feasible?

**Answer: Yes, with caveats.**

| Aspect | Feasibility | Notes |
|--------|-------------|-------|
| **Basic Confidence Display** | High | Heuristics + logprobs work today |
| **Accurate Calibration** | Medium | Requires iteration and user feedback |
| **Pushback Detection** | Medium | Prompt engineering works; verification is V2 |
| **Trust Improvement** | Unknown | Requires user testing |

### The Core Bet

We're betting that:
1. Imperfect-but-visible confidence is better than hidden confidence
2. Users will appreciate transparency even when it shows uncertainty
3. We can calibrate thresholds through iteration

**If the bet is wrong:** Users may find Blunt "less helpful" than agreeable AIs.

**If the bet is right:** Blunt becomes the default for trust-conscious users.

---

## 10. Recommendations

### Immediate Actions

1. **Build confidence heuristics MVP** (hedging, sources, logprobs)
2. **Create calibration test dataset** (100+ Q&A pairs with known accuracy)
3. **Test framing hypothesis** (empowering vs warning language)
4. **Implement user feedback loop** (was this accurate?)

### Strategic Decision Needed

**Should we launch with imperfect confidence or wait for better calibration?**

- **Launch imperfect:** First-mover advantage, learn from real users
- **Wait:** Risk of trust damage from miscalibration

**Recommendation:** Launch with conservative calibration (bias toward MEDIUM/LOW) and iterate based on feedback.

---

*Technical Feasibility Assessment — Session 9*
