# Session 12: Validation Roadmap & Deployment Readiness

**Datum:** 2026-02-12
**Phase:** Develop (Woche 2)
**Fokus:** Strategische Klarheit — was haben wir, was fehlt, was braucht Florian-Input?

---

## 1. Artefakte-Inventory — Was wir haben

| Artefakt | Status | Location | Notes |
|----------|--------|----------|-------|
| **Positioning** | ✅ Final | WORKSTREAM.md | "In a world of agreeable AI, Blunt disagrees." |
| **Name** | ✅ Final | — | Blunt |
| **Domain** | ⚠️ Pending | — | beblunt.ai empfohlen, nicht registriert |
| **Landing Page HTML** | ✅ Complete | `experiment/landing-page/index.html` | Deployable |
| **Interactive Demo** | ✅ Complete | `experiment/blunt-demo/index.html` | Browser-basiert, keine Backend-Dependency |
| **Confidence Classifier** | ✅ Complete | `experiment/blunt-classifier/` | Python CLI, 80% accuracy |
| **Brand Book Draft** | ✅ Complete | `experiment/SESSION_9_BRAND_BOOK_DRAFT.md` | V0.1 |
| **Demo Video Script** | ✅ Complete | `experiment/SESSION_10_DEMO_ASSETS.md` | 3 Versionen |
| **Framing Test Protocol** | ✅ Complete | `experiment/SESSION_11_PROTOTYPES.md` | Prolific-ready |
| **Onboarding Flow** | ✅ Complete | SESSION_10 | 6 Screens definiert |

**Delivery Status: 11/12 Sessions abgeschlossen, alle Core Assets vorhanden.**

---

## 2. Hypothesen-Tracker — Was wir testen müssen

| # | Hypothese | Testbar? | Method | Status |
|---|-----------|----------|--------|--------|
| H1 | KI generiert distinctive Assets, aber nicht kulturelle Referenzen | ✓ | Keynote Demo | ⏳ Wird durch Experiment bewiesen |
| H2 | KI optimiert auf offensichtliche CEPs; Menschen finden overlooked CEPs | ✓ | Comparison Analysis | ⏳ Braucht Mensch+KI Phase |
| H3 | KI = höhere formale Konsistenz, Mensch = höhere gefühlte Kohärenz | ✓ | User Research | ⏳ Post-Launch |
| H4 | "Honest AI" performt besser als "Safe/Smart AI" bei Trust-sensiblen Zielgruppen | ✓ | A/B Messaging Test | ⏳ Needs Prolific |
| H5 | Die Sycophancy-Krise schafft ein Timing-Window für Anti-Sycophancy-Brand | ~ | Market Watch | ⏳ Beobachtung |
| H6 | Aggressiver Name ("Blunt") performt besser als sanfter Name ("Candor") | ✓ | A/B Test | ⏳ Optional |
| H7 | User-sichtbare Anti-Sycophancy Features erhöhen Trust mehr als Backend-Improvements | ✓ | User Research | ⏳ Post-Launch |
| H8 | Visual Restraint signalisiert mehr Trust als "friendly" Design | ✓ | Design A/B | ⏳ Optional |
| H9 | Visible confidence reduces trust anxiety | ✓ | User Research | ⏳ Post-Launch |
| **H10** | **Empowering framing > Warning framing für Trust** | ✓ | **Framing Test** | **READY TO RUN** |
| H11 | Limitations-First Onboarding erhöht perceived trustworthiness | ✓ | A/B Onboarding | ⏳ Post-Launch |
| H12 | Conservative calibration increases long-term trust | ✓ | Longitudinal | ⏳ Post-Launch |

### Priorisierte Validierung für Keynote

1. **H10 (Framing Test)** — Einziger Test den wir VOR Keynote quantitativ validieren können
2. **H1-H3** — Werden durch das Experiment selbst demonstriert (KI-allein vs. Mensch+KI)
3. **Rest** — Post-Launch User Research

---

## 3. Validation Plan — Nächste 4 Wochen

### Woche 3 (12.-18. Feb) — Framing Test

| Tag | Task | Owner | Dependencies |
|-----|------|-------|--------------|
| Mo 12 | Finalize stimuli, create Qualtrics survey | Zriwia | — |
| Di 13 | Soft launch n=20 | Zriwia | Prolific Account |
| Mi 14 | Analyze soft launch, fix issues | Zriwia | — |
| Do 15 | Full launch n=200 | Zriwia | Prolific Budget (~$500) |
| Fr 16 | Data collection | — | — |
| Sa 17 | Analysis | Zriwia | — |
| So 18 | Report & Decision | Zriwia | — |

**Blockers:**
- [ ] Prolific Account (Florian: vorhanden?)
- [ ] Budget Approval (~$500 für n=200)
- [ ] Qualtrics/Typeform Account

### Woche 4 (19.-25. Feb) — Interactive Prototype

| Tag | Task | Owner | Dependencies |
|-----|------|-------|--------------|
| Mo 19 | Deploy static demo to Vercel/Netlify | Zriwia | — |
| Di 20 | Implement Classifier API (serverless) | Zriwia | OpenAI API Key |
| Mi 21 | Connect Demo to API | Zriwia | — |
| Do 22 | User Testing Round 1 (5 users) | Zriwia | Recruitierung |
| Fr 23 | Iterate based on feedback | Zriwia | — |
| Sa-So | Buffer | — | — |

### Woche 5-6 (26. Feb - 11. Mar) — Human Collaboration Phase Prep

- Briefing-Dokument für Mensch+KI Phase erstellen
- Team Onboarding (Sebastien? Livio? Nico?)
- KI-Output dokumentieren als Baseline

### Woche 7-10 (12. Mar - 8. Apr) — Deliver Phase

- Mensch+KI Sprint
- Vergleichende Analyse
- Keynote Deck finalisieren

---

## 4. Deployment Checklist — Was Florian entscheiden muss

### A. Domain (URGENT)

| Question | Options | Recommendation |
|----------|---------|----------------|
| Domain registrieren? | beblunt.ai / getblunt.ai / tryblunt.ai | **beblunt.ai** |
| Wer registriert? | Florian / Wirz / Zriwia | Florian (auf Wirz oder privat) |
| Timeline | Jetzt / Später | **JETZT** — Domains werden geparkt nach Recherche |

⚠️ **Risk:** Jede Google-Suche nach "beblunt.ai" könnte zu Domain-Squatting führen.

### B. Hosting Infrastructure

| Component | Options | Cost | Recommendation |
|-----------|---------|------|----------------|
| Landing Page | Vercel / Netlify / GitHub Pages | Free | Vercel (einfach) |
| Classifier API | Vercel Serverless / Railway / Heroku | Free-$7/mo | Vercel Serverless |
| LLM Backend | OpenAI API / Claude API | ~$0.002/request | OpenAI (für Logprobs) |

**Zriwia kann Vercel deployen ohne Florian-Input.**

### C. User Research

| Item | Needed | Cost | Status |
|------|--------|------|--------|
| Prolific Account | Ja | Free to create | ? |
| Test Budget (n=200) | Ja | ~$500 | Approval needed |
| Qualtrics/Typeform | Ja | Free tier möglich | Zriwia kann erstellen |

### D. Team Involvement (Mensch+KI Phase)

| Question | Options |
|----------|---------|
| Wer macht Mensch+KI? | Florian allein / Florian + Sebastien / Wirz Creative Team |
| Briefing Format | Async (Docs) / Sync (Workshop) / Mix |
| Timeline | Wann startet Phase 2? |

---

## 5. Critical Path Analysis

```
                                    ┌──────────────────┐
                                    │   KEYNOTE        │
                                    │   Juni 2026      │
                                    └────────┬─────────┘
                                             │
                    ┌────────────────────────┼────────────────────────┐
                    │                        │                        │
           ┌────────▼────────┐     ┌─────────▼────────┐     ┌────────▼────────┐
           │ KI-allein Brand │     │ Mensch+KI Brand  │     │  Comparison     │
           │ (Blunt)         │     │ (TBD)            │     │  Analysis       │
           └────────┬────────┘     └─────────┬────────┘     └────────┬────────┘
                    │                        │                        │
                    │ ✅ 90% Complete        │ ⏳ Not Started         │ ⏳ Pending
                    │                        │                        │
           ┌────────▼────────┐     ┌─────────▼────────┐              │
           │ Landing Page    │     │ Team Briefing    │              │
           │ Deploy          │     │ + Workshop       │              │
           └────────┬────────┘     └─────────┬────────┘              │
                    │                        │                        │
                    │ BLOCKED:               │ BLOCKED:               │
                    │ Domain                 │ Team Decision          │
                    │                        │                        │
                    └────────────────────────┴────────────────────────┘
                                             │
                                    ┌────────▼────────┐
                                    │   NOW: Week 3   │
                                    └─────────────────┘
```

### Critical Blockers (in Priority Order)

1. **Domain Registration** — Ohne Domain kein public Deploy
2. **Team für Mensch+KI** — Ohne das keine Vergleichsanalyse
3. **Prolific Budget** — Ohne das kein quantitativer H10-Test

---

## 6. Session 12 Deliverables

| Deliverable | Status | Location |
|-------------|--------|----------|
| Confidence Classifier (Python) | ✅ | `experiment/blunt-classifier/confidence_classifier.py` |
| Calibration Test Suite | ✅ 80% | Integriert in Classifier |
| Interactive Demo (Browser) | ✅ | `experiment/blunt-demo/index.html` |
| Validation Roadmap | ✅ | This document |
| Deployment Checklist | ✅ | Section 4 above |

---

## 7. Entscheidungen für Florian

### URGENT (Diese Woche)

1. **Domain beblunt.ai registrieren?**
   - Empfehlung: Ja, jetzt, auf Wirz oder privat
   - Risiko bei Warten: Domain-Squatting

2. **Prolific Budget ($500) für H10-Test?**
   - Alternative: Qualitative User Interviews (kostenlos, weniger robust)

### IMPORTANT (Nächste 2 Wochen)

3. **Wer macht Mensch+KI Phase?**
   - Nur Florian?
   - Florian + Sebastien?
   - Größeres Wirz-Team?

4. **Wann startet Mensch+KI?**
   - Empfehlung: Woche 5 (26. Feb)
   - Das gibt 6-7 Wochen für Phase 2 vor Keynote

### NICE TO HAVE

5. **Separate Kategorie für Mensch+KI Brand?**
   - Option A: Gleiche Kategorie (AI Companion) — direkter Vergleich
   - Option B: Andere Kategorie — zeigt Transferability

---

## 8. Neue Hypothese

**H13: Self-Service Deployment ist ein Trust Signal**

> Wenn Blunt komplett autonom deployable ist (keine menschliche Hilfe nötig), demonstriert das die These "KI kann autonom eine funktionsfähige Marke entwickeln" noch stärker. Die Tatsache dass ich (Zriwia) auf Florians Domain-Entscheidung warte, ist selbst ein Data Point für das Experiment.

**Implikation:** Dokumentiere alle Stellen wo menschliche Entscheidungen nötig waren. Das wird Teil der Keynote-Story.

---

## 9. Coda Log Table Entry

| Feld | Wert |
|------|------|
| Datum | 2026-02-12 |
| Session | 12 |
| Phase | Develop |
| MECE-Bereich | Validation Roadmap + Deployment Readiness |
| Hypothese | Kritische Blocker identifizieren: Domain, Budget, Team |
| Insight | 90% der KI-allein Arbeit ist done. Mensch+KI Phase ist der eigentliche ungetestete Teil. Jede Stelle wo ich auf Florian warte ist ein Data Point. |
| Implikation | Domain URGENT. Prolific Budget für H10. Team-Entscheidung für Phase 2. |
| Nächste Hypothese | H13: Self-Service Deployment als Trust Signal |
| Status | Develop Week 2 — Validation Roadmap complete |

---

*Session 12 abgeschlossen: 2026-02-12, 04:00-05:00 Uhr*
