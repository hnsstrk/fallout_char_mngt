# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Generates printable Markdown character sheets from FoundryVTT Fallout TTRPG JSON exports — for offline gameplay without FoundryVTT access.

**Tech**: Python 3.6+ (stdlib only), Fallout 2d20 System v11.16.4, FVTT Core v13.x

## Task Management

```bash
task project:fallout_char_mngt list
```

## Commands

```bash
# Character sheet generieren
python generate_character_sheet.py fvtt_export/<character-file>.json
# Ausgabe: character_sheets/{character_name}.md
```

## Repository Structure

```
fallout_char_mngt/
├── fvtt_export/            # FVTT character exports (6 JSON files, 100KB-186KB)
├── reference_data/
│   ├── formulas.json       # Validated derived statistics formulas
│   └── SOURCE.md           # Licensing and attribution
├── character_sheets/       # Generated Markdown output
├── generate_character_sheet.py  # Main script (662 lines, CharacterSheetGenerator class)
├── CLAUDE.md
└── README.md
```

## Character Sheet Structure (15 Sections)

1. Header (Name, Origin, Level, XP)
2. S.P.E.C.I.A.L. Attributes
3. Derived Statistics (Health, Defense, Initiative, Melee Damage, Carry Weight)
4. Conditions (Hunger, Thirst, Sleep, Fatigue, Intoxication, Well Rested)
5. Body Status (6 body parts, injuries, resistances E/P/Po/R from 3 sources)
6. Skills (table with Tag, Rank, Attribute, Description)
7. Perks (full descriptions)
8. Trait
9. Addictions
10. Diseases
11. Weapons + Ammunition
12. Apparel (locations, resistances)
13. Consumables (full descriptions, not table)
14. Gear & Miscellany
15. Data (biography)

## Character Data Format

Actor types: `"character"` (human/ghoul/supermutant) vs `"robot"` — unterschiedliche Datenstrukturen. **Immer `type`-Feld prüfen zuerst.**

Wichtige Felder:
- `system.level.value` — Level
- `system.body_parts.*` — Body part injuries + resistances
- `items[]` — All owned items (skill, perk, weapon, apparel, consumable, ammo, miscellany, books_and_magz, trait)

Dateinamen-Pattern: `fvtt-Actor-{name}-{foundryId}.json`

## Formulas (reference_data/formulas.json)

Alle Derived Stats werden berechnet (JSON exports haben oft 0 als Wert):
- **Max Health**: Endurance-basiert + Well Rested +2, Radiation Penalty
- **Defense**: Agility-basiert
- **Initiative**: PER + AGI
- **Melee Damage**: Strength-Tiers
- **Carry Weight**: 150 + STR×10

## Critical Code Patterns

**JSON-Zugriff immer mit `.get()` und Defaults:**
```python
attrs = system.get('attributes', {})
STR = attrs.get('str', {}).get('value', 0)  # Good
STR = system['attributes']['str']['value']   # Bad — crashes
```

**Resistance Calculation** — 3 Quellen summieren:
1. `system.body_parts.*.resistance.*`
2. `system.resistance.*` (global)
3. Equipped apparel (falls location abgedeckt)

**Alle Descriptions** müssen durch `strip_html()` + `format_description()`.

## Code Conventions

- Type hints und Docstrings für alle public methods
- `Path`-Objekte (nicht strings) für Dateipfade
- UTF-8 encoding für alle Dateioperationen
- Single-class design: `CharacterSheetGenerator`

## Pre-Commit Checklist

1. README.md aktualisieren falls: neue CLI-Argumente, neue Output-Sektionen, geänderte Formeln, Phase-Transitions
2. Generator mit Testcharakter laufen lassen
3. Beide Dateien zusammen committen

## Documentation

Projektdokumentation: Siehe Obsidian Vault [[Fallout Character Management]]
