# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository manages Fallout TTRPG character data exported from FoundryVTT (Foundry Virtual Tabletop). The repository contains JSON files representing character actors from the Fallout tabletop RPG system (version 11.16.4 running on FoundryVTT core version 13.x).

## Project Goal

**Generate comprehensive printable character sheets from FVTT JSON exports for offline gameplay.**

The primary objective is to create complete character sheets that include:
- All character statistics and values (S.P.E.C.I.A.L., level, XP, etc.)
- Complete skill list with values
- All perks/talents with full descriptions
- Complete equipment inventory (weapons, armor, consumables, misc items) with descriptions and stats
- Body part injury tracking and resistances
- Character biography and background information
- All item descriptions and mechanical details

These comprehensive offline character sheets are essential because the group has limited opportunities to play offline, and when they do, players need complete access to all character information without FoundryVTT.

## Project Phases and Approach

### Phase 1: Analysis (Current)
**Milestone 1: Identify all required data fields**

The analysis phase focuses on systematically identifying and documenting all data, metadata, and information available in the FVTT character exports. The target format for this phase is Markdown to enable rapid iteration and validation.

**Hybrid Analysis Approach (Option 5):**

The analysis uses a combination of automated extraction and human evaluation:

1. **Automated Field Extraction** - Python script analyzes JSON files
   - `analyze_character.py` - Recursively extracts all JSON fields
   - Outputs `extracted_fields.json` (machine-readable complete field inventory)
   - Outputs `FIELD_INVENTORY.md` (human-readable table of all fields)
   - Ensures no fields are overlooked

2. **Human Evaluation and Documentation** - Manual assessment in Markdown
   - **DATA_ANALYSIS.md** - Central protocol for categorization, prioritization, and notes
   - Documents which fields are important for character sheets
   - Tracks analysis status and decisions
   - Contains notes on special cases and edge conditions

3. **Reference Screenshots** - Visual reference from FVTT
   - `screenshots/{character}/` - Screenshots from FoundryVTT character sheets
   - Serve as basis for identifying required values
   - Serve as design inspiration for final character sheet layout

**Primary Analysis Character:**
- **Dr. Eloise 'Ellie' Harper** (fvtt-Actor-dr.-eloise-'ellie'-harper-jkTOphZz7Tvl7Qqn.json)
- Has complete screenshot reference in `screenshots/ellie/`
- Type: "character", Origin: "Vault 77"
- Initial analysis will focus exclusively on this character

**Analysis Workflow:**
1. Run `analyze_character.py` on Ellie's JSON file
2. Review generated `FIELD_INVENTORY.md` for completeness
3. Cross-reference with screenshots to identify displayed values
4. Transfer relevant fields to `DATA_ANALYSIS.md` with categorization
5. Document data types, example values, and relationships
6. Iterate until all screenshot-visible data is mapped
7. Validate against FVTT Fallout system requirements

**Success Criteria for Milestone 1:**
- All relevant character data fields identified and documented
- Data structure understood and mapped
- Clear understanding of what will appear on the final character sheet

### Phase 2: Implementation (Future)
Generate Markdown character sheets from JSON exports using automated tooling.

### Phase 3: Enhancement (Future)
Refine output format, add PDF generation, styling, and layout optimization.

## Repository Structure

```
fallout_char_mngt/
├── fvtt_export/                    # FoundryVTT character export files
│   └── fvtt-Actor-*.json          # Individual character JSON exports
├── screenshots/                    # Reference screenshots from FVTT
│   └── ellie/                     # Screenshots for Dr. Eloise Harper
│       └── Screenshot *.png       # 7 screenshots showing character sheet sections
├── reference_data/                 # Extracted reference data (formulas, lookups)
│   ├── SOURCE.md                  # Licensing and attribution information
│   ├── README.md                  # Usage guide for reference data
│   └── formulas.json              # Derived statistics calculation formulas
├── CLAUDE.md                       # This file - guidance for Claude Code
├── DATA_ANALYSIS.md               # Analysis protocol and field documentation
└── ANALYSIS_EXPECTATIONS.md       # Comprehensive expectations for data extraction script
```

## Character Data Format

Each character JSON file follows the FoundryVTT actor schema and contains:

- **Metadata**: `_stats` object with system/core versions, timestamps, and export source info
- **Character Info**: name, type (character/robot), level, XP, origin, biography
- **Body Parts**: Injury tracking and resistances (physical, energy, poison, radiation) for each body part (armL, armR, head, torso, legL, legR)
- **Items Array**: Embedded documents for skills, perks, weapons, armor, consumables, etc.
- **Effects Array**: Active effects applied to the character
- **Flags**: System-specific metadata

### Character Types

**IMPORTANT**: The FVTT Fallout system has different actor types with different data structures:

- **type: "character"** - Standard humanoid characters (humans, ghouls, super mutants)
  - Examples: Dr. Eloise Harper, Ralph (Supermutant), Rebecca Holt, Roger Barkley, Lorian Manson
  - Full S.P.E.C.I.A.L. attributes, skills, perks, body parts

- **type: "robot"** - Robot/mechanical characters
  - Example: Marcel (Mister Gutsy)
  - Origin: "Mister Gutsy"
  - Different attribute structure and capabilities compared to humanoid characters
  - May have different body part configurations

**When analyzing or generating character sheets, always check the `type` field first to ensure correct data structure handling.**

### Key Character Properties

- `system.level.value` - Character level
- `system.origin` - Character background/origin (e.g., "Supermutant")
- `system.body_parts.*` - Injury and resistance tracking per body part
- `items[]` - All owned items (skills, equipment, perks) as embedded documents
- Each item has its own `_id`, `type`, `system` object with type-specific properties

### Naming Convention

Character files use the pattern: `fvtt-Actor-{name}-{foundryId}.json`

## Working with Character Data

When parsing or modifying character JSON files:

1. Large files (100KB+) may need to be read in chunks or with offset/limit parameters
2. Preserve the `_stats` metadata when modifying files
3. Each embedded item in the `items` array has its own complete FoundryVTT document structure
4. Character images reference paths like `tokenizer/pc-images/` or `tokenizer/npc-images/`

## Reference Data

The `reference_data/` directory contains extracted formulas and reference information:

### `formulas.json`
**Complete calculation formulas for all derived statistics:**
- Max Health (including Well Rested +2 bonus, radiation penalty)
- Defense (Agility-based)
- Initiative (PER + AGI)
- Melee Damage (Strength tiers)
- Carry Weight (150 + STR×10)
- Next Level XP ((Level × (Level-1) / 2) × 100)
- Encumbrance levels

**All formulas are validated** against Dr. Eloise Harper character data.

**Usage**: When generating character sheets, use these formulas to calculate values that are often 0 in JSON exports (system.health.max, system.defense.value, etc.).

**Source**: Extracted from [FVTT Fallout System code](https://github.com/Muttley/foundryvtt-fallout/blob/main/system/src/documents/FalloutActor.mjs) and Fallout 2d20 Rulebook.

**License**: See `reference_data/SOURCE.md` for attribution and licensing information. For personal/group offline play only.

## System Information

- **FoundryVTT Core**: Version 13.347-13.351
- **Fallout System**: Version 11.14.3-11.16.4
- **World ID**: neuland
