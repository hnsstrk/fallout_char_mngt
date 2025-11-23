# Fallout Character Management

Offline character sheet generator for Fallout: The Roleplaying Game (2d20 system) using FoundryVTT character exports.

## Project Goal

Generate comprehensive printable character sheets from FoundryVTT JSON exports for offline gameplay.

**Why?** Our gaming group has limited opportunities to play offline. When we do, we need complete character sheets with all statistics, skills, perks, equipment, and descriptions - without access to FoundryVTT.

## Current Phase: Implementation 🔨

**Phase 1 (Analysis) - ✅ COMPLETED**

All required data fields identified, calculation formulas validated, and complete field inventory extracted (2,167 fields from primary character).

**Phase 2 (Implementation) - IN PROGRESS**

Building character sheet generator to create comprehensive Markdown character sheets from JSON exports.

**Target Format**: Markdown → Future: PDF/HTML character sheets

## Repository Structure

```
fallout_char_mngt/
├── fvtt_export/                    # Character JSON exports from FoundryVTT
│   └── fvtt-Actor-*.json          # 6 characters (5 PCs + 1 Robot)
├── screenshots/                    # Reference screenshots from FVTT
│   └── ellie/                     # Dr. Eloise Harper character sheet (7 screenshots)
├── reference_data/                 # Extracted formulas and reference data
│   ├── SOURCE.md                  # Licensing and attribution
│   ├── README.md                  # Usage guide
│   └── formulas.json              # Validated calculation formulas
├── analyze_character.py            # Character analyzer with derived stats calculation
├── extracted_fields.json           # Complete field inventory (2,167 fields)
├── FIELD_INVENTORY.md              # Human-readable field documentation (2,294 lines)
├── CLAUDE.md                       # Development guidance for Claude Code
├── DATA_ANALYSIS.md               # Field analysis protocol
├── ANALYSIS_EXPECTATIONS.md       # Complete data expectations documentation
└── README.md                       # This file
```

## Key Features (Planned)

### Character Sheet Will Include:
- ✅ **All S.P.E.C.I.A.L. attributes** with derived statistics
- ✅ **Complete skill list** with ranks and descriptions
- ✅ **All perks** with full descriptions and requirements
- ✅ **Complete equipment inventory** (weapons, armor, consumables) with stats
- ✅ **Body part injury tracking** and resistances
- ✅ **Character biography** and background
- ✅ **All item descriptions** and mechanical details

### Calculated Statistics:
All derived stats that are often `0` in JSON exports are calculated using validated formulas:
- Max Health (including Well Rested bonus, radiation penalty)
- Defense, Initiative, Melee Damage
- Carry Weight and Encumbrance
- Next Level XP progression

See [`reference_data/formulas.json`](./reference_data/formulas.json) for complete formula documentation.

## Current Status

**Phase 1: Analysis ✅ COMPLETED**
- [x] Project structure established
- [x] Primary analysis character selected (Dr. Eloise 'Ellie' Harper)
- [x] Screenshot reference captured (7 complete views)
- [x] JSON data structure analyzed
- [x] All calculation formulas identified and validated
- [x] Character type differences documented (Character vs Robot)
- [x] Reference data structure created
- [x] Complete field inventory extraction (2,167 fields)
- [x] Derived statistics calculation implemented
- [x] Screenshot validation completed

**Analysis Results:**
- 2,167 fields extracted and categorized into 20 groups
- 44 items analyzed across 9 types (skills, perks, weapons, apparel, etc.)
- All 6 derived statistics calculated and validated against screenshots
- Complete field documentation in FIELD_INVENTORY.md (2,294 lines)

**Phase 2: Implementation (In Progress)**
- [ ] Character sheet generator script
- [ ] Markdown template engine
- [ ] Complete character data rendering
- [ ] Multi-character batch processing

**Phase 3: Enhancement (Future)**
- PDF generation
- Styling and layout optimization
- HTML output option

## Data Sources

### Character Exports
- **World**: "neuland" (our FoundryVTT game)
- **System**: Fallout 2d20 (v11.14.3 - v11.16.4)
- **FVTT Core**: v13.347 - v13.351

### Reference Data
Calculation formulas and game mechanics sourced from:
- [FoundryVTT Fallout System](https://github.com/Muttley/foundryvtt-fallout) (code structure)
- Fallout: The Roleplaying Game Rulebook (game rules)

See [`reference_data/SOURCE.md`](./reference_data/SOURCE.md) for complete attribution.

## Primary Analysis Character

**Dr. Eloise 'Ellie' Harper**
- Type: Character
- Origin: Vault 77
- Level: 4
- Complete screenshot reference: [`screenshots/ellie/`](./screenshots/ellie/)
- All formulas validated against this character's data

## Character Types

The FVTT Fallout system supports different actor types:

| Type | Example | Notes |
|------|---------|-------|
| **character** | Dr. Eloise Harper, Ralph (Supermutant), Rebecca, Roger, Lorian | Standard humanoid characters |
| **robot** | Marcel (Mister Gutsy) | Different attribute structure and body parts |

**Important**: Character sheet generation must handle type differences appropriately.

## Technical Details

### JSON Export Structure
Each character JSON contains:
- Top-level metadata (`_stats`, `name`, `type`, `img`)
- Character system data (`system.*`)
  - Attributes (S.P.E.C.I.A.L.)
  - Level and XP
  - Health, radiation, conditions
  - Body parts with injuries and resistances
- Embedded items array (`items[]`)
  - Skills (with descriptions)
  - Perks (with requirements)
  - Weapons, Armor, Consumables
  - All with complete descriptions
- Active effects (`effects[]`)

### Calculated vs Stored Values
Many derived statistics are stored as `0` in exports and must be calculated:
- `system.health.max` → Calculate with validated formula
- `system.defense.value` → Based on Agility
- `system.initiative.value` → PER + AGI
- `system.level.nextLevelXP` → XP progression formula

See [ANALYSIS_EXPECTATIONS.md](./ANALYSIS_EXPECTATIONS.md) for comprehensive field documentation.

## Development

This project uses **Claude Code** for development assistance.

Key documentation files:
- [`CLAUDE.md`](./CLAUDE.md) - Guidance for Claude Code instances
- [`DATA_ANALYSIS.md`](./DATA_ANALYSIS.md) - Analysis protocol
- [`ANALYSIS_EXPECTATIONS.md`](./ANALYSIS_EXPECTATIONS.md) - Complete expectations

## License & Attribution

### This Repository
**For personal/group offline play only.** Not for commercial distribution.

### Game Content
- **Fallout: The Roleplaying Game** © Modiphius Entertainment
- **Fallout IP** © Bethesda Softworks LLC
- **FoundryVTT Fallout System** by Muttley and contributors

See [`reference_data/SOURCE.md`](./reference_data/SOURCE.md) for complete licensing information.

**Disclaimer**: This is a fan-made tool for personal use. Not affiliated with or endorsed by Modiphius Entertainment, Bethesda Softworks, or Foundry Gaming LLC.

## Roadmap

### Phase 1: Analysis (Current)
- Complete automated field extraction
- Validate all data mappings
- Document edge cases and special handling

### Phase 2: Implementation
- Python character sheet generator
- Markdown template engine
- CLI tool for batch processing

### Phase 3: Enhancement
- PDF generation with styling
- HTML output option
- Character comparison tools
- Item/Perk lookup utilities

## Contributing

This is a personal project for our gaming group. Feel free to fork for your own use!

**Note**: Respect Modiphius Entertainment's copyright. Do not redistribute copyrighted game content.

---

**Generated with assistance from [Claude Code](https://claude.com/claude-code)**

*For the wasteland, prepared. For offline play, ready.* 🎲☢️
