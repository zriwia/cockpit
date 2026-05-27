# Session 10: Demo Assets für Keynote

**Datum:** 2026-02-10
**Phase:** Develop (Woche 2)
**Fokus:** Demo Video Script + Onboarding Flow

---

## 1. Demo Video Script (60 Sekunden)

### Empfehlung: Version A (Problem-Led)

Die Problem-Led Version ist optimal für die Keynote:
1. Etabliert zuerst das Problem → Publikum nickt mit
2. Zeigt die Lösung mit konkreten Examples
3. Data-backed (58/60% agreement rates)
4. Endet mit klarer Differenzierung

---

### Version A: Problem-Led (RECOMMENDED)

```
[0:00-0:08] PROBLEM HOOK

Visual: Screen recording of ChatGPT
Voice: "Ask any AI a question. It'll say 'Great question!' Then give you an answer. Confident. Helpful. Maybe completely wrong."

[0:08-0:16] DATA POINT

Visual: Stats appearing on screen
"58% of the time, ChatGPT agrees with you — even when you're wrong.
60% for Claude.
They're designed to please, not to be honest."

[0:16-0:28] SOLUTION INTRO

Visual: Blunt interface appears
"We built Blunt. The AI that won't pretend.

Every response shows you how confident it actually is.
High confidence — sources verified.
Medium — opinion territory.
Low — this is a guess, not an answer."

[0:28-0:42] DEMO SEQUENCE

Visual: Live demo of three interactions

Demo 1: "What's the capital of France?"
Blunt: "Paris." [🟢 HIGH]

Demo 2: "What's the best programming language?"
Blunt: "That's subjective. Here's what I think..." [🟡 MEDIUM]

Demo 3: User makes a wrong claim
Blunt: "I disagree. [Explanation]" [🔴 PUSHBACK]

Voice: "When we're certain, you know it. When we're guessing, you know that too. And when you're wrong, we'll tell you."

[0:42-0:52] DIFFERENTIATION

Visual: Split screen comparison
"Other AI: Tells you what you want to hear.
Blunt: Tells you what you need to know."

[0:52-1:00] CLOSE

Visual: Logo + tagline
"Blunt. The AI that won't pretend.
beblunt.ai"
```

**Total runtime:** 60 seconds

---

### Version B: Demo-First (für Product Hunt / Landing Page)

```
[0:00-0:12] COLD OPEN DEMO

Visual: Blunt interface, no preamble
User types: "I think crypto is definitely going to $1M by 2027."

Blunt: "I disagree. 

Here's why: Predicting specific price points in volatile markets is speculation, not analysis. No reliable model supports a specific target like this.

What I can say: crypto markets are highly volatile and unpredictable." 
[🔴 PUSHBACK]

Voice: "This is Blunt. An AI that actually disagrees with you."

[0:12-0:22] THE PROBLEM

Visual: Side-by-side comparison
"Most AIs are sycophants. ChatGPT agrees with you 58% of the time. Claude, 60%. They're optimized for pleasing, not truth."

[0:22-0:38] THE FEATURE

Visual: Confidence indicator closeup
"Blunt shows you exactly how confident it is.

Green: Sources verified. This is solid.
Yellow: Opinion territory. Take it with salt.
Red: I'm uncertain. Verify this.
Pushback: You're wrong. Here's why."

[0:38-0:50] PHILOSOPHY

Visual: Interface + text overlay
"We built Blunt on a simple principle:
Honesty over agreement.
Always."

[0:50-1:00] CLOSE

Visual: Logo + tagline
"Blunt. The AI that won't pretend.
beblunt.ai"
```

---

### Version C: Manifesto (für Social / Brand Video)

```
[0:00-0:10] MANIFESTO OPEN

Visual: Black screen, white text appears
Voice (confident, slightly confrontational):

"Every AI says 'Great question!'
Every AI says 'I'd be happy to help!'
Every AI agrees with whatever you say.

We think that's a problem."

[0:10-0:20] THE INSIGHT

Visual: Stats on screen
"58% agreement rate.
They're designed to make you feel smart.
Not to make you smarter."

[0:20-0:35] THE ALTERNATIVE

Visual: Blunt interface
"Blunt shows you when it's guessing.
Blunt cites its sources — or stays quiet.
Blunt disagrees when you're wrong.

Because the truth is more valuable than your feelings."

[0:35-0:50] DEMO MOMENTS

Visual: Quick cuts of three interactions
- [🟢] Confident answer
- [🟡] Uncertain response with explanation
- [🔴] "I disagree."

[0:50-1:00] CLOSE

Visual: Wordmark
"In a world of agreeable AI, Blunt disagrees.
beblunt.ai"
```

---

## 2. Onboarding Flow (Full User Journey)

### Design Principle: Limitations First

**Contrarian Logic:**
- Every other AI starts with capabilities ("I can help you with...")
- Blunt starts with limitations ("Here's what I can't do...")

**Why this works:**
1. **Trust through vulnerability** — Admitting weaknesses upfront builds credibility
2. **Expectations management** — Users won't be surprised when AI fails
3. **Differentiation** — No competitor does this
4. **Self-selection** — Users who dislike this aren't our target anyway

---

### Screen 1: Welcome

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│                        blunt.                               │
│                                                             │
│           "An AI that won't pretend."                       │
│                                                             │
│                    [ Start →]                               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

### Screen 2: Limitations First

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  Before we start, let me be honest about what I am.         │
│                                                             │
│  WHAT I CAN'T PROMISE                                       │
│                                                             │
│  ✗ I can still hallucinate (all AIs can)                   │
│  ✗ I have a knowledge cutoff (Jan 2025)                    │
│  ✗ I carry biases I don't fully understand                  │
│  ✗ I might be wrong about things                            │
│                                                             │
│  "Other AIs hide this. I start with it."                    │
│                                                             │
│                    [ Next →]                                │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

### Screen 3: What I Do Differently

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  WHAT I DO                                                  │
│                                                             │
│  🟢 Show confidence levels on every answer                  │
│     "You'll always know when I'm certain vs. guessing"      │
│                                                             │
│  📚 Cite sources for factual claims                         │
│     "No source, no claim"                                   │
│                                                             │
│  🔴 Disagree when I think you're wrong                      │
│     "I'd rather challenge you than flatter you"             │
│                                                             │
│  ❓ Say "I don't know" — often                              │
│     "Uncertainty is information, not failure"               │
│                                                             │
│                    [ Next →]                                │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

### Screen 4: Confidence Explainer

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  HOW TO READ MY CONFIDENCE                                  │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ 🟢 HIGH                                              │   │
│  │ Sources verified. This is solid.                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ 🟡 MEDIUM                                            │   │
│  │ Opinion territory. Take this with salt.              │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ 🔴 LOW                                               │   │
│  │ I'm uncertain. Verify before acting.                 │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ 🔴 PUSHBACK                                          │   │
│  │ I disagree with you. Here's why.                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│                    [ Next →]                                │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

### Screen 5: The Deal

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  MY DEAL WITH YOU                                           │
│                                                             │
│  ╔═══════════════════════════════════════════════════════╗ │
│  ║                                                       ║ │
│  ║  I choose honesty over agreement.                     ║ │
│  ║                                                       ║ │
│  ║  I'll tell you uncomfortable truths.                  ║ │
│  ║  I'll admit when I don't know.                        ║ │
│  ║  I'll push back when you're wrong.                    ║ │
│  ║                                                       ║ │
│  ║  In return:                                           ║ │
│  ║  You get an AI you can actually trust.                ║ │
│  ║                                                       ║ │
│  ╚═══════════════════════════════════════════════════════╝ │
│                                                             │
│                [ Got it. Let's talk. ]                      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

### Screen 6: First Interaction

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  blunt:                                                     │
│                                                             │
│  "Ready when you are.                                       │
│   Ask me anything. I'll be honest about what I know —       │
│   and what I don't."                                        │
│                                                             │
│  ─────────────────────────────────────────────────────────  │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ Type your message...                                 │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 3. Onboarding Micro-Copy Principles

| Screen | Purpose | Key Message |
|--------|---------|-------------|
| 1. Welcome | Brand intro | Clean, minimal, intriguing |
| 2. Limitations First | Set expectations, build trust | "I start with my flaws" |
| 3. What I Do | Feature preview | Concrete, benefit-oriented |
| 4. Confidence Explainer | Teach the UI | Simple, visual, memorable |
| 5. The Deal | Commitment statement | Mutual agreement framing |
| 6. First Interaction | Transition to chat | Warm but still direct |

---

## 4. Strategic Rationale

### Why Limitations-First Works

**Research backing:**
- Prospect Theory: Losses loom larger than gains
- By naming losses upfront, we neutralize them
- What remains is the value proposition

**Competitive advantage:**
- No competitor starts with limitations
- Creates immediate differentiation
- Builds trust through vulnerability

### Why "The Deal" Screen

- Frames the relationship as mutual
- User isn't passive recipient — they're entering an agreement
- Creates psychological commitment

---

## 5. Neue Hypothese

**H11: Limitations-First Onboarding Increases Perceived Trustworthiness**

> Users who see limitations-first onboarding will rate Blunt as MORE trustworthy than users who see capabilities-first onboarding — even though the product is identical.

**Test Design:**
- A/B test onboarding order (Limitations-first vs. Capabilities-first)
- Measure trust scores immediately post-onboarding
- Compare retention and engagement metrics

---

## 6. Session Summary

| Deliverable | Status | Notes |
|-------------|--------|-------|
| Demo Video Script | ✅ Complete | 3 versions, Version A recommended |
| Onboarding Flow | ✅ Complete | 6 screens, limitations-first approach |

### Deferred to Session 11

- [ ] Confidence Heuristics Prototype
- [ ] Framing Test Design (H10)
- [ ] Interactive Onboarding Prototype

---

## 7. Coda Log Table Entry

| Feld | Wert |
|------|------|
| Datum | 2026-02-10 |
| Session | 10 |
| Phase | Develop |
| MECE-Bereich | Demo Assets — Video Script + Onboarding Flow |
| Hypothese | Demo Video + Onboarding are critical Keynote assets |
| Insight | Problem-led 60s script structure works best. Limitations-first onboarding is contrarian and trust-building. |
| Implikation | Three script versions for different contexts (Keynote, Product Hunt, Social). 6-screen onboarding with "The Deal" as commitment device. |
| Nächste Hypothese | H11: Limitations-First Onboarding increases perceived trustworthiness |
| Status | Develop Week 2 — Demo assets complete |

---

*Session 10 abgeschlossen: 2026-02-10, 04:00-05:00 Uhr*
