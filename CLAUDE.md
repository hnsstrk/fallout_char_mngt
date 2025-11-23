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

**Analysis Results:**
- All data fields identified and categorized (2,167 fields total)
- 9 item types analyzed: skill, perk, weapon, apparel, consumable, ammo, miscellany, books_and_magz, trait
- All derived statistics formulas validated and implemented
- Character sheet structure designed and implemented

**Success Criteria - ALL ACHIEVED:**
- ✅ All relevant character data fields identified (2,167 fields)
- ✅ Data structure understood and mapped (20 categories)
- ✅ Derived statistics calculation implemented and validated
- ✅ Complete field inventory generated
- ✅ Screenshot validation completed
- ✅ Clear understanding of character sheet requirements

### Phase 2: Implementation ✅ COMPLETED

**Milestone 2: Character sheet generator - ACHIEVED**

The implementation phase successfully created a fully functional character sheet generator with comprehensive data rendering.

**Implementation Results:**
- Complete Python character sheet generator (`generate_character_sheet.py`, 662 lines)
- 20+ specialized methods for different character sheet sections
- Validated derived statistics calculation (formulas.json integration)
- Full Markdown output with all character data
- 15-section character sheet structure

**Success Criteria - ALL ACHIEVED:**
- ✅ Character sheet generator implemented
- ✅ All statistics calculated correctly (max health, defense, initiative, etc.)
- ✅ Complete skill rendering with descriptions
- ✅ Full perk and trait descriptions included
- ✅ Comprehensive equipment lists (weapons, apparel, consumables, gear)
- ✅ Body part tracking with resistances (E/P/Po/R from 3 sources)
- ✅ Conditions tracking (hunger, thirst, sleep, etc.)
- ✅ Clean Markdown output format
- ✅ Character sheet validated against reference data

### Phase 3: Enhancement (Future)
Refine output format, add PDF generation, styling, and layout optimization.

## Repository Structure

```
fallout_char_mngt/
├── fvtt_export/                    # FoundryVTT character export files
│   └── fvtt-Actor-*.json          # Individual character JSON exports (6 characters)
├── reference_data/                 # Calculation formulas and attribution
│   ├── SOURCE.md                  # Licensing and attribution information
│   ├── README.md                  # Usage guide for reference data
│   └── formulas.json              # Validated calculation formulas for derived statistics
├── character_sheets/               # Generated character sheets (Markdown)
│   └── *.md                       # Individual character sheets for offline use
├── generate_character_sheet.py    # Character sheet generator (Markdown output)
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

## Character Sheet Generator

### Script Overview

The `generate_character_sheet.py` script is a comprehensive character sheet generator with the following capabilities:

**Core Functionality:**
- Loads FVTT character JSON exports
- Calculates all derived statistics using validated formulas
- Generates 15-section Markdown character sheets
- Handles both "character" and "robot" actor types
- Strips HTML from descriptions and formats text properly
- Sanitizes filenames for safe output

**Generator Methods:**

The `CharacterSheetGenerator` class contains these specialized methods:

1. **Data Loading:**
   - `load_character()` - Load and validate character JSON
   - `load_formulas()` - Load calculation formulas from reference_data/

2. **Calculations:**
   - `calculate_derived_statistics()` - Calculate all derived stats (health, defense, initiative, melee damage, carry weight)

3. **Utilities:**
   - `strip_html()` - Remove HTML tags from descriptions
   - `format_description()` - Format and indent description text

4. **Sheet Sections (in render order):**
   - `generate_header()` - Name, origin, level, XP
   - `generate_special_attributes()` - S.P.E.C.I.A.L. table
   - `generate_derived_stats()` - Health, defense, initiative, etc.
   - `generate_conditions()` - Hunger, thirst, sleep, fatigue, etc.
   - `generate_body_status()` - Body parts with injuries and resistances
   - `generate_skills()` - Skills table with tags, ranks, descriptions
   - `generate_perks()` - Perks with full descriptions
   - `generate_trait()` - Character trait with description
   - `generate_addictions()` - Addiction tracking
   - `generate_diseases()` - Disease tracking
   - `generate_weapons()` - Weapons + ammunition with descriptions
   - `generate_apparel()` - Armor with locations and resistances
   - `generate_consumables()` - Food/chems with descriptions
   - `generate_gear()` - Books and miscellany
   - `generate_data()` - Biography and background

5. **Output:**
   - `generate_character_sheet()` - Assembles all sections
   - `run()` - Main execution flow

### Usage

**Command Line:**
```bash
python generate_character_sheet.py fvtt_export/<character-file>.json
```

**Output:**
- Character sheet saved to `character_sheets/{character_name}.md`
- Filename sanitized: lowercase, underscores, no special chars
- Example: `dr_eloise_ellie_harper.md`

### Key Design Patterns

**HTML Handling:**
- All descriptions stripped of HTML tags (`<p>`, `<em>`, etc.)
- HTML entities decoded (`&rsquo;` → `'`)
- Preserves readability in plain Markdown

**Resistance Calculation:**
- Body part resistances combine 3 sources:
  1. Body part base resistance (`system.body_parts.*.resistance.*`)
  2. Global character resistance (`system.resistance.*`)
  3. Equipped apparel resistance (if item covers that location)
- Order: E/P/Po/R (Energy/Physical/Poison/Radiation)

**Section Ordering:**
- Conditions before Skills (survival tracking priority)
- Body Status before Skills (combat readiness)
- Addictions/Diseases before Weapons (combat preparation)
- Ammunition within Weapons section (not separate)

## Development Workflows

### Adding New Features

When adding new features to the character sheet generator:

1. **Read the code first** - Always use the Read tool to understand existing implementation
2. **Update formulas.json** - If adding new calculations, document formulas in `reference_data/formulas.json`
3. **Follow section order** - Maintain the 15-section structure unless explicitly changing design
4. **Preserve HTML stripping** - All descriptions must pass through `strip_html()` and `format_description()`
5. **Test with multiple characters** - Validate changes against different character types
6. **Update README.md** - Follow the Documentation Maintenance protocol (see below)

### Code Conventions

**Python Style:**
- Type hints for all method signatures
- Docstrings for all public methods
- Path objects (not strings) for file paths
- UTF-8 encoding for all file operations
- Class-based organization (single CharacterSheetGenerator class)

**Naming Conventions:**
- Methods: `snake_case` (e.g., `generate_special_attributes()`)
- Private attributes: Prefix with underscore if needed
- Constants: UPPER_CASE (in formulas.json)
- File outputs: lowercase with underscores (e.g., `character_name.md`)

**Error Handling:**
- Check file existence before processing
- Provide clear error messages with file paths
- Use `sys.exit(1)` for fatal errors
- Print progress messages for long operations

**JSON Access Patterns:**
```python
# Always use .get() with defaults for nested JSON
attrs = system.get('attributes', {})
STR = attrs.get('str', {}).get('value', 0)

# Never assume keys exist
level = system.get('level', {}).get('value', 1)  # Good
level = system['level']['value']                  # Bad - will crash
```

### Testing Character Sheets

**Manual Validation:**
1. Generate sheet for a test character
2. Compare against FVTT character sheet (screenshots)
3. Verify all sections present and in correct order
4. Check derived statistics match expected values
5. Confirm all descriptions are readable (no HTML artifacts)

**Reference Characters:**
- Use existing exports in `fvtt_export/` as test cases
- 6 characters available for validation
- Test with both "character" and "robot" types

**Validation Checklist:**
- [ ] All 15 sections present
- [ ] S.P.E.C.I.A.L. values match JSON
- [ ] Derived stats calculated correctly
- [ ] Skills table complete with descriptions
- [ ] Perks show full text
- [ ] Weapons include damage, range, qualities
- [ ] Body part resistances include all 3 sources
- [ ] No HTML tags in output
- [ ] Markdown renders correctly

### Git Workflow

**Branch Strategy:**
- Main branch: `main` (or default branch)
- Feature branches: `feature/description` or `fix/issue-description`
- Use provided claude/ branches for Claude Code sessions

**Commit Messages:**
- Use clear, descriptive commit messages
- Format: `Verb noun phrase` (e.g., "Add conditions section to character sheets")
- Focus on what changed, not why (use PR descriptions for why)
- Keep commits atomic (one logical change per commit)

**Pre-Commit Workflow:**
1. Review all changes
2. Check if README.md needs updates (see Documentation Maintenance)
3. Run generator on test character to verify functionality
4. Commit both code and documentation changes together

**Example:**
```bash
# Make changes to generator
vim generate_character_sheet.py

# Test changes
python generate_character_sheet.py fvtt_export/fvtt-Actor-686727-_ralph_-SGf3yxAMbFEqmONj.json

# Update README.md if needed
vim README.md

# Commit together
git add generate_character_sheet.py README.md
git commit -m "Add XP progression display to character header"
git push -u origin claude/your-branch-name
```

### Working with Large JSON Files

Character JSON files can be 100KB+ (e.g., Roger Barkley at 186KB). When reading:

1. **Use Read tool with offset/limit** - For initial exploration
2. **Load full file with json.load()** - For processing (Python handles memory efficiently)
3. **Access nested data safely** - Always use `.get()` with defaults
4. **Filter items by type** - Use list comprehensions for efficiency

**Example:**
```python
# Get all weapons
weapons = [item for item in character_data.get('items', [])
           if item.get('type') == 'weapon']

# Get specific skill
athletics = next((item for item in character_data.get('items', [])
                  if item.get('type') == 'skill' and
                  item.get('name') == 'Athletics'), None)
```

## Troubleshooting

### Common Issues

**"File not found" errors:**
- Verify file path is correct (use Tab completion)
- Check that file is in `fvtt_export/` directory
- Remember to quote filenames with special characters

**Empty or missing sections:**
- Check if character has that item type in JSON
- Verify item type filter in generator method
- Some sections show "None" if empty (addictions, diseases)

**Incorrect derived statistics:**
- Verify formulas.json is present in reference_data/
- Check S.P.E.C.I.A.L. attributes are loaded correctly
- Review calculation in `calculate_derived_statistics()`

**HTML in output:**
- Ensure all descriptions pass through `strip_html()`
- Check that `format_description()` is called
- Some HTML entities may need additional handling

**Wrong resistance values:**
- Verify all 3 resistance sources are summed
- Check apparel location coverage
- Confirm body part mapping (armL, armR, head, torso, legL, legR)

## System Information

- **Python**: 3.6+ required (tested with 3.11.14)
- **Dependencies**: None (uses Python standard library only)
- **FoundryVTT Core**: Version 13.347-13.351 (tested)
- **Fallout System**: Version 11.14.3-11.16.4 (tested)
- **Operating System**: Cross-platform (Linux, macOS, Windows)
