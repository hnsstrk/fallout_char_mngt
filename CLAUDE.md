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

### Phase 1: Analysis ✅ COMPLETED

**Milestone 1: Identify all required data fields - ACHIEVED**

The analysis phase systematically identified and documented all data fields available in FVTT character exports, with complete validation against reference screenshots.

**Analysis Approach:**

1. **Automated Field Extraction** - Python script analyzes JSON files
   - `analyze_character.py` - Recursively extracts all JSON fields (2,167 fields total)
   - **Calculates derived statistics** using validated formulas from `reference_data/formulas.json`
   - Outputs `extracted_fields.json` (machine-readable complete field inventory with calculations)
   - Outputs `FIELD_INVENTORY.md` (human-readable categorized tables with 20 categories)
   - All calculations validated against reference character data

**Analysis Results:**
- **Primary Character**: Level 4 Character (Standard character type)
- **Total Fields Extracted**: 2,167
- **Total Items Analyzed**: 44 items across 9 types
- **Item Types**: skill (17), perk (4), weapon (3), apparel (6), consumable (4), ammo (1), miscellany (7), books_and_magz (1), trait (1)

**Derived Statistics Calculated & Validated:**
- Max Health: 13 ✓ (END 4 + LCK 4 + (Level-1) 3 - Radiation 0 + bonus 0 + wellRested +2)
- Defense: 1 ✓ (AGI 6 ≤ 8 → 1, +bonus 0)
- Initiative: 14 ✓ (PER 8 + AGI 6 + bonus 0)
- Melee Damage: 0 ✓ (STR 4 < 7 → 0, +bonus 0)
- Carry Weight: 190 ✓ (150 + STR 4 × 10 + mod 0)
- Next Level XP: 1000 ✓ ((5 × 4 / 2) × 100)

**Success Criteria - ALL ACHIEVED:**
- ✅ All relevant character data fields identified (2,167 fields)
- ✅ Data structure understood and mapped (20 categories)
- ✅ Derived statistics calculation implemented and validated
- ✅ Complete field inventory generated
- ✅ Screenshot validation completed
- ✅ Clear understanding of character sheet requirements

### Phase 2: Implementation (Current)
Generate comprehensive Markdown character sheets from JSON exports.

**Objectives:**
- Python character sheet generator script
- Use extracted field inventory and calculated statistics
- Template-based Markdown generation
- Complete character data rendering (all stats, skills, perks, equipment, descriptions)

### Phase 3: Enhancement (Future)
Refine output format, add PDF generation, styling, and layout optimization.

## Repository Structure

```
fallout_char_mngt/
├── fvtt_export/                    # FoundryVTT character export files
│   └── fvtt-Actor-*.json          # Individual character JSON exports (6 characters)
├── reference_data/                 # Extracted reference data (formulas, lookups)
│   ├── SOURCE.md                  # Licensing and attribution information
│   ├── README.md                  # Usage guide for reference data
│   └── formulas.json              # Validated calculation formulas for derived statistics
├── character_sheets/               # Generated character sheets (Markdown)
│   └── *.md                       # Individual character sheets for offline use
├── analyze_character.py            # Character JSON analyzer with derived stats calculation
├── generate_character_sheet.py    # Character sheet generator (Markdown output)
├── extracted_fields.json           # Complete field inventory (2,167 fields) with calculations
├── FIELD_INVENTORY.md              # Human-readable categorized field documentation (2,294 lines)
├── CLAUDE.md                       # This file - guidance for Claude Code
└── README.md                       # GitHub repository overview
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
  - Examples: Standard characters, Supermutant characters, Ghoul characters
  - Full S.P.E.C.I.A.L. attributes, skills, perks, body parts

- **type: "robot"** - Robot/mechanical characters
  - Examples: Mister Gutsy, Protectron, Sentry Bot, etc.
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

**All formulas are validated** against reference character data.

**Usage**: When generating character sheets, use these formulas to calculate values that are often 0 in JSON exports (system.health.max, system.defense.value, etc.).

**Source**: Extracted from [FVTT Fallout System code](https://github.com/Muttley/foundryvtt-fallout/blob/main/system/src/documents/FalloutActor.mjs) and Fallout 2d20 Rulebook.

**License**: See `reference_data/SOURCE.md` for attribution and licensing information. For personal/group offline play only.

## Generated Character Sheets

Character sheets are generated in Markdown format to `character_sheets/` directory.

**File naming**: `{character_name}.md` (lowercase, underscores, no special chars)
- Example: `character_name.md`

**Character Sheet Structure** (in order):
1. **Header** - Name, Origin, Level, XP
2. **S.P.E.C.I.A.L. Attributes** - Table with all 7 attributes
3. **Derived Statistics** - Health, Defense, Initiative, Melee Damage, Carry Weight, Radiation
4. **Conditions** - Hunger, Thirst, Sleep, Fatigue, Intoxication, Alcoholic, Well Rested
5. **Body Status** - All 6 body parts with status, injuries, resistances (E/P/Po/R)
6. **Skills** - Table with Tag, Rank, Attribute, Description columns
7. **Perks** - Full descriptions and requirements
8. **Trait** - Character trait with description
9. **Addictions** - Placeholder section (*None* if empty) - BEFORE weapons
10. **Diseases** - Placeholder section (*None* if empty) - BEFORE weapons
11. **Weapons** - Weapon stats with full descriptions + Ammunition with descriptions
12. **Apparel** - Locations covered, resistances, full descriptions
13. **Consumables** - Full descriptions with quantities (not table format)
14. **Gear & Miscellany** - Books, misc items with full descriptions
15. **Data** - Character biography and background (from system.biography)

**Important Design Decisions**:
- **Conditions** appear after Derived Stats, before Skills (survival tracking)
- **Skills** in table format with full descriptions included in table
- **Body Status** resistances combine 3 sources: body part + global + equipped apparel
- **Resistances order**: E/P/Po/R (Energy/Physical/Poison/Radiation)
- **Addictions/Diseases** appear BEFORE Weapons for combat readiness check
- **Ammunition** is part of Weapons section with full descriptions
- **Consumables** show full descriptions (not table) for proper usage info
- All items with descriptions show FULL text (no truncation)
- "Data" section (not "Biography") matches FVTT DATA tab naming

## Documentation Maintenance

### README.md Update Protocol

**IMPORTANT**: Before every commit, check if README.md needs to be updated.

The README.md serves as the primary user-facing documentation and must accurately reflect:
1. **Current project status** - Installation requirements, usage instructions
2. **Tool capabilities** - What the tool does, what output to expect
3. **Development phase** - Phase 1 (Analysis), Phase 2 (Implementation), Phase 3 (Enhancement)

#### When to Update README.md

Check and update README.md when ANY of the following occur:

**Feature Changes:**
- New command-line arguments added to scripts
- New output formats supported
- Character sheet structure changes
- New sections added to generated sheets
- Calculation formulas modified

**Project Status Changes:**
- Phase transitions (Analysis → Implementation → Enhancement)
- Major milestones completed
- New capabilities added
- Requirements changed

**Usage Changes:**
- Installation steps modified
- New dependencies added
- Command syntax changed
- File paths or naming conventions changed

**Documentation Focus:**
- README.md is for **users** - focus on practical usage
- Remove specific character names/examples (keep generic)
- Keep "Generated Character Sheet Contents" section up to date
- Ensure examples work and reflect current command syntax

#### Pre-Commit Checklist

Before creating any commit:

1. **Review changes**: What functionality was added/modified?
2. **Check README.md**: Does it accurately describe current tool behavior?
3. **Update if needed**: Modify sections that are now outdated
4. **Verify examples**: Ensure command examples still work
5. **Commit README.md**: Include README.md updates in the same commit if changed

**Example commit workflow:**
```bash
# Make code changes
# ... modify generate_character_sheet.py ...

# Before committing, check README.md
# Does it describe the new feature?
# Do the examples still work?

# If outdated, update README.md
# Then commit both files together
git add generate_character_sheet.py README.md
git commit -m "Add feature X and update documentation"
```

## System Information

- **FoundryVTT Core**: Version 13.347-13.351 (tested)
- **Fallout System**: Version 11.14.3-11.16.4 (tested)
