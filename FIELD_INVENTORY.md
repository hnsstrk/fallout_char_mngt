# Complete Field Inventory

**Character**: Dr. Eloise 'Ellie' Harper
**Type**: character
**Level**: 4
**Analyzed**: 2025-11-23 14:21

**Statistics**:
- Total Fields: 2167
- Total Items: 44
- Item Types: 9

---

## Item Type Summary

| Item Type | Count | Examples |
|-----------|-------|----------|
| ammo | 1 | 10mm Round |
| apparel | 6 | Vault Jumpsuit, Formal Hat, Lab Coat |
| books_and_magz | 1 | Apotheker von Gestern Band I |
| consumable | 4 | Stimpak, Purified Water, Mentats |
| miscellany | 7 | Pip-Boy, First Aid Kit, Multi-Tool |
| perk | 4 | Medic, Robotics Expert (2), Intense Training (3) |
| skill | 17 | Unarmed, Athletics, Science |
| trait | 1 | Vault Kid |
| weapon | 3 | 10mm Pistol, Switchblade, Polierte Pfanne "Sophie" |

---

## Calculated Derived Statistics

These values are calculated from character attributes using validated formulas.

| Statistic | Calculated | Stored in JSON | Formula | Status |
|-----------|------------|----------------|---------|--------|
| Max Health | 13 | 0 | `END + LCK + (Level-1) - Radiation + health_bonus + (wellRested ? 2 : 0)` | ✓ Calculated (stored as 0) |
| Defense | 1 | 0 | `AGI <= 8 ? 1 : 2 (+ bonus)` | ✓ Calculated (stored as 0) |
| Initiative | 14 | 0 | `PER + AGI + bonus` | ✓ Calculated (stored as 0) |
| Melee Damage | 0 | 0 | `STR 7-8: +1, STR 9-10: +2, STR 11+: +3 (+ bonus)` | ✓ Calculated (stored as 0) |
| Carry Weight | 190 | 0 | `150 + (STR × 10) + mod` | ✓ Calculated (stored as 0) |
| Next Level Xp | 1000 | 0 | `(Level × (Level-1) / 2) × 100` | ✓ Calculated (stored as 0) |

**Component Values:**

- **Max Health**: END=4, LCK=4, level=4, radiation=0, health_bonus=0, well_rested=True
- **Defense**: AGI=6, defense_bonus=0
- **Initiative**: PER=8, AGI=6, initiative_bonus=0
- **Melee Damage**: STR=4, melee_damage_bonus=0
- **Carry Weight**: base=150, STR=4, carry_weight_mod=0
- **Next Level Xp**: current_level=4, next_level=5

---

## Character Basic Information

| JSON Path | Type | Examples | Min | Max | Notes |
|-----------|------|----------|-----|-----|-------|
| `img` | string | `tokenizer/pc-images/dr._eloise_ellie_harper.Avatar...` |  |  |  |
| `name` | string | `Dr. Eloise 'Ellie' Harper` |  |  |  |
| `system.biography` | string | `<h3>Allgemeine Informationen</h3>
<ul>
<li>Geburts...` |  |  |  |
| `system.complication` | number | `20` | 20 | 20 |  |
| `system.description` | string | `` |  |  |  |
| `system.origin` | string | `Vault 77` |  |  |  |
| `system.trait` | string | `` |  |  |  |
| `type` | string | `character` |  |  |  |

## S.P.E.C.I.A.L. Attributes

| JSON Path | Type | Examples | Min | Max | Notes |
|-----------|------|----------|-----|-----|-------|
| `system.attributes.agi.value` | number | `6` | 6 | 6 |  |
| `system.attributes.cha.value` | number | `6` | 6 | 6 |  |
| `system.attributes.end.value` | number | `4` | 4 | 4 |  |
| `system.attributes.int.value` | number | `9` | 9 | 9 |  |
| `system.attributes.luc.value` | number | `4` | 4 | 4 |  |
| `system.attributes.per.value` | number | `8` | 8 | 8 |  |
| `system.attributes.str.value` | number | `4` | 4 | 4 |  |

## Derived Statistics

| JSON Path | Type | Examples | Min | Max | Notes |
|-----------|------|----------|-----|-----|-------|
| `system.bodyType` | string | `humanoid` |  |  |  |
| `system.carryWeight.base` | number | `0` | 0 | 0 | Often 0 |
| `system.carryWeight.encumbranceLevel` | number | `0` | 0 | 0 | Often 0 |
| `system.carryWeight.mod` | number | `0` | 0 | 0 | Often 0 |
| `system.carryWeight.total` | number | `0` | 0 | 0 | Often 0 |
| `system.carryWeight.value` | number | `0` | 0 | 0 | Often 0 |
| `system.defense.bonus` | number | `0` | 0 | 0 | Often 0 |
| `system.defense.value` | number | `0` | 0 | 0 | Often 0 |
| `system.health.bonus` | number | `0` | 0 | 0 | Often 0 |
| `system.health.max` | number | `0` | 0 | 0 | Often 0 |
| `system.health.value` | number | `8` | 8 | 8 |  |
| `system.initiative.bonus` | number | `0` | 0 | 0 | Often 0 |
| `system.initiative.value` | number | `0` | 0 | 0 | Often 0 |
| `system.meleeDamage.bonus` | number | `0` | 0 | 0 | Often 0 |
| `system.meleeDamage.value` | number | `0` | 0 | 0 | Often 0 |
| `system.radiation` | number | `0` | 0 | 0 | Often 0 |
| `system.resistance.energy` | number | `0` | 0 | 0 | Often 0 |
| `system.resistance.physical` | number | `0` | 0 | 0 | Often 0 |
| `system.resistance.poison` | number | `0` | 0 | 0 | Often 0 |
| `system.resistance.radiation` | number | `0` | 0 | 0 | Often 0 |

## Body Parts

| JSON Path | Type | Examples | Min | Max | Notes |
|-----------|------|----------|-----|-----|-------|
| `system.body_parts.armL.injuries` | array | `[5 items]` |  |  |  |
| `system.body_parts.armL.injuries[0]` | number | `0` | 0 | 0 | Often 0 |
| `system.body_parts.armL.injuries[1]` | number | `0` | 0 | 0 | Often 0 |
| `system.body_parts.armL.injuries[2]` | number | `0` | 0 | 0 | Often 0 |
| `system.body_parts.armL.injuries[3]` | number | `0` | 0 | 0 | Often 0 |
| `system.body_parts.armL.injuries[4]` | number | `0` | 0 | 0 | Often 0 |
| `system.body_parts.armL.injuryOpenCount` | number | `0` | 0 | 0 | Often 0 |
| `system.body_parts.armL.injuryTreatedCount` | number | `0` | 0 | 0 | Often 0 |
| `system.body_parts.armL.resistance.energy` | number | `0` | 0 | 0 | Often 0 |
| `system.body_parts.armL.resistance.physical` | number | `0` | 0 | 0 | Often 0 |
| `system.body_parts.armL.resistance.poison` | number | `0` | 0 | 0 | Often 0 |
| `system.body_parts.armL.resistance.radiation` | number | `0` | 0 | 0 | Often 0 |
| `system.body_parts.armL.status` | string | `healthy` |  |  |  |
| `system.body_parts.armR.injuries` | array | `[5 items]` |  |  |  |
| `system.body_parts.armR.injuries[0]` | number | `0` | 0 | 0 | Often 0 |
| `system.body_parts.armR.injuries[1]` | number | `0` | 0 | 0 | Often 0 |
| `system.body_parts.armR.injuries[2]` | number | `0` | 0 | 0 | Often 0 |
| `system.body_parts.armR.injuries[3]` | number | `0` | 0 | 0 | Often 0 |
| `system.body_parts.armR.injuries[4]` | number | `0` | 0 | 0 | Often 0 |
| `system.body_parts.armR.injuryOpenCount` | number | `0` | 0 | 0 | Often 0 |
| `system.body_parts.armR.injuryTreatedCount` | number | `0` | 0 | 0 | Often 0 |
| `system.body_parts.armR.resistance.energy` | number | `0` | 0 | 0 | Often 0 |
| `system.body_parts.armR.resistance.physical` | number | `0` | 0 | 0 | Often 0 |
| `system.body_parts.armR.resistance.poison` | number | `0` | 0 | 0 | Often 0 |
| `system.body_parts.armR.resistance.radiation` | number | `0` | 0 | 0 | Often 0 |
| `system.body_parts.armR.status` | string | `healthy` |  |  |  |
| `system.body_parts.head.injuries` | array | `[5 items]` |  |  |  |
| `system.body_parts.head.injuries[0]` | number | `0` | 0 | 0 | Often 0 |
| `system.body_parts.head.injuries[1]` | number | `0` | 0 | 0 | Often 0 |
| `system.body_parts.head.injuries[2]` | number | `0` | 0 | 0 | Often 0 |
| `system.body_parts.head.injuries[3]` | number | `0` | 0 | 0 | Often 0 |
| `system.body_parts.head.injuries[4]` | number | `0` | 0 | 0 | Often 0 |
| `system.body_parts.head.injuryOpenCount` | number | `0` | 0 | 0 | Often 0 |
| `system.body_parts.head.injuryTreatedCount` | number | `0` | 0 | 0 | Often 0 |
| `system.body_parts.head.resistance.energy` | number | `0` | 0 | 0 | Often 0 |
| `system.body_parts.head.resistance.physical` | number | `0` | 0 | 0 | Often 0 |
| `system.body_parts.head.resistance.poison` | number | `0` | 0 | 0 | Often 0 |
| `system.body_parts.head.resistance.radiation` | number | `0` | 0 | 0 | Often 0 |
| `system.body_parts.head.status` | string | `healthy` |  |  |  |
| `system.body_parts.legL.injuries` | array | `[5 items]` |  |  |  |
| `system.body_parts.legL.injuries[0]` | number | `0` | 0 | 0 | Often 0 |
| `system.body_parts.legL.injuries[1]` | number | `0` | 0 | 0 | Often 0 |
| `system.body_parts.legL.injuries[2]` | number | `0` | 0 | 0 | Often 0 |
| `system.body_parts.legL.injuries[3]` | number | `0` | 0 | 0 | Often 0 |
| `system.body_parts.legL.injuries[4]` | number | `0` | 0 | 0 | Often 0 |
| `system.body_parts.legL.injuryOpenCount` | number | `0` | 0 | 0 | Often 0 |
| `system.body_parts.legL.injuryTreatedCount` | number | `0` | 0 | 0 | Often 0 |
| `system.body_parts.legL.resistance.energy` | number | `0` | 0 | 0 | Often 0 |
| `system.body_parts.legL.resistance.physical` | number | `0` | 0 | 0 | Often 0 |
| `system.body_parts.legL.resistance.poison` | number | `0` | 0 | 0 | Often 0 |
| `system.body_parts.legL.resistance.radiation` | number | `0` | 0 | 0 | Often 0 |
| `system.body_parts.legL.status` | string | `healthy` |  |  |  |
| `system.body_parts.legR.injuries` | array | `[5 items]` |  |  |  |
| `system.body_parts.legR.injuries[0]` | number | `0` | 0 | 0 | Often 0 |
| `system.body_parts.legR.injuries[1]` | number | `0` | 0 | 0 | Often 0 |
| `system.body_parts.legR.injuries[2]` | number | `0` | 0 | 0 | Often 0 |
| `system.body_parts.legR.injuries[3]` | number | `0` | 0 | 0 | Often 0 |
| `system.body_parts.legR.injuries[4]` | number | `0` | 0 | 0 | Often 0 |
| `system.body_parts.legR.injuryOpenCount` | number | `0` | 0 | 0 | Often 0 |
| `system.body_parts.legR.injuryTreatedCount` | number | `0` | 0 | 0 | Often 0 |
| `system.body_parts.legR.resistance.energy` | number | `0` | 0 | 0 | Often 0 |
| `system.body_parts.legR.resistance.physical` | number | `0` | 0 | 0 | Often 0 |
| `system.body_parts.legR.resistance.poison` | number | `0` | 0 | 0 | Often 0 |
| `system.body_parts.legR.resistance.radiation` | number | `0` | 0 | 0 | Often 0 |
| `system.body_parts.legR.status` | string | `healthy` |  |  |  |
| `system.body_parts.torso.injuries` | array | `[5 items]` |  |  |  |
| `system.body_parts.torso.injuries[0]` | number | `0` | 0 | 0 | Often 0 |
| `system.body_parts.torso.injuries[1]` | number | `0` | 0 | 0 | Often 0 |
| `system.body_parts.torso.injuries[2]` | number | `0` | 0 | 0 | Often 0 |
| `system.body_parts.torso.injuries[3]` | number | `0` | 0 | 0 | Often 0 |
| `system.body_parts.torso.injuries[4]` | number | `0` | 0 | 0 | Often 0 |
| `system.body_parts.torso.injuryOpenCount` | number | `0` | 0 | 0 | Often 0 |
| `system.body_parts.torso.injuryTreatedCount` | number | `0` | 0 | 0 | Often 0 |
| `system.body_parts.torso.resistance.energy` | number | `0` | 0 | 0 | Often 0 |
| `system.body_parts.torso.resistance.physical` | number | `0` | 0 | 0 | Often 0 |
| `system.body_parts.torso.resistance.poison` | number | `0` | 0 | 0 | Often 0 |
| `system.body_parts.torso.resistance.radiation` | number | `0` | 0 | 0 | Often 0 |
| `system.body_parts.torso.status` | string | `healthy` |  |  |  |

## Conditions & Status

| JSON Path | Type | Examples | Min | Max | Notes |
|-----------|------|----------|-----|-----|-------|
| `system.conditions.alcoholic` | boolean | `False` |  |  |  |
| `system.conditions.fatigue` | number | `0` | 0 | 0 | Often 0 |
| `system.conditions.hunger` | number | `0` | 0 | 0 | Often 0 |
| `system.conditions.intoxication` | number | `0` | 0 | 0 | Often 0 |
| `system.conditions.lastChanged.hunger` | number | `10061821800` | 10061821800 | 10061821800 |  |
| `system.conditions.lastChanged.sleep` | number | `10061821800` | 10061821800 | 10061821800 |  |
| `system.conditions.lastChanged.thirst` | number | `10061821800` | 10061821800 | 10061821800 |  |
| `system.conditions.sleep` | number | `0` | 0 | 0 | Often 0 |
| `system.conditions.thirst` | number | `0` | 0 | 0 | Often 0 |
| `system.conditions.wellRested` | boolean | `True` |  |  |  |
| `system.immunities.poison` | boolean | `False` |  |  |  |
| `system.immunities.radiation` | boolean | `False` |  |  |  |

## Currency & Materials

| JSON Path | Type | Examples | Min | Max | Notes |
|-----------|------|----------|-----|-----|-------|
| `system.currency.caps` | number | `8` | 8 | 8 |  |
| `system.currency.other` | string | `Der Kleine Prinz (Buch aus der Vault Bibliothek, n...` |  |  |  |
| `system.materials.common` | number | `0` | 0 | 0 | Often 0 |
| `system.materials.junk` | number | `0` | 0 | 0 | Often 0 |
| `system.materials.rare` | number | `0` | 0 | 0 | Often 0 |
| `system.materials.uncommon` | number | `0` | 0 | 0 | Often 0 |

## Level & XP

| JSON Path | Type | Examples | Min | Max | Notes |
|-----------|------|----------|-----|-----|-------|
| `system.level.currentXP` | number | `0` | 0 | 0 | Often 0 |
| `system.level.nextLevelXP` | number | `0` | 0 | 0 | Often 0 |
| `system.level.rewardXP` | number | `0` | 0 | 0 | Often 0 |
| `system.level.value` | number | `4` | 4 | 4 |  |

## Metadata

| JSON Path | Type | Examples | Min | Max | Notes |
|-----------|------|----------|-----|-----|-------|
| `_stats.compendiumSource` | null |  |  |  |  |
| `_stats.coreVersion` | string | `13.350` |  |  |  |
| `_stats.createdTime` | number | `1737751205134` | 1737751205134 | 1737751205134 |  |
| `_stats.duplicateSource` | null |  |  |  |  |
| `_stats.exportSource.coreVersion` | string | `13.351` |  |  |  |
| `_stats.exportSource.systemId` | string | `fallout` |  |  |  |
| `_stats.exportSource.systemVersion` | string | `11.16.4` |  |  |  |
| `_stats.exportSource.uuid` | string | `Actor.jkTOphZz7Tvl7Qqn` |  |  |  |
| `_stats.exportSource.worldId` | string | `neuland` |  |  |  |
| `_stats.lastModifiedBy` | string | `qqb2lyM0FgEMachb` |  |  |  |
| `_stats.modifiedTime` | number | `1760036344564` | 1760036344564 | 1760036344564 |  |
| `_stats.systemId` | string | `fallout` |  |  |  |
| `_stats.systemVersion` | string | `11.16.4` |  |  |  |
| `folder` | null |  |  |  |  |
| `ownership.default` | number | `1` | 1 | 1 |  |
| `prototypeToken.actorLink` | boolean | `True` |  |  |  |
| `prototypeToken.alpha` | number | `1` | 1 | 1 |  |
| `prototypeToken.appendNumber` | boolean | `False` |  |  |  |
| `prototypeToken.bar1.attribute` | null |  |  |  |  |
| `prototypeToken.bar2.attribute` | null |  |  |  |  |
| `prototypeToken.detectionModes` | array | `[]` |  |  | Empty array |
| `prototypeToken.displayBars` | number | `0` | 0 | 0 | Often 0 |
| `prototypeToken.displayName` | number | `30` | 30 | 30 |  |
| `prototypeToken.disposition` | number | `1` | 1 | 1 |  |
| `prototypeToken.flags.healthEstimate.dontMarkDead` | boolean | `False` |  |  |  |
| `prototypeToken.flags.healthEstimate.hideHealthEstimate` | boolean | `False` |  |  |  |
| `prototypeToken.flags.healthEstimate.hideName` | boolean | `False` |  |  |  |
| `prototypeToken.flags.splatter.bloodColor` | string | `` |  |  |  |
| `prototypeToken.height` | number | `1` | 1 | 1 |  |
| `prototypeToken.light.alpha` | number | `0.5` | 0.5 | 0.5 |  |
| `prototypeToken.light.angle` | number | `360` | 360 | 360 |  |
| `prototypeToken.light.animation.intensity` | number | `5` | 5 | 5 |  |
| `prototypeToken.light.animation.reverse` | boolean | `False` |  |  |  |
| `prototypeToken.light.animation.speed` | number | `5` | 5 | 5 |  |
| `prototypeToken.light.animation.type` | null |  |  |  |  |
| `prototypeToken.light.attenuation` | number | `0.5` | 0.5 | 0.5 |  |
| `prototypeToken.light.bright` | number | `0` | 0 | 0 | Often 0 |
| `prototypeToken.light.color` | null |  |  |  |  |
| `prototypeToken.light.coloration` | number | `1` | 1 | 1 |  |
| `prototypeToken.light.contrast` | number | `0` | 0 | 0 | Often 0 |
| `prototypeToken.light.darkness.max` | number | `1` | 1 | 1 |  |
| `prototypeToken.light.darkness.min` | number | `0` | 0 | 0 | Often 0 |
| `prototypeToken.light.dim` | number | `0` | 0 | 0 | Often 0 |
| `prototypeToken.light.luminosity` | number | `0.5` | 0.5 | 0.5 |  |
| `prototypeToken.light.negative` | boolean | `False` |  |  |  |
| `prototypeToken.light.priority` | number | `0` | 0 | 0 | Often 0 |
| `prototypeToken.light.saturation` | number | `0` | 0 | 0 | Often 0 |
| `prototypeToken.light.shadows` | number | `0` | 0 | 0 | Often 0 |
| `prototypeToken.lockRotation` | boolean | `False` |  |  |  |
| `prototypeToken.movementAction` | null |  |  |  |  |
| `prototypeToken.name` | string | `Ellie` |  |  |  |
| `prototypeToken.occludable.radius` | number | `0` | 0 | 0 | Often 0 |
| `prototypeToken.prependAdjective` | boolean | `False` |  |  |  |
| `prototypeToken.randomImg` | boolean | `False` |  |  |  |
| `prototypeToken.ring.colors.background` | null |  |  |  |  |
| `prototypeToken.ring.colors.ring` | string | `#ffd500` |  |  |  |
| `prototypeToken.ring.effects` | number | `5` | 5 | 5 |  |
| `prototypeToken.ring.enabled` | boolean | `False` |  |  |  |
| `prototypeToken.ring.subject.scale` | number | `1` | 1 | 1 |  |
| `prototypeToken.ring.subject.texture` | string | `tokenizer/pc-images/dr._eloise_ellie_harper.Token....` |  |  |  |
| `prototypeToken.rotation` | number | `0` | 0 | 0 | Often 0 |
| `prototypeToken.sight.angle` | number | `160` | 160 | 160 |  |
| `prototypeToken.sight.attenuation` | number | `0.1` | 0.1 | 0.1 |  |
| `prototypeToken.sight.brightness` | number | `0` | 0 | 0 | Often 0 |
| `prototypeToken.sight.color` | null |  |  |  |  |
| `prototypeToken.sight.contrast` | number | `0` | 0 | 0 | Often 0 |
| `prototypeToken.sight.enabled` | boolean | `True` |  |  |  |
| `prototypeToken.sight.range` | number | `25` | 25 | 25 |  |
| `prototypeToken.sight.saturation` | number | `0` | 0 | 0 | Often 0 |
| `prototypeToken.sight.visionMode` | string | `basic` |  |  |  |
| `prototypeToken.texture.alphaThreshold` | number | `0.75` | 0.75 | 0.75 |  |
| `prototypeToken.texture.anchorX` | number | `0.5` | 0.5 | 0.5 |  |
| `prototypeToken.texture.anchorY` | number | `0.5` | 0.5 | 0.5 |  |
| `prototypeToken.texture.fit` | string | `contain` |  |  |  |
| `prototypeToken.texture.offsetX` | number | `0` | 0 | 0 | Often 0 |
| `prototypeToken.texture.offsetY` | number | `0` | 0 | 0 | Often 0 |
| `prototypeToken.texture.rotation` | number | `0` | 0 | 0 | Often 0 |
| `prototypeToken.texture.scaleX` | number | `1` | 1 | 1 |  |
| `prototypeToken.texture.scaleY` | number | `1` | 1 | 1 |  |
| `prototypeToken.texture.src` | string | `tokenizer/pc-images/dr._eloise_ellie_harper.Token....` |  |  |  |
| `prototypeToken.texture.tint` | string | `#ffffff` |  |  |  |
| `prototypeToken.turnMarker.animation` | null |  |  |  |  |
| `prototypeToken.turnMarker.disposition` | boolean | `False` |  |  |  |
| `prototypeToken.turnMarker.mode` | number | `1` | 1 | 1 |  |
| `prototypeToken.turnMarker.src` | null |  |  |  |  |
| `prototypeToken.width` | number | `1` | 1 | 1 |  |

## Items - Skills

| JSON Path | Type | Examples | Min | Max | Notes |
|-----------|------|----------|-----|-----|-------|
| `items[0]._id` | string | `5xAG0eRrcvDeJAFk` |  |  |  |
| `items[0]._stats.compendiumSource` | null |  |  |  |  |
| `items[0]._stats.coreVersion` | string | `13.344` |  |  |  |
| `items[0]._stats.createdTime` | null |  |  |  |  |
| `items[0]._stats.duplicateSource` | null |  |  |  |  |
| `items[0]._stats.exportSource` | null |  |  |  |  |
| `items[0]._stats.lastModifiedBy` | string | `qqb2lyM0FgEMachb` |  |  |  |
| `items[0]._stats.modifiedTime` | number | `1739550074578` | 1739550074578 | 1739550074578 |  |
| `items[0]._stats.systemId` | string | `fallout` |  |  |  |
| `items[0]._stats.systemVersion` | string | `11.14.3` |  |  |  |
| `items[0].effects` | array | `[]` |  |  | Empty array |
| `items[0].folder` | null |  |  |  |  |
| `items[0].img` | string | `systems/fallout/assets/icons/items/skill.webp` |  |  |  |
| `items[0].name` | string | `Unarmed` |  |  |  |
| `items[0].ownership.default` | number | `0` | 0 | 0 | Often 0 |
| `items[0].sort` | number | `0` | 0 | 0 | Often 0 |
| `items[0].system.defaultAttribute` | string | `str` |  |  |  |
| `items[0].system.description` | string | `<p>The Unarmed skill covers your ability to fight ...` |  |  |  |
| `items[0].system.favorite` | boolean | `False` |  |  |  |
| `items[0].system.source` | string | `core_rulebook` |  |  |  |
| `items[0].system.summary` | string | `` |  |  |  |
| `items[0].system.tag` | boolean | `False` |  |  |  |
| `items[0].system.value` | number | `1` | 1 | 1 |  |
| `items[0].type` | string | `skill` |  |  |  |
| `items[10]._id` | string | `ZQw4TLZbaLm5F0BW` |  |  |  |
| `items[10]._stats.compendiumSource` | null |  |  |  |  |
| `items[10]._stats.coreVersion` | string | `13.344` |  |  |  |
| `items[10]._stats.createdTime` | null |  |  |  |  |
| `items[10]._stats.duplicateSource` | null |  |  |  |  |
| `items[10]._stats.exportSource` | null |  |  |  |  |
| `items[10]._stats.lastModifiedBy` | string | `qqb2lyM0FgEMachb` |  |  |  |
| `items[10]._stats.modifiedTime` | number | `1747332263248` | 1747332263248 | 1747332263248 |  |
| `items[10]._stats.systemId` | string | `fallout` |  |  |  |
| `items[10]._stats.systemVersion` | string | `11.15.6` |  |  |  |
| `items[10].effects` | array | `[]` |  |  | Empty array |
| `items[10].folder` | null |  |  |  |  |
| `items[10].img` | string | `systems/fallout/assets/icons/items/skill.webp` |  |  |  |
| `items[10].name` | string | `Repair` |  |  |  |
| `items[10].ownership.default` | number | `0` | 0 | 0 | Often 0 |
| `items[10].sort` | number | `0` | 0 | 0 | Often 0 |
| `items[10].system.defaultAttribute` | string | `int` |  |  |  |
| `items[10].system.description` | string | `<p>Building and repairing items, from guns to buil...` |  |  |  |
| `items[10].system.favorite` | boolean | `False` |  |  |  |
| `items[10].system.source` | string | `core_rulebook` |  |  |  |
| `items[10].system.summary` | string | `` |  |  |  |
| `items[10].system.tag` | boolean | `False` |  |  |  |
| `items[10].system.value` | number | `4` | 4 | 4 |  |
| `items[10].type` | string | `skill` |  |  |  |
| `items[11]._id` | string | `dOTrlwZ60XWqegQA` |  |  |  |
| `items[11]._stats.compendiumSource` | null |  |  |  |  |
| `items[11]._stats.coreVersion` | string | `13.344` |  |  |  |
| `items[11]._stats.createdTime` | null |  |  |  |  |
| `items[11]._stats.duplicateSource` | null |  |  |  |  |
| `items[11]._stats.exportSource` | null |  |  |  |  |
| `items[11]._stats.lastModifiedBy` | string | `qqb2lyM0FgEMachb` |  |  |  |
| `items[11]._stats.modifiedTime` | number | `1739550045496` | 1739550045496 | 1739550045496 |  |
| `items[11]._stats.systemId` | string | `fallout` |  |  |  |
| `items[11]._stats.systemVersion` | string | `11.14.3` |  |  |  |
| `items[11].effects` | array | `[]` |  |  | Empty array |
| `items[11].folder` | null |  |  |  |  |
| `items[11].img` | string | `systems/fallout/assets/icons/items/skill.webp` |  |  |  |
| `items[11].name` | string | `Speech` |  |  |  |
| `items[11].ownership.default` | number | `0` | 0 | 0 | Often 0 |
| `items[11].sort` | number | `0` | 0 | 0 | Often 0 |
| `items[11].system.defaultAttribute` | string | `cha` |  |  |  |
| `items[11].system.description` | string | `<p>The Speech skill covers the techniques you&rsqu...` |  |  |  |
| `items[11].system.favorite` | boolean | `False` |  |  |  |
| `items[11].system.source` | string | `core_rulebook` |  |  |  |
| `items[11].system.summary` | string | `` |  |  |  |
| `items[11].system.tag` | boolean | `True` |  |  |  |
| `items[11].system.value` | number | `3` | 3 | 3 |  |
| `items[11].type` | string | `skill` |  |  |  |
| `items[12]._id` | string | `ejKiqeUyjkahCjQf` |  |  |  |
| `items[12]._stats.compendiumSource` | null |  |  |  |  |
| `items[12]._stats.coreVersion` | string | `13.344` |  |  |  |
| `items[12]._stats.createdTime` | null |  |  |  |  |
| `items[12]._stats.duplicateSource` | null |  |  |  |  |
| `items[12]._stats.exportSource` | null |  |  |  |  |
| `items[12]._stats.lastModifiedBy` | string | `qqb2lyM0FgEMachb` |  |  |  |
| `items[12]._stats.modifiedTime` | number | `1739550059132` | 1739550059132 | 1739550059132 |  |
| `items[12]._stats.systemId` | string | `fallout` |  |  |  |
| `items[12]._stats.systemVersion` | string | `11.14.3` |  |  |  |
| `items[12].effects` | array | `[]` |  |  | Empty array |
| `items[12].folder` | null |  |  |  |  |
| `items[12].img` | string | `systems/fallout/assets/icons/items/skill.webp` |  |  |  |
| `items[12].name` | string | `Explosives` |  |  |  |
| `items[12].ownership.default` | number | `0` | 0 | 0 | Often 0 |
| `items[12].sort` | number | `0` | 0 | 0 | Often 0 |
| `items[12].system.defaultAttribute` | string | `per` |  |  |  |
| `items[12].system.description` | string | `<p>Whether you throw them, place them as a trap, o...` |  |  |  |
| `items[12].system.favorite` | boolean | `False` |  |  |  |
| `items[12].system.source` | string | `core_rulebook` |  |  |  |
| `items[12].system.summary` | string | `` |  |  |  |
| `items[12].system.tag` | boolean | `False` |  |  |  |
| `items[12].system.value` | number | `1` | 1 | 1 |  |
| `items[12].type` | string | `skill` |  |  |  |
| `items[13]._id` | string | `jAJPNJpHYawNBp2h` |  |  |  |
| `items[13]._stats.compendiumSource` | null |  |  |  |  |
| `items[13]._stats.coreVersion` | string | `13.344` |  |  |  |
| `items[13]._stats.createdTime` | null |  |  |  |  |
| `items[13]._stats.duplicateSource` | null |  |  |  |  |
| `items[13]._stats.exportSource` | null |  |  |  |  |
| `items[13]._stats.lastModifiedBy` | string | `qqb2lyM0FgEMachb` |  |  |  |
| `items[13]._stats.modifiedTime` | number | `1739549891221` | 1739549891221 | 1739549891221 |  |
| `items[13]._stats.systemId` | string | `fallout` |  |  |  |
| `items[13]._stats.systemVersion` | string | `11.14.3` |  |  |  |
| `items[13].effects` | array | `[]` |  |  | Empty array |
| `items[13].folder` | null |  |  |  |  |
| `items[13].img` | string | `systems/fallout/assets/icons/items/skill.webp` |  |  |  |
| `items[13].name` | string | `Energy Weapons` |  |  |  |
| `items[13].ownership.default` | number | `0` | 0 | 0 | Often 0 |
| `items[13].sort` | number | `0` | 0 | 0 | Often 0 |
| `items[13].system.defaultAttribute` | string | `per` |  |  |  |
| `items[13].system.description` | string | `<p>Energy Weapons is the skill to use any time you...` |  |  |  |
| `items[13].system.favorite` | boolean | `False` |  |  |  |
| `items[13].system.source` | string | `core_rulebook` |  |  |  |
| `items[13].system.summary` | string | `` |  |  |  |
| `items[13].system.tag` | boolean | `False` |  |  |  |
| `items[13].system.value` | number | `1` | 1 | 1 |  |
| `items[13].type` | string | `skill` |  |  |  |
| `items[14]._id` | string | `kCGaEuF27yXyE04i` |  |  |  |
| `items[14]._stats.compendiumSource` | null |  |  |  |  |
| `items[14]._stats.coreVersion` | string | `13.344` |  |  |  |
| `items[14]._stats.createdTime` | null |  |  |  |  |
| `items[14]._stats.duplicateSource` | null |  |  |  |  |
| `items[14]._stats.exportSource` | null |  |  |  |  |
| `items[14]._stats.lastModifiedBy` | string | `qqb2lyM0FgEMachb` |  |  |  |
| `items[14]._stats.modifiedTime` | number | `1739549929856` | 1739549929856 | 1739549929856 |  |
| `items[14]._stats.systemId` | string | `fallout` |  |  |  |
| `items[14]._stats.systemVersion` | string | `11.14.3` |  |  |  |
| `items[14].effects` | array | `[]` |  |  | Empty array |
| `items[14].folder` | null |  |  |  |  |
| `items[14].img` | string | `systems/fallout/assets/icons/items/skill.webp` |  |  |  |
| `items[14].name` | string | `Melee Weapons` |  |  |  |
| `items[14].ownership.default` | number | `0` | 0 | 0 | Often 0 |
| `items[14].sort` | number | `0` | 0 | 0 | Often 0 |
| `items[14].system.defaultAttribute` | string | `str` |  |  |  |
| `items[14].system.description` | string | `<p>The Melee Weapons skill describes how able you ...` |  |  |  |
| `items[14].system.favorite` | boolean | `False` |  |  |  |
| `items[14].system.source` | string | `core_rulebook` |  |  |  |
| `items[14].system.summary` | string | `` |  |  |  |
| `items[14].system.tag` | boolean | `False` |  |  |  |
| `items[14].system.value` | number | `1` | 1 | 1 |  |
| `items[14].type` | string | `skill` |  |  |  |
| `items[15]._id` | string | `p3GhRmIwrYTJmuhr` |  |  |  |
| `items[15]._stats.compendiumSource` | null |  |  |  |  |
| `items[15]._stats.coreVersion` | string | `13.344` |  |  |  |
| `items[15]._stats.createdTime` | null |  |  |  |  |
| `items[15]._stats.duplicateSource` | null |  |  |  |  |
| `items[15]._stats.exportSource` | null |  |  |  |  |
| `items[15]._stats.lastModifiedBy` | null |  |  |  |  |
| `items[15]._stats.modifiedTime` | null |  |  |  |  |
| `items[15]._stats.systemId` | string | `fallout` |  |  |  |
| `items[15]._stats.systemVersion` | string | `11.14.3` |  |  |  |
| `items[15].effects` | array | `[]` |  |  | Empty array |
| `items[15].folder` | null |  |  |  |  |
| `items[15].img` | string | `systems/fallout/assets/icons/items/skill.webp` |  |  |  |
| `items[15].name` | string | `Big Guns` |  |  |  |
| `items[15].ownership.default` | number | `0` | 0 | 0 | Often 0 |
| `items[15].sort` | number | `0` | 0 | 0 | Often 0 |
| `items[15].system.defaultAttribute` | string | `end` |  |  |  |
| `items[15].system.description` | string | `<p>Big Guns is the skill that describes the traini...` |  |  |  |
| `items[15].system.favorite` | boolean | `False` |  |  |  |
| `items[15].system.source` | string | `core_rulebook` |  |  |  |
| `items[15].system.summary` | string | `` |  |  |  |
| `items[15].system.tag` | boolean | `False` |  |  |  |
| `items[15].system.value` | number | `0` | 0 | 0 | Often 0 |
| `items[15].type` | string | `skill` |  |  |  |
| `items[16]._id` | string | `vf1Qszkq1om2Xgmn` |  |  |  |
| `items[16]._stats.compendiumSource` | null |  |  |  |  |
| `items[16]._stats.coreVersion` | string | `13.344` |  |  |  |
| `items[16]._stats.createdTime` | null |  |  |  |  |
| `items[16]._stats.duplicateSource` | null |  |  |  |  |
| `items[16]._stats.exportSource` | null |  |  |  |  |
| `items[16]._stats.lastModifiedBy` | string | `qqb2lyM0FgEMachb` |  |  |  |
| `items[16]._stats.modifiedTime` | number | `1739549896834` | 1739549896834 | 1739549896834 |  |
| `items[16]._stats.systemId` | string | `fallout` |  |  |  |
| `items[16]._stats.systemVersion` | string | `11.14.3` |  |  |  |
| `items[16].effects` | array | `[]` |  |  | Empty array |
| `items[16].folder` | null |  |  |  |  |
| `items[16].img` | string | `systems/fallout/assets/icons/items/skill.webp` |  |  |  |
| `items[16].name` | string | `Barter` |  |  |  |
| `items[16].ownership.default` | number | `0` | 0 | 0 | Often 0 |
| `items[16].sort` | number | `0` | 0 | 0 | Often 0 |
| `items[16].system.defaultAttribute` | string | `cha` |  |  |  |
| `items[16].system.description` | string | `<p>Barter describes your skill with money: how sav...` |  |  |  |
| `items[16].system.favorite` | boolean | `False` |  |  |  |
| `items[16].system.source` | string | `core_rulebook` |  |  |  |
| `items[16].system.summary` | string | `` |  |  |  |
| `items[16].system.tag` | boolean | `False` |  |  |  |
| `items[16].system.value` | number | `1` | 1 | 1 |  |
| `items[16].type` | string | `skill` |  |  |  |
| `items[1]._id` | string | `F4uIprrKWh9ApMaU` |  |  |  |
| `items[1]._stats.compendiumSource` | null |  |  |  |  |
| `items[1]._stats.coreVersion` | string | `13.344` |  |  |  |
| `items[1]._stats.createdTime` | null |  |  |  |  |
| `items[1]._stats.duplicateSource` | null |  |  |  |  |
| `items[1]._stats.exportSource` | null |  |  |  |  |
| `items[1]._stats.lastModifiedBy` | string | `qqb2lyM0FgEMachb` |  |  |  |
| `items[1]._stats.modifiedTime` | number | `1739549882823` | 1739549882823 | 1739549882823 |  |
| `items[1]._stats.systemId` | string | `fallout` |  |  |  |
| `items[1]._stats.systemVersion` | string | `11.14.3` |  |  |  |
| `items[1].effects` | array | `[]` |  |  | Empty array |
| `items[1].folder` | null |  |  |  |  |
| `items[1].img` | string | `systems/fallout/assets/icons/items/skill.webp` |  |  |  |
| `items[1].name` | string | `Athletics` |  |  |  |
| `items[1].ownership.default` | number | `0` | 0 | 0 | Often 0 |
| `items[1].sort` | number | `0` | 0 | 0 | Often 0 |
| `items[1].system.defaultAttribute` | string | `str` |  |  |  |
| `items[1].system.description` | string | `<p>Athletics describes your ability to apply your ...` |  |  |  |
| `items[1].system.favorite` | boolean | `False` |  |  |  |
| `items[1].system.source` | string | `core_rulebook` |  |  |  |
| `items[1].system.summary` | string | `` |  |  |  |
| `items[1].system.tag` | boolean | `False` |  |  |  |
| `items[1].system.value` | number | `1` | 1 | 1 |  |
| `items[1].type` | string | `skill` |  |  |  |
| `items[2]._id` | string | `G3mN15diMiTCDZ0U` |  |  |  |
| `items[2]._stats.compendiumSource` | null |  |  |  |  |
| `items[2]._stats.coreVersion` | string | `13.344` |  |  |  |
| `items[2]._stats.createdTime` | null |  |  |  |  |
| `items[2]._stats.duplicateSource` | null |  |  |  |  |
| `items[2]._stats.exportSource` | null |  |  |  |  |
| `items[2]._stats.lastModifiedBy` | string | `qqb2lyM0FgEMachb` |  |  |  |
| `items[2]._stats.modifiedTime` | number | `1739550085041` | 1739550085041 | 1739550085041 |  |
| `items[2]._stats.systemId` | string | `fallout` |  |  |  |
| `items[2]._stats.systemVersion` | string | `11.14.3` |  |  |  |
| `items[2].effects` | array | `[]` |  |  | Empty array |
| `items[2].folder` | null |  |  |  |  |
| `items[2].img` | string | `systems/fallout/assets/icons/items/skill.webp` |  |  |  |
| `items[2].name` | string | `Science` |  |  |  |
| `items[2].ownership.default` | number | `0` | 0 | 0 | Often 0 |
| `items[2].sort` | number | `0` | 0 | 0 | Often 0 |
| `items[2].system.defaultAttribute` | string | `int` |  |  |  |
| `items[2].system.description` | string | `<p>The Science skill covers academic and practical...` |  |  |  |
| `items[2].system.favorite` | boolean | `False` |  |  |  |
| `items[2].system.source` | string | `core_rulebook` |  |  |  |
| `items[2].system.summary` | string | `` |  |  |  |
| `items[2].system.tag` | boolean | `True` |  |  |  |
| `items[2].system.value` | number | `3` | 3 | 3 |  |
| `items[2].type` | string | `skill` |  |  |  |
| `items[3]._id` | string | `HEegw2EUmmEzfdDM` |  |  |  |
| `items[3]._stats.compendiumSource` | null |  |  |  |  |
| `items[3]._stats.coreVersion` | string | `13.344` |  |  |  |
| `items[3]._stats.createdTime` | null |  |  |  |  |
| `items[3]._stats.duplicateSource` | null |  |  |  |  |
| `items[3]._stats.exportSource` | null |  |  |  |  |
| `items[3]._stats.lastModifiedBy` | string | `qqb2lyM0FgEMachb` |  |  |  |
| `items[3]._stats.modifiedTime` | number | `1739549950843` | 1739549950843 | 1739549950843 |  |
| `items[3]._stats.systemId` | string | `fallout` |  |  |  |
| `items[3]._stats.systemVersion` | string | `11.14.3` |  |  |  |
| `items[3].effects` | array | `[]` |  |  | Empty array |
| `items[3].folder` | null |  |  |  |  |
| `items[3].img` | string | `systems/fallout/assets/icons/items/skill.webp` |  |  |  |
| `items[3].name` | string | `Sneak` |  |  |  |
| `items[3].ownership.default` | number | `0` | 0 | 0 | Often 0 |
| `items[3].sort` | number | `0` | 0 | 0 | Often 0 |
| `items[3].system.defaultAttribute` | string | `agi` |  |  |  |
| `items[3].system.description` | string | `<p>The Sneak skill covers stealthy movement and an...` |  |  |  |
| `items[3].system.favorite` | boolean | `False` |  |  |  |
| `items[3].system.source` | string | `core_rulebook` |  |  |  |
| `items[3].system.summary` | string | `` |  |  |  |
| `items[3].system.tag` | boolean | `False` |  |  |  |
| `items[3].system.value` | number | `2` | 2 | 2 |  |
| `items[3].type` | string | `skill` |  |  |  |
| `items[4]._id` | string | `PEN70F6ovA3g5HI2` |  |  |  |
| `items[4]._stats.compendiumSource` | null |  |  |  |  |
| `items[4]._stats.coreVersion` | string | `13.344` |  |  |  |
| `items[4]._stats.createdTime` | null |  |  |  |  |
| `items[4]._stats.duplicateSource` | null |  |  |  |  |
| `items[4]._stats.exportSource` | null |  |  |  |  |
| `items[4]._stats.lastModifiedBy` | string | `qqb2lyM0FgEMachb` |  |  |  |
| `items[4]._stats.modifiedTime` | number | `1739549937648` | 1739549937648 | 1739549937648 |  |
| `items[4]._stats.systemId` | string | `fallout` |  |  |  |
| `items[4]._stats.systemVersion` | string | `11.14.3` |  |  |  |
| `items[4].effects` | array | `[]` |  |  | Empty array |
| `items[4].folder` | null |  |  |  |  |
| `items[4].img` | string | `systems/fallout/assets/icons/items/skill.webp` |  |  |  |
| `items[4].name` | string | `Pilot` |  |  |  |
| `items[4].ownership.default` | number | `0` | 0 | 0 | Often 0 |
| `items[4].sort` | number | `0` | 0 | 0 | Often 0 |
| `items[4].system.defaultAttribute` | string | `per` |  |  |  |
| `items[4].system.description` | string | `<p>The Pilot skill covers your ability to operate ...` |  |  |  |
| `items[4].system.favorite` | boolean | `False` |  |  |  |
| `items[4].system.source` | string | `core_rulebook` |  |  |  |
| `items[4].system.summary` | string | `` |  |  |  |
| `items[4].system.tag` | boolean | `False` |  |  |  |
| `items[4].system.value` | number | `1` | 1 | 1 |  |
| `items[4].type` | string | `skill` |  |  |  |
| `items[5]._id` | string | `R8YnBNUwhZhG89iQ` |  |  |  |
| `items[5]._stats.compendiumSource` | null |  |  |  |  |
| `items[5]._stats.coreVersion` | string | `13.344` |  |  |  |
| `items[5]._stats.createdTime` | null |  |  |  |  |
| `items[5]._stats.duplicateSource` | null |  |  |  |  |
| `items[5]._stats.exportSource` | null |  |  |  |  |
| `items[5]._stats.lastModifiedBy` | string | `qqb2lyM0FgEMachb` |  |  |  |
| `items[5]._stats.modifiedTime` | number | `1739550066672` | 1739550066672 | 1739550066672 |  |
| `items[5]._stats.systemId` | string | `fallout` |  |  |  |
| `items[5]._stats.systemVersion` | string | `11.14.3` |  |  |  |
| `items[5].effects` | array | `[]` |  |  | Empty array |
| `items[5].folder` | null |  |  |  |  |
| `items[5].img` | string | `systems/fallout/assets/icons/items/skill.webp` |  |  |  |
| `items[5].name` | string | `Survival` |  |  |  |
| `items[5].ownership.default` | number | `0` | 0 | 0 | Often 0 |
| `items[5].sort` | number | `0` | 0 | 0 | Often 0 |
| `items[5].system.defaultAttribute` | string | `end` |  |  |  |
| `items[5].system.description` | string | `<p>The Survival skill covers all manner of practic...` |  |  |  |
| `items[5].system.favorite` | boolean | `False` |  |  |  |
| `items[5].system.source` | string | `core_rulebook` |  |  |  |
| `items[5].system.summary` | string | `` |  |  |  |
| `items[5].system.tag` | boolean | `False` |  |  |  |
| `items[5].system.value` | number | `1` | 1 | 1 |  |
| `items[5].type` | string | `skill` |  |  |  |
| `items[6]._id` | string | `SH09XavazYU9CqY4` |  |  |  |
| `items[6]._stats.compendiumSource` | null |  |  |  |  |
| `items[6]._stats.coreVersion` | string | `13.344` |  |  |  |
| `items[6]._stats.createdTime` | null |  |  |  |  |
| `items[6]._stats.duplicateSource` | null |  |  |  |  |
| `items[6]._stats.exportSource` | null |  |  |  |  |
| `items[6]._stats.lastModifiedBy` | string | `qqb2lyM0FgEMachb` |  |  |  |
| `items[6]._stats.modifiedTime` | number | `1739549959522` | 1739549959522 | 1739549959522 |  |
| `items[6]._stats.systemId` | string | `fallout` |  |  |  |
| `items[6]._stats.systemVersion` | string | `11.14.3` |  |  |  |
| `items[6].effects` | array | `[]` |  |  | Empty array |
| `items[6].folder` | null |  |  |  |  |
| `items[6].img` | string | `systems/fallout/assets/icons/items/skill.webp` |  |  |  |
| `items[6].name` | string | `Lockpick` |  |  |  |
| `items[6].ownership.default` | number | `0` | 0 | 0 | Often 0 |
| `items[6].sort` | number | `0` | 0 | 0 | Often 0 |
| `items[6].system.defaultAttribute` | string | `per` |  |  |  |
| `items[6].system.description` | string | `<p>The Lockpick skill reflects your knowledge of m...` |  |  |  |
| `items[6].system.favorite` | boolean | `False` |  |  |  |
| `items[6].system.source` | string | `core_rulebook` |  |  |  |
| `items[6].system.summary` | string | `` |  |  |  |
| `items[6].system.tag` | boolean | `False` |  |  |  |
| `items[6].system.value` | number | `1` | 1 | 1 |  |
| `items[6].type` | string | `skill` |  |  |  |
| `items[7]._id` | string | `UQ4TLtVUR2kRlYkb` |  |  |  |
| `items[7]._stats.compendiumSource` | null |  |  |  |  |
| `items[7]._stats.coreVersion` | string | `13.344` |  |  |  |
| `items[7]._stats.createdTime` | null |  |  |  |  |
| `items[7]._stats.duplicateSource` | null |  |  |  |  |
| `items[7]._stats.exportSource` | null |  |  |  |  |
| `items[7]._stats.lastModifiedBy` | string | `qqb2lyM0FgEMachb` |  |  |  |
| `items[7]._stats.modifiedTime` | number | `1739550082969` | 1739550082969 | 1739550082969 |  |
| `items[7]._stats.systemId` | string | `fallout` |  |  |  |
| `items[7]._stats.systemVersion` | string | `11.14.3` |  |  |  |
| `items[7].effects` | array | `[]` |  |  | Empty array |
| `items[7].folder` | null |  |  |  |  |
| `items[7].img` | string | `systems/fallout/assets/icons/items/skill.webp` |  |  |  |
| `items[7].name` | string | `Throwing` |  |  |  |
| `items[7].ownership.default` | number | `0` | 0 | 0 | Often 0 |
| `items[7].sort` | number | `0` | 0 | 0 | Often 0 |
| `items[7].system.defaultAttribute` | string | `agi` |  |  |  |
| `items[7].system.description` | string | `<p>The Throwing skill describes your ability to ef...` |  |  |  |
| `items[7].system.favorite` | boolean | `False` |  |  |  |
| `items[7].system.source` | string | `core_rulebook` |  |  |  |
| `items[7].system.summary` | string | `` |  |  |  |
| `items[7].system.tag` | boolean | `False` |  |  |  |
| `items[7].system.value` | number | `1` | 1 | 1 |  |
| `items[7].type` | string | `skill` |  |  |  |
| `items[8]._id` | string | `UZDBirrZeUxrAk7b` |  |  |  |
| `items[8]._stats.compendiumSource` | null |  |  |  |  |
| `items[8]._stats.coreVersion` | string | `13.344` |  |  |  |
| `items[8]._stats.createdTime` | null |  |  |  |  |
| `items[8]._stats.duplicateSource` | null |  |  |  |  |
| `items[8]._stats.exportSource` | null |  |  |  |  |
| `items[8]._stats.lastModifiedBy` | string | `qqb2lyM0FgEMachb` |  |  |  |
| `items[8]._stats.modifiedTime` | number | `1739549901007` | 1739549901007 | 1739549901007 |  |
| `items[8]._stats.systemId` | string | `fallout` |  |  |  |
| `items[8]._stats.systemVersion` | string | `11.14.3` |  |  |  |
| `items[8].effects` | array | `[]` |  |  | Empty array |
| `items[8].folder` | null |  |  |  |  |
| `items[8].img` | string | `systems/fallout/assets/icons/items/skill.webp` |  |  |  |
| `items[8].name` | string | `Small Guns` |  |  |  |
| `items[8].ownership.default` | number | `0` | 0 | 0 | Often 0 |
| `items[8].sort` | number | `0` | 0 | 0 | Often 0 |
| `items[8].system.defaultAttribute` | string | `agi` |  |  |  |
| `items[8].system.description` | string | `<p>The Small Guns skill describes your accuracy an...` |  |  |  |
| `items[8].system.favorite` | boolean | `False` |  |  |  |
| `items[8].system.source` | string | `core_rulebook` |  |  |  |
| `items[8].system.summary` | string | `` |  |  |  |
| `items[8].system.tag` | boolean | `False` |  |  |  |
| `items[8].system.value` | number | `2` | 2 | 2 |  |
| `items[8].type` | string | `skill` |  |  |  |
| `items[9]._id` | string | `UrVd0BmoXkAxmrvv` |  |  |  |
| `items[9]._stats.compendiumSource` | null |  |  |  |  |
| `items[9]._stats.coreVersion` | string | `13.350` |  |  |  |
| `items[9]._stats.createdTime` | null |  |  |  |  |
| `items[9]._stats.duplicateSource` | null |  |  |  |  |
| `items[9]._stats.exportSource` | null |  |  |  |  |
| `items[9]._stats.lastModifiedBy` | string | `qqb2lyM0FgEMachb` |  |  |  |
| `items[9]._stats.modifiedTime` | number | `1760029691457` | 1760029691457 | 1760029691457 |  |
| `items[9]._stats.systemId` | string | `fallout` |  |  |  |
| `items[9]._stats.systemVersion` | string | `11.16.4` |  |  |  |
| `items[9].effects` | array | `[]` |  |  | Empty array |
| `items[9].folder` | null |  |  |  |  |
| `items[9].img` | string | `systems/fallout/assets/icons/items/skill.webp` |  |  |  |
| `items[9].name` | string | `Medicine` |  |  |  |
| `items[9].ownership.default` | number | `0` | 0 | 0 | Often 0 |
| `items[9].sort` | number | `0` | 0 | 0 | Often 0 |
| `items[9].system.defaultAttribute` | string | `int` |  |  |  |
| `items[9].system.description` | string | `<p>Medicine is the skill that covers all medical a...` |  |  |  |
| `items[9].system.favorite` | boolean | `False` |  |  |  |
| `items[9].system.source` | string | `core_rulebook` |  |  |  |
| `items[9].system.summary` | string | `` |  |  |  |
| `items[9].system.tag` | boolean | `True` |  |  |  |
| `items[9].system.value` | number | `5` | 5 | 5 |  |
| `items[9].type` | string | `skill` |  |  |  |

## Items - Perks

| JSON Path | Type | Examples | Min | Max | Notes |
|-----------|------|----------|-----|-----|-------|
| `items[30]._id` | string | `Pctb3UCcwu1er2c3` |  |  |  |
| `items[30]._stats.compendiumSource` | string | `Compendium.fallout.perks.Item.fMU0zfQYyhkwZ6Ck` |  |  |  |
| `items[30]._stats.coreVersion` | string | `13.344` |  |  |  |
| `items[30]._stats.createdTime` | number | `1739551327121` | 1739551327121 | 1739551327121 |  |
| `items[30]._stats.duplicateSource` | null |  |  |  |  |
| `items[30]._stats.exportSource` | null |  |  |  |  |
| `items[30]._stats.lastModifiedBy` | string | `XPIM5aN65eH5LXee` |  |  |  |
| `items[30]._stats.modifiedTime` | number | `1746721330799` | 1746721330799 | 1746721330799 |  |
| `items[30]._stats.systemId` | string | `fallout` |  |  |  |
| `items[30]._stats.systemVersion` | string | `11.15.4` |  |  |  |
| `items[30].effects` | array | `[]` |  |  | Empty array |
| `items[30].folder` | null |  |  |  |  |
| `items[30].img` | string | `systems/fallout/assets/icons/items/perk.svg` |  |  |  |
| `items[30].name` | string | `Medic` |  |  |  |
| `items[30].ownership.default` | number | `0` | 0 | 0 | Often 0 |
| `items[30].sort` | number | `0` | 0 | 0 | Often 0 |
| `items[30].system.description` | string | `<p>When you use the First Aid action to try to tre...` |  |  |  |
| `items[30].system.favorite` | boolean | `False` |  |  |  |
| `items[30].system.rank.levelIncrease` | number | `0` | 0 | 0 | Often 0 |
| `items[30].system.rank.levelStart` | number | `1` | 1 | 1 |  |
| `items[30].system.rank.max` | number | `1` | 1 | 1 |  |
| `items[30].system.rank.value` | number | `1` | 1 | 1 |  |
| `items[30].system.requirements` | string | `` |  |  |  |
| `items[30].system.requirementsEx.attributes.agi.value` | number | `0` | 0 | 0 | Often 0 |
| `items[30].system.requirementsEx.attributes.cha.value` | number | `0` | 0 | 0 | Often 0 |
| `items[30].system.requirementsEx.attributes.end.value` | number | `0` | 0 | 0 | Often 0 |
| `items[30].system.requirementsEx.attributes.int.value` | number | `8` | 8 | 8 |  |
| `items[30].system.requirementsEx.attributes.luc.value` | number | `0` | 0 | 0 | Often 0 |
| `items[30].system.requirementsEx.attributes.per.value` | number | `0` | 0 | 0 | Often 0 |
| `items[30].system.requirementsEx.attributes.str.value` | number | `0` | 0 | 0 | Often 0 |
| `items[30].system.requirementsEx.isCompanion` | boolean | `False` |  |  |  |
| `items[30].system.requirementsEx.level` | number | `1` | 1 | 1 |  |
| `items[30].system.requirementsEx.levelIncrease` | number | `0` | 0 | 0 | Often 0 |
| `items[30].system.requirementsEx.magazineUuids` | array | `[]` |  |  | Empty array |
| `items[30].system.requirementsEx.notGhoul` | boolean | `False` |  |  |  |
| `items[30].system.requirementsEx.notHuman` | boolean | `False` |  |  |  |
| `items[30].system.requirementsEx.notRadiationImmune` | boolean | `False` |  |  |  |
| `items[30].system.requirementsEx.notRobot` | boolean | `False` |  |  |  |
| `items[30].system.requirementsEx.notSupermutant` | boolean | `False` |  |  |  |
| `items[30].system.source` | string | `core_rulebook` |  |  |  |
| `items[30].type` | string | `perk` |  |  |  |
| `items[33]._id` | string | `yemWFUjgxTGC7g22` |  |  |  |
| `items[33]._stats.compendiumSource` | string | `Compendium.fallout.perks.Item.GiPKNxmrkWA2k76W` |  |  |  |
| `items[33]._stats.coreVersion` | string | `13.344` |  |  |  |
| `items[33]._stats.createdTime` | number | `1742128561904` | 1742128561904 | 1742128561904 |  |
| `items[33]._stats.duplicateSource` | null |  |  |  |  |
| `items[33]._stats.exportSource` | null |  |  |  |  |
| `items[33]._stats.lastModifiedBy` | string | `qqb2lyM0FgEMachb` |  |  |  |
| `items[33]._stats.modifiedTime` | number | `1747332473270` | 1747332473270 | 1747332473270 |  |
| `items[33]._stats.systemId` | string | `fallout` |  |  |  |
| `items[33]._stats.systemVersion` | string | `11.15.4` |  |  |  |
| `items[33].effects` | array | `[]` |  |  | Empty array |
| `items[33].folder` | null |  |  |  |  |
| `items[33].img` | string | `systems/fallout/assets/icons/items/perk.svg` |  |  |  |
| `items[33].name` | string | `Robotics Expert (2)` |  |  |  |
| `items[33].ownership.default` | number | `0` | 0 | 0 | Often 0 |
| `items[33].sort` | number | `0` | 0 | 0 | Often 0 |
| `items[33].system.description` | string | `<p>At rank 1, you can modify robot armor, weapon m...` |  |  |  |
| `items[33].system.favorite` | boolean | `False` |  |  |  |
| `items[33].system.rank.levelIncrease` | number | `0` | 0 | 0 | Often 0 |
| `items[33].system.rank.levelStart` | number | `1` | 1 | 1 |  |
| `items[33].system.rank.max` | number | `3` | 3 | 3 |  |
| `items[33].system.rank.value` | number | `1` | 1 | 1 |  |
| `items[33].system.requirements` | string | `` |  |  |  |
| `items[33].system.requirementsEx.attributes.agi.value` | number | `0` | 0 | 0 | Often 0 |
| `items[33].system.requirementsEx.attributes.cha.value` | number | `0` | 0 | 0 | Often 0 |
| `items[33].system.requirementsEx.attributes.end.value` | number | `0` | 0 | 0 | Often 0 |
| `items[33].system.requirementsEx.attributes.int.value` | number | `8` | 8 | 8 |  |
| `items[33].system.requirementsEx.attributes.luc.value` | number | `0` | 0 | 0 | Often 0 |
| `items[33].system.requirementsEx.attributes.per.value` | number | `0` | 0 | 0 | Often 0 |
| `items[33].system.requirementsEx.attributes.str.value` | number | `0` | 0 | 0 | Often 0 |
| `items[33].system.requirementsEx.isCompanion` | boolean | `False` |  |  |  |
| `items[33].system.requirementsEx.level` | number | `2` | 2 | 2 |  |
| `items[33].system.requirementsEx.levelIncrease` | number | `4` | 4 | 4 |  |
| `items[33].system.requirementsEx.magazineUuids` | array | `[]` |  |  | Empty array |
| `items[33].system.requirementsEx.notGhoul` | boolean | `False` |  |  |  |
| `items[33].system.requirementsEx.notHuman` | boolean | `False` |  |  |  |
| `items[33].system.requirementsEx.notRadiationImmune` | boolean | `False` |  |  |  |
| `items[33].system.requirementsEx.notRobot` | boolean | `False` |  |  |  |
| `items[33].system.requirementsEx.notSupermutant` | boolean | `False` |  |  |  |
| `items[33].system.source` | string | `core_rulebook` |  |  |  |
| `items[33].type` | string | `perk` |  |  |  |
| `items[36]._id` | string | `KNEdg9QUDu1S4JSN` |  |  |  |
| `items[36]._stats.compendiumSource` | string | `Compendium.fallout.perks.Item.P3SMmJulZT5OyArI` |  |  |  |
| `items[36]._stats.coreVersion` | string | `13.344` |  |  |  |
| `items[36]._stats.createdTime` | number | `1747332665167` | 1747332665167 | 1747332665167 |  |
| `items[36]._stats.duplicateSource` | null |  |  |  |  |
| `items[36]._stats.exportSource` | null |  |  |  |  |
| `items[36]._stats.lastModifiedBy` | string | `qqb2lyM0FgEMachb` |  |  |  |
| `items[36]._stats.modifiedTime` | number | `1747332700489` | 1747332700489 | 1747332700489 |  |
| `items[36]._stats.systemId` | string | `fallout` |  |  |  |
| `items[36]._stats.systemVersion` | string | `11.15.6` |  |  |  |
| `items[36].effects` | array | `[]` |  |  | Empty array |
| `items[36].folder` | null |  |  |  |  |
| `items[36].img` | string | `systems/fallout/assets/icons/items/perk.svg` |  |  |  |
| `items[36].name` | string | `Intense Training (3)` |  |  |  |
| `items[36].ownership.default` | number | `0` | 0 | 0 | Often 0 |
| `items[36].sort` | number | `0` | 0 | 0 | Often 0 |
| `items[36].system.description` | string | `<p>Increase any one S.P.E.C.I.A.L attribute by 1 r...` |  |  |  |
| `items[36].system.favorite` | boolean | `False` |  |  |  |
| `items[36].system.rank.max` | number | `10` | 10 | 10 |  |
| `items[36].system.rank.value` | number | `1` | 1 | 1 |  |
| `items[36].system.requirements` | string | `` |  |  |  |
| `items[36].system.requirementsEx.attributes.agi.value` | number | `0` | 0 | 0 | Often 0 |
| `items[36].system.requirementsEx.attributes.cha.value` | number | `0` | 0 | 0 | Often 0 |
| `items[36].system.requirementsEx.attributes.end.value` | number | `0` | 0 | 0 | Often 0 |
| `items[36].system.requirementsEx.attributes.int.value` | number | `0` | 0 | 0 | Often 0 |
| `items[36].system.requirementsEx.attributes.luc.value` | number | `0` | 0 | 0 | Often 0 |
| `items[36].system.requirementsEx.attributes.per.value` | number | `0` | 0 | 0 | Often 0 |
| `items[36].system.requirementsEx.attributes.str.value` | number | `0` | 0 | 0 | Often 0 |
| `items[36].system.requirementsEx.isCompanion` | boolean | `False` |  |  |  |
| `items[36].system.requirementsEx.level` | number | `2` | 2 | 2 |  |
| `items[36].system.requirementsEx.levelIncrease` | number | `2` | 2 | 2 |  |
| `items[36].system.requirementsEx.magazineUuids` | array | `[]` |  |  | Empty array |
| `items[36].system.requirementsEx.notGhoul` | boolean | `False` |  |  |  |
| `items[36].system.requirementsEx.notHuman` | boolean | `False` |  |  |  |
| `items[36].system.requirementsEx.notRadiationImmune` | boolean | `False` |  |  |  |
| `items[36].system.requirementsEx.notRobot` | boolean | `False` |  |  |  |
| `items[36].system.requirementsEx.notSupermutant` | boolean | `False` |  |  |  |
| `items[36].system.source` | string | `core_rulebook` |  |  |  |
| `items[36].type` | string | `perk` |  |  |  |
| `items[42]._id` | string | `51W72MtJpUzAiURf` |  |  |  |
| `items[42]._stats.compendiumSource` | string | `Compendium.fallout.perks.Item.HUmwhrS7v9g31nOG` |  |  |  |
| `items[42]._stats.coreVersion` | string | `13.350` |  |  |  |
| `items[42]._stats.createdTime` | number | `1760030357425` | 1760030357425 | 1760030357425 |  |
| `items[42]._stats.duplicateSource` | null |  |  |  |  |
| `items[42]._stats.exportSource` | null |  |  |  |  |
| `items[42]._stats.lastModifiedBy` | string | `XPIM5aN65eH5LXee` |  |  |  |
| `items[42]._stats.modifiedTime` | number | `1760030388635` | 1760030388635 | 1760030388635 |  |
| `items[42]._stats.systemId` | string | `fallout` |  |  |  |
| `items[42]._stats.systemVersion` | string | `11.16.4` |  |  |  |
| `items[42].effects` | array | `[]` |  |  | Empty array |
| `items[42].folder` | null |  |  |  |  |
| `items[42].img` | string | `systems/fallout/assets/icons/items/perk.svg` |  |  |  |
| `items[42].name` | string | `Chemist` |  |  |  |
| `items[42].ownership.default` | number | `0` | 0 | 0 | Often 0 |
| `items[42].sort` | number | `0` | 0 | 0 | Often 0 |
| `items[42].system.description` | string | `<p>Chems you create last twice as long as normal (...` |  |  |  |
| `items[42].system.favorite` | boolean | `False` |  |  |  |
| `items[42].system.rank.max` | number | `1` | 1 | 1 |  |
| `items[42].system.rank.value` | number | `1` | 1 | 1 |  |
| `items[42].system.requirements` | string | `` |  |  |  |
| `items[42].system.requirementsEx.attributes.agi.value` | number | `0` | 0 | 0 | Often 0 |
| `items[42].system.requirementsEx.attributes.cha.value` | number | `0` | 0 | 0 | Often 0 |
| `items[42].system.requirementsEx.attributes.end.value` | number | `0` | 0 | 0 | Often 0 |
| `items[42].system.requirementsEx.attributes.int.value` | number | `7` | 7 | 7 |  |
| `items[42].system.requirementsEx.attributes.luc.value` | number | `0` | 0 | 0 | Often 0 |
| `items[42].system.requirementsEx.attributes.per.value` | number | `0` | 0 | 0 | Often 0 |
| `items[42].system.requirementsEx.attributes.str.value` | number | `0` | 0 | 0 | Often 0 |
| `items[42].system.requirementsEx.isCompanion` | boolean | `False` |  |  |  |
| `items[42].system.requirementsEx.level` | number | `1` | 1 | 1 |  |
| `items[42].system.requirementsEx.levelIncrease` | number | `0` | 0 | 0 | Often 0 |
| `items[42].system.requirementsEx.magazineUuids` | array | `[]` |  |  | Empty array |
| `items[42].system.requirementsEx.notGhoul` | boolean | `False` |  |  |  |
| `items[42].system.requirementsEx.notHuman` | boolean | `False` |  |  |  |
| `items[42].system.requirementsEx.notRadiationImmune` | boolean | `False` |  |  |  |
| `items[42].system.requirementsEx.notRobot` | boolean | `False` |  |  |  |
| `items[42].system.requirementsEx.notSupermutant` | boolean | `False` |  |  |  |
| `items[42].system.source` | string | `core_rulebook` |  |  |  |
| `items[42].type` | string | `perk` |  |  |  |

## Items - Traits

| JSON Path | Type | Examples | Min | Max | Notes |
|-----------|------|----------|-----|-----|-------|
| `items[31]._id` | string | `1NcmYRdzlSmgf0Tq` |  |  |  |
| `items[31]._stats.compendiumSource` | string | `Compendium.fallout.traits.Item.XbVNgNTQ9MLaAWEx` |  |  |  |
| `items[31]._stats.coreVersion` | string | `13.344` |  |  |  |
| `items[31]._stats.createdTime` | number | `1739552197293` | 1739552197293 | 1739552197293 |  |
| `items[31]._stats.duplicateSource` | null |  |  |  |  |
| `items[31]._stats.exportSource` | null |  |  |  |  |
| `items[31]._stats.lastModifiedBy` | string | `qqb2lyM0FgEMachb` |  |  |  |
| `items[31]._stats.modifiedTime` | number | `1739552197293` | 1739552197293 | 1739552197293 |  |
| `items[31]._stats.systemId` | string | `fallout` |  |  |  |
| `items[31]._stats.systemVersion` | string | `11.14.3` |  |  |  |
| `items[31].effects` | array | `[]` |  |  | Empty array |
| `items[31].folder` | null |  |  |  |  |
| `items[31].img` | string | `systems/fallout/assets/icons/items/trait.svg` |  |  |  |
| `items[31].name` | string | `Vault Kid` |  |  |  |
| `items[31].ownership.default` | number | `0` | 0 | 0 | Often 0 |
| `items[31].sort` | number | `0` | 0 | 0 | Often 0 |
| `items[31].system.description` | string | `<p>Your healthier start to life at the hands of tr...` |  |  |  |
| `items[31].system.favorite` | boolean | `False` |  |  |  |
| `items[31].system.source` | string | `core_rulebook` |  |  |  |
| `items[31].type` | string | `trait` |  |  |  |

## Items - Weapons

| JSON Path | Type | Examples | Min | Max | Notes |
|-----------|------|----------|-----|-----|-------|
| `items[17]._id` | string | `ywJr7QMrfEXBHZcM` |  |  |  |
| `items[17]._stats.compendiumSource` | string | `Compendium.fallout.weapons.Item.mRB3W7wrHDbWhb9i` |  |  |  |
| `items[17]._stats.coreVersion` | string | `13.344` |  |  |  |
| `items[17]._stats.createdTime` | number | `1739550514421` | 1739550514421 | 1739550514421 |  |
| `items[17]._stats.duplicateSource` | null |  |  |  |  |
| `items[17]._stats.exportSource` | null |  |  |  |  |
| `items[17]._stats.lastModifiedBy` | string | `XPIM5aN65eH5LXee` |  |  |  |
| `items[17]._stats.modifiedTime` | number | `1746721328955` | 1746721328955 | 1746721328955 |  |
| `items[17]._stats.systemId` | string | `fallout` |  |  |  |
| `items[17]._stats.systemVersion` | string | `11.15.4` |  |  |  |
| `items[17].effects` | array | `[]` |  |  | Empty array |
| `items[17].folder` | string | `Fvz7mUEk61qB057V` |  |  |  |
| `items[17].img` | string | `systems/fallout/assets/icons/items/weapon.svg` |  |  |  |
| `items[17].name` | string | `10mm Pistol` |  |  |  |
| `items[17].ownership.default` | number | `0` | 0 | 0 | Often 0 |
| `items[17].sort` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.ammo` | string | `10mm Round` |  |  |  |
| `items[17].system.ammoPerShot` | number | `1` | 1 | 1 |  |
| `items[17].system.attribute` | string | `` |  |  |  |
| `items[17].system.canBeScrapped` | boolean | `True` |  |  |  |
| `items[17].system.condition` | string | `` |  |  |  |
| `items[17].system.cost` | number | `50` | 50 | 50 |  |
| `items[17].system.creatureAttribute` | string | `body` |  |  |  |
| `items[17].system.creatureSkill` | string | `guns` |  |  |  |
| `items[17].system.damage.damageEffect.arc.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.damage.damageEffect.arc.value` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.damage.damageEffect.breaking.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.damage.damageEffect.breaking.value` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.damage.damageEffect.burst.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.damage.damageEffect.burst.value` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.damage.damageEffect.freeze.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.damage.damageEffect.freeze.value` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.damage.damageEffect.persistent.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.damage.damageEffect.persistent.value` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.damage.damageEffect.piercing_x.rank` | number | `1` | 1 | 1 |  |
| `items[17].system.damage.damageEffect.piercing_x.value` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.damage.damageEffect.radioactive.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.damage.damageEffect.radioactive.value` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.damage.damageEffect.spread.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.damage.damageEffect.spread.value` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.damage.damageEffect.stun.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.damage.damageEffect.stun.value` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.damage.damageEffect.tranquilize_x.rank` | number | `1` | 1 | 1 |  |
| `items[17].system.damage.damageEffect.tranquilize_x.value` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.damage.damageEffect.vicious.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.damage.damageEffect.vicious.value` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.damage.damageType.energy` | boolean | `False` |  |  |  |
| `items[17].system.damage.damageType.physical` | boolean | `True` |  |  |  |
| `items[17].system.damage.damageType.poison` | boolean | `False` |  |  |  |
| `items[17].system.damage.damageType.radiation` | boolean | `False` |  |  |  |
| `items[17].system.damage.originalDamageType.energy` | boolean | `False` |  |  |  |
| `items[17].system.damage.originalDamageType.physical` | boolean | `False` |  |  |  |
| `items[17].system.damage.originalDamageType.poison` | boolean | `False` |  |  |  |
| `items[17].system.damage.originalDamageType.radiation` | boolean | `False` |  |  |  |
| `items[17].system.damage.originalRating` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.damage.rating` | number | `4` | 4 | 4 |  |
| `items[17].system.damage.weaponQuality.accurate.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.damage.weaponQuality.accurate.value` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.damage.weaponQuality.ammo_hungry_x.rank` | number | `1` | 1 | 1 |  |
| `items[17].system.damage.weaponQuality.ammo_hungry_x.value` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.damage.weaponQuality.aquatic.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.damage.weaponQuality.aquatic.value` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.damage.weaponQuality.blast.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.damage.weaponQuality.blast.value` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.damage.weaponQuality.bombard.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.damage.weaponQuality.bombard.value` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.damage.weaponQuality.close_quarters.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.damage.weaponQuality.close_quarters.value` | number | `1` | 1 | 1 |  |
| `items[17].system.damage.weaponQuality.concealed.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.damage.weaponQuality.concealed.value` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.damage.weaponQuality.debilitating.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.damage.weaponQuality.debilitating.value` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.damage.weaponQuality.delay_x.rank` | number | `1` | 1 | 1 |  |
| `items[17].system.damage.weaponQuality.delay_x.value` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.damage.weaponQuality.fuel_x.rank` | number | `1` | 1 | 1 |  |
| `items[17].system.damage.weaponQuality.fuel_x.value` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.damage.weaponQuality.gatling.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.damage.weaponQuality.gatling.value` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.damage.weaponQuality.inaccurate.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.damage.weaponQuality.inaccurate.value` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.damage.weaponQuality.limited.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.damage.weaponQuality.limited.value` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.damage.weaponQuality.mine.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.damage.weaponQuality.mine.value` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.damage.weaponQuality.night_vision.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.damage.weaponQuality.night_vision.value` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.damage.weaponQuality.parry.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.damage.weaponQuality.parry.value` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.damage.weaponQuality.placed.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.damage.weaponQuality.placed.value` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.damage.weaponQuality.recoil_x.rank` | number | `1` | 1 | 1 |  |
| `items[17].system.damage.weaponQuality.recoil_x.value` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.damage.weaponQuality.recon.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.damage.weaponQuality.recon.value` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.damage.weaponQuality.reliable.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.damage.weaponQuality.reliable.value` | number | `1` | 1 | 1 |  |
| `items[17].system.damage.weaponQuality.slow_load.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.damage.weaponQuality.slow_load.value` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.damage.weaponQuality.suppressed.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.damage.weaponQuality.suppressed.value` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.damage.weaponQuality.surge.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.damage.weaponQuality.surge.value` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.damage.weaponQuality.thrown.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.damage.weaponQuality.thrown.value` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.damage.weaponQuality.two_handed.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.damage.weaponQuality.two_handed.value` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.damage.weaponQuality.unreliable.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.damage.weaponQuality.unreliable.value` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.damage.weaponQuality.unstable_radiation.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.damage.weaponQuality.unstable_radiation.value` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.damage.weaponQuality.wrangle.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.damage.weaponQuality.wrangle.value` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.description` | string | `<p><span class="fontstyle0">Small, dependable, rea...` |  |  |  |
| `items[17].system.equippable` | boolean | `True` |  |  |  |
| `items[17].system.equipped` | boolean | `False` |  |  |  |
| `items[17].system.favorite` | boolean | `True` |  |  |  |
| `items[17].system.fireRate` | number | `2` | 2 | 2 |  |
| `items[17].system.isJunk` | boolean | `False` |  |  |  |
| `items[17].system.melee` | boolean | `False` |  |  |  |
| `items[17].system.mods.current` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.mods.installedMods` | string | `` |  |  |  |
| `items[17].system.mods.list` | string | `` |  |  |  |
| `items[17].system.mods.max` | number | `6` | 6 | 6 |  |
| `items[17].system.mods.modded` | boolean | `False` |  |  |  |
| `items[17].system.naturalWeapon` | boolean | `False` |  |  |  |
| `items[17].system.originalAmmoPerShot` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.quantity` | number | `1` | 1 | 1 |  |
| `items[17].system.range` | string | `close` |  |  |  |
| `items[17].system.rarity` | number | `1` | 1 | 1 |  |
| `items[17].system.skill` | string | `` |  |  |  |
| `items[17].system.source` | string | `core_rulebook` |  |  |  |
| `items[17].system.stashed` | boolean | `False` |  |  |  |
| `items[17].system.tear` | number | `0` | 0 | 0 | Often 0 |
| `items[17].system.weaponType` | string | `smallGuns` |  |  |  |
| `items[17].system.weight` | number | `4` | 4 | 4 |  |
| `items[17].type` | string | `weapon` |  |  |  |
| `items[19]._id` | string | `BuNbqeZPbNkwZ5VL` |  |  |  |
| `items[19]._stats.compendiumSource` | string | `Compendium.fallout.weapons.Item.ijD12AylGdTDshsy` |  |  |  |
| `items[19]._stats.coreVersion` | string | `13.344` |  |  |  |
| `items[19]._stats.createdTime` | number | `1739550560711` | 1739550560711 | 1739550560711 |  |
| `items[19]._stats.duplicateSource` | null |  |  |  |  |
| `items[19]._stats.exportSource` | null |  |  |  |  |
| `items[19]._stats.lastModifiedBy` | string | `XPIM5aN65eH5LXee` |  |  |  |
| `items[19]._stats.modifiedTime` | number | `1746721328985` | 1746721328985 | 1746721328985 |  |
| `items[19]._stats.systemId` | string | `fallout` |  |  |  |
| `items[19]._stats.systemVersion` | string | `11.15.4` |  |  |  |
| `items[19].effects` | array | `[]` |  |  | Empty array |
| `items[19].folder` | string | `8HBxoFI4IGjaL6eX` |  |  |  |
| `items[19].img` | string | `systems/fallout/assets/icons/items/weapon.svg` |  |  |  |
| `items[19].name` | string | `Switchblade` |  |  |  |
| `items[19].ownership.default` | number | `0` | 0 | 0 | Often 0 |
| `items[19].sort` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.ammo` | string | `` |  |  |  |
| `items[19].system.ammoPerShot` | number | `1` | 1 | 1 |  |
| `items[19].system.attribute` | string | `` |  |  |  |
| `items[19].system.canBeScrapped` | boolean | `True` |  |  |  |
| `items[19].system.condition` | string | `` |  |  |  |
| `items[19].system.cost` | number | `20` | 20 | 20 |  |
| `items[19].system.creatureAttribute` | string | `body` |  |  |  |
| `items[19].system.creatureSkill` | string | `melee` |  |  |  |
| `items[19].system.damage.damageEffect.arc.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.damage.damageEffect.arc.value` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.damage.damageEffect.breaking.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.damage.damageEffect.breaking.value` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.damage.damageEffect.burst.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.damage.damageEffect.burst.value` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.damage.damageEffect.freeze.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.damage.damageEffect.freeze.value` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.damage.damageEffect.persistent.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.damage.damageEffect.persistent.value` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.damage.damageEffect.piercing_x.rank` | number | `1` | 1 | 1 |  |
| `items[19].system.damage.damageEffect.piercing_x.value` | number | `1` | 1 | 1 |  |
| `items[19].system.damage.damageEffect.radioactive.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.damage.damageEffect.radioactive.value` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.damage.damageEffect.spread.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.damage.damageEffect.spread.value` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.damage.damageEffect.stun.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.damage.damageEffect.stun.value` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.damage.damageEffect.tranquilize_x.rank` | number | `1` | 1 | 1 |  |
| `items[19].system.damage.damageEffect.tranquilize_x.value` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.damage.damageEffect.vicious.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.damage.damageEffect.vicious.value` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.damage.damageType.energy` | boolean | `False` |  |  |  |
| `items[19].system.damage.damageType.physical` | boolean | `True` |  |  |  |
| `items[19].system.damage.damageType.poison` | boolean | `False` |  |  |  |
| `items[19].system.damage.damageType.radiation` | boolean | `False` |  |  |  |
| `items[19].system.damage.originalDamageType.energy` | boolean | `False` |  |  |  |
| `items[19].system.damage.originalDamageType.physical` | boolean | `False` |  |  |  |
| `items[19].system.damage.originalDamageType.poison` | boolean | `False` |  |  |  |
| `items[19].system.damage.originalDamageType.radiation` | boolean | `False` |  |  |  |
| `items[19].system.damage.originalRating` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.damage.rating` | number | `2` | 2 | 2 |  |
| `items[19].system.damage.weaponQuality.accurate.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.damage.weaponQuality.accurate.value` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.damage.weaponQuality.ammo_hungry_x.rank` | number | `1` | 1 | 1 |  |
| `items[19].system.damage.weaponQuality.ammo_hungry_x.value` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.damage.weaponQuality.aquatic.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.damage.weaponQuality.aquatic.value` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.damage.weaponQuality.blast.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.damage.weaponQuality.blast.value` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.damage.weaponQuality.bombard.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.damage.weaponQuality.bombard.value` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.damage.weaponQuality.close_quarters.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.damage.weaponQuality.close_quarters.value` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.damage.weaponQuality.concealed.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.damage.weaponQuality.concealed.value` | number | `1` | 1 | 1 |  |
| `items[19].system.damage.weaponQuality.debilitating.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.damage.weaponQuality.debilitating.value` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.damage.weaponQuality.delay_x.rank` | number | `1` | 1 | 1 |  |
| `items[19].system.damage.weaponQuality.delay_x.value` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.damage.weaponQuality.fuel_x.rank` | number | `1` | 1 | 1 |  |
| `items[19].system.damage.weaponQuality.fuel_x.value` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.damage.weaponQuality.gatling.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.damage.weaponQuality.gatling.value` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.damage.weaponQuality.inaccurate.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.damage.weaponQuality.inaccurate.value` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.damage.weaponQuality.limited.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.damage.weaponQuality.limited.value` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.damage.weaponQuality.mine.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.damage.weaponQuality.mine.value` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.damage.weaponQuality.night_vision.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.damage.weaponQuality.night_vision.value` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.damage.weaponQuality.parry.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.damage.weaponQuality.parry.value` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.damage.weaponQuality.placed.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.damage.weaponQuality.placed.value` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.damage.weaponQuality.recoil_x.rank` | number | `1` | 1 | 1 |  |
| `items[19].system.damage.weaponQuality.recoil_x.value` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.damage.weaponQuality.recon.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.damage.weaponQuality.recon.value` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.damage.weaponQuality.reliable.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.damage.weaponQuality.reliable.value` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.damage.weaponQuality.slow_load.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.damage.weaponQuality.slow_load.value` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.damage.weaponQuality.suppressed.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.damage.weaponQuality.suppressed.value` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.damage.weaponQuality.surge.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.damage.weaponQuality.surge.value` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.damage.weaponQuality.thrown.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.damage.weaponQuality.thrown.value` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.damage.weaponQuality.two_handed.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.damage.weaponQuality.two_handed.value` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.damage.weaponQuality.unreliable.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.damage.weaponQuality.unreliable.value` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.damage.weaponQuality.unstable_radiation.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.damage.weaponQuality.unstable_radiation.value` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.damage.weaponQuality.wrangle.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.damage.weaponQuality.wrangle.value` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.description` | string | `<p><span class="fontstyle0">The switchblade is a c...` |  |  |  |
| `items[19].system.equippable` | boolean | `True` |  |  |  |
| `items[19].system.equipped` | boolean | `False` |  |  |  |
| `items[19].system.favorite` | boolean | `True` |  |  |  |
| `items[19].system.fireRate` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.isJunk` | boolean | `False` |  |  |  |
| `items[19].system.melee` | boolean | `False` |  |  |  |
| `items[19].system.mods.current` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.mods.installedMods` | string | `` |  |  |  |
| `items[19].system.mods.list` | string | `` |  |  |  |
| `items[19].system.mods.max` | number | `1` | 1 | 1 |  |
| `items[19].system.mods.modded` | boolean | `False` |  |  |  |
| `items[19].system.naturalWeapon` | boolean | `False` |  |  |  |
| `items[19].system.originalAmmoPerShot` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.quantity` | number | `1` | 1 | 1 |  |
| `items[19].system.range` | string | `close` |  |  |  |
| `items[19].system.rarity` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.skill` | string | `` |  |  |  |
| `items[19].system.source` | string | `core_rulebook` |  |  |  |
| `items[19].system.stashed` | boolean | `False` |  |  |  |
| `items[19].system.tear` | number | `0` | 0 | 0 | Often 0 |
| `items[19].system.weaponType` | string | `meleeWeapons` |  |  |  |
| `items[19].system.weight` | number | `1` | 1 | 1 |  |
| `items[19].type` | string | `weapon` |  |  |  |
| `items[34]._id` | string | `lS7rIqefVVvEy7X5` |  |  |  |
| `items[34]._stats.compendiumSource` | null |  |  |  |  |
| `items[34]._stats.coreVersion` | string | `13.344` |  |  |  |
| `items[34]._stats.createdTime` | number | `1744225144229` | 1744225144229 | 1744225144229 |  |
| `items[34]._stats.duplicateSource` | null |  |  |  |  |
| `items[34]._stats.exportSource` | null |  |  |  |  |
| `items[34]._stats.lastModifiedBy` | string | `XPIM5aN65eH5LXee` |  |  |  |
| `items[34]._stats.modifiedTime` | number | `1746731831603` | 1746731831603 | 1746731831603 |  |
| `items[34]._stats.systemId` | string | `fallout` |  |  |  |
| `items[34]._stats.systemVersion` | string | `11.15.4` |  |  |  |
| `items[34].effects` | array | `[]` |  |  | Empty array |
| `items[34].folder` | null |  |  |  |  |
| `items[34].img` | string | `systems/fallout/assets/icons/items/weapon.svg` |  |  |  |
| `items[34].name` | string | `Polierte Pfanne "Sophie"` |  |  |  |
| `items[34].ownership.default` | number | `0` | 0 | 0 | Often 0 |
| `items[34].sort` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.ammo` | string | `` |  |  |  |
| `items[34].system.ammoPerShot` | number | `1` | 1 | 1 |  |
| `items[34].system.attribute` | string | `` |  |  |  |
| `items[34].system.canBeScrapped` | boolean | `True` |  |  |  |
| `items[34].system.condition` | string | `` |  |  |  |
| `items[34].system.cost` | number | `100` | 100 | 100 |  |
| `items[34].system.creatureAttribute` | string | `body` |  |  |  |
| `items[34].system.creatureSkill` | string | `melee` |  |  |  |
| `items[34].system.damage.damageEffect.arc.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.damage.damageEffect.arc.value` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.damage.damageEffect.breaking.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.damage.damageEffect.breaking.value` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.damage.damageEffect.burst.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.damage.damageEffect.burst.value` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.damage.damageEffect.freeze.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.damage.damageEffect.freeze.value` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.damage.damageEffect.persistent.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.damage.damageEffect.persistent.value` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.damage.damageEffect.piercing_x.rank` | number | `1` | 1 | 1 |  |
| `items[34].system.damage.damageEffect.piercing_x.value` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.damage.damageEffect.radioactive.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.damage.damageEffect.radioactive.value` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.damage.damageEffect.spread.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.damage.damageEffect.spread.value` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.damage.damageEffect.stun.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.damage.damageEffect.stun.value` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.damage.damageEffect.tranquilize_x.rank` | number | `1` | 1 | 1 |  |
| `items[34].system.damage.damageEffect.tranquilize_x.value` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.damage.damageEffect.vicious.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.damage.damageEffect.vicious.value` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.damage.damageType.energy` | boolean | `False` |  |  |  |
| `items[34].system.damage.damageType.physical` | boolean | `True` |  |  |  |
| `items[34].system.damage.damageType.poison` | boolean | `False` |  |  |  |
| `items[34].system.damage.damageType.radiation` | boolean | `False` |  |  |  |
| `items[34].system.damage.originalDamageType.energy` | boolean | `False` |  |  |  |
| `items[34].system.damage.originalDamageType.physical` | boolean | `False` |  |  |  |
| `items[34].system.damage.originalDamageType.poison` | boolean | `False` |  |  |  |
| `items[34].system.damage.originalDamageType.radiation` | boolean | `False` |  |  |  |
| `items[34].system.damage.originalRating` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.damage.rating` | number | `4` | 4 | 4 |  |
| `items[34].system.damage.weaponQuality.accurate.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.damage.weaponQuality.accurate.value` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.damage.weaponQuality.ammo_hungry_x.rank` | number | `1` | 1 | 1 |  |
| `items[34].system.damage.weaponQuality.ammo_hungry_x.value` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.damage.weaponQuality.aquatic.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.damage.weaponQuality.aquatic.value` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.damage.weaponQuality.blast.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.damage.weaponQuality.blast.value` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.damage.weaponQuality.bombard.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.damage.weaponQuality.bombard.value` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.damage.weaponQuality.close_quarters.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.damage.weaponQuality.close_quarters.value` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.damage.weaponQuality.concealed.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.damage.weaponQuality.concealed.value` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.damage.weaponQuality.debilitating.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.damage.weaponQuality.debilitating.value` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.damage.weaponQuality.delay_x.rank` | number | `1` | 1 | 1 |  |
| `items[34].system.damage.weaponQuality.delay_x.value` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.damage.weaponQuality.fuel_x.rank` | number | `1` | 1 | 1 |  |
| `items[34].system.damage.weaponQuality.fuel_x.value` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.damage.weaponQuality.gatling.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.damage.weaponQuality.gatling.value` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.damage.weaponQuality.inaccurate.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.damage.weaponQuality.inaccurate.value` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.damage.weaponQuality.limited.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.damage.weaponQuality.limited.value` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.damage.weaponQuality.mine.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.damage.weaponQuality.mine.value` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.damage.weaponQuality.night_vision.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.damage.weaponQuality.night_vision.value` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.damage.weaponQuality.parry.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.damage.weaponQuality.parry.value` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.damage.weaponQuality.placed.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.damage.weaponQuality.placed.value` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.damage.weaponQuality.recoil_x.rank` | number | `1` | 1 | 1 |  |
| `items[34].system.damage.weaponQuality.recoil_x.value` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.damage.weaponQuality.recon.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.damage.weaponQuality.recon.value` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.damage.weaponQuality.reliable.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.damage.weaponQuality.reliable.value` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.damage.weaponQuality.slow_load.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.damage.weaponQuality.slow_load.value` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.damage.weaponQuality.suppressed.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.damage.weaponQuality.suppressed.value` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.damage.weaponQuality.surge.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.damage.weaponQuality.surge.value` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.damage.weaponQuality.thrown.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.damage.weaponQuality.thrown.value` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.damage.weaponQuality.two_handed.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.damage.weaponQuality.two_handed.value` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.damage.weaponQuality.unreliable.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.damage.weaponQuality.unreliable.value` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.damage.weaponQuality.unstable_radiation.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.damage.weaponQuality.unstable_radiation.value` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.damage.weaponQuality.wrangle.rank` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.damage.weaponQuality.wrangle.value` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.description` | string | `<p>Eine Pfanne, die Ellie in einer Notsituation da...` |  |  |  |
| `items[34].system.equippable` | boolean | `True` |  |  |  |
| `items[34].system.equipped` | boolean | `False` |  |  |  |
| `items[34].system.favorite` | boolean | `False` |  |  |  |
| `items[34].system.fireRate` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.isJunk` | boolean | `False` |  |  |  |
| `items[34].system.melee` | boolean | `False` |  |  |  |
| `items[34].system.mods.current` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.mods.installedMods` | string | `` |  |  |  |
| `items[34].system.mods.list` | string | `` |  |  |  |
| `items[34].system.mods.max` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.mods.modded` | boolean | `False` |  |  |  |
| `items[34].system.naturalWeapon` | boolean | `False` |  |  |  |
| `items[34].system.originalAmmoPerShot` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.quantity` | number | `1` | 1 | 1 |  |
| `items[34].system.quantityRoll` | string | `` |  |  |  |
| `items[34].system.range` | string | `close` |  |  |  |
| `items[34].system.rarity` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.skill` | string | `` |  |  |  |
| `items[34].system.source` | string | `` |  |  |  |
| `items[34].system.stashed` | boolean | `False` |  |  |  |
| `items[34].system.tear` | number | `0` | 0 | 0 | Often 0 |
| `items[34].system.weaponType` | string | `meleeWeapons` |  |  |  |
| `items[34].system.weight` | number | `1` | 1 | 1 |  |
| `items[34].type` | string | `weapon` |  |  |  |

## Items - Ammo

| JSON Path | Type | Examples | Min | Max | Notes |
|-----------|------|----------|-----|-----|-------|
| `items[18]._id` | string | `YuKWXibLXToIm03t` |  |  |  |
| `items[18]._stats.compendiumSource` | string | `Compendium.fallout.ammunition.Item.1Mku27VQTcwBCwO...` |  |  |  |
| `items[18]._stats.coreVersion` | string | `13.350` |  |  |  |
| `items[18]._stats.createdTime` | number | `1739550524263` | 1739550524263 | 1739550524263 |  |
| `items[18]._stats.duplicateSource` | null |  |  |  |  |
| `items[18]._stats.exportSource` | null |  |  |  |  |
| `items[18]._stats.lastModifiedBy` | string | `qqb2lyM0FgEMachb` |  |  |  |
| `items[18]._stats.modifiedTime` | number | `1760035829273` | 1760035829273 | 1760035829273 |  |
| `items[18]._stats.systemId` | string | `fallout` |  |  |  |
| `items[18]._stats.systemVersion` | string | `11.16.4` |  |  |  |
| `items[18].effects` | array | `[]` |  |  | Empty array |
| `items[18].folder` | null |  |  |  |  |
| `items[18].img` | string | `systems/fallout/assets/icons/items/ammo.svg` |  |  |  |
| `items[18].name` | string | `10mm Round` |  |  |  |
| `items[18].ownership.default` | number | `0` | 0 | 0 | Often 0 |
| `items[18].sort` | number | `0` | 0 | 0 | Often 0 |
| `items[18].system.charges.current` | number | `1` | 1 | 1 |  |
| `items[18].system.charges.max` | number | `1` | 1 | 1 |  |
| `items[18].system.cost` | number | `2` | 2 | 2 |  |
| `items[18].system.description` | string | `<p><span class="fontstyle0">One of the most common...` |  |  |  |
| `items[18].system.effect` | string | `` |  |  |  |
| `items[18].system.favorite` | boolean | `False` |  |  |  |
| `items[18].system.fusionCore` | boolean | `False` |  |  |  |
| `items[18].system.quantity` | number | `10` | 10 | 10 |  |
| `items[18].system.quantityRoll` | string | `8+4dc` |  |  |  |
| `items[18].system.rarity` | number | `0` | 0 | 0 | Often 0 |
| `items[18].system.shots.current` | number | `1` | 1 | 1 |  |
| `items[18].system.shots.max` | number | `1` | 1 | 1 |  |
| `items[18].system.source` | string | `core_rulebook` |  |  |  |
| `items[18].system.stashed` | boolean | `False` |  |  |  |
| `items[18].system.type` | string | `` |  |  |  |
| `items[18].system.weight` | number | `0.025` | 0.025 | 0.025 |  |
| `items[18].type` | string | `ammo` |  |  |  |

## Items - Apparel

| JSON Path | Type | Examples | Min | Max | Notes |
|-----------|------|----------|-----|-----|-------|
| `items[20]._id` | string | `USgGkNgQiA30uJfi` |  |  |  |
| `items[20]._stats.compendiumSource` | string | `Compendium.fallout.apparel.Item.aOmUGU0KhxIusQzy` |  |  |  |
| `items[20]._stats.coreVersion` | string | `13.344` |  |  |  |
| `items[20]._stats.createdTime` | number | `1739550604410` | 1739550604410 | 1739550604410 |  |
| `items[20]._stats.duplicateSource` | null |  |  |  |  |
| `items[20]._stats.exportSource` | null |  |  |  |  |
| `items[20]._stats.lastModifiedBy` | string | `qqb2lyM0FgEMachb` |  |  |  |
| `items[20]._stats.modifiedTime` | number | `1739550620119` | 1739550620119 | 1739550620119 |  |
| `items[20]._stats.systemId` | string | `fallout` |  |  |  |
| `items[20]._stats.systemVersion` | string | `11.14.3` |  |  |  |
| `items[20].effects` | array | `[]` |  |  | Empty array |
| `items[20].folder` | string | `mtR30GikhQq9bCZw` |  |  |  |
| `items[20].img` | string | `systems/fallout/assets/icons/items/apparel.svg` |  |  |  |
| `items[20].name` | string | `Vault Jumpsuit` |  |  |  |
| `items[20].ownership.default` | number | `0` | 0 | 0 | Often 0 |
| `items[20].sort` | number | `0` | 0 | 0 | Often 0 |
| `items[20].system.apparelType` | string | `clothing` |  |  |  |
| `items[20].system.canBeScrapped` | boolean | `True` |  |  |  |
| `items[20].system.cost` | number | `20` | 20 | 20 |  |
| `items[20].system.description` | string | `<p><span class="fontstyle0">The standard garment f...` |  |  |  |
| `items[20].system.equippable` | boolean | `True` |  |  |  |
| `items[20].system.equipped` | boolean | `True` |  |  |  |
| `items[20].system.favorite` | boolean | `False` |  |  |  |
| `items[20].system.health.max` | number | `0` | 0 | 0 | Often 0 |
| `items[20].system.health.min` | number | `0` | 0 | 0 | Often 0 |
| `items[20].system.health.mod` | number | `0` | 0 | 0 | Often 0 |
| `items[20].system.health.value` | number | `0` | 0 | 0 | Often 0 |
| `items[20].system.isJunk` | boolean | `False` |  |  |  |
| `items[20].system.location.armL` | boolean | `True` |  |  |  |
| `items[20].system.location.armR` | boolean | `True` |  |  |  |
| `items[20].system.location.head` | boolean | `False` |  |  |  |
| `items[20].system.location.legL` | boolean | `True` |  |  |  |
| `items[20].system.location.legR` | boolean | `True` |  |  |  |
| `items[20].system.location.torso` | boolean | `True` |  |  |  |
| `items[20].system.mods.current` | number | `0` | 0 | 0 | Often 0 |
| `items[20].system.mods.installedMods` | string | `` |  |  |  |
| `items[20].system.mods.list` | string | `` |  |  |  |
| `items[20].system.mods.max` | number | `1` | 1 | 1 |  |
| `items[20].system.mods.modded` | boolean | `False` |  |  |  |
| `items[20].system.powerArmor.frameId` | string | `` |  |  |  |
| `items[20].system.powerArmor.isFrame` | boolean | `False` |  |  |  |
| `items[20].system.powerArmor.powered` | boolean | `False` |  |  |  |
| `items[20].system.quantity` | number | `1` | 1 | 1 |  |
| `items[20].system.rarity` | number | `2` | 2 | 2 |  |
| `items[20].system.resistance.energy` | number | `1` | 1 | 1 |  |
| `items[20].system.resistance.physical` | number | `0` | 0 | 0 | Often 0 |
| `items[20].system.resistance.radiation` | number | `2` | 2 | 2 |  |
| `items[20].system.shadowed` | boolean | `False` |  |  |  |
| `items[20].system.source` | string | `core_rulebook` |  |  |  |
| `items[20].system.stashed` | boolean | `False` |  |  |  |
| `items[20].system.weight` | number | `1` | 1 | 1 |  |
| `items[20].type` | string | `apparel` |  |  |  |
| `items[21]._id` | string | `EO5kuPSw0mNskG3K` |  |  |  |
| `items[21]._stats.compendiumSource` | string | `Compendium.fallout.apparel.Item.WeHTP6Gw6Sr6HN8N` |  |  |  |
| `items[21]._stats.coreVersion` | string | `13.344` |  |  |  |
| `items[21]._stats.createdTime` | number | `1739550616552` | 1739550616552 | 1739550616552 |  |
| `items[21]._stats.duplicateSource` | null |  |  |  |  |
| `items[21]._stats.exportSource` | null |  |  |  |  |
| `items[21]._stats.lastModifiedBy` | string | `qqb2lyM0FgEMachb` |  |  |  |
| `items[21]._stats.modifiedTime` | number | `1740688287088` | 1740688287088 | 1740688287088 |  |
| `items[21]._stats.systemId` | string | `fallout` |  |  |  |
| `items[21]._stats.systemVersion` | string | `11.14.3` |  |  |  |
| `items[21].effects` | array | `[]` |  |  | Empty array |
| `items[21].folder` | string | `wq5Mhfa0U7SlJgyP` |  |  |  |
| `items[21].img` | string | `systems/fallout/assets/icons/items/apparel.svg` |  |  |  |
| `items[21].name` | string | `Formal Hat` |  |  |  |
| `items[21].ownership.default` | number | `0` | 0 | 0 | Often 0 |
| `items[21].sort` | number | `0` | 0 | 0 | Often 0 |
| `items[21].system.apparelType` | string | `headgear` |  |  |  |
| `items[21].system.canBeScrapped` | boolean | `True` |  |  |  |
| `items[21].system.cost` | number | `15` | 15 | 15 |  |
| `items[21].system.description` | string | `<p><span class="fontstyle0">A smart-looking hat, t...` |  |  |  |
| `items[21].system.equippable` | boolean | `True` |  |  |  |
| `items[21].system.equipped` | boolean | `False` |  |  |  |
| `items[21].system.favorite` | boolean | `False` |  |  |  |
| `items[21].system.health.max` | number | `0` | 0 | 0 | Often 0 |
| `items[21].system.health.min` | number | `0` | 0 | 0 | Often 0 |
| `items[21].system.health.mod` | number | `0` | 0 | 0 | Often 0 |
| `items[21].system.health.value` | number | `0` | 0 | 0 | Often 0 |
| `items[21].system.isJunk` | boolean | `False` |  |  |  |
| `items[21].system.location.armL` | boolean | `False` |  |  |  |
| `items[21].system.location.armR` | boolean | `False` |  |  |  |
| `items[21].system.location.head` | boolean | `True` |  |  |  |
| `items[21].system.location.legL` | boolean | `False` |  |  |  |
| `items[21].system.location.legR` | boolean | `False` |  |  |  |
| `items[21].system.location.torso` | boolean | `False` |  |  |  |
| `items[21].system.mods.current` | number | `0` | 0 | 0 | Often 0 |
| `items[21].system.mods.installedMods` | string | `` |  |  |  |
| `items[21].system.mods.list` | string | `` |  |  |  |
| `items[21].system.mods.max` | number | `1` | 1 | 1 |  |
| `items[21].system.mods.modded` | boolean | `False` |  |  |  |
| `items[21].system.powerArmor.frameId` | string | `` |  |  |  |
| `items[21].system.powerArmor.isFrame` | boolean | `False` |  |  |  |
| `items[21].system.powerArmor.powered` | boolean | `False` |  |  |  |
| `items[21].system.quantity` | number | `1` | 1 | 1 |  |
| `items[21].system.rarity` | number | `2` | 2 | 2 |  |
| `items[21].system.resistance.energy` | number | `0` | 0 | 0 | Often 0 |
| `items[21].system.resistance.physical` | number | `0` | 0 | 0 | Often 0 |
| `items[21].system.resistance.radiation` | number | `0` | 0 | 0 | Often 0 |
| `items[21].system.shadowed` | boolean | `False` |  |  |  |
| `items[21].system.source` | string | `core_rulebook` |  |  |  |
| `items[21].system.stashed` | boolean | `False` |  |  |  |
| `items[21].system.weight` | number | `0` | 0 | 0 | Often 0 |
| `items[21].type` | string | `apparel` |  |  |  |
| `items[22]._id` | string | `5ivt9Eusm1o5zy3s` |  |  |  |
| `items[22]._stats.compendiumSource` | string | `Compendium.fallout.apparel.Item.cdwX7EVolnIWRaZi` |  |  |  |
| `items[22]._stats.coreVersion` | string | `13.344` |  |  |  |
| `items[22]._stats.createdTime` | number | `1739550639599` | 1739550639599 | 1739550639599 |  |
| `items[22]._stats.duplicateSource` | null |  |  |  |  |
| `items[22]._stats.exportSource` | null |  |  |  |  |
| `items[22]._stats.lastModifiedBy` | string | `qqb2lyM0FgEMachb` |  |  |  |
| `items[22]._stats.modifiedTime` | number | `1739550642215` | 1739550642215 | 1739550642215 |  |
| `items[22]._stats.systemId` | string | `fallout` |  |  |  |
| `items[22]._stats.systemVersion` | string | `11.14.3` |  |  |  |
| `items[22].effects` | array | `[]` |  |  | Empty array |
| `items[22].folder` | string | `FiAqKiTwXAp5BbMw` |  |  |  |
| `items[22].img` | string | `systems/fallout/assets/icons/items/apparel.svg` |  |  |  |
| `items[22].name` | string | `Lab Coat` |  |  |  |
| `items[22].ownership.default` | number | `0` | 0 | 0 | Often 0 |
| `items[22].sort` | number | `0` | 0 | 0 | Often 0 |
| `items[22].system.apparelType` | string | `outfit` |  |  |  |
| `items[22].system.canBeScrapped` | boolean | `True` |  |  |  |
| `items[22].system.cost` | number | `10` | 10 | 10 |  |
| `items[22].system.description` | string | `<p><span class="fontstyle0">A white coat&mdash;tho...` |  |  |  |
| `items[22].system.equippable` | boolean | `True` |  |  |  |
| `items[22].system.equipped` | boolean | `True` |  |  |  |
| `items[22].system.favorite` | boolean | `False` |  |  |  |
| `items[22].system.health.max` | number | `0` | 0 | 0 | Often 0 |
| `items[22].system.health.min` | number | `0` | 0 | 0 | Often 0 |
| `items[22].system.health.mod` | number | `0` | 0 | 0 | Often 0 |
| `items[22].system.health.value` | number | `0` | 0 | 0 | Often 0 |
| `items[22].system.isJunk` | boolean | `False` |  |  |  |
| `items[22].system.location.armL` | boolean | `True` |  |  |  |
| `items[22].system.location.armR` | boolean | `True` |  |  |  |
| `items[22].system.location.head` | boolean | `False` |  |  |  |
| `items[22].system.location.legL` | boolean | `True` |  |  |  |
| `items[22].system.location.legR` | boolean | `True` |  |  |  |
| `items[22].system.location.torso` | boolean | `True` |  |  |  |
| `items[22].system.mods.current` | number | `0` | 0 | 0 | Often 0 |
| `items[22].system.mods.installedMods` | string | `` |  |  |  |
| `items[22].system.mods.list` | string | `` |  |  |  |
| `items[22].system.mods.max` | number | `1` | 1 | 1 |  |
| `items[22].system.mods.modded` | boolean | `False` |  |  |  |
| `items[22].system.powerArmor.frameId` | string | `` |  |  |  |
| `items[22].system.powerArmor.isFrame` | boolean | `False` |  |  |  |
| `items[22].system.powerArmor.powered` | boolean | `False` |  |  |  |
| `items[22].system.quantity` | number | `1` | 1 | 1 |  |
| `items[22].system.rarity` | number | `1` | 1 | 1 |  |
| `items[22].system.resistance.energy` | number | `0` | 0 | 0 | Often 0 |
| `items[22].system.resistance.physical` | number | `0` | 0 | 0 | Often 0 |
| `items[22].system.resistance.radiation` | number | `0` | 0 | 0 | Often 0 |
| `items[22].system.shadowed` | boolean | `False` |  |  |  |
| `items[22].system.source` | string | `core_rulebook` |  |  |  |
| `items[22].system.stashed` | boolean | `False` |  |  |  |
| `items[22].system.weight` | number | `2` | 2 | 2 |  |
| `items[22].type` | string | `apparel` |  |  |  |
| `items[23]._id` | string | `OkeMaAwEgA86qYrk` |  |  |  |
| `items[23]._stats.compendiumSource` | null |  |  |  |  |
| `items[23]._stats.coreVersion` | string | `13.344` |  |  |  |
| `items[23]._stats.createdTime` | number | `1739550708367` | 1739550708367 | 1739550708367 |  |
| `items[23]._stats.duplicateSource` | null |  |  |  |  |
| `items[23]._stats.exportSource` | null |  |  |  |  |
| `items[23]._stats.lastModifiedBy` | string | `qqb2lyM0FgEMachb` |  |  |  |
| `items[23]._stats.modifiedTime` | number | `1739550708367` | 1739550708367 | 1739550708367 |  |
| `items[23]._stats.systemId` | string | `fallout` |  |  |  |
| `items[23]._stats.systemVersion` | string | `11.14.3` |  |  |  |
| `items[23].effects` | array | `[]` |  |  | Empty array |
| `items[23].folder` | null |  |  |  |  |
| `items[23].img` | string | `systems/fallout/assets/icons/items/apparel.svg` |  |  |  |
| `items[23].name` | string | `New Apparel` |  |  |  |
| `items[23].ownership.default` | number | `0` | 0 | 0 | Often 0 |
| `items[23].sort` | number | `0` | 0 | 0 | Often 0 |
| `items[23].system.apparelType` | string | `powerArmor` |  |  |  |
| `items[23].system.canBeScrapped` | boolean | `True` |  |  |  |
| `items[23].system.cost` | number | `0` | 0 | 0 | Often 0 |
| `items[23].system.description` | string | `` |  |  |  |
| `items[23].system.equippable` | boolean | `True` |  |  |  |
| `items[23].system.equipped` | boolean | `False` |  |  |  |
| `items[23].system.favorite` | boolean | `False` |  |  |  |
| `items[23].system.health.max` | number | `0` | 0 | 0 | Often 0 |
| `items[23].system.health.min` | number | `0` | 0 | 0 | Often 0 |
| `items[23].system.health.mod` | number | `0` | 0 | 0 | Often 0 |
| `items[23].system.health.value` | number | `0` | 0 | 0 | Often 0 |
| `items[23].system.isJunk` | boolean | `False` |  |  |  |
| `items[23].system.location.armL` | boolean | `False` |  |  |  |
| `items[23].system.location.armR` | boolean | `False` |  |  |  |
| `items[23].system.location.head` | boolean | `False` |  |  |  |
| `items[23].system.location.legL` | boolean | `False` |  |  |  |
| `items[23].system.location.legR` | boolean | `False` |  |  |  |
| `items[23].system.location.torso` | boolean | `False` |  |  |  |
| `items[23].system.mods.current` | number | `0` | 0 | 0 | Often 0 |
| `items[23].system.mods.installedMods` | string | `` |  |  |  |
| `items[23].system.mods.list` | string | `` |  |  |  |
| `items[23].system.mods.max` | number | `0` | 0 | 0 | Often 0 |
| `items[23].system.mods.modded` | boolean | `False` |  |  |  |
| `items[23].system.powerArmor.frameId` | string | `` |  |  |  |
| `items[23].system.powerArmor.isFrame` | boolean | `False` |  |  |  |
| `items[23].system.powerArmor.powered` | boolean | `False` |  |  |  |
| `items[23].system.quantity` | number | `1` | 1 | 1 |  |
| `items[23].system.rarity` | number | `0` | 0 | 0 | Often 0 |
| `items[23].system.resistance.energy` | number | `0` | 0 | 0 | Often 0 |
| `items[23].system.resistance.physical` | number | `0` | 0 | 0 | Often 0 |
| `items[23].system.resistance.radiation` | number | `0` | 0 | 0 | Often 0 |
| `items[23].system.shadowed` | boolean | `False` |  |  |  |
| `items[23].system.source` | string | `` |  |  |  |
| `items[23].system.stashed` | boolean | `False` |  |  |  |
| `items[23].system.weight` | number | `0` | 0 | 0 | Often 0 |
| `items[23].type` | string | `apparel` |  |  |  |
| `items[24]._id` | string | `dmaRfey1nUQEKIv7` |  |  |  |
| `items[24]._stats.compendiumSource` | string | `Compendium.fallout.apparel.Item.RWHypmbHATEbfGdU` |  |  |  |
| `items[24]._stats.coreVersion` | string | `13.344` |  |  |  |
| `items[24]._stats.createdTime` | number | `1739550840576` | 1739550840576 | 1739550840576 |  |
| `items[24]._stats.duplicateSource` | null |  |  |  |  |
| `items[24]._stats.exportSource` | null |  |  |  |  |
| `items[24]._stats.lastModifiedBy` | string | `qqb2lyM0FgEMachb` |  |  |  |
| `items[24]._stats.modifiedTime` | number | `1739550840576` | 1739550840576 | 1739550840576 |  |
| `items[24]._stats.systemId` | string | `fallout` |  |  |  |
| `items[24]._stats.systemVersion` | string | `11.14.3` |  |  |  |
| `items[24].effects` | array | `[]` |  |  | Empty array |
| `items[24].folder` | string | `FiAqKiTwXAp5BbMw` |  |  |  |
| `items[24].img` | string | `systems/fallout/assets/icons/items/apparel.svg` |  |  |  |
| `items[24].name` | string | `Formal Clothing` |  |  |  |
| `items[24].ownership.default` | number | `0` | 0 | 0 | Often 0 |
| `items[24].sort` | number | `0` | 0 | 0 | Often 0 |
| `items[24].system.apparelType` | string | `outfit` |  |  |  |
| `items[24].system.canBeScrapped` | boolean | `True` |  |  |  |
| `items[24].system.cost` | number | `30` | 30 | 30 |  |
| `items[24].system.description` | string | `<p><span class="fontstyle0">A nice suit, a pretty ...` |  |  |  |
| `items[24].system.equippable` | boolean | `True` |  |  |  |
| `items[24].system.equipped` | boolean | `False` |  |  |  |
| `items[24].system.favorite` | boolean | `False` |  |  |  |
| `items[24].system.health.max` | number | `0` | 0 | 0 | Often 0 |
| `items[24].system.health.min` | number | `0` | 0 | 0 | Often 0 |
| `items[24].system.health.mod` | number | `0` | 0 | 0 | Often 0 |
| `items[24].system.health.value` | number | `0` | 0 | 0 | Often 0 |
| `items[24].system.isJunk` | boolean | `False` |  |  |  |
| `items[24].system.location.armL` | boolean | `True` |  |  |  |
| `items[24].system.location.armR` | boolean | `True` |  |  |  |
| `items[24].system.location.head` | boolean | `False` |  |  |  |
| `items[24].system.location.legL` | boolean | `True` |  |  |  |
| `items[24].system.location.legR` | boolean | `True` |  |  |  |
| `items[24].system.location.torso` | boolean | `True` |  |  |  |
| `items[24].system.mods.current` | number | `0` | 0 | 0 | Often 0 |
| `items[24].system.mods.installedMods` | string | `` |  |  |  |
| `items[24].system.mods.list` | string | `` |  |  |  |
| `items[24].system.mods.max` | number | `1` | 1 | 1 |  |
| `items[24].system.mods.modded` | boolean | `False` |  |  |  |
| `items[24].system.powerArmor.frameId` | string | `` |  |  |  |
| `items[24].system.powerArmor.isFrame` | boolean | `False` |  |  |  |
| `items[24].system.powerArmor.powered` | boolean | `False` |  |  |  |
| `items[24].system.quantity` | number | `1` | 1 | 1 |  |
| `items[24].system.rarity` | number | `2` | 2 | 2 |  |
| `items[24].system.resistance.energy` | number | `0` | 0 | 0 | Often 0 |
| `items[24].system.resistance.physical` | number | `0` | 0 | 0 | Often 0 |
| `items[24].system.resistance.radiation` | number | `0` | 0 | 0 | Often 0 |
| `items[24].system.shadowed` | boolean | `False` |  |  |  |
| `items[24].system.source` | string | `core_rulebook` |  |  |  |
| `items[24].system.stashed` | boolean | `False` |  |  |  |
| `items[24].system.weight` | number | `2` | 2 | 2 |  |
| `items[24].type` | string | `apparel` |  |  |  |
| `items[39]._id` | string | `veeMX0047eQOk3mx` |  |  |  |
| `items[39]._stats.compendiumSource` | string | `Compendium.fallout.apparel.Item.hKGbIZhOnncmk7UT` |  |  |  |
| `items[39]._stats.coreVersion` | string | `13.344` |  |  |  |
| `items[39]._stats.createdTime` | number | `1747944664357` | 1747944664357 | 1747944664357 |  |
| `items[39]._stats.duplicateSource` | null |  |  |  |  |
| `items[39]._stats.exportSource` | null |  |  |  |  |
| `items[39]._stats.lastModifiedBy` | string | `qqb2lyM0FgEMachb` |  |  |  |
| `items[39]._stats.modifiedTime` | number | `1747944788903` | 1747944788903 | 1747944788903 |  |
| `items[39]._stats.systemId` | string | `fallout` |  |  |  |
| `items[39]._stats.systemVersion` | string | `11.15.6` |  |  |  |
| `items[39].effects` | array | `[]` |  |  | Empty array |
| `items[39].folder` | string | `wq5Mhfa0U7SlJgyP` |  |  |  |
| `items[39].img` | string | `systems/fallout/assets/icons/items/apparel.svg` |  |  |  |
| `items[39].name` | string | `Casual Hat` |  |  |  |
| `items[39].ownership.default` | number | `0` | 0 | 0 | Often 0 |
| `items[39].sort` | number | `0` | 0 | 0 | Often 0 |
| `items[39].system.apparelType` | string | `headgear` |  |  |  |
| `items[39].system.canBeScrapped` | boolean | `True` |  |  |  |
| `items[39].system.cost` | number | `15` | 15 | 15 |  |
| `items[39].system.description` | string | `<p><span class="fontstyle0">A simple, lightweight ...` |  |  |  |
| `items[39].system.equippable` | boolean | `True` |  |  |  |
| `items[39].system.equipped` | boolean | `False` |  |  |  |
| `items[39].system.favorite` | boolean | `False` |  |  |  |
| `items[39].system.health.max` | number | `0` | 0 | 0 | Often 0 |
| `items[39].system.health.min` | number | `0` | 0 | 0 | Often 0 |
| `items[39].system.health.mod` | number | `0` | 0 | 0 | Often 0 |
| `items[39].system.health.value` | number | `0` | 0 | 0 | Often 0 |
| `items[39].system.isJunk` | boolean | `False` |  |  |  |
| `items[39].system.location.armL` | boolean | `False` |  |  |  |
| `items[39].system.location.armR` | boolean | `False` |  |  |  |
| `items[39].system.location.head` | boolean | `True` |  |  |  |
| `items[39].system.location.legL` | boolean | `False` |  |  |  |
| `items[39].system.location.legR` | boolean | `False` |  |  |  |
| `items[39].system.location.torso` | boolean | `False` |  |  |  |
| `items[39].system.mods.8JID23VwOdXqwESb._id` | string | `8JID23VwOdXqwESb` |  |  |  |
| `items[39].system.mods.8JID23VwOdXqwESb._stats.compendiumSource` | null |  |  |  |  |
| `items[39].system.mods.8JID23VwOdXqwESb._stats.coreVersion` | string | `12.331` |  |  |  |
| `items[39].system.mods.8JID23VwOdXqwESb._stats.createdTime` | null |  |  |  |  |
| `items[39].system.mods.8JID23VwOdXqwESb._stats.duplicateSource` | null |  |  |  |  |
| `items[39].system.mods.8JID23VwOdXqwESb._stats.lastModifiedBy` | null |  |  |  |  |
| `items[39].system.mods.8JID23VwOdXqwESb._stats.modifiedTime` | null |  |  |  |  |
| `items[39].system.mods.8JID23VwOdXqwESb._stats.systemId` | null |  |  |  |  |
| `items[39].system.mods.8JID23VwOdXqwESb._stats.systemVersion` | null |  |  |  |  |
| `items[39].system.mods.8JID23VwOdXqwESb.effects` | array | `[]` |  |  | Empty array |
| `items[39].system.mods.8JID23VwOdXqwESb.folder` | string | `zV91jOW1G58krnbG` |  |  |  |
| `items[39].system.mods.8JID23VwOdXqwESb.img` | string | `systems/fallout/assets/icons/items/apparel_mod.svg` |  |  |  |
| `items[39].system.mods.8JID23VwOdXqwESb.name` | string | `Ballistic Weave Mk II` |  |  |  |
| `items[39].system.mods.8JID23VwOdXqwESb.ownership.default` | number | `0` | 0 | 0 | Often 0 |
| `items[39].system.mods.8JID23VwOdXqwESb.sort` | number | `0` | 0 | 0 | Often 0 |
| `items[39].system.mods.8JID23VwOdXqwESb.system.apparelType` | string | `clothing` |  |  |  |
| `items[39].system.mods.8JID23VwOdXqwESb.system.attachable` | boolean | `True` |  |  |  |
| `items[39].system.mods.8JID23VwOdXqwESb.system.attached` | boolean | `False` |  |  |  |
| `items[39].system.mods.8JID23VwOdXqwESb.system.canBeScrapped` | boolean | `True` |  |  |  |
| `items[39].system.mods.8JID23VwOdXqwESb.system.cost` | number | `30` | 30 | 30 |  |
| `items[39].system.mods.8JID23VwOdXqwESb.system.description` | string | `<p><span class="fontstyle0">Ballistic polymer weav...` |  |  |  |
| `items[39].system.mods.8JID23VwOdXqwESb.system.effect` | string | `` |  |  |  |
| `items[39].system.mods.8JID23VwOdXqwESb.system.favorite` | boolean | `False` |  |  |  |
| `items[39].system.mods.8JID23VwOdXqwESb.system.health.value` | number | `0` | 0 | 0 | Often 0 |
| `items[39].system.mods.8JID23VwOdXqwESb.system.isJunk` | boolean | `False` |  |  |  |
| `items[39].system.mods.8JID23VwOdXqwESb.system.location` | string | `` |  |  |  |
| `items[39].system.mods.8JID23VwOdXqwESb.system.modType` | string | `lining` |  |  |  |
| `items[39].system.mods.8JID23VwOdXqwESb.system.perks` | string | `Armorer 1` |  |  |  |
| `items[39].system.mods.8JID23VwOdXqwESb.system.quantity` | number | `1` | 1 | 1 |  |
| `items[39].system.mods.8JID23VwOdXqwESb.system.rarity` | string | `common` |  |  |  |
| `items[39].system.mods.8JID23VwOdXqwESb.system.resistance.energy` | number | `3` | 3 | 3 |  |
| `items[39].system.mods.8JID23VwOdXqwESb.system.resistance.physical` | number | `3` | 3 | 3 |  |
| `items[39].system.mods.8JID23VwOdXqwESb.system.resistance.radiation` | number | `0` | 0 | 0 | Often 0 |
| `items[39].system.mods.8JID23VwOdXqwESb.system.shadowed` | boolean | `False` |  |  |  |
| `items[39].system.mods.8JID23VwOdXqwESb.system.source` | string | `core_rulebook` |  |  |  |
| `items[39].system.mods.8JID23VwOdXqwESb.system.stashed` | boolean | `False` |  |  |  |
| `items[39].system.mods.8JID23VwOdXqwESb.system.summary` | string | `` |  |  |  |
| `items[39].system.mods.8JID23VwOdXqwESb.system.weight` | number | `0` | 0 | 0 | Often 0 |
| `items[39].system.mods.8JID23VwOdXqwESb.type` | string | `apparel_mod` |  |  |  |
| `items[39].system.mods.R0OekXuLrtHf0j8f._id` | string | `R0OekXuLrtHf0j8f` |  |  |  |
| `items[39].system.mods.R0OekXuLrtHf0j8f._stats.compendiumSource` | null |  |  |  |  |
| `items[39].system.mods.R0OekXuLrtHf0j8f._stats.coreVersion` | string | `12.331` |  |  |  |
| `items[39].system.mods.R0OekXuLrtHf0j8f._stats.createdTime` | null |  |  |  |  |
| `items[39].system.mods.R0OekXuLrtHf0j8f._stats.duplicateSource` | null |  |  |  |  |
| `items[39].system.mods.R0OekXuLrtHf0j8f._stats.lastModifiedBy` | null |  |  |  |  |
| `items[39].system.mods.R0OekXuLrtHf0j8f._stats.modifiedTime` | null |  |  |  |  |
| `items[39].system.mods.R0OekXuLrtHf0j8f._stats.systemId` | null |  |  |  |  |
| `items[39].system.mods.R0OekXuLrtHf0j8f._stats.systemVersion` | null |  |  |  |  |
| `items[39].system.mods.R0OekXuLrtHf0j8f.effects` | array | `[]` |  |  | Empty array |
| `items[39].system.mods.R0OekXuLrtHf0j8f.folder` | string | `zV91jOW1G58krnbG` |  |  |  |
| `items[39].system.mods.R0OekXuLrtHf0j8f.img` | string | `systems/fallout/assets/icons/items/apparel_mod.svg` |  |  |  |
| `items[39].system.mods.R0OekXuLrtHf0j8f.name` | string | `Ballistic Weave` |  |  |  |
| `items[39].system.mods.R0OekXuLrtHf0j8f.ownership.default` | number | `0` | 0 | 0 | Often 0 |
| `items[39].system.mods.R0OekXuLrtHf0j8f.sort` | number | `0` | 0 | 0 | Often 0 |
| `items[39].system.mods.R0OekXuLrtHf0j8f.system.apparelType` | string | `clothing` |  |  |  |
| `items[39].system.mods.R0OekXuLrtHf0j8f.system.attachable` | boolean | `True` |  |  |  |
| `items[39].system.mods.R0OekXuLrtHf0j8f.system.attached` | boolean | `False` |  |  |  |
| `items[39].system.mods.R0OekXuLrtHf0j8f.system.canBeScrapped` | boolean | `True` |  |  |  |
| `items[39].system.mods.R0OekXuLrtHf0j8f.system.cost` | number | `20` | 20 | 20 |  |
| `items[39].system.mods.R0OekXuLrtHf0j8f.system.description` | string | `<p><span class="fontstyle0">Ballistic polymer weav...` |  |  |  |
| `items[39].system.mods.R0OekXuLrtHf0j8f.system.effect` | string | `` |  |  |  |
| `items[39].system.mods.R0OekXuLrtHf0j8f.system.favorite` | boolean | `False` |  |  |  |
| `items[39].system.mods.R0OekXuLrtHf0j8f.system.health.value` | number | `0` | 0 | 0 | Often 0 |
| `items[39].system.mods.R0OekXuLrtHf0j8f.system.isJunk` | boolean | `False` |  |  |  |
| `items[39].system.mods.R0OekXuLrtHf0j8f.system.location` | string | `` |  |  |  |
| `items[39].system.mods.R0OekXuLrtHf0j8f.system.modType` | string | `lining` |  |  |  |
| `items[39].system.mods.R0OekXuLrtHf0j8f.system.perks` | string | `` |  |  |  |
| `items[39].system.mods.R0OekXuLrtHf0j8f.system.quantity` | number | `1` | 1 | 1 |  |
| `items[39].system.mods.R0OekXuLrtHf0j8f.system.rarity` | string | `common` |  |  |  |
| `items[39].system.mods.R0OekXuLrtHf0j8f.system.resistance.energy` | number | `2` | 2 | 2 |  |
| `items[39].system.mods.R0OekXuLrtHf0j8f.system.resistance.physical` | number | `2` | 2 | 2 |  |
| `items[39].system.mods.R0OekXuLrtHf0j8f.system.resistance.radiation` | number | `0` | 0 | 0 | Often 0 |
| `items[39].system.mods.R0OekXuLrtHf0j8f.system.shadowed` | boolean | `False` |  |  |  |
| `items[39].system.mods.R0OekXuLrtHf0j8f.system.source` | string | `core_rulebook` |  |  |  |
| `items[39].system.mods.R0OekXuLrtHf0j8f.system.stashed` | boolean | `False` |  |  |  |
| `items[39].system.mods.R0OekXuLrtHf0j8f.system.summary` | string | `` |  |  |  |
| `items[39].system.mods.R0OekXuLrtHf0j8f.system.weight` | number | `0` | 0 | 0 | Often 0 |
| `items[39].system.mods.R0OekXuLrtHf0j8f.type` | string | `apparel_mod` |  |  |  |
| `items[39].system.mods.current` | number | `0` | 0 | 0 | Often 0 |
| `items[39].system.mods.ew9m8xT2GbnWCHeu._id` | string | `ew9m8xT2GbnWCHeu` |  |  |  |
| `items[39].system.mods.ew9m8xT2GbnWCHeu._stats.compendiumSource` | null |  |  |  |  |
| `items[39].system.mods.ew9m8xT2GbnWCHeu._stats.coreVersion` | string | `12.331` |  |  |  |
| `items[39].system.mods.ew9m8xT2GbnWCHeu._stats.createdTime` | null |  |  |  |  |
| `items[39].system.mods.ew9m8xT2GbnWCHeu._stats.duplicateSource` | null |  |  |  |  |
| `items[39].system.mods.ew9m8xT2GbnWCHeu._stats.lastModifiedBy` | null |  |  |  |  |
| `items[39].system.mods.ew9m8xT2GbnWCHeu._stats.modifiedTime` | null |  |  |  |  |
| `items[39].system.mods.ew9m8xT2GbnWCHeu._stats.systemId` | null |  |  |  |  |
| `items[39].system.mods.ew9m8xT2GbnWCHeu._stats.systemVersion` | null |  |  |  |  |
| `items[39].system.mods.ew9m8xT2GbnWCHeu.effects` | array | `[]` |  |  | Empty array |
| `items[39].system.mods.ew9m8xT2GbnWCHeu.folder` | string | `zV91jOW1G58krnbG` |  |  |  |
| `items[39].system.mods.ew9m8xT2GbnWCHeu.img` | string | `systems/fallout/assets/icons/items/apparel_mod.svg` |  |  |  |
| `items[39].system.mods.ew9m8xT2GbnWCHeu.name` | string | `Ballistic Weave Mk V` |  |  |  |
| `items[39].system.mods.ew9m8xT2GbnWCHeu.ownership.default` | number | `0` | 0 | 0 | Often 0 |
| `items[39].system.mods.ew9m8xT2GbnWCHeu.sort` | number | `0` | 0 | 0 | Often 0 |
| `items[39].system.mods.ew9m8xT2GbnWCHeu.system.apparelType` | string | `clothing` |  |  |  |
| `items[39].system.mods.ew9m8xT2GbnWCHeu.system.attachable` | boolean | `True` |  |  |  |
| `items[39].system.mods.ew9m8xT2GbnWCHeu.system.attached` | boolean | `False` |  |  |  |
| `items[39].system.mods.ew9m8xT2GbnWCHeu.system.canBeScrapped` | boolean | `True` |  |  |  |
| `items[39].system.mods.ew9m8xT2GbnWCHeu.system.cost` | number | `60` | 60 | 60 |  |
| `items[39].system.mods.ew9m8xT2GbnWCHeu.system.description` | string | `<p><span class="fontstyle0">Ballistic polymer weav...` |  |  |  |
| `items[39].system.mods.ew9m8xT2GbnWCHeu.system.effect` | string | `` |  |  |  |
| `items[39].system.mods.ew9m8xT2GbnWCHeu.system.favorite` | boolean | `False` |  |  |  |
| `items[39].system.mods.ew9m8xT2GbnWCHeu.system.health.value` | number | `0` | 0 | 0 | Often 0 |
| `items[39].system.mods.ew9m8xT2GbnWCHeu.system.isJunk` | boolean | `False` |  |  |  |
| `items[39].system.mods.ew9m8xT2GbnWCHeu.system.location` | string | `` |  |  |  |
| `items[39].system.mods.ew9m8xT2GbnWCHeu.system.modType` | string | `lining` |  |  |  |
| `items[39].system.mods.ew9m8xT2GbnWCHeu.system.perks` | string | `Armorer 4` |  |  |  |
| `items[39].system.mods.ew9m8xT2GbnWCHeu.system.quantity` | number | `1` | 1 | 1 |  |
| `items[39].system.mods.ew9m8xT2GbnWCHeu.system.rarity` | string | `common` |  |  |  |
| `items[39].system.mods.ew9m8xT2GbnWCHeu.system.resistance.energy` | number | `6` | 6 | 6 |  |
| `items[39].system.mods.ew9m8xT2GbnWCHeu.system.resistance.physical` | number | `6` | 6 | 6 |  |
| `items[39].system.mods.ew9m8xT2GbnWCHeu.system.resistance.radiation` | number | `0` | 0 | 0 | Often 0 |
| `items[39].system.mods.ew9m8xT2GbnWCHeu.system.shadowed` | boolean | `False` |  |  |  |
| `items[39].system.mods.ew9m8xT2GbnWCHeu.system.source` | string | `core_rulebook` |  |  |  |
| `items[39].system.mods.ew9m8xT2GbnWCHeu.system.stashed` | boolean | `False` |  |  |  |
| `items[39].system.mods.ew9m8xT2GbnWCHeu.system.summary` | string | `` |  |  |  |
| `items[39].system.mods.ew9m8xT2GbnWCHeu.system.weight` | number | `0` | 0 | 0 | Often 0 |
| `items[39].system.mods.ew9m8xT2GbnWCHeu.type` | string | `apparel_mod` |  |  |  |
| `items[39].system.mods.fGvLq6Ku80a5cTSg._id` | string | `fGvLq6Ku80a5cTSg` |  |  |  |
| `items[39].system.mods.fGvLq6Ku80a5cTSg._stats.compendiumSource` | null |  |  |  |  |
| `items[39].system.mods.fGvLq6Ku80a5cTSg._stats.coreVersion` | string | `12.331` |  |  |  |
| `items[39].system.mods.fGvLq6Ku80a5cTSg._stats.createdTime` | null |  |  |  |  |
| `items[39].system.mods.fGvLq6Ku80a5cTSg._stats.duplicateSource` | null |  |  |  |  |
| `items[39].system.mods.fGvLq6Ku80a5cTSg._stats.lastModifiedBy` | null |  |  |  |  |
| `items[39].system.mods.fGvLq6Ku80a5cTSg._stats.modifiedTime` | null |  |  |  |  |
| `items[39].system.mods.fGvLq6Ku80a5cTSg._stats.systemId` | null |  |  |  |  |
| `items[39].system.mods.fGvLq6Ku80a5cTSg._stats.systemVersion` | null |  |  |  |  |
| `items[39].system.mods.fGvLq6Ku80a5cTSg.effects` | array | `[]` |  |  | Empty array |
| `items[39].system.mods.fGvLq6Ku80a5cTSg.folder` | string | `zV91jOW1G58krnbG` |  |  |  |
| `items[39].system.mods.fGvLq6Ku80a5cTSg.img` | string | `systems/fallout/assets/icons/items/apparel_mod.svg` |  |  |  |
| `items[39].system.mods.fGvLq6Ku80a5cTSg.name` | string | `Ballistic Weave Mk IV` |  |  |  |
| `items[39].system.mods.fGvLq6Ku80a5cTSg.ownership.default` | number | `0` | 0 | 0 | Often 0 |
| `items[39].system.mods.fGvLq6Ku80a5cTSg.sort` | number | `0` | 0 | 0 | Often 0 |
| `items[39].system.mods.fGvLq6Ku80a5cTSg.system.apparelType` | string | `clothing` |  |  |  |
| `items[39].system.mods.fGvLq6Ku80a5cTSg.system.attachable` | boolean | `True` |  |  |  |
| `items[39].system.mods.fGvLq6Ku80a5cTSg.system.attached` | boolean | `False` |  |  |  |
| `items[39].system.mods.fGvLq6Ku80a5cTSg.system.canBeScrapped` | boolean | `True` |  |  |  |
| `items[39].system.mods.fGvLq6Ku80a5cTSg.system.cost` | number | `50` | 50 | 50 |  |
| `items[39].system.mods.fGvLq6Ku80a5cTSg.system.description` | string | `<p><span class="fontstyle0">Ballistic polymer weav...` |  |  |  |
| `items[39].system.mods.fGvLq6Ku80a5cTSg.system.effect` | string | `` |  |  |  |
| `items[39].system.mods.fGvLq6Ku80a5cTSg.system.favorite` | boolean | `False` |  |  |  |
| `items[39].system.mods.fGvLq6Ku80a5cTSg.system.health.value` | number | `0` | 0 | 0 | Often 0 |
| `items[39].system.mods.fGvLq6Ku80a5cTSg.system.isJunk` | boolean | `False` |  |  |  |
| `items[39].system.mods.fGvLq6Ku80a5cTSg.system.location` | string | `` |  |  |  |
| `items[39].system.mods.fGvLq6Ku80a5cTSg.system.modType` | string | `lining` |  |  |  |
| `items[39].system.mods.fGvLq6Ku80a5cTSg.system.perks` | string | `Armorer 3` |  |  |  |
| `items[39].system.mods.fGvLq6Ku80a5cTSg.system.quantity` | number | `1` | 1 | 1 |  |
| `items[39].system.mods.fGvLq6Ku80a5cTSg.system.rarity` | string | `common` |  |  |  |
| `items[39].system.mods.fGvLq6Ku80a5cTSg.system.resistance.energy` | number | `5` | 5 | 5 |  |
| `items[39].system.mods.fGvLq6Ku80a5cTSg.system.resistance.physical` | number | `5` | 5 | 5 |  |
| `items[39].system.mods.fGvLq6Ku80a5cTSg.system.resistance.radiation` | number | `0` | 0 | 0 | Often 0 |
| `items[39].system.mods.fGvLq6Ku80a5cTSg.system.shadowed` | boolean | `False` |  |  |  |
| `items[39].system.mods.fGvLq6Ku80a5cTSg.system.source` | string | `core_rulebook` |  |  |  |
| `items[39].system.mods.fGvLq6Ku80a5cTSg.system.stashed` | boolean | `False` |  |  |  |
| `items[39].system.mods.fGvLq6Ku80a5cTSg.system.summary` | string | `` |  |  |  |
| `items[39].system.mods.fGvLq6Ku80a5cTSg.system.weight` | number | `0` | 0 | 0 | Often 0 |
| `items[39].system.mods.fGvLq6Ku80a5cTSg.type` | string | `apparel_mod` |  |  |  |
| `items[39].system.mods.installedMods` | string | `` |  |  |  |
| `items[39].system.mods.kRuMVjqK0tr5aZDY._id` | string | `kRuMVjqK0tr5aZDY` |  |  |  |
| `items[39].system.mods.kRuMVjqK0tr5aZDY._stats.compendiumSource` | null |  |  |  |  |
| `items[39].system.mods.kRuMVjqK0tr5aZDY._stats.coreVersion` | string | `12.331` |  |  |  |
| `items[39].system.mods.kRuMVjqK0tr5aZDY._stats.createdTime` | null |  |  |  |  |
| `items[39].system.mods.kRuMVjqK0tr5aZDY._stats.duplicateSource` | null |  |  |  |  |
| `items[39].system.mods.kRuMVjqK0tr5aZDY._stats.lastModifiedBy` | null |  |  |  |  |
| `items[39].system.mods.kRuMVjqK0tr5aZDY._stats.modifiedTime` | null |  |  |  |  |
| `items[39].system.mods.kRuMVjqK0tr5aZDY._stats.systemId` | null |  |  |  |  |
| `items[39].system.mods.kRuMVjqK0tr5aZDY._stats.systemVersion` | null |  |  |  |  |
| `items[39].system.mods.kRuMVjqK0tr5aZDY.effects` | array | `[]` |  |  | Empty array |
| `items[39].system.mods.kRuMVjqK0tr5aZDY.folder` | string | `zV91jOW1G58krnbG` |  |  |  |
| `items[39].system.mods.kRuMVjqK0tr5aZDY.img` | string | `systems/fallout/assets/icons/items/apparel_mod.svg` |  |  |  |
| `items[39].system.mods.kRuMVjqK0tr5aZDY.name` | string | `Ballistic Weave Mk III` |  |  |  |
| `items[39].system.mods.kRuMVjqK0tr5aZDY.ownership.default` | number | `0` | 0 | 0 | Often 0 |
| `items[39].system.mods.kRuMVjqK0tr5aZDY.sort` | number | `0` | 0 | 0 | Often 0 |
| `items[39].system.mods.kRuMVjqK0tr5aZDY.system.apparelType` | string | `clothing` |  |  |  |
| `items[39].system.mods.kRuMVjqK0tr5aZDY.system.attachable` | boolean | `True` |  |  |  |
| `items[39].system.mods.kRuMVjqK0tr5aZDY.system.attached` | boolean | `False` |  |  |  |
| `items[39].system.mods.kRuMVjqK0tr5aZDY.system.canBeScrapped` | boolean | `True` |  |  |  |
| `items[39].system.mods.kRuMVjqK0tr5aZDY.system.cost` | number | `40` | 40 | 40 |  |
| `items[39].system.mods.kRuMVjqK0tr5aZDY.system.description` | string | `<p><span class="fontstyle0">Ballistic polymer weav...` |  |  |  |
| `items[39].system.mods.kRuMVjqK0tr5aZDY.system.effect` | string | `` |  |  |  |
| `items[39].system.mods.kRuMVjqK0tr5aZDY.system.favorite` | boolean | `False` |  |  |  |
| `items[39].system.mods.kRuMVjqK0tr5aZDY.system.health.value` | number | `0` | 0 | 0 | Often 0 |
| `items[39].system.mods.kRuMVjqK0tr5aZDY.system.isJunk` | boolean | `False` |  |  |  |
| `items[39].system.mods.kRuMVjqK0tr5aZDY.system.location` | string | `` |  |  |  |
| `items[39].system.mods.kRuMVjqK0tr5aZDY.system.modType` | string | `lining` |  |  |  |
| `items[39].system.mods.kRuMVjqK0tr5aZDY.system.perks` | string | `Armorer 2` |  |  |  |
| `items[39].system.mods.kRuMVjqK0tr5aZDY.system.quantity` | number | `1` | 1 | 1 |  |
| `items[39].system.mods.kRuMVjqK0tr5aZDY.system.rarity` | string | `common` |  |  |  |
| `items[39].system.mods.kRuMVjqK0tr5aZDY.system.resistance.energy` | number | `4` | 4 | 4 |  |
| `items[39].system.mods.kRuMVjqK0tr5aZDY.system.resistance.physical` | number | `4` | 4 | 4 |  |
| `items[39].system.mods.kRuMVjqK0tr5aZDY.system.resistance.radiation` | number | `0` | 0 | 0 | Often 0 |
| `items[39].system.mods.kRuMVjqK0tr5aZDY.system.shadowed` | boolean | `False` |  |  |  |
| `items[39].system.mods.kRuMVjqK0tr5aZDY.system.source` | string | `core_rulebook` |  |  |  |
| `items[39].system.mods.kRuMVjqK0tr5aZDY.system.stashed` | boolean | `False` |  |  |  |
| `items[39].system.mods.kRuMVjqK0tr5aZDY.system.summary` | string | `` |  |  |  |
| `items[39].system.mods.kRuMVjqK0tr5aZDY.system.weight` | number | `0` | 0 | 0 | Often 0 |
| `items[39].system.mods.kRuMVjqK0tr5aZDY.type` | string | `apparel_mod` |  |  |  |
| `items[39].system.mods.list` | string | `` |  |  |  |
| `items[39].system.mods.max` | number | `0` | 0 | 0 | Often 0 |
| `items[39].system.mods.modded` | boolean | `False` |  |  |  |
| `items[39].system.powerArmor.frameId` | string | `` |  |  |  |
| `items[39].system.powerArmor.isFrame` | boolean | `False` |  |  |  |
| `items[39].system.powerArmor.powered` | boolean | `False` |  |  |  |
| `items[39].system.quantity` | number | `1` | 1 | 1 |  |
| `items[39].system.rarity` | number | `1` | 1 | 1 |  |
| `items[39].system.resistance.energy` | number | `0` | 0 | 0 | Often 0 |
| `items[39].system.resistance.physical` | number | `0` | 0 | 0 | Often 0 |
| `items[39].system.resistance.radiation` | number | `0` | 0 | 0 | Often 0 |
| `items[39].system.shadowed` | boolean | `False` |  |  |  |
| `items[39].system.source` | string | `core_rulebook` |  |  |  |
| `items[39].system.stashed` | boolean | `False` |  |  |  |
| `items[39].system.weight` | number | `0` | 0 | 0 | Often 0 |
| `items[39].type` | string | `apparel` |  |  |  |

## Items - Consumables

| JSON Path | Type | Examples | Min | Max | Notes |
|-----------|------|----------|-----|-----|-------|
| `items[25]._id` | string | `pnZdMHnpq06qBy0n` |  |  |  |
| `items[25]._stats.compendiumSource` | string | `Compendium.fallout.consumables.Item.860ofdvpufUzSq...` |  |  |  |
| `items[25]._stats.coreVersion` | string | `13.344` |  |  |  |
| `items[25]._stats.createdTime` | number | `1739550893982` | 1739550893982 | 1739550893982 |  |
| `items[25]._stats.duplicateSource` | null |  |  |  |  |
| `items[25]._stats.exportSource` | null |  |  |  |  |
| `items[25]._stats.lastModifiedBy` | string | `qqb2lyM0FgEMachb` |  |  |  |
| `items[25]._stats.modifiedTime` | number | `1739551096484` | 1739551096484 | 1739551096484 |  |
| `items[25]._stats.systemId` | string | `fallout` |  |  |  |
| `items[25]._stats.systemVersion` | string | `11.14.3` |  |  |  |
| `items[25].effects` | array | `[]` |  |  | Empty array |
| `items[25].folder` | string | `n3Q9X70ZsFFCTZqu` |  |  |  |
| `items[25].img` | string | `systems/fallout/assets/icons/items/consumable.svg` |  |  |  |
| `items[25].name` | string | `Stimpak` |  |  |  |
| `items[25].ownership.default` | number | `0` | 0 | 0 | Often 0 |
| `items[25].sort` | number | `0` | 0 | 0 | Often 0 |
| `items[25].system.addiction` | number | `0` | 0 | 0 | Often 0 |
| `items[25].system.addictive` | boolean | `False` |  |  |  |
| `items[25].system.alcoholic` | boolean | `True` |  |  |  |
| `items[25].system.butchery` | boolean | `False` |  |  |  |
| `items[25].system.consumableGroup` | string | `` |  |  |  |
| `items[25].system.consumableType` | string | `chem` |  |  |  |
| `items[25].system.cost` | number | `50` | 50 | 50 |  |
| `items[25].system.description` | string | `<p>A stimulation delivery package, or Stimpak, is ...` |  |  |  |
| `items[25].system.duration` | string | `instant` |  |  |  |
| `items[25].system.effect` | string | `<p>Heals 4 HP (see description)</p>` |  |  |  |
| `items[25].system.equipped` | boolean | `False` |  |  |  |
| `items[25].system.favorite` | boolean | `False` |  |  |  |
| `items[25].system.group` | string | `` |  |  |  |
| `items[25].system.hp` | number | `4` | 4 | 4 |  |
| `items[25].system.irradiated` | boolean | `True` |  |  |  |
| `items[25].system.prepared` | boolean | `False` |  |  |  |
| `items[25].system.providesCap` | boolean | `False` |  |  |  |
| `items[25].system.quantity` | number | `3` | 3 | 3 |  |
| `items[25].system.radiation` | number | `0` | 0 | 0 | Often 0 |
| `items[25].system.radiationDamage` | number | `1` | 1 | 1 |  |
| `items[25].system.rarity` | number | `2` | 2 | 2 |  |
| `items[25].system.source` | string | `core_rulebook` |  |  |  |
| `items[25].system.stashed` | boolean | `True` |  |  |  |
| `items[25].system.thirstReduction` | number | `0` | 0 | 0 | Often 0 |
| `items[25].system.weight` | number | `0.1` | 0.1 | 0.1 |  |
| `items[25].type` | string | `consumable` |  |  |  |
| `items[26]._id` | string | `Sg3BOl3jrBYMjGZW` |  |  |  |
| `items[26]._stats.compendiumSource` | string | `Compendium.fallout.consumables.Item.xuXzlEC3V0co3w...` |  |  |  |
| `items[26]._stats.coreVersion` | string | `13.344` |  |  |  |
| `items[26]._stats.createdTime` | number | `1739551070780` | 1739551070780 | 1739551070780 |  |
| `items[26]._stats.duplicateSource` | null |  |  |  |  |
| `items[26]._stats.exportSource` | null |  |  |  |  |
| `items[26]._stats.lastModifiedBy` | string | `qqb2lyM0FgEMachb` |  |  |  |
| `items[26]._stats.modifiedTime` | number | `1739551092993` | 1739551092993 | 1739551092993 |  |
| `items[26]._stats.systemId` | string | `fallout` |  |  |  |
| `items[26]._stats.systemVersion` | string | `11.14.3` |  |  |  |
| `items[26].effects` | array | `[]` |  |  | Empty array |
| `items[26].folder` | string | `ajMustngwNZwFiQS` |  |  |  |
| `items[26].img` | string | `systems/fallout/assets/icons/items/consumable.svg` |  |  |  |
| `items[26].name` | string | `Purified Water` |  |  |  |
| `items[26].ownership.default` | number | `0` | 0 | 0 | Often 0 |
| `items[26].sort` | number | `0` | 0 | 0 | Often 0 |
| `items[26].system.addiction` | number | `0` | 0 | 0 | Often 0 |
| `items[26].system.addictive` | boolean | `False` |  |  |  |
| `items[26].system.alcoholic` | boolean | `False` |  |  |  |
| `items[26].system.butchery` | boolean | `False` |  |  |  |
| `items[26].system.consumableGroup` | string | `` |  |  |  |
| `items[26].system.consumableType` | string | `beverage` |  |  |  |
| `items[26].system.cost` | number | `20` | 20 | 20 |  |
| `items[26].system.description` | string | `<p><span class="fontstyle0">Water which has been c...` |  |  |  |
| `items[26].system.duration` | string | `` |  |  |  |
| `items[26].system.effect` | string | `` |  |  |  |
| `items[26].system.equipped` | boolean | `False` |  |  |  |
| `items[26].system.favorite` | boolean | `False` |  |  |  |
| `items[26].system.group` | string | `` |  |  |  |
| `items[26].system.hp` | number | `3` | 3 | 3 |  |
| `items[26].system.irradiated` | boolean | `False` |  |  |  |
| `items[26].system.prepared` | boolean | `False` |  |  |  |
| `items[26].system.providesCap` | boolean | `False` |  |  |  |
| `items[26].system.quantity` | number | `1` | 1 | 1 |  |
| `items[26].system.radiation` | number | `0` | 0 | 0 | Often 0 |
| `items[26].system.radiationDamage` | number | `1` | 1 | 1 |  |
| `items[26].system.rarity` | number | `1` | 1 | 1 |  |
| `items[26].system.source` | string | `core_rulebook` |  |  |  |
| `items[26].system.stashed` | boolean | `True` |  |  |  |
| `items[26].system.thirstReduction` | number | `2` | 2 | 2 |  |
| `items[26].system.weight` | number | `0.5` | 0.5 | 0.5 |  |
| `items[26].type` | string | `consumable` |  |  |  |
| `items[32]._id` | string | `wJXCSEkhDeqOoesb` |  |  |  |
| `items[32]._stats.compendiumSource` | string | `Compendium.fallout.consumables.Item.hc8DSkMGN2Gxug...` |  |  |  |
| `items[32]._stats.coreVersion` | string | `13.344` |  |  |  |
| `items[32]._stats.createdTime` | number | `1739552582257` | 1739552582257 | 1739552582257 |  |
| `items[32]._stats.duplicateSource` | null |  |  |  |  |
| `items[32]._stats.exportSource` | null |  |  |  |  |
| `items[32]._stats.lastModifiedBy` | string | `qqb2lyM0FgEMachb` |  |  |  |
| `items[32]._stats.modifiedTime` | number | `1739552590414` | 1739552590414 | 1739552590414 |  |
| `items[32]._stats.systemId` | string | `fallout` |  |  |  |
| `items[32]._stats.systemVersion` | string | `11.14.3` |  |  |  |
| `items[32].effects` | array | `[]` |  |  | Empty array |
| `items[32].folder` | string | `n3Q9X70ZsFFCTZqu` |  |  |  |
| `items[32].img` | string | `systems/fallout/assets/icons/items/consumable.svg` |  |  |  |
| `items[32].name` | string | `Mentats` |  |  |  |
| `items[32].ownership.default` | number | `0` | 0 | 0 | Often 0 |
| `items[32].sort` | number | `0` | 0 | 0 | Often 0 |
| `items[32].system.addiction` | number | `3` | 3 | 3 |  |
| `items[32].system.addictive` | boolean | `True` |  |  |  |
| `items[32].system.alcoholic` | boolean | `True` |  |  |  |
| `items[32].system.butchery` | boolean | `False` |  |  |  |
| `items[32].system.consumableGroup` | string | `Mentat` |  |  |  |
| `items[32].system.consumableType` | string | `chem` |  |  |  |
| `items[32].system.cost` | number | `50` | 50 | 50 |  |
| `items[32].system.description` | string | `<p>Mentats were a popular recreational and perform...` |  |  |  |
| `items[32].system.duration` | string | `lasting` |  |  |  |
| `items[32].system.effect` | string | `<p>Re-roll 1d20 on PER and INT tests</p>` |  |  |  |
| `items[32].system.equipped` | boolean | `False` |  |  |  |
| `items[32].system.favorite` | boolean | `False` |  |  |  |
| `items[32].system.group` | string | `` |  |  |  |
| `items[32].system.hp` | number | `0` | 0 | 0 | Often 0 |
| `items[32].system.irradiated` | boolean | `True` |  |  |  |
| `items[32].system.prepared` | boolean | `False` |  |  |  |
| `items[32].system.providesCap` | boolean | `False` |  |  |  |
| `items[32].system.quantity` | number | `1` | 1 | 1 |  |
| `items[32].system.radiation` | number | `0` | 0 | 0 | Often 0 |
| `items[32].system.radiationDamage` | number | `1` | 1 | 1 |  |
| `items[32].system.rarity` | number | `2` | 2 | 2 |  |
| `items[32].system.source` | string | `core_rulebook` |  |  |  |
| `items[32].system.stashed` | boolean | `True` |  |  |  |
| `items[32].system.thirstReduction` | number | `0` | 0 | 0 | Often 0 |
| `items[32].system.weight` | number | `0.1` | 0.1 | 0.1 |  |
| `items[32].type` | string | `consumable` |  |  |  |
| `items[41]._id` | string | `LoJTYB2Qhqa36g2U` |  |  |  |
| `items[41]._stats.compendiumSource` | string | `Compendium.fallout.consumables.Item.vDzTAi2iRrZ5XT...` |  |  |  |
| `items[41]._stats.coreVersion` | string | `13.350` |  |  |  |
| `items[41]._stats.createdTime` | number | `1760030024280` | 1760030024280 | 1760030024280 |  |
| `items[41]._stats.duplicateSource` | null |  |  |  |  |
| `items[41]._stats.exportSource` | null |  |  |  |  |
| `items[41]._stats.lastModifiedBy` | string | `qqb2lyM0FgEMachb` |  |  |  |
| `items[41]._stats.modifiedTime` | number | `1760035486524` | 1760035486524 | 1760035486524 |  |
| `items[41]._stats.systemId` | string | `fallout` |  |  |  |
| `items[41]._stats.systemVersion` | string | `11.16.4` |  |  |  |
| `items[41].effects` | array | `[]` |  |  | Empty array |
| `items[41].folder` | string | `n3Q9X70ZsFFCTZqu` |  |  |  |
| `items[41].img` | string | `systems/fallout/assets/icons/items/consumable.svg` |  |  |  |
| `items[41].name` | string | `RadAway` |  |  |  |
| `items[41].ownership.default` | number | `0` | 0 | 0 | Often 0 |
| `items[41].sort` | number | `0` | 0 | 0 | Often 0 |
| `items[41].system.addiction` | number | `0` | 0 | 0 | Often 0 |
| `items[41].system.addictive` | boolean | `False` |  |  |  |
| `items[41].system.alcoholic` | boolean | `True` |  |  |  |
| `items[41].system.butchery` | boolean | `False` |  |  |  |
| `items[41].system.consumableGroup` | string | `` |  |  |  |
| `items[41].system.consumableType` | string | `chem` |  |  |  |
| `items[41].system.cost` | number | `80` | 80 | 80 |  |
| `items[41].system.description` | string | `<p>An intravenous drug which purges radiation from...` |  |  |  |
| `items[41].system.duration` | string | `instant` |  |  |  |
| `items[41].system.effect` | string | `<p>Heals 4 Radiation damage (see description)</p>` |  |  |  |
| `items[41].system.equipped` | boolean | `False` |  |  |  |
| `items[41].system.favorite` | boolean | `False` |  |  |  |
| `items[41].system.group` | string | `` |  |  |  |
| `items[41].system.hp` | number | `0` | 0 | 0 | Often 0 |
| `items[41].system.irradiated` | boolean | `True` |  |  |  |
| `items[41].system.prepared` | boolean | `False` |  |  |  |
| `items[41].system.providesCap` | boolean | `False` |  |  |  |
| `items[41].system.quantity` | number | `4` | 4 | 4 |  |
| `items[41].system.radiation` | number | `4` | 4 | 4 |  |
| `items[41].system.radiationDamage` | number | `1` | 1 | 1 |  |
| `items[41].system.rarity` | number | `2` | 2 | 2 |  |
| `items[41].system.source` | string | `core_rulebook` |  |  |  |
| `items[41].system.stashed` | boolean | `True` |  |  |  |
| `items[41].system.thirstReduction` | number | `0` | 0 | 0 | Often 0 |
| `items[41].system.weight` | number | `0.1` | 0.1 | 0.1 |  |
| `items[41].type` | string | `consumable` |  |  |  |

## Items - Books & Magazines

| JSON Path | Type | Examples | Min | Max | Notes |
|-----------|------|----------|-----|-----|-------|
| `items[43]._id` | string | `BAMJ5Xg35X9AudYx` |  |  |  |
| `items[43]._stats.compendiumSource` | null |  |  |  |  |
| `items[43]._stats.coreVersion` | string | `13.350` |  |  |  |
| `items[43]._stats.createdTime` | number | `1760030525567` | 1760030525567 | 1760030525567 |  |
| `items[43]._stats.duplicateSource` | null |  |  |  |  |
| `items[43]._stats.exportSource` | null |  |  |  |  |
| `items[43]._stats.lastModifiedBy` | string | `XPIM5aN65eH5LXee` |  |  |  |
| `items[43]._stats.modifiedTime` | number | `1760030577700` | 1760030577700 | 1760030577700 |  |
| `items[43]._stats.systemId` | string | `fallout` |  |  |  |
| `items[43]._stats.systemVersion` | string | `11.16.4` |  |  |  |
| `items[43].effects` | array | `[]` |  |  | Empty array |
| `items[43].folder` | null |  |  |  |  |
| `items[43].img` | string | `systems/fallout/assets/icons/items/books_and_magz....` |  |  |  |
| `items[43].name` | string | `Apotheker von Gestern Band I` |  |  |  |
| `items[43].ownership.default` | number | `0` | 0 | 0 | Often 0 |
| `items[43].sort` | number | `0` | 0 | 0 | Often 0 |
| `items[43].system.cost` | number | `0` | 0 | 0 | Often 0 |
| `items[43].system.description` | string | `` |  |  |  |
| `items[43].system.effect` | string | `` |  |  |  |
| `items[43].system.equipped` | boolean | `False` |  |  |  |
| `items[43].system.favorite` | boolean | `False` |  |  |  |
| `items[43].system.publication` | string | `` |  |  |  |
| `items[43].system.quantity` | number | `1` | 1 | 1 |  |
| `items[43].system.rarity` | number | `0` | 0 | 0 | Often 0 |
| `items[43].system.read` | boolean | `False` |  |  |  |
| `items[43].system.source` | string | `` |  |  |  |
| `items[43].system.stashed` | boolean | `True` |  |  |  |
| `items[43].system.uses.max` | number | `1` | 1 | 1 |  |
| `items[43].system.uses.value` | number | `0` | 0 | 0 | Often 0 |
| `items[43].system.weight` | number | `1` | 1 | 1 |  |
| `items[43].type` | string | `books_and_magz` |  |  |  |

## Items - Miscellany

| JSON Path | Type | Examples | Min | Max | Notes |
|-----------|------|----------|-----|-----|-------|
| `items[27]._id` | string | `8mD0NoCSglL8pj41` |  |  |  |
| `items[27]._stats.compendiumSource` | string | `Compendium.fallout.miscellany.Item.Fkgwa1FrCdfQPvh...` |  |  |  |
| `items[27]._stats.coreVersion` | string | `13.344` |  |  |  |
| `items[27]._stats.createdTime` | number | `1739551116299` | 1739551116299 | 1739551116299 |  |
| `items[27]._stats.duplicateSource` | null |  |  |  |  |
| `items[27]._stats.exportSource` | null |  |  |  |  |
| `items[27]._stats.lastModifiedBy` | string | `qqb2lyM0FgEMachb` |  |  |  |
| `items[27]._stats.modifiedTime` | number | `1739551125087` | 1739551125087 | 1739551125087 |  |
| `items[27]._stats.systemId` | string | `fallout` |  |  |  |
| `items[27]._stats.systemVersion` | string | `11.14.3` |  |  |  |
| `items[27].effects` | array | `[]` |  |  | Empty array |
| `items[27].folder` | null |  |  |  |  |
| `items[27].img` | string | `systems/fallout/assets/icons/items/miscellany.svg` |  |  |  |
| `items[27].name` | string | `Pip-Boy` |  |  |  |
| `items[27].ownership.default` | number | `0` | 0 | 0 | Often 0 |
| `items[27].sort` | number | `0` | 0 | 0 | Often 0 |
| `items[27].system.canBeScrapped` | boolean | `True` |  |  |  |
| `items[27].system.cost` | number | `0` | 0 | 0 | Often 0 |
| `items[27].system.description` | string | `<p>A Personal Information Processor manufactured b...` |  |  |  |
| `items[27].system.effect` | string | `<p>See description</p>` |  |  |  |
| `items[27].system.equipped` | boolean | `False` |  |  |  |
| `items[27].system.favorite` | boolean | `False` |  |  |  |
| `items[27].system.isJunk` | boolean | `False` |  |  |  |
| `items[27].system.quantity` | number | `1` | 1 | 1 |  |
| `items[27].system.rarity` | number | `0` | 0 | 0 | Often 0 |
| `items[27].system.source` | string | `core_rulebook` |  |  |  |
| `items[27].system.stashed` | boolean | `True` |  |  |  |
| `items[27].system.weight` | number | `0` | 0 | 0 | Often 0 |
| `items[27].type` | string | `miscellany` |  |  |  |
| `items[28]._id` | string | `L9aMXU55Ejn0lcDR` |  |  |  |
| `items[28]._stats.compendiumSource` | string | `Compendium.fallout.miscellany.Item.WyjtxDmxyBdGcD6...` |  |  |  |
| `items[28]._stats.coreVersion` | string | `13.344` |  |  |  |
| `items[28]._stats.createdTime` | number | `1739551171582` | 1739551171582 | 1739551171582 |  |
| `items[28]._stats.duplicateSource` | null |  |  |  |  |
| `items[28]._stats.exportSource` | null |  |  |  |  |
| `items[28]._stats.lastModifiedBy` | string | `qqb2lyM0FgEMachb` |  |  |  |
| `items[28]._stats.modifiedTime` | number | `1739551175382` | 1739551175382 | 1739551175382 |  |
| `items[28]._stats.systemId` | string | `fallout` |  |  |  |
| `items[28]._stats.systemVersion` | string | `11.14.3` |  |  |  |
| `items[28].effects` | array | `[]` |  |  | Empty array |
| `items[28].folder` | null |  |  |  |  |
| `items[28].img` | string | `systems/fallout/assets/icons/items/miscellany.svg` |  |  |  |
| `items[28].name` | string | `First Aid Kit` |  |  |  |
| `items[28].ownership.default` | number | `0` | 0 | 0 | Often 0 |
| `items[28].sort` | number | `0` | 0 | 0 | Often 0 |
| `items[28].system.canBeScrapped` | boolean | `True` |  |  |  |
| `items[28].system.cost` | number | `200` | 200 | 200 |  |
| `items[28].system.description` | string | `<p>A pack full of bandages, antiseptic spray, and ...` |  |  |  |
| `items[28].system.effect` | string | `<p>Heal +2 HP upon succeeding at the First Aid act...` |  |  |  |
| `items[28].system.equipped` | boolean | `False` |  |  |  |
| `items[28].system.favorite` | boolean | `False` |  |  |  |
| `items[28].system.isJunk` | boolean | `False` |  |  |  |
| `items[28].system.quantity` | number | `1` | 1 | 1 |  |
| `items[28].system.rarity` | number | `2` | 2 | 2 |  |
| `items[28].system.source` | string | `core_rulebook` |  |  |  |
| `items[28].system.stashed` | boolean | `True` |  |  |  |
| `items[28].system.weight` | number | `4` | 4 | 4 |  |
| `items[28].type` | string | `miscellany` |  |  |  |
| `items[29]._id` | string | `hnkLiEbfY1itiNqb` |  |  |  |
| `items[29]._stats.compendiumSource` | string | `Compendium.fallout.miscellany.Item.1wxcXIYvgK4GTYU...` |  |  |  |
| `items[29]._stats.coreVersion` | string | `13.344` |  |  |  |
| `items[29]._stats.createdTime` | number | `1739551204339` | 1739551204339 | 1739551204339 |  |
| `items[29]._stats.duplicateSource` | null |  |  |  |  |
| `items[29]._stats.exportSource` | null |  |  |  |  |
| `items[29]._stats.lastModifiedBy` | string | `qqb2lyM0FgEMachb` |  |  |  |
| `items[29]._stats.modifiedTime` | number | `1739551207479` | 1739551207479 | 1739551207479 |  |
| `items[29]._stats.systemId` | string | `fallout` |  |  |  |
| `items[29]._stats.systemVersion` | string | `11.14.3` |  |  |  |
| `items[29].effects` | array | `[]` |  |  | Empty array |
| `items[29].folder` | null |  |  |  |  |
| `items[29].img` | string | `systems/fallout/assets/icons/items/miscellany.svg` |  |  |  |
| `items[29].name` | string | `Multi-Tool` |  |  |  |
| `items[29].ownership.default` | number | `0` | 0 | 0 | Often 0 |
| `items[29].sort` | number | `0` | 0 | 0 | Often 0 |
| `items[29].system.canBeScrapped` | boolean | `True` |  |  |  |
| `items[29].system.cost` | number | `100` | 100 | 100 |  |
| `items[29].system.description` | string | `<p>A handy little device, containing a set of plie...` |  |  |  |
| `items[29].system.effect` | string | `<p>Reduce the difficulty of Repair tests by 1 (min...` |  |  |  |
| `items[29].system.equipped` | boolean | `False` |  |  |  |
| `items[29].system.favorite` | boolean | `False` |  |  |  |
| `items[29].system.isJunk` | boolean | `False` |  |  |  |
| `items[29].system.quantity` | number | `1` | 1 | 1 |  |
| `items[29].system.rarity` | number | `2` | 2 | 2 |  |
| `items[29].system.source` | string | `core_rulebook` |  |  |  |
| `items[29].system.stashed` | boolean | `True` |  |  |  |
| `items[29].system.weight` | number | `1` | 1 | 1 |  |
| `items[29].type` | string | `miscellany` |  |  |  |
| `items[35]._id` | string | `noKdidsZWGVBXrXA` |  |  |  |
| `items[35]._stats.compendiumSource` | string | `Compendium.fallout.miscellany.Item.tJzODq60DVEMlpF...` |  |  |  |
| `items[35]._stats.coreVersion` | string | `13.350` |  |  |  |
| `items[35]._stats.createdTime` | number | `1746730327425` | 1746730327425 | 1746730327425 |  |
| `items[35]._stats.duplicateSource` | null |  |  |  |  |
| `items[35]._stats.exportSource` | null |  |  |  |  |
| `items[35]._stats.lastModifiedBy` | string | `XPIM5aN65eH5LXee` |  |  |  |
| `items[35]._stats.modifiedTime` | number | `1760030503274` | 1760030503274 | 1760030503274 |  |
| `items[35]._stats.systemId` | string | `fallout` |  |  |  |
| `items[35]._stats.systemVersion` | string | `11.16.4` |  |  |  |
| `items[35].effects` | array | `[]` |  |  | Empty array |
| `items[35].folder` | null |  |  |  |  |
| `items[35].img` | string | `systems/fallout/assets/icons/items/miscellany.svg` |  |  |  |
| `items[35].name` | string | `Doctor's Bag` |  |  |  |
| `items[35].ownership.default` | number | `0` | 0 | 0 | Often 0 |
| `items[35].sort` | number | `0` | 0 | 0 | Often 0 |
| `items[35].system.canBeScrapped` | boolean | `True` |  |  |  |
| `items[35].system.cost` | number | `300` | 300 | 300 |  |
| `items[35].system.description` | string | `<p>A well-stocked bag of medical supplies and usef...` |  |  |  |
| `items[35].system.effect` | string | `<p>Reduce the difficulty of Medicine tests by 1 (m...` |  |  |  |
| `items[35].system.equipped` | boolean | `False` |  |  |  |
| `items[35].system.favorite` | boolean | `False` |  |  |  |
| `items[35].system.isJunk` | boolean | `False` |  |  |  |
| `items[35].system.quantity` | number | `1` | 1 | 1 |  |
| `items[35].system.rarity` | number | `3` | 3 | 3 |  |
| `items[35].system.source` | string | `core_rulebook` |  |  |  |
| `items[35].system.stashed` | boolean | `True` |  |  |  |
| `items[35].system.weight` | number | `10` | 10 | 10 |  |
| `items[35].type` | string | `miscellany` |  |  |  |
| `items[37]._id` | string | `XD7TZvbUkiymiH9Q` |  |  |  |
| `items[37]._stats.compendiumSource` | null |  |  |  |  |
| `items[37]._stats.coreVersion` | string | `13.350` |  |  |  |
| `items[37]._stats.createdTime` | number | `1747936566318` | 1747936566318 | 1747936566318 |  |
| `items[37]._stats.duplicateSource` | null |  |  |  |  |
| `items[37]._stats.exportSource` | null |  |  |  |  |
| `items[37]._stats.lastModifiedBy` | string | `XPIM5aN65eH5LXee` |  |  |  |
| `items[37]._stats.modifiedTime` | number | `1760030514309` | 1760030514309 | 1760030514309 |  |
| `items[37]._stats.systemId` | string | `fallout` |  |  |  |
| `items[37]._stats.systemVersion` | string | `11.16.4` |  |  |  |
| `items[37].effects` | array | `[]` |  |  | Empty array |
| `items[37].folder` | null |  |  |  |  |
| `items[37].img` | string | `systems/fallout/assets/icons/items/miscellany.svg` |  |  |  |
| `items[37].name` | string | `Wasseraufbereitungstabletten` |  |  |  |
| `items[37].ownership.default` | number | `0` | 0 | 0 | Often 0 |
| `items[37].sort` | number | `0` | 0 | 0 | Often 0 |
| `items[37].system.canBeScrapped` | boolean | `True` |  |  |  |
| `items[37].system.cost` | number | `0` | 0 | 0 | Often 0 |
| `items[37].system.description` | string | `` |  |  |  |
| `items[37].system.effect` | string | `<p>1 Tablette = 2 Liter aufbereitetes Wasser</p>` |  |  |  |
| `items[37].system.equipped` | boolean | `False` |  |  |  |
| `items[37].system.favorite` | boolean | `False` |  |  |  |
| `items[37].system.isJunk` | boolean | `False` |  |  |  |
| `items[37].system.quantity` | number | `12` | 12 | 12 |  |
| `items[37].system.rarity` | number | `0` | 0 | 0 | Often 0 |
| `items[37].system.source` | string | `` |  |  |  |
| `items[37].system.stashed` | boolean | `True` |  |  |  |
| `items[37].system.weight` | number | `0` | 0 | 0 | Often 0 |
| `items[37].type` | string | `miscellany` |  |  |  |
| `items[38]._id` | string | `evaXjNqKeKQJfUsR` |  |  |  |
| `items[38]._stats.compendiumSource` | null |  |  |  |  |
| `items[38]._stats.coreVersion` | string | `13.350` |  |  |  |
| `items[38]._stats.createdTime` | number | `1747937554071` | 1747937554071 | 1747937554071 |  |
| `items[38]._stats.duplicateSource` | null |  |  |  |  |
| `items[38]._stats.exportSource` | null |  |  |  |  |
| `items[38]._stats.lastModifiedBy` | string | `XPIM5aN65eH5LXee` |  |  |  |
| `items[38]._stats.modifiedTime` | number | `1760030502302` | 1760030502302 | 1760030502302 |  |
| `items[38]._stats.systemId` | string | `fallout` |  |  |  |
| `items[38]._stats.systemVersion` | string | `11.16.4` |  |  |  |
| `items[38].effects` | array | `[]` |  |  | Empty array |
| `items[38].folder` | null |  |  |  |  |
| `items[38].img` | string | `systems/fallout/assets/icons/items/miscellany.svg` |  |  |  |
| `items[38].name` | string | `Desinfektionsmittel` |  |  |  |
| `items[38].ownership.default` | number | `0` | 0 | 0 | Often 0 |
| `items[38].sort` | number | `0` | 0 | 0 | Often 0 |
| `items[38].system.canBeScrapped` | boolean | `True` |  |  |  |
| `items[38].system.cost` | number | `0` | 0 | 0 | Often 0 |
| `items[38].system.description` | string | `` |  |  |  |
| `items[38].system.effect` | string | `<p>Desinfektionsmittel f&uuml;r chirugisches Beste...` |  |  |  |
| `items[38].system.equipped` | boolean | `False` |  |  |  |
| `items[38].system.favorite` | boolean | `False` |  |  |  |
| `items[38].system.isJunk` | boolean | `False` |  |  |  |
| `items[38].system.quantity` | number | `1` | 1 | 1 |  |
| `items[38].system.rarity` | number | `0` | 0 | 0 | Often 0 |
| `items[38].system.source` | string | `` |  |  |  |
| `items[38].system.stashed` | boolean | `True` |  |  |  |
| `items[38].system.weight` | number | `0` | 0 | 0 | Often 0 |
| `items[38].type` | string | `miscellany` |  |  |  |
| `items[40]._id` | string | `AgkvD2rQFpZqJzuy` |  |  |  |
| `items[40]._stats.compendiumSource` | null |  |  |  |  |
| `items[40]._stats.coreVersion` | string | `13.350` |  |  |  |
| `items[40]._stats.createdTime` | number | `1753986778812` | 1753986778812 | 1753986778812 |  |
| `items[40]._stats.duplicateSource` | null |  |  |  |  |
| `items[40]._stats.exportSource` | null |  |  |  |  |
| `items[40]._stats.lastModifiedBy` | string | `XPIM5aN65eH5LXee` |  |  |  |
| `items[40]._stats.modifiedTime` | number | `1760030508034` | 1760030508034 | 1760030508034 |  |
| `items[40]._stats.systemId` | string | `fallout` |  |  |  |
| `items[40]._stats.systemVersion` | string | `11.16.4` |  |  |  |
| `items[40].effects` | array | `[]` |  |  | Empty array |
| `items[40].folder` | null |  |  |  |  |
| `items[40].img` | string | `systems/fallout/assets/icons/items/miscellany.svg` |  |  |  |
| `items[40].name` | string | `Glowing Goo` |  |  |  |
| `items[40].ownership.default` | number | `0` | 0 | 0 | Often 0 |
| `items[40].sort` | number | `0` | 0 | 0 | Often 0 |
| `items[40].system.canBeScrapped` | boolean | `True` |  |  |  |
| `items[40].system.cost` | number | `0` | 0 | 0 | Often 0 |
| `items[40].system.description` | string | `` |  |  |  |
| `items[40].system.effect` | string | `<p>Daraus kann das "Glow Ointment" hergestellt wer...` |  |  |  |
| `items[40].system.equipped` | boolean | `False` |  |  |  |
| `items[40].system.favorite` | boolean | `False` |  |  |  |
| `items[40].system.isJunk` | boolean | `False` |  |  |  |
| `items[40].system.quantity` | number | `3` | 3 | 3 |  |
| `items[40].system.quantityRoll` | string | `` |  |  |  |
| `items[40].system.rarity` | number | `0` | 0 | 0 | Often 0 |
| `items[40].system.source` | string | `` |  |  |  |
| `items[40].system.stashed` | boolean | `True` |  |  |  |
| `items[40].system.weight` | number | `0` | 0 | 0 | Often 0 |
| `items[40].type` | string | `miscellany` |  |  |  |

## Effects

| JSON Path | Type | Examples | Min | Max | Notes |
|-----------|------|----------|-----|-----|-------|
| `effects` | array | `[]` |  |  | Empty array |

## Other

| JSON Path | Type | Examples | Min | Max | Notes |
|-----------|------|----------|-----|-----|-------|
| `system.luckPoints` | number | `4` | 4 | 4 |  |
| `system.readMagazines` | array | `[]` |  |  | Empty array |
| `system.skill.tags.additionalTags` | array | `[]` |  |  | Empty array |
| `system.skill.tags.bonus` | number | `0` | 0 | 0 | Often 0 |
| `system.skill.tags.max` | number | `3` | 3 | 3 |  |

