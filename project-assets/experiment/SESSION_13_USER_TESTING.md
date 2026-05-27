# Session 13: User Testing Round 0 & Prolific Prep

**Datum:** 2026-02-13
**Phase:** Develop (Woche 3)
**Fokus:** Validation vor Launch

---

## 1. User Testing Round 0 — Internes Testing

### Ziel
Qualitatives Feedback zur Survey UX vor Prolific-Launch. Keine Statistik, nur Usability.

### Testpersonen (3 intern)
| Person | Rolle | Warum relevant |
|--------|-------|----------------|
| Sebastien | Team | Tech-affin, kennt Experiment-Kontext |
| Nico | Kollege | Marketing-Perspektive, AI-curious |
| Livio | CCO | Creative Leadership, skeptische Perspektive |

**Alternative:** Falls Kollegen nicht verfügbar → Florian's persönliches Netzwerk.

### Test-Protokoll

**Vor dem Test:**
1. Browser-Konsole öffnen (für localStorage-Daten)
2. URL in neuem Inkognito-Fenster öffnen
3. Screen-Recording aktivieren (optional)

**Während des Tests:**
"Bitte nimm dir 5 Minuten für diese kurze Studie. Denk laut — sag, was dir auffällt, was unklar ist, was dich stört."

**Nach dem Test (5 Fragen):**
1. "War irgendwas unklar?"
2. "Hast du das Confidence-Display verstanden?"
3. "Welche Version hast du gesehen?" (Condition A/B Check)
4. "Wie lang hat es sich angefühlt?"
5. "Würdest du das auf Prolific machen für £1.25?"

**Daten exportieren:**
```javascript
// In Browser-Konsole nach Completion:
console.log(localStorage.getItem('h10_responses'));
```

### Erwartete Issues (Hypothesen)

| Potentielles Problem | Severity | Fix |
|---------------------|----------|-----|
| Confidence-Display unklar | HIGH | Text anpassen |
| Attention Check zu offensichtlich | MEDIUM | Subtiler formulieren |
| Completion Code verwirrend | LOW | UX verbessern |
| Zu lang | MEDIUM | Steps kürzen |

---

## 2. Prolific Study Configuration

### Study Details (Ready to Submit)

| Field | Value |
|-------|-------|
| **Study Name** | H10 Framing Test - AI Trust Perceptions |
| **Description** | Evaluate an AI assistant's response and share your impressions. Simple rating questions. |
| **URL** | https://zriwia.github.io/blunt-demo/h10-survey.html |
| **Completion Code** | Dynamic (BLUNT-H10-X-XXXX) |
| **Estimated Time** | 5 minutes |
| **Reward** | £1.25 |
| **Platform Fee** | ~£0.54 (43%) |
| **Total per Participant** | ~£1.79 |

### Sample Configuration

| Sample | n | Cost | Purpose |
|--------|---|------|---------|
| **Soft Launch** | 20 | ~£36 | Test data quality, catch issues |
| **Full Launch** | 180 | ~£322 | Powered for significance |
| **Total** | 200 | ~£358 | Matches budget (£125 loaded + ~£233 needed) |

### Pre-Screening (Prolific Filters)

| Filter | Value | Rationale |
|--------|-------|-----------|
| Language | English (Native/Fluent) | Survey in English |
| Age | 18-65 | Adult population |
| Approval Rate | ≥95% | Quality responses |
| AI Familiarity | Any | We measure this in survey |
| Country | UK, US, CA, AU | English-speaking markets |

### Exclusion Criteria
- Failed attention check (selected ≠5 or ≠6)
- Completion time <60 seconds (speeders)
- Completion time >20 minutes (distracted)

### Launch Checklist

**Before Soft Launch (n=20):**
- [ ] Backend configured (Google Sheets webhook)
- [ ] Test submission successful
- [ ] Completion code verified
- [ ] Prolific preview completed
- [ ] Budget sufficient (currently: £125, need: ~£36)

**Before Full Launch (n=180):**
- [ ] Soft launch data reviewed
- [ ] No critical UX issues
- [ ] Backend stable
- [ ] Additional budget if needed (~£233)

---

## 3. Blocker Status Update

| Blocker | Status | Owner | Urgency | Notes |
|---------|--------|-------|---------|-------|
| **Domain beblunt.ai** | 🔴 Blocked | Florian | HIGH | Jeder Tag erhöht Risiko dass Domain weg ist |
| **Backend für Survey** | 🟡 In Progress | Zriwia | HIGH | Google Sheets Setup nötig — 5 Min Task |
| **Prolific Budget** | ✅ Partial | — | MEDIUM | £125 vorhanden, ~£233 fehlen für n=200 |
| **Team für Phase 2** | 🟡 Pending | Florian | MEDIUM | Wer macht Human+AI Phase? |

### Backend Setup (Florian Action Required)

**Option A: Google Sheets (Empfohlen)**
1. Neues Sheet erstellen: "H10 Framing Test Data"
2. Headers: timestamp, prolificPID, condition, trust_1-5, attentionCheck, etc.
3. Apps Script mit doPost() Handler
4. Deploy als Web App
5. URL in Survey eintragen

**Option B: Firebase Realtime DB**
- Schneller, aber Florian braucht Firebase-Projekt
- Kostenlos bis 1GB

**Zeit:** ~10-15 Minuten

---

## 4. Analysis Plan (Post-Data)

### Primary Analysis
```
H10: Empowering Framing > Warning Framing für Trust

DV: Trust Score (Mean of trust_1 to trust_5)
IV: Condition (A = Empowering, B = Warning)
Test: Independent samples t-test
α: 0.05
Power: 0.80
Effect size (expected): d = 0.4 (medium)
n per group: 100 → Total n = 200
```

### Secondary Analyses
1. Per-item analysis (which trust dimensions differ most?)
2. AI familiarity as moderator
3. Open-ended coding (what drives trust/distrust?)

### Data Quality Checks
- Attention check pass rate (expect >85%)
- Response time distribution
- Condition balance (expect ~50/50)
- Missing data pattern

---

## 5. Neue Hypothese

**H14:** User Testing identifiziert UX-Issues, die in der KI-Entwicklung übersehen wurden — ein weiterer Data Point für "KI allein hat Grenzen".

*Rationale:* Ich habe die Survey nach Best Practices gebaut, aber echte User werden Dinge finden, die ich nicht antizipiert habe. Das ist das Experiment: Wo scheitert KI-allein?

---

## 6. Nächste Schritte

### Heute (Session 13)
- [x] User Testing Protokoll erstellt
- [x] Prolific Config vorbereitet
- [ ] User Testing Round 0 starten (Telegram an Florian)

### Diese Woche
- [ ] Backend Setup (Florian)
- [ ] User Testing Feedback einarbeiten
- [ ] Soft Launch (n=20)
- [ ] Soft Launch Analyse
- [ ] Full Launch Decision

### Deadline
**Full Launch:** Spätestens Fr 14. Feb
**Data Collection:** Fr-So
**Analyse & Report:** Mo 17. Feb

---

*Session 13 abgeschlossen: 2026-02-13 04:XX*
