# Data Analysis Protocol

**Purpose**: Systematically identify and document all data fields from FVTT Fallout character exports to ensure comprehensive offline character sheets.

**Primary Analysis Character**: Dr. Eloise 'Ellie' Harper
- JSON File: `fvtt-Actor-dr.-eloise-'ellie'-harper-jkTOphZz7Tvl7Qqn.json`
- Type: "character"
- Origin: "Vault 77"
- Screenshots: `screenshots/ellie/` (7 screenshots showing complete FVTT character sheet)

**Analysis Approach**:
1. Automated extraction via `analyze_character.py` → generates `FIELD_INVENTORY.md`
2. Cross-reference extracted fields with screenshots to identify displayed values
3. Document relevant fields in this file with categorization and notes

**Screenshot Reference**:
The screenshots in `screenshots/ellie/` serve two purposes:
1. **Data validation**: Ensure all visible values in FVTT are captured in our analysis
2. **Design inspiration**: Guide the layout and organization of the generated character sheets

**Analysis Status Legend**:
- ✓ Analyzed and documented
- ⚠ Partially analyzed or unclear
- ✗ Identified but not yet analyzed
- ? Unknown/To be investigated

---

## Character Basic Information

| Field | JSON Path | Type | Status | Notes |
|-------|-----------|------|--------|-------|
| Character Name | `name` | string | ✗ | |
| Character Type | `type` | string | ✗ | Values: "character", "robot" (Marcel is type "robot") |
| Character Image | `img` | string | ✗ | Path to character portrait |
| Biography | `system.biography` | HTML string | ✗ | May contain rich text |
| Level | `system.level.value` | number | ✗ | |
| Current XP | `system.level.currentXP` | number | ✗ | |
| Next Level XP | `system.level.nextLevelXP` | number | ✗ | |
| Reward XP | `system.level.rewardXP` | number | ✗ | |
| Origin | `system.origin` | string | ✗ | Character background (e.g., "Supermutant") |
| Trait | `system.trait` | string | ✗ | |
| Complication | `system.complication` | number | ✗ | |
| Description | `system.description` | string | ✗ | |

---

## S.P.E.C.I.A.L. Attributes

| Attribute | JSON Path | Type | Status | Notes |
|-----------|-----------|------|--------|-------|
| Strength | `system.attributes.str` | object | ? | Need to analyze subfields |
| Perception | `system.attributes.per` | object | ? | Need to analyze subfields |
| Endurance | `system.attributes.end` | object | ? | Need to analyze subfields |
| Charisma | `system.attributes.cha` | object | ? | Need to analyze subfields |
| Intelligence | `system.attributes.int` | object | ? | Need to analyze subfields |
| Agility | `system.attributes.agi` | object | ? | Need to analyze subfields |
| Luck | `system.attributes.luc` | object | ? | Need to analyze subfields |

---

## Derived Statistics

| Statistic | JSON Path | Type | Status | Notes |
|-----------|-----------|------|--------|-------|
| Hit Points | `system.health` | object | ? | Likely contains max, current, temporary |
| Action Points | `system.action_points` | object | ? | |
| Defense | `system.defense` | number | ? | |
| Initiative | `system.initiative` | object | ? | |
| Carry Weight | `system.carry_weight` | object | ? | |
| Melee Damage | `system.melee_damage` | object | ? | |

---

## Body Parts and Injuries

| Body Part | JSON Path | Type | Status | Notes |
|-----------|-----------|------|--------|-------|
| Head | `system.body_parts.head` | object | ⚠ | Contains injuries, resistances, status |
| Torso | `system.body_parts.torso` | object | ⚠ | Contains injuries, resistances, status |
| Left Arm | `system.body_parts.armL` | object | ⚠ | Contains injuries, resistances, status |
| Right Arm | `system.body_parts.armR` | object | ⚠ | Contains injuries, resistances, status |
| Left Leg | `system.body_parts.legL` | object | ⚠ | Contains injuries, resistances, status |
| Right Leg | `system.body_parts.legR` | object | ⚠ | Contains injuries, resistances, status |

**Body Part Subfields** (applies to all body parts):
- `injuries[]` - Array of injury levels [0-5 typically]
- `injuryOpenCount` - Count of untreated injuries
- `injuryTreatedCount` - Count of treated injuries
- `resistance.physical` - Physical damage resistance
- `resistance.energy` - Energy damage resistance
- `resistance.poison` - Poison resistance
- `resistance.radiation` - Radiation resistance
- `status` - Current status (e.g., "healthy")

---

## Skills

Skills are stored in the `items[]` array with `type: "skill"`.

| Field | JSON Path (relative to item) | Type | Status | Notes |
|-------|-------------------------------|------|--------|-------|
| Skill Name | `name` | string | ⚠ | e.g., "Unarmed", "Athletics" |
| Skill Value | `system.value` | number | ⚠ | Skill rank/level |
| Description | `system.description` | HTML string | ⚠ | Full skill description |
| Default Attribute | `system.defaultAttribute` | string | ⚠ | Associated S.P.E.C.I.A.L. (e.g., "str") |
| Tagged | `system.tag` | boolean | ⚠ | Whether skill is tagged |
| Favorite | `system.favorite` | boolean | ⚠ | |
| Source | `system.source` | string | ⚠ | e.g., "core_rulebook" |

**Known Skills to document**: Unarmed, Athletics, (more to be discovered)

---

## Perks and Talents

Perks are stored in the `items[]` array (type to be determined).

| Field | JSON Path | Type | Status | Notes |
|-------|-----------|------|--------|-------|
| Perk Name | | | ? | To be analyzed |
| Description | | | ? | To be analyzed |
| Requirements | | | ? | To be analyzed |
| Ranks | | | ? | To be analyzed |

---

## Equipment - Weapons

Weapons are stored in the `items[]` array with `type: "weapon"` (to be verified).

| Field | JSON Path | Type | Status | Notes |
|-------|-----------|------|--------|-------|
| Weapon Name | | | ? | To be analyzed |
| Weapon Type | | | ? | To be analyzed |
| Damage | | | ? | To be analyzed |
| Damage Type | | | ? | Physical, Energy, etc. |
| Range | | | ? | To be analyzed |
| Ammo Type | | | ? | To be analyzed |
| Qualities | | | ? | Special weapon properties |
| Description | | | ? | To be analyzed |

---

## Equipment - Armor

Armor items are stored in the `items[]` array (type to be determined).

| Field | JSON Path | Type | Status | Notes |
|-------|-----------|------|--------|-------|
| Armor Name | | | ? | To be analyzed |
| Armor Type | | | ? | To be analyzed |
| Defense Bonus | | | ? | To be analyzed |
| Resistances | | | ? | Physical, Energy, Radiation, Poison |
| Description | | | ? | To be analyzed |

---

## Equipment - Consumables

Consumables (stimpaks, food, chems, etc.) stored in `items[]` array.

| Field | JSON Path | Type | Status | Notes |
|-------|-----------|------|--------|-------|
| Item Name | | | ? | To be analyzed |
| Quantity | | | ? | To be analyzed |
| Effect | | | ? | To be analyzed |
| Description | | | ? | To be analyzed |

---

## Equipment - Miscellaneous Items

| Field | JSON Path | Type | Status | Notes |
|-------|-----------|------|--------|-------|
| Item Name | | | ? | To be analyzed |
| Quantity | | | ? | To be analyzed |
| Weight | | | ? | To be analyzed |
| Value | | | ? | Caps value |
| Description | | | ? | To be analyzed |

---

## Active Effects

Effects are stored in the `effects[]` array.

| Field | JSON Path | Type | Status | Notes |
|-------|-----------|------|--------|-------|
| Effect Name | | | ? | To be analyzed |
| Effect Type | | | ? | To be analyzed |
| Duration | | | ? | To be analyzed |
| Modifiers | | | ? | To be analyzed |

---

## Currency and Resources

| Field | JSON Path | Type | Status | Notes |
|-------|-----------|------|--------|-------|
| Caps | | | ? | To be analyzed |
| Other Currency | | | ? | To be analyzed |

---

## Metadata (for reference, not for character sheet)

| Field | JSON Path | Type | Status | Notes |
|-------|-----------|------|--------|-------|
| Actor ID | `_id` | string | ✗ | FoundryVTT unique identifier |
| System Version | `_stats.systemVersion` | string | ✗ | |
| Core Version | `_stats.coreVersion` | string | ✗ | |
| Created Time | `_stats.createdTime` | timestamp | ✗ | |
| Modified Time | `_stats.modifiedTime` | timestamp | ✗ | |

---

## Analysis Tasks

### Immediate Next Steps
1. [ ] Analyze complete S.P.E.C.I.A.L. attribute structure
2. [ ] Analyze derived statistics structure
3. [ ] Complete skills analysis with all available skills
4. [ ] Identify and analyze perk/talent structure
5. [ ] Analyze weapon item structure
6. [ ] Analyze armor item structure
7. [ ] Analyze consumable item structure
8. [ ] Analyze miscellaneous item structure
9. [ ] Identify currency/caps storage location
10. [ ] Document all item types found in items[] array

### Character Files to Analyze
- [ ] Ralph (Supermutant) - fvtt-Actor-686727-_ralph_-SGf3yxAMbFEqmONj.json
- [ ] Marcel - fvtt-Actor-marcel-O44zYNGmMfYtSjVw.json
- [ ] Dr. Eloise Harper - fvtt-Actor-dr.-eloise-'ellie'-harper-jkTOphZz7Tvl7Qqn.json
- [ ] Lorian Manson - fvtt-Actor-lorian-manson-nMnH5OtZZPWGpdra.json
- [ ] Rebecca Holt - fvtt-Actor-rebecca-'becca'-holt-NIUjLEk7Dbx1I0N1.json
- [ ] Roger Barkley - fvtt-Actor-roger-barkley-EKwGRuFdsSSquJ3j.json

---

## Open Questions

1. What are all possible item types in the items[] array?
2. Are there any fields specific to certain character origins (e.g., Supermutant)?
3. How are equipped vs. carried items distinguished?
4. Are there any conditional fields that only appear under certain circumstances?
5. What is the complete list of possible body part statuses?

---

## Analysis Notes

*This section will be populated as analysis progresses.*
