# Fallout Character Management

Offline character sheet generator for Fallout: The Roleplaying Game (2d20 system) using FoundryVTT character exports.

## Project Goal

Generate comprehensive printable character sheets from FoundryVTT JSON exports for offline gameplay.

**Why?** Our gaming group has limited opportunities to play offline. When we do, we need complete character sheets with all statistics, skills, perks, equipment, and descriptions - without access to FoundryVTT.

## Requirements

- Python 3.6+
- FoundryVTT character export (JSON format)
- Fallout 2d20 system (tested with v11.14.3 - v11.16.4)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/hnsstrk/fallout_char_mngt.git
cd fallout_char_mngt
```

2. No additional dependencies required - uses Python standard library only.

## Usage

### Exporting Characters from FoundryVTT

1. Open your FoundryVTT world
2. Right-click on the character in the Actors directory
3. Select "Export Data"
4. Save the JSON file to the `fvtt_export/` directory

### Generating Character Sheets

Run the generator script with your character JSON file:

```bash
python generate_character_sheet.py fvtt_export/your-character-file.json
```

The generated character sheet will be saved to `character_sheets/` as a Markdown file.

**Example:**
```bash
python generate_character_sheet.py "fvtt_export/fvtt-Actor-character-name-ABC123XYZ.json"
```

Output: `character_sheets/character_name.md`

### Validating Character Data

Before generating character sheets, you can validate your character JSON exports for data quality and completeness:

```bash
python validate_character.py fvtt_export/your-character-file.json
```

Or validate all characters at once:

```bash
python validate_character.py --all
```

**Example:**
```bash
python validate_character.py "fvtt_export/fvtt-Actor-character-name-ABC123XYZ.json"
```

The validation tool checks for:

#### Schema Validation
- Required JSON fields present (name, type, system, items, etc.)
- Correct FoundryVTT structure
- Valid character type (character, robot, creature, npc)
- All S.P.E.C.I.A.L. attributes present
- Body parts structure complete

#### Health Checks
- S.P.E.C.I.A.L. attributes in valid range (typically 1-10)
- No negative health or radiation values
- Character level >= 1
- Conditions (hunger, thirst, sleep) in expected ranges
- Body part status valid (healthy, injured, crippled)
- Untreated injuries detected
- Item quantities valid (no negative values)

#### Completeness Report
- Missing character origin or biography
- Skills count (expects 17 skills for characters)
- Missing item descriptions
- Unequipped weapons or apparel
- Empty XP tracking fields
- Calculated fields that need updating (max health, initiative, etc.)

**Validation Output:**

The tool produces a detailed report with:
- ✅ **Passed checks** - Green checkmarks for valid data
- ⚠️  **Warnings** - Yellow warnings for unusual values
- ❌ **Errors** - Red errors for missing required fields
- ℹ️  **Info** - Blue notices for completeness issues

Example validation result:
```
======================================================================
Character Validation Report: Wasteland Wanderer
======================================================================
File: fvtt-Actor-character-name-ABC123XYZ.json
Type: character
======================================================================

## Schema Validation
----------------------------------------------------------------------
✅ Schema validation passed - all required fields present

## Health Checks
----------------------------------------------------------------------
⚠️  Found 2 warning(s):
  1. Max health is 0 (likely needs calculation)
  2. Initiative value is 0 but should be calculated (PER + AGI)

## Completeness Report
----------------------------------------------------------------------
ℹ️  Found 3 completeness issue(s):
  1. Next level XP is 0 (needs calculation)
  2. Items missing descriptions: custom item (miscellany)
  3. Character has 3 weapons but none equipped

## Summary
----------------------------------------------------------------------
⚠️  Validation completed with 5 total issue(s):
   - Schema errors: 0
   - Health warnings: 2
   - Completeness issues: 3
```

**Note:** Some warnings are expected (e.g., "max health is 0") because FoundryVTT stores some derived statistics as 0, which the character sheet generator calculates automatically.


## Generated Character Sheet Contents

The generated Markdown character sheet includes:

### Core Statistics
- **S.P.E.C.I.A.L. Attributes** - All 7 attributes in table format
- **Derived Statistics** - Health, Defense, Initiative, Melee Damage, Carry Weight, Radiation
  - All derived stats are **calculated** using validated formulas (not taken from JSON exports)
- **Level & XP** - Current level, XP, and next level requirements

### Character Details
- **Conditions** - Hunger, Thirst, Sleep, Fatigue, Intoxication, Alcoholic status, Well Rested status
- **Skills** - Complete skill list with tags, ranks, attributes, and descriptions (table format)
- **Body Status** - All body parts with health status, injuries, and resistances (E/P/Po/R)
  - Resistances combine body part + global + equipped apparel
- **Perks** - Full descriptions and requirements for each perk
- **Trait** - Character trait with complete description

### Health & Status
- **Addictions** - Current addictions (if any)
- **Diseases** - Current diseases (if any)

### Equipment & Inventory
- **Weapons** - All weapons with stats (damage, range, fire rate, qualities) and full descriptions
  - **Ammunition** - Ammunition inventory with quantities and descriptions
- **Apparel** - Armor and clothing with covered locations, resistances, and descriptions
- **Consumables** - Food, chems, and other consumables with full descriptions and quantities
- **Gear & Miscellany** - Books, misc items, and other equipment with descriptions

### Background
- **Data** - Character biography and background information

### Format Details
- **Output Format**: Markdown (.md)
- **Tables**: Skills, S.P.E.C.I.A.L., Body Status
- **Sections**: 14 organized sections for easy reference
- **Descriptions**: All item and ability descriptions included in full
- **Ready for**: Direct printing, PDF conversion, or viewing in any Markdown viewer

## Calculated Statistics

Many derived statistics are stored as `0` in FoundryVTT JSON exports. This tool calculates them using validated formulas:

| Statistic | Formula |
|-----------|---------|
| **Max Health** | 30 + END + (Level × END) + Well Rested - Radiation |
| **Defense** | 1 + AGI |
| **Initiative** | PER + AGI |
| **Melee Damage** | 1 + STR + (Rank 1 Unarmed Skill) |
| **Carry Weight** | 150 + (STR × 10) |
| **Next Level XP** | CurrentLevel × (CurrentLevel + 1) × 500 |

See [`reference_data/formulas.json`](./reference_data/formulas.json) for complete formula documentation and edge cases.

## Character Types

The tool supports both character types from the FVTT Fallout system:

- **character** - Standard humanoid characters (humans, super mutants, ghouls)
- **robot** - Robots and mechanical units (different attribute structure)

## Repository Structure

```
fallout_char_mngt/
├── fvtt_export/                    # Place your exported JSON files here
├── character_sheets/               # Generated character sheets (Markdown)
├── reference_data/                 # Calculation formulas and attribution
├── generate_character_sheet.py    # Character sheet generator
├── validate_character.py           # Character data validation tool
├── CLAUDE.md                       # Development guidance
└── README.md                       # This file
```

## Technical Details

### JSON Export Structure

FoundryVTT character exports contain:
- Top-level metadata (`_stats`, `name`, `type`, `img`)
- Character system data (`system.*`)
  - Attributes (S.P.E.C.I.A.L.)
  - Level and XP
  - Health, radiation, conditions
  - Body parts with injuries and resistances
- Embedded items array (`items[]`)
  - Skills, Perks, Traits
  - Weapons, Armor, Consumables
  - All with complete descriptions
- Active effects (`effects[]`)

### Data Sources

Calculation formulas and game mechanics sourced from:
- [FoundryVTT Fallout System](https://github.com/Muttley/foundryvtt-fallout) (code structure)
- Fallout: The Roleplaying Game Rulebook (game rules)

See [`reference_data/SOURCE.md`](./reference_data/SOURCE.md) for complete attribution.

## Development Status

**Phase 1: Analysis** ✅ COMPLETED
- All data fields identified and analyzed (2,167 fields)
- Calculation formulas validated and implemented
- Character sheet structure designed

**Phase 2: Implementation** ✅ COMPLETED
- Character sheet generator functional
- Markdown output with all character data
- Derived statistics calculation
- Data validation and quality checks

**Phase 3: Enhancement** (Future)
- PDF generation
- HTML output option
- Batch processing for multiple characters

## Development

This project uses **Claude Code** for development assistance.

Developer documentation:
- [`CLAUDE.md`](./CLAUDE.md) - Development guidance and project overview

## License & Attribution

### This Repository
**For personal/group offline play only.** Not for commercial distribution.

### Game Content
- **Fallout: The Roleplaying Game** © Modiphius Entertainment
- **Fallout IP** © Bethesda Softworks LLC
- **FoundryVTT Fallout System** by Muttley and contributors

See [`reference_data/SOURCE.md`](./reference_data/SOURCE.md) for complete licensing information.

**Disclaimer**: This is a fan-made tool for personal use. Not affiliated with or endorsed by Modiphius Entertainment, Bethesda Softworks, or Foundry Gaming LLC.

## Contributing

This is a personal project for our gaming group. Feel free to fork for your own use!

**Note**: Respect Modiphius Entertainment's copyright. Do not redistribute copyrighted game content.

---

**Generated with assistance from [Claude Code](https://claude.com/claude-code)**

*For the wasteland, prepared. For offline play, ready.* 🎲☢️
