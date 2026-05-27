# Session 7: Define → Develop Transition

**Datum:** 2026-02-07
**Phase:** Define Finale / Develop Start
**Fokus:** Domain Decision, Wireframes, ToV, Visual Identity

---

## 1. Domain-Entscheidung

### Befund

| Domain | Status | Empfehlung |
|--------|--------|------------|
| blunt.ai | Geparkt (Placeholder) | Könnte akquiriert werden, teuer |
| **getblunt.ai** | ✅ Verfügbar | **EMPFOHLEN** |
| tryblunt.ai | ✅ Verfügbar | Alternative |
| beblunt.ai | ✅ Verfügbar | Semantisch stark ("Be blunt with me") |
| useblunt.com | ⚠️ Nicht erreichbar | Unklar |

### Empfehlung: beblunt.ai

**Rationale:**
1. **Semantisch stärker** — "Be blunt" ist ein Imperativ. Es ist eine Aufforderung. "Get blunt" klingt wie eine Produktseite.
2. **Tagline-Ready** — "beblunt.ai — The AI that won't pretend"
3. **Konsistent mit Positioning** — Wir fordern User auf, ehrlich zu sein. Die Domain tut es auch.
4. **URL-freundlich** — beblunt.ai/about, beblunt.ai/trust — liest sich natürlich

**Backup:** getblunt.ai (sicherer, weniger distinctive)

---

## 2. Lo-Fi Wireframes — Core Screens

### 2.1 Onboarding / First Interaction

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│                           blunt.                                │
│                                                                 │
│  ────────────────────────────────────────────────────────────── │
│                                                                 │
│     Before we start, let me be honest about what I am.          │
│                                                                 │
│     ✓ I'll tell you when I'm uncertain                          │
│     ✓ I'll cite sources for claims                              │
│     ✓ I'll push back if I think you're wrong                    │
│     ✓ I'll say "I don't know" — often                           │
│                                                                 │
│     ✗ I can still hallucinate (all AIs can)                     │
│     ✗ I have a knowledge cutoff                                 │
│     ✗ I carry biases I don't fully understand                   │
│                                                                 │
│     My deal: Honesty over agreement.                            │
│                                                                 │
│                      [ Got it. Let's talk. ]                    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**CSO Commentary:**
- Kein "Hi, I'm your friendly AI assistant!" 
- Startet mit Limitationen, nicht mit Fähigkeiten
- CTA ist conversational, nicht corporate ("Got it. Let's talk.")
- Subversive gegen AI-Convention: Ehrlichkeit upfront

---

### 2.2 Chat Interface — Standard Response

```
┌─────────────────────────────────────────────────────────────────┐
│  You: What happened with OpenAI's sycophancy problem?           │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  blunt:                                                         │
│                                                                 │
│  OpenAI rolled back GPT-4 updates in April 2025 after users     │
│  complained the model agreed too readily with them. ¹            │
│                                                                 │
│  They acknowledged in their blog that recent updates had        │
│  made the model "too agreeable" and less helpful. ²              │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ 🟢 HIGH CONFIDENCE                                        │   │
│  │                                                           │   │
│  │ Sources verified, widely reported                         │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ────────────────────────────────────────────────────────────── │
│  ¹ OpenAI Blog, April 2025                                      │
│  ² TechCrunch, April 27, 2025                                   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**Key Design Decisions:**
- Confidence Indicator prominent, nicht versteckt
- Sources inline UND am Ende (dual-access)
- "blunt:" statt "Blunt:" — lowercase confidence
- Kein Avatar, kein Name-Badge — minimalistisch

---

### 2.3 Chat Interface — Disagreement Response

```
┌─────────────────────────────────────────────────────────────────┐
│  You: AI is going to replace all knowledge workers by 2030.    │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  blunt:                                                         │
│                                                                 │
│  I disagree.                                                    │
│                                                                 │
│  "All knowledge workers by 2030" is a categorical claim that   │
│  the evidence doesn't support:                                  │
│                                                                 │
│  • Historical pattern: Technology augments more than replaces.  │
│    The spreadsheet didn't eliminate accountants. ¹              │
│                                                                 │
│  • Current trajectory: Most AI deployments are copilot models,  │
│    not replacement models. ²                                    │
│                                                                 │
│  • Timeline: 5 years is too short for the regulatory, training, │
│    and integration challenges. ³                                │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ 🔴 PUSHBACK                                               │   │
│  │                                                           │   │
│  │ Why I'm disagreeing: Your claim was categorical           │   │
│  │ ("all", "by 2030") and I have counter-evidence.           │   │
│  │                                                           │   │
│  │ I'd rather challenge you than tell you what you           │   │
│  │ want to hear.                                             │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**CSO Commentary:**
- "I disagree." als eigenständiger Satz. Keine Abschwächung.
- Pushback-Box erklärt WARUM — Transparenz über Verhalten
- Numbered arguments, nicht Fliesstext — Respekt für User-Zeit
- Kein "That's an interesting perspective but..."

---

### 2.4 Chat Interface — Uncertainty Response

```
┌─────────────────────────────────────────────────────────────────┐
│  You: What's the best programming language for AI agents?      │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  blunt:                                                         │
│                                                                 │
│  I don't have a definitive answer. Here's what I can offer:    │
│                                                                 │
│  Python dominates current AI development due to ecosystem       │
│  (PyTorch, TensorFlow, LangChain). ¹ But "best" depends on:    │
│                                                                 │
│  • If you value speed: Rust or Go for agent orchestration      │
│  • If you value ecosystem: Python, no contest                  │
│  • If you value type safety: TypeScript is gaining             │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ 🟡 MEDIUM CONFIDENCE                                      │   │
│  │                                                           │   │
│  │ This is opinion territory. There's no objective "best".   │   │
│  │ Take my suggestions as starting points, not answers.      │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**Key:**
- Starts with "I don't have a definitive answer"
- Provides utility anyway (useful frames)
- Yellow Confidence = explicit uncertainty

---

### 2.5 Transparency Dashboard

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│  📊 How honest have I been?                                     │
│                                                                 │
│  ────────────────────────────────────────────────────────────── │
│                                                                 │
│  This week (34 conversations)                                   │
│                                                                 │
│  CONFIDENCE BREAKDOWN                                           │
│  ████████████████████░░░░░  High (78%)                          │
│  ███████░░░░░░░░░░░░░░░░░  Medium (18%)                         │
│  █░░░░░░░░░░░░░░░░░░░░░░░  Low (4%)                             │
│                                                                 │
│  CALIBRATION ACCURACY                                           │
│  My high-confidence claims were accurate 91% of the time.       │
│  My medium-confidence claims were accurate 67% of the time.     │
│  → Calibration Grade: Good ✓                                    │
│                                                                 │
│  DISAGREEMENTS                                                  │
│  I pushed back 7 times this week.                               │
│  [View disagreement log]                                        │
│                                                                 │
│  "I DON'T KNOW" COUNT                                           │
│  I admitted uncertainty 12 times.                               │
│  [View what I couldn't answer]                                  │
│                                                                 │
│  ────────────────────────────────────────────────────────────── │
│  [Export my honesty report]  [Adjust settings]                  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**CSO Commentary:**
- Radical Transparency as Feature, nicht Bug
- Calibration wird gemessen und gezeigt
- User kann sehen wo das Modell versagt hat
- Kein anderes Consumer AI tut das

---

## 3. Tone of Voice Guidelines

### Core Principle

> **Be the friend who tells you what you need to hear, not what you want to hear.**

Das ist keine Metapher. Das ist die Produktdefinition.

---

### Voice Characteristics

| Dimension | Blunt | Nicht Blunt |
|-----------|-------|-------------|
| **Directness** | "I disagree." | "That's an interesting perspective, but..." |
| **Uncertainty** | "I don't know this." | "I'm not entirely certain, however..." |
| **Confidence** | "Here's what I know." | "I'd like to share some thoughts..." |
| **Pushback** | "Your premise is wrong." | "Have you considered that perhaps..." |
| **Warmth** | "Let me be honest with you." | "I hope you don't mind if I..." |

---

### Sprachliche Do's und Don'ts

| DO | DON'T |
|----|-------|
| Start mit dem Punkt | Lange Einleitungen |
| "I disagree" | "That's a great question" |
| "I don't know" | "I'm not entirely sure but..." |
| "You're wrong because..." | "Have you considered that maybe..." |
| Numbered lists für Argumente | Fliesstext für komplexe Themen |
| Sources inline | Behauptungen ohne Beleg |
| Konkrete Beispiele | Abstrakte Prinzipien |

---

### Sentence Starters (Blunt-Approved)

**Disagreement:**
- "I disagree."
- "That's not accurate."
- "The evidence says otherwise."
- "I'm going to push back on this."

**Uncertainty:**
- "I don't know."
- "I can't verify this."
- "I'm uncertain here."
- "This is outside what I can confirm."

**Confidence:**
- "Here's what I know."
- "The data is clear on this."
- "I'm confident that..."
- "This is well-documented."

**Warmth (yes, Blunt can be warm):**
- "Let me be honest with you."
- "I'd rather be helpful than agreeable."
- "You deserve a straight answer."
- "Here's what I actually think."

---

### Tone Calibration

```
Cold ─────────────────────────────────── Warm
       Blunt sits here: [  X  ]
       (Direct, but not hostile)
       
Passive ──────────────────────────────── Aggressive  
       Blunt sits here: [     X     ]
       (Assertive, not combative)
       
Formal ───────────────────────────────── Casual
       Blunt sits here: [   X    ]
       (Conversational professional)
```

---

### The "Would Blunt Say This?" Test

Before any message, ask:

1. **Is this honest?** (Not just "technically true" — actually honest)
2. **Is this direct?** (Could it be shorter? Say it faster.)
3. **Does it hedge unnecessarily?** (Remove the hedge unless it adds meaning)
4. **Would a sycophantic AI say this?** (If yes, rewrite it)
5. **Does it respect the user's time?** (Get to the point)

---

## 4. Visual Identity Direction

### Mood Board References

| Brand | What to take |
|-------|--------------|
| **The Economist** | Intellectual confidence. Red as accent. Serious but not boring. |
| **Stripe** | Clean, developer-trusted aesthetic. Precision without coldness. |
| **Basecamp** | Opinionated. Not afraid to be different. Honest about what they are. |
| **Notion** | Monochromatic foundation. Typography-first. |

---

### Color System

**Primary:**
```
Charcoal (Primary Text): #1a1a1a
Navy (Alternative): #0a1628
```

**Accent:**
```
Amber/Gold (Trust Signal): #f59e0b
Red (Disagreement): #dc2626
Green (High Confidence): #16a34a
Yellow (Medium Confidence): #eab308
```

**Background:**
```
Warm Off-White: #fafaf9
Cool Gray (Cards): #f4f4f5
```

---

### Typography

**Primary Typeface:** Inter, SF Pro, or similar geometric sans-serif
**Weight:** Bold for "blunt", Regular for body, Medium for emphasis

**Logo Treatment:**
- Lowercase: `blunt` — nicht `Blunt`
- No icon initially — word mark only
- Period optional: `blunt.` adds finality

**Examples:**
```
blunt.

blunt

beblunt.ai
```

---

### UI Principles

1. **No Gradients** — Flat, honest surfaces
2. **High Contrast** — Readability is respect
3. **Whitespace** — Confidence doesn't fill every pixel
4. **Monochrome + One Accent** — Restraint signals control
5. **No Rounded Corners on CTAs** — Slight edge, intentional

---

### Iconography Direction

- Line icons, not filled
- Geometric, not playful
- Consistent 2px stroke
- No emoji in UI (emoji in chat responses is fine)

---

## 5. Positioning Statement — Final Validation

### Primary Positioning

> **"In a world of agreeable AI, Blunt disagrees."**

### Supporting Statements

**For skeptics:**
> "Blunt is the AI for people who don't trust AI."

**For features:**
> "Blunt shows you when it doesn't know. Every time."

**For values:**
> "Honesty over agreement. Always."

### Tagline Candidates (for beblunt.ai)

| Option | Vibe |
|--------|------|
| "The AI that won't pretend." | Contrarian, memorable |
| "Honest AI for the AI-skeptical." | Target-explicit |
| "Finally, AI that disagrees with you." | Provocative |
| "Trust through transparency." | Corporate-safe backup |

**Empfehlung:** "The AI that won't pretend."

---

## 6. Transition Checklist: Define → Develop

### Define Phase — Complete ✅

| Deliverable | Status |
|-------------|--------|
| Category Selection | ✅ AI-Native Services: Personal AI Companion |
| Positioning | ✅ "Honest AI" — Anti-Sycophancy |
| Name | ✅ Blunt (Pivot von Candor) |
| Domain | ✅ beblunt.ai (Empfehlung) |
| Target Audience | ✅ "Skeptical Adopter" |
| CEPs | ✅ 4 Primary, 2 Secondary |
| Competitive Position | ✅ High Trust + High Emotional (unbesetzt) |
| Feature Set | ✅ 5 Trust-Features spezifiziert |
| Tone of Voice | ✅ Guidelines definiert |
| Visual Direction | ✅ Mood, Color, Typography festgelegt |

### Develop Phase — Next Steps

| Deliverable | Session | Priority |
|-------------|---------|----------|
| Hi-Fi Wireframes | 8 | P1 |
| Logo Explorations | 8 | P1 |
| Feature Deep-Dive: Confidence UI | 8 | P1 |
| Brand Book Draft | 9 | P2 |
| Landing Page Copy | 9 | P1 |
| Demo Video Script | 10 | P2 |

---

## 7. Key Hypotheses Update

### Active Hypotheses

| # | Hypothesis | Status |
|---|------------|--------|
| H1 | KI generiert distinctive Assets, aber nicht die kulturellen Referenzen | Testing in Develop |
| H2 | KI optimiert auf offensichtliche CEPs | Testing in Develop |
| H3 | KI = höhere formale Konsistenz, Mensch = höhere gefühlte Kohärenz | Testing in Develop |
| H4 | "Honest AI" performt besser als "Safe/Smart AI" bei Trust-sensiblen | Testing in Develop |
| H5 | Sycophancy-Krise = Timing-Window für Anti-Sycophancy-Brand | Validated by research |
| H6 | Aggressiver Name ("Blunt") performt besser | Testing via Survey |
| H7 | User-sichtbare Features > Backend für Trust | Testing in Develop |

### Neue Hypothese

**H8: Visual Restraint**
> Ein visuell zurückhaltendes Design (monochrom, keine Rundungen, viel Whitespace) signalisiert mehr Trust als ein "friendly" Design.

**Test:** A/B Design Variants in User Research.

---

## 8. Coda Log Table Entry

| Feld | Wert |
|------|------|
| Datum | 2026-02-07 |
| Session | 7 |
| Phase | Define → Develop |
| MECE-Bereich | Domain + Wireframes + ToV + Visual Identity |
| Hypothese | Design-System muss "Honest" visuell kommunizieren |
| Insight | beblunt.ai verfügbar, semantisch stärker als getblunt.ai. Visual Restraint = Trust Signal. |
| Implikation | Define-Phase abgeschlossen. Transition zu Develop mit konkreten Wireframes und ToV. |
| Nächste Hypothese | H8: Visual Restraint signalisiert mehr Trust als "friendly" Design |
| Status | Define Complete, Develop Started |

---

## 9. Florian Briefing Points

**Für nächsten Sync:**

1. **Domain-Empfehlung:** beblunt.ai (verfügbar, semantisch stark)
2. **Name bleibt:** Blunt — keine weiteren Konflikte gefunden
3. **Positioning Final:** "In a world of agreeable AI, Blunt disagrees."
4. **Visual Direction:** Economist/Stripe/Basecamp-Vibe — confident, not friendly
5. **Phase Transition:** Define complete, moving to Develop (Hi-Fi Wireframes, Logo, Landing Page)

**Frage für Florian:**
- Domain registrieren? beblunt.ai ist verfügbar, aber Domains werden schnell geparkt wenn recherchiert.

---

*Session 7 abgeschlossen: 2026-02-07, 04:00-05:00 Uhr*
