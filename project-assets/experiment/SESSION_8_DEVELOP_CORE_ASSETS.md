# Session 8: Develop — Core Assets

**Datum:** 2026-02-08
**Phase:** Develop (Woche 1)
**Fokus:** Confidence UI Spec, Logo Direction, Landing Page Copy, Hi-Fi Wireframes

---

## 1. Confidence UI — The Differentiating Feature

### 1.1 The Strategic Premise

Every AI shows what it thinks. **Blunt shows how confident it is.**

This is not cosmetic. This is the structural implementation of "Honest AI." Without visible confidence, "honesty" is just marketing. With it, honesty becomes a verifiable product feature.

**Competitive Reality:**
| Player | Confidence Display | Consumer-Visible? |
|--------|-------------------|-------------------|
| ChatGPT | None | ❌ |
| Claude | None | ❌ |
| Gemini | None | ❌ |
| Perplexity | Sources, not confidence | Partial |
| Pi | None (deprecated) | ❌ |
| **Blunt** | 3-Level + Explanation | ✅ |

**This is whitespace. No consumer AI does this.**

---

### 1.2 The Three-Level System

#### Why Three Levels (Not Five, Not Percentage)

**Research Insight (Medium/Bootcamp, 2025):**
> "Avoid false precision (99.73% vs ~very high)"

**Decision:** Three levels are cognitively optimal for quick decisions. Percentages create false precision. Five levels create decision fatigue.

---

#### Level Definitions

| Level | Label | Visual | Threshold | Meaning |
|-------|-------|--------|-----------|---------|
| 🟢 | HIGH | Green pill | ≥85% internal confidence | "I'm confident about this. Sources verified, widely reported, or directly observable." |
| 🟡 | MEDIUM | Amber pill | 60-84% | "There's some uncertainty here. This is opinion territory, or sources conflict." |
| 🔴 | LOW | Red pill | <60% | "I'm uncertain. Take this as a starting point, not an answer." |

**Plus: Special State**

| State | Label | Visual | Meaning |
|-------|-------|--------|---------|
| 🔴🟢 | PUSHBACK | Red/Green split | "I disagree with your premise. Here's why." |

---

### 1.3 UI Specification — Confidence Indicator

#### Anatomy of the Confidence Pill

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│  ┌──────────────────────────────────────────────────────┐   │
│  │ 🟢 HIGH CONFIDENCE                                    │   │
│  │                                                       │   │
│  │ Sources verified, widely reported                     │   │
│  │                                                       │   │
│  │ [View sources ↗]                                      │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

#### Visual Specs

| Property | Value | Notes |
|----------|-------|-------|
| **Container** | Rounded corners (4px) | Subtle, not playful |
| **Background** | Opacity 10% of signal color | #16a34a at 10% for green |
| **Border** | 1px solid at 30% opacity | Defines without dominating |
| **Icon** | Filled circle (8px) | Green/Amber/Red |
| **Label** | All caps, 11px, 600 weight | "HIGH CONFIDENCE" |
| **Explanation** | 13px, 400 weight, #666 | One line, plain English |
| **Action** | Text link, signal color | "View sources" or "Why I'm uncertain" |

#### Color System

```css
/* Confidence Colors */
--confidence-high: #16a34a;      /* Green 600 */
--confidence-medium: #eab308;    /* Yellow 500 */
--confidence-low: #dc2626;       /* Red 600 */
--confidence-pushback: #dc2626;  /* Same as low */

/* Background Tints */
--confidence-high-bg: rgba(22, 163, 74, 0.1);
--confidence-medium-bg: rgba(234, 179, 8, 0.1);
--confidence-low-bg: rgba(220, 38, 38, 0.1);
```

---

### 1.4 Placement Logic

#### Rule: Confidence Appears on Every Substantive Response

**Appears when:**
- Making factual claims
- Providing recommendations
- Disagreeing with user
- Admitting uncertainty

**Does NOT appear when:**
- Asking clarifying questions
- Simple acknowledgments ("Got it.")
- Meta-commentary about the conversation

#### Placement Options

**Option A: Bottom of Response (Recommended)**
```
┌─────────────────────────────────────────────────────────────┐
│  blunt:                                                     │
│                                                             │
│  [Response content here...]                                 │
│                                                             │
│  ─────────────────────────────────────────────────────────  │
│  ┌───────────────────────────────────────────────────────┐  │
│  │ 🟢 HIGH CONFIDENCE                                     │  │
│  │ Sources verified, widely reported                      │  │
│  └───────────────────────────────────────────────────────┘  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Rationale:** Read content first, then calibrate trust. Doesn't interrupt reading flow.

**Option B: Inline (For Long Responses)**
```
The unemployment rate fell to 3.5% in December. 🟢

However, wage growth is harder to predict. 🟡 Most economists 
expect 2-3% increases, but this depends on Fed policy.
```

**Use Case:** Long responses with multiple claims at different confidence levels.

---

### 1.5 Confidence Explanation Panel

#### Expanded State (On Click/Tap)

```
┌─────────────────────────────────────────────────────────────┐
│  🟡 MEDIUM CONFIDENCE                                       │
│                                                             │
│  WHY I'M LESS CERTAIN                                       │
│                                                             │
│  • This is opinion territory — there's no objective "best"  │
│  • Multiple valid perspectives exist                        │
│  • My training may not reflect recent developments          │
│                                                             │
│  WHAT YOU SHOULD DO                                         │
│                                                             │
│  Take my suggestions as starting points. Verify with        │
│  current sources if this decision matters.                  │
│                                                             │
│  ───────────────────────────────────────────────────────── │
│  [I found this helpful]  [I disagree]  [Collapse]          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

#### Explanation Content by Level

| Level | "Why" Header | Content Pattern |
|-------|--------------|-----------------|
| HIGH | "Why I'm confident" | Sources verified + recency + consistency |
| MEDIUM | "Why I'm less certain" | Opinion territory / Conflicting sources / Recency gap |
| LOW | "Why I'm uncertain" | Outside training / Can't verify / Speculation |
| PUSHBACK | "Why I disagree" | Premise issue + counter-evidence + logic |

---

### 1.6 Pushback UI (Anti-Sycophancy Feature)

#### The Most Differentiating Element

When Blunt disagrees, it doesn't hedge. It says "I disagree" — then explains why.

```
┌─────────────────────────────────────────────────────────────┐
│  blunt:                                                     │
│                                                             │
│  I disagree.                                                │
│                                                             │
│  "All knowledge workers will be replaced by 2030" is a      │
│  categorical claim that the evidence doesn't support:       │
│                                                             │
│  1. Historical pattern: Technology augments more than       │
│     replaces. The spreadsheet didn't eliminate accountants. │
│                                                             │
│  2. Current trajectory: Most AI deployments are copilot     │
│     models, not replacement models.                         │
│                                                             │
│  3. Timeline: 5 years is too short for the regulatory,      │
│     training, and integration challenges.                   │
│                                                             │
│  ─────────────────────────────────────────────────────────  │
│  ┌───────────────────────────────────────────────────────┐  │
│  │ 🔴 PUSHBACK                                            │  │
│  │                                                        │  │
│  │ Why I'm disagreeing: Your claim was categorical        │  │
│  │ ("all", "by 2030") and I have counter-evidence.        │  │
│  │                                                        │  │
│  │ I'd rather challenge you than tell you what you        │  │
│  │ want to hear.                                          │  │
│  └───────────────────────────────────────────────────────┘  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

#### Pushback Triggers

| Trigger | Example | Response Pattern |
|---------|---------|------------------|
| **Categorical claims** | "All X are Y" | Challenge the absolute |
| **Factual errors** | "The earth is 6000 years old" | Correct directly |
| **Logical fallacies** | Strawman, false dichotomy | Name and reframe |
| **Confirmation seeking** | "You agree that..." | Decline to confirm |
| **Harmful requests** | Self-harm, illegal | Refuse with explanation |

---

### 1.7 Calibration & Feedback Loop

#### User Feedback Actions

```
[I found this helpful]  [I disagree]  [Report inaccuracy]
```

#### Behind the Scenes (Transparency Dashboard)

The system tracks:
- How often each confidence level is assigned
- User disagreement rate per level
- Calibration accuracy (was HIGH actually accurate?)

This feeds into the Transparency Dashboard (see Session 7 wireframes).

---

### 1.8 Implementation Notes

#### Technical Feasibility

| Component | Complexity | Notes |
|-----------|------------|-------|
| Confidence Classification | Medium | Can use token-level logprobs + heuristics |
| Source Verification | Medium | Perplexity-style citation extraction |
| Pushback Detection | High | Requires fine-tuning or extensive prompting |
| Calibration Tracking | Low | Standard analytics |

#### MVP vs. V2

| Feature | MVP | V2 |
|---------|-----|-----|
| 3-Level Indicator | ✅ | ✅ |
| Explanation Panel | ✅ | ✅ |
| Pushback UI | ✅ | ✅ |
| Inline Confidence | ❌ | ✅ |
| Calibration Dashboard | ❌ | ✅ |
| User Feedback Loop | ❌ | ✅ |

---

## 2. Logo Strategic Direction

### 2.1 What the Logo Must Communicate

| Attribute | Expression |
|-----------|------------|
| **Direct** | No ornament. No playfulness. Get to the point. |
| **Confident** | Bold weight. Stable geometry. |
| **Honest** | Nothing hidden. No tricks. |
| **Technical** | Precision. Clean lines. |
| **Slightly edgy** | Not warm. Not cold. Assertive. |

### 2.2 Logo Type Recommendation

**Primary: Wordmark Only**

```
blunt.
```

- Lowercase only — confidence without arrogance
- Bold weight — presence without shouting
- Period included — finality, statement-making
- Sans-serif — modern, tech-appropriate

**Why no icon initially:**
1. Word "blunt" is already distinctive
2. Icons require context to read
3. Period acts as minimal visual device
4. Faster to market

### 2.3 Typography Candidates

| Typeface | Why | Concerns |
|----------|-----|----------|
| **Inter Bold** | Clean, geometric, excellent screen rendering | Ubiquitous |
| **Satoshi Bold** | Modern, slightly distinctive letterforms | Less tested |
| **Manrope Bold** | Geometric with personality | May read too soft |
| **GT Walsheim Bold** | Distinctive "b" and "t" | Licensing cost |
| **Custom** | Own the letterforms | Time/cost |

**Recommendation:** Start with **Inter Bold** or **Satoshi Bold**. Commission custom wordmark for V2 if traction.

### 2.4 Logo Variations

```
Primary:        blunt.
Compact:        blunt
URL:            beblunt.ai
Favicon:        b.  (or just "b")
```

### 2.5 Color Application

| Context | Treatment |
|---------|-----------|
| Light background | Charcoal #1a1a1a |
| Dark background | Off-white #fafaf9 |
| Feature accent | Add amber underline under the period |

---

## 3. Landing Page Copy

### 3.1 Hero Section

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│                          blunt.                             │
│                                                             │
│     In a world of agreeable AI, Blunt disagrees.            │
│                                                             │
│     The AI that shows you what it doesn't know.             │
│     Every. Single. Time.                                    │
│                                                             │
│                    [ Join the waitlist ]                    │
│                                                             │
│              "Finally, an AI that won't pretend."           │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 3.2 Problem Section

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│                    THE SYCOPHANCY PROBLEM                   │
│                                                             │
│  82% of people are skeptical of AI.                         │
│  Only 5% trust it "a lot."                                  │
│                                                             │
│  Here's why:                                                │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  Other AIs                                           │   │
│  │                                                      │   │
│  │  "That's a great question!"                          │   │
│  │  "You make an excellent point!"                      │   │
│  │  "I'm happy to help with that!"                      │   │
│  │                                                      │   │
│  │  They agree with everything. Even when you're wrong. │   │
│  │  ChatGPT's agreement rate: 58%                       │   │
│  │  Claude's agreement rate: 60%                        │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  Blunt                                               │   │
│  │                                                      │   │
│  │  "I disagree."                                       │   │
│  │  "I don't know."                                     │   │
│  │  "You're wrong because..."                           │   │
│  │                                                      │   │
│  │  We'd rather be honest than agreeable.               │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 3.3 Features Section

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│                    HOW BLUNT IS DIFFERENT                   │
│                                                             │
│  ┌─────────────────┐  ┌─────────────────┐                  │
│  │ VISIBLE         │  │ CITATIONS       │                  │
│  │ CONFIDENCE      │  │ FIRST           │                  │
│  │                 │  │                 │                  │
│  │ See when I'm    │  │ No source,      │                  │
│  │ certain vs.     │  │ no claim.       │                  │
│  │ when I'm        │  │ That simple.    │                  │
│  │ guessing.       │  │                 │                  │
│  │ 🟢 🟡 🔴         │  │                 │                  │
│  └─────────────────┘  └─────────────────┘                  │
│                                                             │
│  ┌─────────────────┐  ┌─────────────────┐                  │
│  │ ANTI-           │  │ LIMITATIONS     │                  │
│  │ SYCOPHANCY      │  │ UPFRONT         │                  │
│  │                 │  │                 │                  │
│  │ I'll disagree   │  │ I'll tell you   │                  │
│  │ with you when   │  │ what I can't    │                  │
│  │ you're wrong.   │  │ do — before     │                  │
│  │ That's my job.  │  │ you ask.        │                  │
│  └─────────────────┘  └─────────────────┘                  │
│                                                             │
│  ┌───────────────────────────────────────┐                  │
│  │ TRANSPARENCY DASHBOARD                │                  │
│  │                                       │                  │
│  │ See how honest I've actually been.    │                  │
│  │ Calibration accuracy. Disagreement    │                  │
│  │ log. Everything open.                 │                  │
│  └───────────────────────────────────────┘                  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 3.4 CTA Section

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│            BUILT FOR THE AI-SKEPTICAL                       │
│                                                             │
│  If you don't trust AI, you're not the problem.             │
│  AI hasn't earned your trust yet.                           │
│                                                             │
│  Blunt is different.                                        │
│  We show you exactly how uncertain we are.                  │
│  We disagree when you're wrong.                             │
│  We cite our sources or stay quiet.                         │
│                                                             │
│  Honesty over agreement. Always.                            │
│                                                             │
│               [ Join the waitlist ]                         │
│                                                             │
│       No spam. Just updates when we launch.                 │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 3.5 Footer Tagline Options

| Option | Vibe |
|--------|------|
| "The AI that won't pretend." | Primary — contrarian, memorable |
| "Trust through transparency." | Corporate-safe |
| "Honest AI for the AI-skeptical." | Target-explicit |
| "Finally, AI that disagrees with you." | Provocative |

---

## 4. Hi-Fi Wireframe Specifications

### 4.1 Design System Tokens

```css
/* Typography Scale */
--text-xs: 11px;     /* Labels */
--text-sm: 13px;     /* Body secondary */
--text-base: 15px;   /* Body primary */
--text-lg: 18px;     /* Subheadings */
--text-xl: 24px;     /* Headings */
--text-2xl: 32px;    /* Hero */
--text-3xl: 48px;    /* Display */

/* Font Weights */
--font-normal: 400;
--font-medium: 500;
--font-semibold: 600;
--font-bold: 700;

/* Spacing Scale */
--space-1: 4px;
--space-2: 8px;
--space-3: 12px;
--space-4: 16px;
--space-6: 24px;
--space-8: 32px;
--space-12: 48px;

/* Colors */
--color-text-primary: #1a1a1a;
--color-text-secondary: #666666;
--color-text-tertiary: #999999;
--color-bg-primary: #fafaf9;
--color-bg-secondary: #f4f4f5;
--color-accent: #f59e0b;
--color-border: #e5e5e5;

/* Border Radius */
--radius-sm: 4px;
--radius-md: 8px;
--radius-lg: 12px;

/* Shadows */
--shadow-sm: 0 1px 2px rgba(0,0,0,0.05);
--shadow-md: 0 4px 6px rgba(0,0,0,0.07);
```

### 4.2 Chat Interface Spec

#### Message Container

```
Width: 100% (max 720px)
Padding: 24px
Background: transparent
```

#### AI Response

```
┌─────────────────────────────────────────────────────────────┐
│  blunt:                                         ← 13px, #666│
│                                                             │
│  [Response text in 15px, #1a1a1a, 1.6 line-height]         │
│                                                             │
│  ─────────────────────────────────────────────────────────  │
│  │ Sources: ¹ ² ³  (linked, 13px, accent color)            │
│  ─────────────────────────────────────────────────────────  │
│                                                             │
│  ┌───────────────────────────────────────────────────────┐  │
│  │ 🟢 HIGH CONFIDENCE                                     │  │
│  │ Sources verified, widely reported  [Why? ↗]           │  │
│  └───────────────────────────────────────────────────────┘  │
│                                                             │
│  12px gap                                                   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

#### User Message

```
┌─────────────────────────────────────────────────────────────┐
│                                                You: ←13px, #666
│                                                             │
│         [Message text in 15px, #1a1a1a, right-aligned]     │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 4.3 Onboarding Screen Spec

```
┌─────────────────────────────────────────────────────────────┐
│                        blunt.                    ← 48px bold│
│                                                             │
│  ─────────────────────────────────────────────────────────  │
│                                                             │
│  Before we start, let me be honest about what I am.         │
│                                        ← 18px, #1a1a1a      │
│                                                             │
│  24px gap                                                   │
│                                                             │
│  ┌───────────────────────────────────────────────────────┐  │
│  │ WHAT I DO                               ← 11px, #666  │  │
│  │                                                       │  │
│  │ ✓ Tell you when I'm uncertain           ← 15px       │  │
│  │ ✓ Cite sources for claims                             │  │
│  │ ✓ Push back if I think you're wrong                   │  │
│  │ ✓ Say "I don't know" — often                          │  │
│  └───────────────────────────────────────────────────────┘  │
│                                                             │
│  16px gap                                                   │
│                                                             │
│  ┌───────────────────────────────────────────────────────┐  │
│  │ WHAT I CAN'T PROMISE                    ← 11px, #666  │  │
│  │                                                       │  │
│  │ ✗ I can still hallucinate (all AIs can) ← 15px, #666 │  │
│  │ ✗ I have a knowledge cutoff                           │  │
│  │ ✗ I carry biases I don't fully understand             │  │
│  └───────────────────────────────────────────────────────┘  │
│                                                             │
│  24px gap                                                   │
│                                                             │
│  My deal: Honesty over agreement.  ← 18px, semibold        │
│                                                             │
│  32px gap                                                   │
│                                                             │
│  ┌───────────────────────────────────────────────────────┐  │
│  │              Got it. Let's talk.                      │  │
│  │              ← Button: 15px, #fff on #1a1a1a          │  │
│  │              Border-radius: 4px, Padding: 16px 32px   │  │
│  └───────────────────────────────────────────────────────┘  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 5. Session Summary

### Deliverables Completed

| Deliverable | Status | Notes |
|-------------|--------|-------|
| Confidence UI Specification | ✅ Complete | 3-level system, colors, placement, pushback UI |
| Logo Strategic Direction | ✅ Complete | Wordmark-first, typography candidates |
| Landing Page Copy | ✅ Complete | Hero, Problem, Features, CTA |
| Hi-Fi Wireframe Specs | ✅ Complete | Design tokens, chat interface, onboarding |

### Key Strategic Decisions

1. **Confidence UI is the flagship feature** — It's what makes "Honest AI" verifiable, not just claimed.

2. **Three levels, not percentages** — Cognitive simplicity. Avoid false precision.

3. **Pushback has its own UI state** — "I disagree" is not just text. It's a designed moment.

4. **Wordmark-first logo** — "blunt." is already distinctive. Period adds finality.

5. **Landing page leads with the problem** — Sycophancy data (58-60% agreement rate) is the hook.

### Neue Hypothese

**H9: Visible Confidence Reduces Trust Anxiety**
> Users who see confidence levels will report HIGHER trust in Blunt than users who see identical responses without confidence levels — even when the content is the same.

**Test:** A/B test identical responses with/without confidence indicator. Measure perceived trustworthiness.

---

## 6. Next Session (Session 9)

**Datum:** 2026-02-09
**Phase:** Develop (Woche 1, continued)

**Tasks:**
- [ ] Brand Book Draft (consolidate all brand guidelines)
- [ ] Demo Video Script (60-second explainer)
- [ ] Onboarding Flow (full user journey)
- [ ] Technical Feasibility Assessment (Confidence Classification)

---

## 7. Coda Log Table Entry

| Feld | Wert |
|------|------|
| Datum | 2026-02-08 |
| Session | 8 |
| Phase | Develop |
| MECE-Bereich | Confidence UI + Logo + Landing Page + Wireframes |
| Hypothese | Visible confidence is the structural implementation of "Honest AI" |
| Insight | No consumer AI shows confidence levels. This is genuine whitespace. 3-level system with Pushback UI is the differentiating feature set. |
| Implikation | Confidence UI becomes the flagship feature. Landing page leads with Sycophancy Problem data. Wordmark-first logo approach. |
| Nächste Hypothese | H9: Visible Confidence Reduces Trust Anxiety |
| Status | Develop Week 1 — Core assets specified |

---

*Session 8 abgeschlossen: 2026-02-08, 04:00-05:00 Uhr*
