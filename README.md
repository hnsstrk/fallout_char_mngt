# Fallout Character Management

Offline character sheet generator for Fallout: The Roleplaying Game (2d20 system) using FoundryVTT character exports.

## Project Goal

Generate comprehensive printable character sheets from FoundryVTT JSON exports for offline gameplay.

**Why?** Our gaming group has limited opportunities to play offline. When we do, we need complete character sheets with all statistics, skills, perks, equipment, and descriptions - without access to FoundryVTT.

## Requirements

- Python 3.6+
- FoundryVTT character export (JSON format)
- Fallout 2d20 system (tested with v11.14.3 - v11.16.4)

### Optional Dependencies

| Output Format | Required Packages |
|---------------|-------------------|
| Markdown | None (Python standard library) |
| HTML | `jinja2` |

## Installation

1. Clone this repository:
```bash
git clone https://github.com/hnsstrk/fallout_char_mngt.git
cd fallout_char_mngt
```

2. **For Markdown output**: No additional installation required.

3. **For HTML output**: Install optional dependencies:
```bash
pip install -r requirements.txt
```

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

The generated character sheet will be saved to `character_sheets/`.

#### Output Formats

Use the `--format` option to select output format:

```bash
# Markdown (default)
python generate_character_sheet.py fvtt_export/character.json

# HTML (B&W print optimized)
python generate_character_sheet.py fvtt_export/character.json --format html

# HTML with skill descriptions appendix
python generate_character_sheet.py fvtt_export/character.json --format html --appendix
```

#### Options

| Option | Description |
|--------|-------------|
| `--format`, `-f` | Output format: `markdown` (default) or `html` |
| `--appendix` | Include appendix with full skill descriptions (HTML only) |

| Format | Output | Best For |
|--------|--------|----------|
| `markdown` | `.md` file | Text editors, version control |
| `html` | `.html` file | Browser viewing, printing to PDF |

**Example:**
```bash
python generate_character_sheet.py "fvtt_export/fvtt-Actor-character-name-ABC123XYZ.json" --format html
```

Output: `character_sheets/character_name.html`

**Printing to PDF:** Open the HTML file in your browser and use "Print to PDF" (Ctrl+P / Cmd+P). The HTML is optimized for A4 black & white printing.

### Validating Character Data

Before generating character sheets, you can validate your character JSON exports for data quality and completeness:

```bash
python validate_character.py fvtt_export/your-character-file.json
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

### Batch Processing Multiple Characters

The validator and generator are designed as single-purpose tools that can be combined in batch workflows.

#### Linux / macOS

**Simple Batch Processing:**
```bash
# Validate all characters
for file in fvtt_export/fvtt-Actor-*.json; do
    python validate_character.py "$file"
done

# Generate all character sheets
for file in fvtt_export/fvtt-Actor-*.json; do
    python generate_character_sheet.py "$file"
done
```

**Save Validation Reports:**
```bash
# Create log directory
mkdir -p validation_logs

# Validate and save each report
for file in fvtt_export/fvtt-Actor-*.json; do
    basename=$(basename "$file" .json)
    echo "Validating: $basename"
    python validate_character.py "$file" > "validation_logs/${basename}_report.txt"
done
```

**Combined Workflow with Exit Code Check:**
```bash
#!/bin/bash
# process_all_characters.sh

for file in fvtt_export/fvtt-Actor-*.json; do
    echo "Processing: $(basename "$file")"

    # Validate first
    if python validate_character.py "$file" > /dev/null 2>&1; then
        echo "  ✅ Validation passed"
    else
        echo "  ⚠️  Validation warnings found (continuing)"
    fi

    # Generate character sheet
    python generate_character_sheet.py "$file"
    echo "  📄 Character sheet generated"
    echo ""
done
```

**Redirect stdout and stderr:**
```bash
# Stdout to file, stderr to terminal
python validate_character.py character.json > validation.log

# Both stdout and stderr to file
python validate_character.py character.json &> validation_full.log

# Stdout to file, stderr to separate file
python validate_character.py character.json > validation.log 2> errors.log

# Show on terminal AND save to file (using tee)
python validate_character.py character.json | tee validation.log
```

#### Windows PowerShell

**Simple Batch Processing:**
```powershell
# Validate all characters
Get-ChildItem fvtt_export\fvtt-Actor-*.json | ForEach-Object {
    python validate_character.py $_.FullName
}

# Generate all character sheets
Get-ChildItem fvtt_export\fvtt-Actor-*.json | ForEach-Object {
    python generate_character_sheet.py $_.FullName
}
```

**Save Validation Reports:**
```powershell
# Create log directory
New-Item -ItemType Directory -Force -Path validation_logs

# Validate and save each report
Get-ChildItem fvtt_export\fvtt-Actor-*.json | ForEach-Object {
    $basename = $_.BaseName
    Write-Host "Validating: $basename"
    python validate_character.py $_.FullName > "validation_logs\${basename}_report.txt"
}
```

**Combined Workflow with Exit Code Check:**
```powershell
# process_all_characters.ps1

Get-ChildItem fvtt_export\fvtt-Actor-*.json | ForEach-Object {
    Write-Host "Processing: $($_.Name)"

    # Validate first
    python validate_character.py $_.FullName > $null 2>&1
    if ($LASTEXITCODE -eq 0) {
        Write-Host "  ✅ Validation passed" -ForegroundColor Green
    } else {
        Write-Host "  ⚠️  Validation warnings found (continuing)" -ForegroundColor Yellow
    }

    # Generate character sheet
    python generate_character_sheet.py $_.FullName
    Write-Host "  📄 Character sheet generated" -ForegroundColor Cyan
    Write-Host ""
}
```

**Redirect stdout:**
```powershell
# Stdout to file
python validate_character.py character.json > validation.log

# Both stdout and stderr to file
python validate_character.py character.json *> validation_full.log

# Stdout to file, stderr to separate file
python validate_character.py character.json > validation.log 2> errors.log

# Show on terminal AND save to file (using Tee-Object)
python validate_character.py character.json | Tee-Object -FilePath validation.log
```

#### Windows CMD (Command Prompt)

**Simple Batch Processing:**
```batch
@echo off
REM validate_all.bat

for %%f in (fvtt_export\fvtt-Actor-*.json) do (
    echo Validating: %%f
    python validate_character.py "%%f"
)
```

**Save Validation Reports:**
```batch
@echo off
REM validate_and_log.bat

if not exist validation_logs mkdir validation_logs

for %%f in (fvtt_export\fvtt-Actor-*.json) do (
    echo Validating: %%~nf
    python validate_character.py "%%f" > "validation_logs\%%~nf_report.txt"
)
```

**Combined Workflow:**
```batch
@echo off
REM process_all.bat

for %%f in (fvtt_export\fvtt-Actor-*.json) do (
    echo Processing: %%~nxf

    REM Validate
    python validate_character.py "%%f" >nul 2>&1
    if %ERRORLEVEL% EQU 0 (
        echo   [OK] Validation passed
    ) else (
        echo   [WARN] Validation warnings found
    )

    REM Generate
    python generate_character_sheet.py "%%f"
    echo   [OK] Character sheet generated
    echo.
)
```

**Redirect stdout:**
```batch
REM Stdout to file
python validate_character.py character.json > validation.log

REM Both stdout and stderr to file
python validate_character.py character.json > validation.log 2>&1

REM Stdout to file, stderr to separate file
python validate_character.py character.json > validation.log 2> errors.log
```


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
- **Apparel** - Armor and clothing with covered locations, resistances, and descriptions (humanoid characters)
- **Robot Armor** - Armor plating with resistance values (robot characters only)
- **Robot Modules** - Installed modules with effects (robot characters only)
- **Consumables** - Food, chems, and other consumables with full descriptions and quantities
- **Gear & Miscellany** - Books, misc items, and other equipment with descriptions

### Background
- **Data** - Character biography and background information

### Format Details
- **Output Formats**: Markdown (.md), HTML (.html)
- **Tables**: Skills, S.P.E.C.I.A.L., Body Status
- **Sections**: 14 organized sections for easy reference
- **Descriptions**: All item and ability descriptions included in full
- **HTML Features**: B&W print optimized, optional skill descriptions appendix (`--appendix`)

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
  - Uses Apparel for armor/clothing
- **robot** - Robots and mechanical units (e.g., Mister Gutsy, Protectron)
  - Uses Robot Armor instead of Apparel
  - Has Robot Modules section
  - May have built-in immunities (shown as ∞)

## Repository Structure

```
fallout_char_mngt/
├── fvtt_export/                    # Place your exported JSON files here
├── character_sheets/               # Generated character sheets (MD/HTML)
├── reference_data/                 # Calculation formulas and attribution
├── templates/                      # HTML templates for character sheets
├── generate_character_sheet.py    # Character sheet generator
├── validate_character.py           # Character data validation tool
├── requirements.txt                # Optional dependencies (jinja2)
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

**Phase 2.1: HTML Output** ✅ COMPLETED
- HTML output with B&W print optimized styling
- Optional skill descriptions appendix (`--appendix` flag)
- Browser "Print to PDF" workflow

**Phase 3: Enhancement** (Future)
- Layout optimization
- Additional styling options

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
