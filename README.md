# Fallout Character Management

Offline character sheet generator for Fallout: The Roleplaying Game (2d20 system) using FoundryVTT character exports.

## Project Goal

Generate comprehensive printable character sheets from FoundryVTT JSON exports for offline gameplay.

**Why?** Our gaming group has limited opportunities to play offline. When we do, we need complete character sheets with all statistics, skills, perks, equipment, and descriptions - without access to FoundryVTT.

## Requirements

- Python 3.6+
- FoundryVTT character export (JSON format)
- Fallout 2d20 system (tested with v11.14.3 - v11.16.4)

### Dependencies

All dependencies are listed in `requirements.txt`:

| Package | Used For |
|---------|----------|
| `jinja2` | HTML character sheet output |
| `textual` | Interactive TUI application |

## Installation

1. Clone this repository:
```bash
git clone https://github.com/hnsstrk/fallout_char_mngt.git
cd fallout_char_mngt
```

2. (Recommended) Create and activate a virtual environment:
```bash
# Create virtual environment
python -m venv venv

# Activate (Linux/macOS)
source venv/bin/activate

# Activate (Windows PowerShell)
.\venv\Scripts\Activate.ps1

# Activate (Windows CMD)
venv\Scripts\activate.bat
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

**Note:** The TUI application will display a helpful error message if dependencies are missing.

## Usage

### Interactive TUI Application

The easiest way to manage characters is the interactive Terminal User Interface (TUI):

```bash
python tui_app.py
```

**Features:**
- Browse all characters in `fvtt_export/` with validation status indicators (`[ok]`, `[!]`, `[X]`)
- View detailed validation reports for each character
- Generate character sheets with a single keypress
- Supports multiple output formats (Markdown, HTML, HTML with Appendix)

**Keyboard Shortcuts:**
| Key | Action |
|-----|--------|
| `M` | Generate Markdown sheet |
| `H` | Generate HTML sheet |
| `A` | Generate HTML with skill appendix |
| `R` | Refresh character list |
| `Q` | Quit |

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

The TUI shows validation status for each character. For command-line validation:

```bash
python validate_character.py fvtt_export/your-character-file.json
```

The validator checks schema structure, data health (attribute ranges, conditions), and completeness (missing descriptions, unequipped items). Some warnings are expected - FoundryVTT stores derived statistics as 0, which the generator calculates automatically.

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
- **Robot Armor** - Armor plating with resistance values (robot characters only)
- **Apparel** - Armor and clothing with covered locations, resistances, and descriptions
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
  - Has Robot Armor section (in addition to Apparel)
  - Has Robot Modules section
  - May have built-in immunities (shown as ∞)

## Repository Structure

```
fallout_char_mngt/
├── fvtt_export/                    # Place your exported JSON files here
├── character_sheets/               # Generated character sheets (MD/HTML)
├── reference_data/                 # Calculation formulas and attribution
├── templates/                      # HTML templates for character sheets
├── lib/                            # Modular character logic library
│   ├── character_data.py          # Core character data class
│   ├── safe_path.py               # Secure path handling
│   ├── system_interface.py        # Abstract system interface
│   └── systems/                   # Game system implementations
│       └── fallout.py             # Fallout 2d20 system handler
├── tui_app.py                      # Interactive TUI application
├── generate_character_sheet.py    # CLI character sheet generator
├── validate_character.py           # Character data validation tool
├── requirements.txt                # Optional dependencies (jinja2, textual)
├── CLAUDE.md                       # Development guidance
└── README.md                       # This file
```

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
