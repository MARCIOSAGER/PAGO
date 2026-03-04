---
name: bible-pago-consultation
description: Validate and consult biblical references for P.A.G.O (Princípio, Alinhamento, Governo, Obediência) methodology materials. Use when creating, reviewing, or validating P.A.G.O mentoring content, handbooks, guides, or any material that references Bible verses in the context of the P.A.G.O system by Jefferson Evangelista.
---

# Bible P.A.G.O Consultation

Validate biblical references and ensure doctrinal consistency in P.A.G.O materials.

## When to Use

- Creating or editing P.A.G.O mentoring materials (handbooks, guides, questionnaires)
- Validating that Bible references are accurate and contextually appropriate
- Finding appropriate Bible verses for specific P.A.G.O pillars
- Reviewing materials for theological consistency

## Quick Reference

Read `references/pago_bible_index.md` for the complete index of P.A.G.O biblical references organized by pillar (P, A, G, O) and Jefferson Evangelista's key phrases.

## Validation Script

Run to validate all Bible references in a document:

```bash
python3 /home/ubuntu/skills/bible-pago-consultation/scripts/validate_bible_refs.py <input_file>
```

Or validate a specific reference:

```bash
python3 /home/ubuntu/skills/bible-pago-consultation/scripts/validate_bible_refs.py --text "Provérbios 11:3"
```

## P.A.G.O Pillar-Verse Mapping

| Pillar | Core Verse | Principle |
|--------|-----------|----------|
| P — Princípio | Provérbios 11:3 | Princípios acima de resultados |
| A — Alinhamento | Romanos 12:2 | Alinhamento gera autoridade |
| G — Governo | Lucas 16:10 | Governo inicia no secreto |
| O — Obediência | Isaías 1:19 | Obediência sustenta o invisível |

## Guidelines

1. Every P.A.G.O material must have biblical foundation — no pillar without a verse
2. Use ARA/NVI for Portuguese, KJV for English materials
3. Verses must be contextually appropriate — not just thematically related
4. Jefferson Evangelista quotes are methodology-specific, not biblical — never mix them
5. The 5 Principles of P.A.G.O: Integridade (Pv 11:3), Mordomia (Lc 16:10), Semeadura (Gl 6:7-9), Excelência (Cl 3:23), Fidelidade (Mt 25:21)
