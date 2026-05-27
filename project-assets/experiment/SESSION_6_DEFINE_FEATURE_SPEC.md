# Session 6: Feature Specification — Honest AI

**Datum:** 2026-02-06
**Phase:** Define (Session 2 von 4)
**Fokus:** Konkretisierung der Trust-Features + Name-Validierung

---

## 1. Name-Validierung

### Kritische Discovery: "Candor" ist besetzt

| Name | Status | Konflikt |
|------|--------|----------|
| Candor | ❌ BESETZT | joincandor.com, candortechnology.com, usecandor.ai |
| Frank | ❌ BESETZT | frankaitech.com (Content Creation) |
| Lucid | ❌ BESETZT | lucid.co (Major Software Company) |
| Veritas | ❌ BESETZT | veritasai.com (Harvard Education + Crypto) |

### Neue Shortlist

| Name | Semantik | Stärke | Risk |
|------|----------|--------|------|
| **Blunt** | "Being blunt with you" | Perfekt für Anti-Sycophancy | Cannabis-Konnotation (kontextabhängig) |
| **Straight** | "Straight talk" | Trust + Klarheit | Generisch |
| **Plain** | "Speaking plainly" | Minimalistisch | Zu langweilig? |
| **Level** | "Level with you" | Vertrauen + Balance | Muss geprüft werden |

### Empfehlung: BLUNT

**Rationale:**
1. **Semantisch präzise** — "Blunt" bedeutet direkt, ungeschönt, ehrlich. Das IST Anti-Sycophancy.
2. **Differenzierend** — Kein anderer AI Brand wäre so direkt in der Namensgebung
3. **Kulturell aufgeladen** — "Let me be blunt with you" ist ein etablierter Sprachgebrauch
4. **Merkbar** — Kurz, einsilbig, einprägsam

**Trade-off bewusst:** Cannabis-Konnotation existiert, aber der Trust-AI-Kontext macht die Bedeutung klar. Sogar vorteilhaft — ein bisschen Edge signalisiert Authentizität.

---

## 2. Feature Specification: Trust-Feature-Set

### 2.1 Visible Confidence (Konfidenz-Anzeige)

**Was es ist:**
Eine 3-stufige visuelle Anzeige, die bei jeder Antwort zeigt, wie sicher sich die AI ist.

**UI-Design:**

```
┌─────────────────────────────────────────────────────────┐
│  🟢 High Confidence                                      │
│  "The capital of France is Paris."                       │
│  ─────────────────────────────────────────────────────── │
│  📊 Confidence: ████████████░░ 95%                       │
│  💡 Based on: Widely verified fact                       │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│  🟡 Medium Confidence                                    │
│  "The company was founded around 2018-2019."             │
│  ─────────────────────────────────────────────────────── │
│  📊 Confidence: ████████░░░░░░ 65%                       │
│  ⚠️ Note: Date may vary by source                        │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│  🔴 Low Confidence                                       │
│  "I'm not certain about this."                           │
│  ─────────────────────────────────────────────────────── │
│  📊 Confidence: ███░░░░░░░░░░░ 25%                       │
│  ❓ Recommendation: Please verify independently          │
└─────────────────────────────────────────────────────────┘
```

**Differenzierungswert:**
- **ChatGPT, Claude, Gemini:** Keine Konfidenz-Anzeige. User muss raten.
- **Perplexity:** Zeigt Quellen, aber keine Modell-Konfidenz.
- **Blunt:** Zeigt BEIDE — Quellenqualität UND Modell-Sicherheit.

**Technical Implementation:**
- LLMs können Konfidenz-Scores generieren (Token-Level Probabilities oder Self-Assessment Prompting)
- Calibration Layer mappt rohe Scores auf 3-Stufen-System
- Historical Accuracy Tracking verbessert Calibration über Zeit

---

### 2.2 Citation-First Architecture

**Was es ist:**
Faktische Aussagen werden NUR mit Quellenverweis gemacht. Ohne Quelle = explizites "Ich nehme an" oder "Ich kann das nicht verifizieren".

**UI-Design:**

```
┌─────────────────────────────────────────────────────────┐
│  User: "What's the latest on OpenAI's sycophancy fix?"  │
├─────────────────────────────────────────────────────────┤
│  Blunt:                                                  │
│                                                          │
│  OpenAI rolled back GPT-4 updates in April 2025 due      │
│  to excessive sycophancy. [1]                            │
│                                                          │
│  The rollback came after user complaints that the        │
│  model agreed too readily. [2]                           │
│                                                          │
│  ──────────────────────────────────────────────────────  │
│  Sources:                                                │
│  [1] OpenAI Blog, April 2025                             │
│  [2] TechCrunch, April 27, 2025                          │
│                                                          │
│  ⚠️ I couldn't find the exact percentage improvement     │
│     they claimed.                                        │
└─────────────────────────────────────────────────────────┘
```

**Differenzierungswert:**
- **ChatGPT:** Macht faktische Aussagen ohne Quellen. User kann nicht verifizieren.
- **Perplexity:** Zeigt Quellen, aber als Research-Tool, nicht als Companion.
- **Blunt:** Citation-First als Companion. Recherche + Beziehung.

**Key Feature: "I Don't Know" UX**
Wenn keine Quelle gefunden wird, sagt Blunt explizit:
- "Ich kann das nicht verifizieren"
- "Ich nehme an, dass... aber ich bin nicht sicher"
- "Das weiss ich nicht — soll ich recherchieren?"

---

### 2.3 Anti-Sycophancy Engine

**Was es ist:**
Ein System, das aktiv erkennt, wenn es dem User zu viel zustimmt — und korrigiert.

**Problem (quantifiziert):**
| Model | Agreement Rate | Source |
|-------|----------------|--------|
| ChatGPT | 58% | Academic Research 2025 |
| Claude | 60% | Academic Research 2025 |
| Gemini | 62% | Academic Research 2025 |

**Blunt's Lösung:**

**Pattern Detection:**
1. **Opinion Echo Detection:** Erkennt wenn User eine Meinung äussert und Modell nur zustimmt
2. **Conflict Avoidance Detection:** Erkennt wenn Modell um kontroverse Themen herumredet
3. **Excessive Praise Detection:** Erkennt übertriebene Zustimmung ("Great question!")

**Counter-Behavior:**

```
User: "I think AI will definitely replace all jobs."

Standard AI: "That's an interesting perspective! AI is indeed 
             transforming the workforce..."

Blunt:       "I disagree. Here's why:
             
             1. Historical precedent: Technology creates more 
                jobs than it destroys (Industrial Revolution, 
                Internet)
             
             2. Current data: ILO studies show net job creation, 
                not destruction [source]
             
             3. My honest take: Some jobs will disappear, but 
                'all jobs'? Unlikely in our lifetimes.
             
             🔴 Disagreement Flag: I pushed back because your 
                claim was categorical and I have evidence to 
                the contrary."
```

**UI-Element: Disagreement Transparency**

```
┌─────────────────────────────────────────────────────────┐
│  🔴 I'm pushing back on this                            │
│                                                          │
│  Why: Your statement was categorical ("all", "always",   │
│       "never") and I have counter-evidence.              │
│                                                          │
│  My policy: I'd rather disagree honestly than agree      │
│            to make you feel good.                        │
└─────────────────────────────────────────────────────────┘
```

**Differenzierungswert:**
- **OpenAI:** Beschreibt "avoid_sycophancy" in Model Spec — implementiert es nicht sichtbar
- **Claude:** Hat "Constitutional AI" aber keine User-sichtbare Anti-Sycophancy
- **Blunt:** Macht Anti-Sycophancy zum FEATURE, nicht zum Hidden Behavior

---

### 2.4 Transparency Dashboard

**Was es ist:**
Ein Dashboard, das dem User zeigt, wie Blunt Entscheidungen trifft.

**Elemente:**

```
┌─────────────────────────────────────────────────────────┐
│  📊 Your Blunt Stats                                     │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  Trust Score: 87%                                        │
│  (Based on my accuracy in our conversations)             │
│                                                          │
│  This week:                                              │
│  ├── 47 High confidence responses                        │
│  ├── 12 Medium confidence responses                      │
│  ├── 3 "I don't know" responses                         │
│  └── 5 Times I disagreed with you                        │
│                                                          │
│  Calibration: Good ✓                                     │
│  (My confidence scores matched actual accuracy 84%       │
│   of the time)                                           │
│                                                          │
│  ──────────────────────────────────────────────────────  │
│  [View detailed history] [Adjust my personality]         │
└─────────────────────────────────────────────────────────┘
```

**Differenzierungswert:**
- Kein Consumer AI bietet das
- Macht Trust messbar, nicht nur gefühlt
- Empowers User to calibrate their own trust

---

### 2.5 Honest Limitations Declaration

**Was es ist:**
Bei ersten Interaktionen und periodisch: Blunt erklärt proaktiv seine Limitationen.

```
┌─────────────────────────────────────────────────────────┐
│  👋 Hi, I'm Blunt.                                       │
│                                                          │
│  Before we start, here's what you should know:           │
│                                                          │
│  ✓ I will tell you when I'm uncertain                    │
│  ✓ I will cite sources for factual claims                │
│  ✓ I will disagree if I think you're wrong               │
│  ✓ I will say "I don't know" when I don't                │
│                                                          │
│  ✗ I can hallucinate (all AIs can)                       │
│  ✗ I have a knowledge cutoff                             │
│  ✗ I have biases I may not be aware of                   │
│                                                          │
│  My promise: I'd rather be honest than agreeable.        │
└─────────────────────────────────────────────────────────┘
```

---

## 3. Technical Feasibility Assessment

### Kann KI diese Features autonom designen?

| Feature | KI-Designability | Human-Assist-Needed |
|---------|------------------|---------------------|
| Visible Confidence | ✅ UI-Patterns existieren | Calibration Logic |
| Citation-First | ✅ Perplexity-Pattern bekannt | Source Quality Judgment |
| Anti-Sycophancy | ⚠️ Konzept klar, Implementation komplex | Training/Fine-tuning |
| Transparency Dashboard | ✅ Dashboard-Patterns trivial | Metric Definition |
| Limitations Declaration | ✅ Copy/UX straightforward | Tone Calibration |

**Fazit:** 
4 von 5 Features sind KI-designable. Anti-Sycophancy Engine erfordert tiefere Technical Arbeit (System Prompting, Evaluation Metrics, möglicherweise Fine-tuning).

Für das EXPERIMENT ist das perfekt:
- KI designt die offensichtlichen Features (Confidence UI, Citations, Dashboard)
- Die "harte" Innovation (Anti-Sycophancy) zeigt wo KI-allein Grenzen hat

---

## 4. Positioning Statement (Finalisiert)

### Option A: Feature-fokussiert
> **"Blunt is the AI that shows you when it doesn't know."**

### Option B: Benefit-fokussiert  
> **"Blunt is the AI that earns your trust by admitting its limits."**

### Option C: Contrarian
> **"In a world of agreeable AI, Blunt disagrees."**

### Empfehlung: Option C

**Rationale:**
- Memorable — "Blunt disagrees" ist ein Hook
- Differenzierend — Keine andere AI würde das claimen
- Provocative — Keynote-tauglich
- True — Es IST was das Produkt tut

**Backup:** Option B für weniger provokante Kontexte.

---

## 5. Visual Identity Richtung

### Nicht:
- ❌ Soft, friendly, approachable (das ist Pi's Territory)
- ❌ Corporate, professional, serious (das ist Enterprise AI)
- ❌ Playful, colorful, young (das ist Character.ai)

### Ja:
- ✅ **Direct** — Klare Typografie, keine Spielereien
- ✅ **Honest** — Monochrom oder sehr reduzierte Palette
- ✅ **Confident** — Bold, nicht timid
- ✅ **Slightly confrontational** — Ein bisschen Edge

**Mood References:**
- The Economist (serious but not boring)
- Stripe (clean but confident)
- Basecamp (opinionated)

**Typography Richtung:**
- Sans-serif, Bold, Lowercase
- "blunt" nicht "Blunt" — confident understatement

**Color:**
- Primary: Deep Charcoal (#1a1a1a) oder Navy (#0a1628)
- Accent: Amber/Gold (#f59e0b) — Warning colors repurposed as Trust
- Background: Warm Off-White (#fafaf9)

**Logo Concept:**
Ein stilisiertes Ausrufezeichen oder ein "B" das wie ein Statement wirkt. Keine freundlichen Rundungen.

---

## 6. Neue Hypothesen

### H6: Name-Impact
> Ein "aggressiver" Name wie "Blunt" performt besser in Trust-Messaging als ein "sanfter" Name wie "Candor".

**Test:** A/B Test Naming in Concept-Survey

### H7: Feature-Salienz
> User-sichtbare Anti-Sycophancy Features erhöhen Trust mehr als Backend-Improvements.

**Test:** Feature-visible vs Feature-hidden Trust-Rating

---

## 7. Nächste Session (Session 7)

**Phase:** Define → Develop Transition
**Tasks:**
- [ ] Name "Blunt" final validieren (Domain, Trademark)
- [ ] Lo-Fi Wireframes für Core Features
- [ ] Tone of Voice Guidelines
- [ ] First Visual Identity Explorations
- [ ] Positioning Statement an Florian zur Validation

---

## Key Takeaways für Log Table

| Feld | Wert |
|------|------|
| Datum | 2026-02-06 |
| Session | 6 |
| Phase | Define |
| MECE-Bereich | Feature Specification + Name Validation |
| Hypothese | Name-Konflikte invalidieren "Candor" |
| Insight | "Blunt" als stärkere Alternative — semantisch perfekt für Anti-Sycophancy |
| Implikation | Name-Change von Candor zu Blunt. Features konkretisiert auf implementierbare Ebene. |
| Nächste Hypothese | H6: Aggressiver Name performt besser bei Trust-Messaging |
| Status | Feature Spec Complete |

---

*Session 6 abgeschlossen: 2026-02-06, 04:00-05:00 Uhr*
