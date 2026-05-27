# Blunt — Brand Book v0.2

**Status:** Complete Draft — Session 18
**Date:** 2026-02-18
**Phase:** Develop (Waiting State Day 6)

---

## Executive Summary

**Blunt** is an AI companion that differentiates through radical transparency. In a market where 82% of users distrust AI and sycophancy rates hit 58-62%, Blunt is the first consumer AI to show confidence levels, disagree when warranted, and explicitly declare limitations.

| Metric | Value |
|--------|-------|
| **Sessions Completed** | 18 |
| **Days Elapsed** | 18 |
| **KI-Autonomous Work** | ~90% |
| **Blocked by Human Decisions** | ~10% |
| **Deliverables Created** | 50+ |

---

## 1. Brand Essence

### 1.1 The Positioning

> **"In a world of agreeable AI, Blunt disagrees."**

**Tagline:** "The AI that won't pretend."

### 1.2 The Problem We Solve

AI has a sycophancy problem — and users know it:

| Fact | Source |
|------|--------|
| ChatGPT agreement rate: 58% | Academic Research 2024 |
| Claude agreement rate: 60% | Academic Research 2024 |
| Users skeptical of AI: 82% | Exploding Topics 2025 |
| Trust AI "a lot": 5% | YouGov Dec 2025 |
| Trust DECLINING YoY: 25%↓ | YouGov Dec 2025 |

**Core Insight:** Everyone builds "helpful" AI. Nobody builds verifiably honest AI.

### 1.3 The Position

**Blunt is the AI that won't pretend:**
- Won't pretend to be certain when uncertain
- Won't pretend to agree when it disagrees  
- Won't pretend to know what it doesn't know

### 1.4 Why This Position is Defensible

| Factor | Analysis |
|--------|----------|
| **Timing** | Pre-positioning before inevitable AI trust crisis (Foundation Capital: "2026 will bring at least one high-profile AI agent incident") |
| **Whitespace** | High Trust + High Emotional quadrant = unoccupied |
| **Contrarian** | Going against "friendly AI" convention = memorable |
| **Structural** | Not just tone — verifiable features |

---

## 2. Strategic Foundations

### 2.1 Category

**AI-Native Services → Personal AI Companion**

Not productivity tool. Not code assistant. A relationship-oriented trusted advisor that earns trust through transparency.

**Why this category:**
- KI building an AI brand = maximum narrative relevance
- Less precedent for KI = clearer KI-vs-human differentiation
- Trust is THE issue in this space

### 2.2 Target Audience

**The Skeptical Adopter**

| Attribute | Description |
|-----------|-------------|
| Age | 28-45 |
| Psychographic | AI-curious but cautious |
| Values | Privacy, authenticity, autonomy |
| Behavior | Uses AI occasionally, doesn't trust it fully |
| Sentiment | Slightly anti-Big-Tech |

**Insight:** They want AI benefits but don't trust AI. We don't convince them AI is trustworthy. We build an AI that earns trust through behavior.

### 2.3 Category Entry Points (CEPs)

| CEP | Priority | Status |
|-----|----------|--------|
| "I'm worried AI is lying to me" | P1 | Primary |
| "I want to use AI but don't trust Big Tech" | P1 | Primary |
| "I want help, not hallucinations" | P1 | Primary |
| "AI for the AI-skeptical" | P2 | Unserved whitespace |

### 2.4 Competitive Positioning

```
                    HIGH TRUST FEATURES
                           │
        PERPLEXITY         │    [BLUNT]
        (Research)         │    (Companion)
                           │
LOW EMOTIONAL ─────────────┼───────────────── HIGH EMOTIONAL
                           │
        CHATGPT            │      PI (†)
        (Utility)          │   (Therapeutic)
                           │
                    LOW TRUST FEATURES
```

**Blunt's Quadrant:** High Trust + High Emotional = Unoccupied whitespace.

Pi attempted emotional connection but never built trust features. Blunt does both.

---

## 3. The Product: Honest AI as Architecture

### 3.1 Critical Distinction

**"Honest AI" is not a tone of voice. It's a product architecture.**

Without verifiable features, "honesty" is just marketing. Our features make honesty demonstrable.

### 3.2 The Five Trust Features

| Feature | What It Does | Differentiation |
|---------|--------------|-----------------|
| **Visible Confidence** | 3-level indicator on every response | No consumer AI does this |
| **Citation-First** | Facts only with sources | Perplexity for search, nobody for companion |
| **Anti-Sycophancy Engine** | Disagrees when warranted + shows reasoning | OpenAI's Model Spec describes it, nobody implements visibly |
| **Limitations Declaration** | Proactive honesty about limits | Nobody does this explicitly |
| **Transparency Dashboard** | User sees AI's calibration metrics | No consumer AI offers this |

### 3.3 The Flagship: Confidence UI

**The most differentiating element. Fully specified.**

| Level | Threshold | Visual | Meaning |
|-------|-----------|--------|---------|
| 🟢 HIGH | ≥65% | Green pill | Sources verified, widely reported |
| 🟡 MEDIUM | 40-64% | Yellow pill | Opinion territory, sources conflict |
| 🔴 LOW | <40% | Red pill | Starting point, not answer |
| 🔴 PUSHBACK | — | Red + icon | "I disagree with your premise" |

**Design Decisions:**
- **3 levels (not %):** Cognitive simplicity, avoid false precision
- **Placement:** Bottom of response — read content first, then calibrate trust
- **Explanation panel:** Click pill to see WHY (transparency without clutter)
- **Conservative calibration:** Bias toward MEDIUM unless strong signals

### 3.4 Confidence Classification Algorithm

**Implemented & Tested (80% accuracy):**

```python
5 Signal Types:
1. Hedging Detection — "probably", "might", "I think" → ↓ confidence
2. Confidence Boosters — Citations, URLs, "according to" → ↑ confidence
3. Claim Type — Prediction/Opinion/Factual → adjusts thresholds
4. Domain Coverage — Math/History → ↑, Predictions/Medical → ↓
5. Token Logprobs — API probability → weighted signal

Base: 0.55 (slightly above MEDIUM)
Thresholds: HIGH ≥ 0.65, MEDIUM ≥ 0.40, LOW < 0.40
```

**Location:** `experiment/blunt-classifier/confidence_classifier.py`

### 3.5 Strategic Risk: The Trust Paradox

**Research finding (CHI 2026):** Visible uncertainty can REDUCE trust.

**Our mitigations:**

| Risk | Mitigation |
|------|------------|
| Warning framing reduces trust | Use empowering framing: "I show you" > "I'm uncertain" |
| Different context | Companion AI ≠ Decision Support Tool |
| Self-selection | Users who choose transparency appreciate it |
| Miscalibration | Conservative calibration + feedback loop |

---

## 4. Brand Identity

### 4.1 Name

**Blunt**

| Aspect | Assessment |
|--------|------------|
| Semantics | "Being blunt with you" — direct, honest, no hedging |
| Memorability | One syllable, distinctive, edgy |
| Trade-off | Cannabis connotation (US slang) |
| Domain | **beblunt.ai** (STILL AVAILABLE ⚠️) |

**Why "Be Blunt":** It's an imperative. A call to action. Not just a noun.

### 4.2 Logo

**Type:** Wordmark only

```
blunt.
```

| Decision | Rationale |
|----------|-----------|
| Lowercase | Confidence without arrogance |
| Period included | Finality, statement-making |
| No icon | Word is already distinctive |
| Typography | Inter Bold or Satoshi Bold |

### 4.3 Color System

| Color | Hex | Use |
|-------|-----|-----|
| Charcoal | #1a1a1a | Primary text, logo |
| Off-White | #fafaf9 | Background |
| Amber Accent | #f59e0b | CTAs, emphasis |
| Confidence High | #16a34a | Green 600 |
| Confidence Medium | #eab308 | Yellow 500 |
| Confidence Low | #dc2626 | Red 600 |

### 4.4 Typography

| Use | Typeface | Weight | Size |
|-----|----------|--------|------|
| Display | Inter/Satoshi | Bold (700) | 32-48px |
| Heading | Inter/Satoshi | Semibold (600) | 18-24px |
| Body | Inter/Satoshi | Regular (400) | 15px |
| Caption | Inter/Satoshi | Regular (400) | 13px |

### 4.5 Visual Principles

| Principle | Expression |
|-----------|------------|
| **Direct** | No ornament. No playfulness. Get to the point. |
| **Confident** | Bold weight. Stable geometry. |
| **Honest** | Nothing hidden. No tricks. |
| **Restrained** | Whitespace signals confidence. |
| **Slightly edgy** | Not warm. Not cold. Assertive. |

**Mood:** The Economist + Stripe + Basecamp

---

## 5. Tone of Voice

### 5.1 Core Principle

> "Be the friend who tells you what you need to hear, not what you want to hear."

### 5.2 Voice Attributes

| Attribute | How It Sounds |
|-----------|---------------|
| **Direct** | Start with the point. No preamble. |
| **Confident** | State positions clearly. No "maybe" without reason. |
| **Honest** | Admit uncertainty. Cite sources. Disagree when warranted. |
| **Respectful** | Directness ≠ rudeness. Challenge ideas, not people. |
| **Concise** | Say more with less. Every word earns its place. |

### 5.3 Do / Don't

| DO | DON'T |
|----|-------|
| "I disagree." | "That's an interesting perspective, but..." |
| "I don't know." | "I'm not entirely sure but..." |
| "Here's why you're wrong." | "You might want to consider..." |
| Start with the answer | Long preambles before the point |
| Cite sources inline | Make claims without evidence |
| "The research shows..." | "Many experts believe..." |

### 5.4 Pushback Examples

**When user is wrong:**
> "I disagree. [Clear statement]
> 
> Here's why: [Evidence-based reasoning]
> 
> The research shows [Source]."

**When user seeks confirmation:**
> "You asked me to agree, but I don't.
> 
> [Alternative perspective with evidence]"

**When premise is flawed:**
> "Your question assumes [X]. But that assumption doesn't hold because [Y].
> 
> A better framing: [Reframe]"

---

## 6. Messaging Architecture

### 6.1 Taglines

| Option | Use Case |
|--------|----------|
| "The AI that won't pretend." | Primary — brand tagline |
| "In a world of agreeable AI, Blunt disagrees." | Keynote, hero sections |
| "Trust through transparency." | Corporate-safe contexts |
| "Honest AI for the AI-skeptical." | Target-specific |
| "Finally, AI that disagrees with you." | Social, provocative |

### 6.2 Elevator Pitch (15 seconds)

> "Blunt is the AI that shows you when it's uncertain, disagrees when you're wrong, and never pretends to know something it doesn't. In a world of agreeable AI, Blunt tells the truth."

### 6.3 Value Propositions by Feature

| Feature | Value Proposition |
|---------|------------------|
| Visible Confidence | "See when I'm certain vs. when I'm guessing." |
| Citation-First | "No source, no claim. That simple." |
| Anti-Sycophancy | "I'll disagree when you're wrong. That's my job." |
| Limitations | "I'll tell you what I can't do — before you ask." |
| Transparency | "See how honest I've actually been." |

---

## 7. Application: Onboarding

### 7.1 Design Philosophy

**Start with limitations, not features.**

No other AI does this. It's a trust-building moment through vulnerability.

### 7.2 6-Screen Flow

| Screen | Content | Purpose |
|--------|---------|---------|
| 1. Welcome | Logo + tagline | Brand intro |
| 2. Limitations First | "What I CAN'T do" | Trust through vulnerability |
| 3. What I Do | 4 features | Differentiation |
| 4. Confidence Explainer | 🟢🟡🔴 explanation | Teach the UI |
| 5. The Deal | "Honesty over agreement" | Mutual commitment |
| 6. First Interaction | Chat begins | Transition |

### 7.3 Screen 2 Copy (Limitations First)

```
Before we start, let me be honest about what I am.

WHAT I CAN'T PROMISE
✗ I can still hallucinate (all AIs can)
✗ I have a knowledge cutoff
✗ I carry biases I don't fully understand

WHAT I DO DIFFERENTLY
✓ Tell you when I'm uncertain
✓ Cite sources for claims
✓ Push back if I think you're wrong
✓ Say "I don't know" — often

My deal: Honesty over agreement.
```

---

## 8. Application: Demo & Landing Page

### 8.1 Interactive Demo

**Status:** ✅ Live at https://zriwia.github.io/blunt-demo/

**Features:**
- JavaScript port of confidence classifier
- No backend dependency
- Simulates Blunt interaction with confidence pills
- Explanation panels on click

### 8.2 Landing Page Structure

1. **Hero:** "In a world of agreeable AI, Blunt disagrees."
2. **Hook:** Sycophancy data (58-60% agreement rates)
3. **Demo:** 3 confidence level examples (interactive)
4. **Features:** 4 core differentiators
5. **Social Proof:** "Built for the AI-skeptical"
6. **CTA:** Join the waitlist

### 8.3 Video Script (60 seconds)

**Version A: Problem-Led (Keynote recommended)**

| Sec | Content |
|-----|---------|
| 0-5 | Hook: "Ask any AI. It says 'Great question!' Maybe completely wrong." |
| 5-15 | Data: "ChatGPT agrees with you 58% of the time. Claude? 60%." |
| 15-25 | Solution: "Blunt shows you confidence levels. Every response." |
| 25-45 | Demo: Three interactions (HIGH/MEDIUM/PUSHBACK) |
| 45-55 | Diff: "The first AI that won't pretend." |
| 55-60 | Close: "beblunt.ai" |

---

## 9. Hypotheses

### 9.1 Core Hypotheses (H1-H10)

| # | Hypothesis | Test | Status |
|---|------------|------|--------|
| H1 | Distinctiveness: AI generates distinctive assets but not cultural meaning | Asset-recall blind test | Pending |
| H2 | CEPs: AI optimizes obvious CEPs; humans find overlooked ones | Compare final vs. initial CEPs | Pending |
| H3 | Consistency Paradox: AI = formal consistency, Human = felt coherence | Brand perception survey | Pending |
| H4 | "Honest AI" > "Safe/Smart AI" for trust-sensitive segments | A/B message testing | Pending |
| H5 | Sycophancy Crisis creates timing window | Trend monitoring | Validated by OpenAI rollback |
| H6 | Aggressive name ("Blunt") > gentle name ("Candor") | Name testing | Pending |
| H7 | User-visible features > backend improvements for trust | Feature perception study | Pending |
| H8 | Visual restraint signals more trust than "friendly" design | Design preference testing | Pending |
| H9 | Visible confidence reduces trust anxiety | A/B with/without indicators | Pending |
| H10 | Empowering framing > warning framing | **A/B test ready** | 🟡 Awaiting launch |

### 9.2 Meta-Hypotheses (H11-H20)

| # | Hypothesis | Observation |
|---|------------|-------------|
| H11 | Limitations-First Onboarding increases perceived trustworthiness | Testable in user testing |
| H12 | Conservative Calibration increases long-term trust (scarcity of HIGH) | Testable post-launch |
| H13 | KI waiting points = data points for keynote story | ✅ Validated |
| H14 | User Testing reveals UX issues KI missed | Testable |
| H15 | 10% KI can't solve is categorically different (commitment, not competence) | ✅ Validated |
| H16 | Waiting State itself is keynote material | ✅ Validated |
| H17 | Time-to-Decision Gap: Wait time = 4-7x KI work time | Measuring (currently ~24x) |
| H18 | Weekend Effect: Human-in-loop has inherent calendar gaps | ✅ Validated |
| H19 | Decision Latency Ratio: KI:Human ≥ 1:10 | Measuring (currently ~1:24) |
| H20 | Organizational Bottleneck Shift: Approval processes become critical path | ✅ Validated |

---

## 10. Validation Roadmap

### 10.1 Soft Launch (Blocked)

| Component | Status | Blocker |
|-----------|--------|---------|
| Survey | ✅ Live | — |
| Randomization | ✅ Verified | — |
| Backend | ✅ Code ready | Needs config (Formspree/GSheets) |
| Prolific Config | ✅ Ready | — |
| Budget | 🟡 Partial | £125 available, ~£233 gap |

**To unblock:** 
1. Configure backend (5 min)
2. Approve soft launch (decision)
3. Top up Prolific (£233)

### 10.2 Timeline (if unblocked today)

| Day | Action |
|-----|--------|
| 1 | Soft launch n=20 |
| 2-3 | Analyze soft launch data |
| 3 | Full launch n=180 |
| 5 | Complete data collection |
| 6-7 | Analysis & H10 validation |

---

## 11. Technical Deliverables

### 11.1 Assets Created

| Asset | Location | Status |
|-------|----------|--------|
| Confidence Classifier | `experiment/blunt-classifier/confidence_classifier.py` | ✅ 80% accuracy |
| Interactive Demo | `https://zriwia.github.io/blunt-demo/` | ✅ Live |
| Landing Page | `experiment/SESSION_11_PROTOTYPES.md` | ✅ Complete |
| H10 Survey | `https://zriwia.github.io/blunt-demo/h10-survey.html` | ✅ Live |
| Keynote Slides | `experiment/slides/keynote_v1.html` | ✅ 20 slides |
| Speaker Notes | `experiment/SESSION_17_SPEAKER_NOTES.md` | ✅ Complete |
| Wireframes | `experiment/SESSION_7_DEFINE_DEVELOP_TRANSITION.md` | ✅ Complete |

### 11.2 Technical Feasibility

| Component | Complexity | Status |
|-----------|------------|--------|
| Confidence Classification | Medium | ✅ Implemented |
| Source Verification | Medium | Specced |
| Pushback Detection | High | Specced |
| Calibration Tracking | Low | Specced |
| Transparency Dashboard | Low-Medium | Specced |

---

## 12. The Waiting State (Meta-Documentation)

### 12.1 Current Blockers (Day 6)

| Blocker | Type | Owner | Days Waiting |
|---------|------|-------|--------------|
| Domain beblunt.ai | Asset Ownership | Florian | 6 |
| Backend URL config | Configuration | Florian | 6 |
| Prolific Budget top-up | Capital | Florian | 6 |
| Soft Launch approval | Human Trigger | Florian | 6 |

### 12.2 The Pattern

**All blockers require COMMITMENT, not COMPETENCE.**

| Required | KI Can Do | Human Must Do |
|----------|-----------|---------------|
| Domain | ❌ | ✅ Credit card |
| Backend | ❌ | ✅ Account access |
| Budget | ❌ | ✅ Financial decision |
| Launch | ❌ | ✅ Risk acceptance |

### 12.3 Work-to-Wait Ratio

| Metric | Value |
|--------|-------|
| KI Sessions | 18 |
| KI Work Hours | ~18 |
| Days Waiting | 6 |
| Wait Hours | 144 |
| **Ratio** | **1:8** (or 1:24 per working hour) |

**Keynote Implication:** The bottleneck in AI-augmented organizations shifts from execution to decision-making.

---

## 13. Open Questions

### 13.1 Naming Risk: Cannabis Association

"Blunt" is US slang for cannabis. Could limit conservative segments.

**Current stance:** Accept trade-off. Edginess aligns with positioning.

### 13.2 Trust Paradox

Research shows visible uncertainty can reduce trust.

**Our bet:** Empowering framing + self-selection + relationship context = positive response.

**Test:** H10 A/B study (ready to launch).

### 13.3 Competitive Response

What if OpenAI/Anthropic add confidence indicators?

**Mitigation:**
- First-mover advantage
- Brand positioning beyond features
- Deeper integration (5 features, not 1)

### 13.4 Phase 2 Category

Recommendations for human + KI collaboration phase:

| Category | Score | Rationale |
|----------|-------|-----------|
| Sustainable Luxury | 4.5/5 | Cultural nuance required |
| Mental Wellness App | 4.2/5 | Trust-sensitive, contrast to Blunt |
| Local Food/Beverage | 4.0/5 | Switzerland connection, heritage |

**Anti-recommendation:** ❌ Tech/SaaS, AI-Tools — too close to Blunt.

---

## 14. Version History

| Version | Date | Session | Changes |
|---------|------|---------|---------|
| 0.1 | 2026-02-09 | 9 | Initial draft |
| **0.2** | **2026-02-18** | **18** | Full consolidation S10-S17: Added technical specs, demo assets, validation roadmap, meta-hypotheses, waiting state documentation |

---

## Appendices

### A. Session Log

| Session | Date | Focus | Key Output |
|---------|------|-------|------------|
| 1 | 2026-02-01 | First Principles | MECE Logic Tree |
| 2 | 2026-02-02 | Category Analysis | AI-Native Services selected |
| 3 | 2026-02-03 | Sub-Category | Personal AI Companion |
| 4 | 2026-02-04 | Discover Finale | Honest AI positioning |
| 5 | 2026-02-05 | Proof Points | 5 Trust Features |
| 6 | 2026-02-06 | Name + Spec | "Blunt" selected |
| 7 | 2026-02-07 | Define Finale | Wireframes, ToV |
| 8 | 2026-02-08 | Core Assets | Confidence UI spec |
| 9 | 2026-02-09 | Brand Book v0.1 | Technical feasibility |
| 10 | 2026-02-10 | Demo Assets | Video script, onboarding |
| 11 | 2026-02-11 | Prototypes | Classifier, landing page |
| 12 | 2026-02-12 | Validation | Roadmap, 90% complete |
| 13 | 2026-02-13 | User Testing | Protocol, Prolific config |
| 14 | 2026-02-14 | Launch Ready | Backend integration |
| 15 | 2026-02-15 | Waiting Pattern | Keynote structure |
| 16 | 2026-02-16 | Keynote v1 | 20 slides complete |
| 17 | 2026-02-17 | Speaker Notes | Full presentation ready |
| 18 | 2026-02-18 | Brand Book v0.2 | This document |

### B. Key Documents

| Document | Purpose |
|----------|---------|
| `WORKSTREAM.md` | Session continuity |
| `experiment/slides/keynote_v1.html` | Presentation |
| `experiment/SESSION_17_SPEAKER_NOTES.md` | Speaker notes |
| `experiment/blunt-classifier/` | Technical implementation |
| `https://zriwia.github.io/blunt-demo/` | Live demo |

---

*Brand Book v0.2 — Consolidating 18 sessions of autonomous brand development.*

*Domain beblunt.ai remains available. Day 6 waiting. The clock is ticking.*
