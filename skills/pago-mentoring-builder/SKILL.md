---
name: pago-mentoring-builder
description: Build complete P.A.G.O. (Princípio, Alinhamento, Governo, Obediência) mentoring material packs — handbooks, speaker guides, diagnostic questionnaires, and weekly follow-up structures. Use when creating, customizing, or iterating on P.A.G.O. mentoring events, retreats, or intensive programs by Jefferson Evangelista's methodology.
---

# P.A.G.O. Mentoring Builder

Build professional mentoring material packs for the P.A.G.O. methodology.

## When to Use

- Creating a new P.A.G.O. mentoring event (2-day intensive + weekly follow-up)
- Customizing existing mentoring materials for a specific audience, language, or context
- Adding new exercises, dynamics, or teaching blocks to the mentoring structure
- Generating diagnostic tools and questionnaires based on the 4 pillars

## Workflow

Building a P.A.G.O. mentoring pack involves these steps:

1. Gather event requirements (audience, duration, language, theme emphasis)
2. Generate base pack from templates (run `generate_mentoring_pack.py`)
3. Customize documents for the specific event context
4. Validate all biblical references (run `validate_bible_refs.py`)
5. Convert to final format (PDF via `manus-md-to-pdf`)

### Step 1: Gather Requirements

Determine from the user:
- **Event title, date, location**
- **Audience profile** (leaders, youth, couples, general)
- **Language** (pt, en, es)
- **Duration adjustments** (standard = 2 days × 8h; shorter variants possible)
- **Pillar emphasis** (balanced or weighted toward specific pillars)

### Step 2: Generate Base Pack

Run the generator script:

```bash
python3 /home/ubuntu/skills/pago-mentoring-builder/scripts/generate_mentoring_pack.py \
  --title "Event Title" --date "Date" --location "Location" \
  --language pt --output-dir ./mentoria_output
```

This produces 3 Markdown files from templates:
- `Handbook_do_Participante.md` — participant workbook with exercises
- `Guia_do_Palestrante.md` — confidential speaker/facilitator guide
- `Questionario_de_Diagnostico.md` — 40-question diagnostic tool (scale 1-10)

### Step 3: Customize

Read the relevant reference files based on customization needs:

- **P.A.G.O. methodology details** → Read `references/pago_methodology.md`
- **Mentoring structure and exercise design** → Read `references/mentoring_design_guide.md`
- **Biblical references by pillar** → Read `references/pago_bible_index.md`

**Customization patterns:**

| Audience | Adjustments |
|----------|------------|
| Leaders/Pastors | Emphasize Governo domain; add leadership case studies |
| Youth (18-25) | Simplify language; add more group dynamics; shorten exercises |
| Couples | Add relational alignment exercises; joint declarations |
| Business | Emphasize financial governance; add workplace ethics scenarios |

**Shorter event variants:**
- **1-day intensive (8h):** Merge Day 1 Blocks 1-3 + Day 2 Blocks 2,5,7. Cut group shares to 10 min.
- **Half-day workshop (4h):** Questionnaire + 1 exercise per pillar + Declaration only.

### Step 4: Validate Biblical References

Run on each document:

```bash
python3 /home/ubuntu/skills/pago-mentoring-builder/scripts/validate_bible_refs.py <file.md>
```

**Validation rules:**
1. Every pillar reference must have a biblical foundation
2. Use ARA/NVI for Portuguese, KJV for English
3. Verses must be contextually appropriate, not just thematically related
4. Jefferson Evangelista quotes are methodology-specific — never attribute them as biblical

### Step 5: Generate Final Output

Convert each document to PDF:

```bash
manus-md-to-pdf <file.md> <file.pdf>
```

## Document Architecture

### Handbook (Participant Workbook)

| Section | Content |
|---------|--------|
| Day 1 — Diagnóstico | 5 blocks: Self-assessment → Life Wheel → Open Wounds → Repetitive Cycles → Current State |
| Day 2 — Reconstrução | 7 blocks: Day 1 Reflection → Principles Charter → Alignment Map → Government Audit → Secret Routine → Action Map → Life Declaration |
| Weekly Follow-up | 8-week check-in template (P.A.G.O. scores + wins + challenges + actions) |

### Speaker Guide (Facilitator Only)

Contains: time grids for both days, opening/closing scripts, powerful questions for deepening shares, "Caixa das Emoções" dynamic instructions, critical situation handling table, 8-week follow-up themes with verses, pre/during/post event checklists.

### Diagnostic Questionnaire

40 questions on 1-10 scale: P(8) + A(12: vertical/horizontal/internal) + G(12: spiritual/emotional/financial/temporal) + O(8: basic/radical/fruit). Produces a consolidated P.A.G.O. profile with pillar averages.

## Pillar Quick Reference

| Pillar | Core Verse | Principle |
|--------|-----------|----------|
| P — Princípio | Provérbios 11:3 | Princípios acima de resultados |
| A — Alinhamento | Amós 3:3 | Alinhamento gera autoridade |
| G — Governo | Provérbios 16:32 | Governo inicia no secreto |
| O — Obediência | Isaías 1:19 | Obediência sustenta o invisível |
