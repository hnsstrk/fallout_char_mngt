# Reference Data Directory

This directory contains extracted reference data from the Fallout 2d20 TTRPG system to support offline character sheet generation.

## Purpose

When generating character sheets from FVTT JSON exports, most data is already embedded in the character files (skills, equipped items, active perks, etc.). However, some reference data is useful for:

1. **Validation**: Ensuring extracted data matches expected formats
2. **Formulas**: Calculating derived statistics consistently
3. **Lookup**: Resolving compendium references or IDs
4. **Offline Play**: Having game rule references without FVTT access

## What's Included

### `formulas.json`
Contains all calculation formulas for derived statistics:
- Max Health (including Well Rested bonus)
- Defense
- Initiative
- Melee Damage
- Carry Weight
- Next Level XP
- Encumbrance calculations

**Source**: Extracted from [FVTT Fallout System code](https://github.com/Muttley/foundryvtt-fallout/blob/main/system/src/documents/FalloutActor.mjs) + Fallout 2d20 Rulebook

### Future Data (Optional)

**Only create these files if needed during implementation:**

- `skills_reference.json` - Complete skill list (if skills need lookup beyond character data)
- `perks_reference.json` - Perk catalog (if perk descriptions need enrichment)
- `traits_reference.json` - Trait catalog (if additional traits needed)
- `items/` - Item compendiums (only if item descriptions are missing from character exports)

## What's NOT Included

### Already in Character JSONs
Character exports (`fvtt_export/*.json`) already contain:
- ✅ All character skills with values and descriptions
- ✅ All equipped/owned items with full descriptions
- ✅ All active perks with descriptions and requirements
- ✅ Character trait with description
- ✅ Body part resistances and injuries
- ✅ Current stats and conditions

### Why We Don't Duplicate
If data exists in character JSONs, we don't extract it here to:
- Avoid redundancy
- Prevent sync issues
- Keep reference data minimal
- Respect licensing (character exports are our own data)

## Usage

The character sheet generator (`analyze_character.py` and future tools) will:

1. **Primary source**: Character JSON files (complete character state)
2. **Reference source**: This directory (formulas, validation, lookups)
3. **Fallback**: Direct calculation using documented formulas

## License

See [SOURCE.md](./SOURCE.md) for detailed licensing information and attribution.

**TL;DR**: For personal/group offline play only. Not for commercial distribution.

---

## File Format

All JSON files in this directory follow this structure:

```json
{
  "meta": {
    "source": "FVTT Fallout System / Fallout 2d20 Rulebook",
    "version": "11.16.4",
    "extracted": "2025-11-23",
    "purpose": "Description of what this file contains"
  },
  "data": {
    // Actual reference data
  }
}
```

This ensures clear provenance and versioning.
