# Reference Data - Source and License Information

## Purpose

This directory contains extracted reference data from the Fallout 2d20 TTRPG system to support offline character sheet generation. The data includes item definitions, descriptions, and game mechanics that are NOT already embedded in individual character JSON exports.

## Data Sources

### 1. Foundry VTT Fallout System
- **Repository**: [Muttley/foundryvtt-fallout](https://github.com/Muttley/foundryvtt-fallout)
- **License**: Foundry VTT Limited License Agreement for module development
- **Content**: System code, compendium structure, derived statistics calculations
- **Usage**: Code structure referenced for formulas; data structure used as template

### 2. Modiphius Entertainment - Fallout: The Roleplaying Game
- **Publisher**: Modiphius Entertainment
- **Game System**: Fallout 2d20 TTRPG
- **License**: Copyrighted content used with permission in FVTT system
- **Content**: Game rules, item descriptions, perk descriptions, skill definitions
- **Usage**: Data extracted from FVTT compendiums (which have Modiphius permission)

### 3. Character Export Data
- **Source**: FoundryVTT World "neuland"
- **License**: Personal game data
- **Content**: Character-specific items with full descriptions
- **Usage**: Items already embedded in character JSONs (fvtt_export/*.json)

## License Compliance

### What We CAN Do ✅
- Reference FVTT system code structure for understanding data formats
- Document calculation formulas derived from public game rules
- Use exported character data from our own game world
- Create offline tools for personal/group use

### What We CANNOT Do ❌
- Redistribute Modiphius Entertainment's copyrighted content without permission
- Create commercial products using this data
- Redistribute the entire FVTT Fallout system compendium
- Claim ownership of Fallout IP or game system content

### Our Approach
**For personal/group offline play only:**
- Extract minimal necessary reference data (item lists, perk descriptions)
- Source data from our own character exports when possible
- Provide clear attribution to Modiphius Entertainment and FVTT system
- Do NOT redistribute commercially

## Data Structure

```
reference_data/
├── SOURCE.md                 # This file - licensing and attribution
├── README.md                 # Usage guide for reference data
├── formulas.json            # Derived statistics calculation formulas
├── skills_reference.json    # Complete skill list with descriptions
├── perks_reference.json     # Perk catalog (for reference during character creation)
├── traits_reference.json    # Trait catalog
└── items/                   # Optional: Item compendium extracts
    ├── weapons.json
    ├── apparel.json
    ├── consumables.json
    └── miscellany.json
```

## Attribution

**Game System**: Fallout: The Roleplaying Game © Modiphius Entertainment
**Digital Implementation**: Foundry VTT Fallout System by Muttley and contributors
**Character Data**: Exported from personal FoundryVTT game world "neuland"

**Fallout and related marks are trademarks of Bethesda Softworks LLC.**

## Disclaimer

This repository is a fan-made tool for personal use. It is not affiliated with, endorsed by, or sponsored by Modiphius Entertainment, Bethesda Softworks, or Foundry Gaming LLC. All copyrights and trademarks belong to their respective owners.

**For personal/group offline play only. Not for commercial distribution.**

---

**Last Updated**: 2025-11-23
**Repository**: https://github.com/hnsstrk/fallout_char_mngt
