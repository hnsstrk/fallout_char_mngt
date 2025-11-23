# Analysis Expectations - Was das Script erfassen muss

**Basierend auf**: Screenshots von Dr. Eloise 'Ellie' Harper + JSON-Struktur-Analyse

Dieses Dokument definiert, welche Daten, Informationen und Werte wir aus den JSON-Exporten erwarten und extrahieren müssen.

---

## 1. Charakter-Grunddaten

### Direkt in JSON gespeichert:
- `name` - Voller Charaktername
- `type` - Charaktertyp ("character" oder "robot")
- `img` - Pfad zum Charakterbild
- `system.origin` - Herkunft/Origin (z.B. "Vault 77")
- `system.level.value` - Charakterlevel
- `system.level.currentXP` - Aktuell gesammelte XP
- `system.level.rewardXP` - Belohnungs-XP
- `system.luckPoints` - Glückspunkte
- `system.biography` - HTML-Biographie (enthält Allgemeine Informationen UND Regelwerk-Texte)
- `system.complication` - Komplikations-Wert
- `system.description` - Zusätzliche Beschreibung (oft leer)

### Berechnet/Abgeleitet:
- **`system.level.nextLevelXP`** - Kann 0 sein in JSON, aber Screenshot zeigt berechneten Wert (z.B. 1000)
- **Biographie-Parsing**: Die `system.biography` enthält structured HTML mit:
  - Allgemeine Informationen (Geburtstag, Geburtsort, Größe, Beruf)
  - Regelwerk-Texte (Traits, besondere Regeln)

---

## 2. S.P.E.C.I.A.L. Attribute

**Alle direkt verfügbar**:
- `system.attributes.str.value` - Strength
- `system.attributes.per.value` - Perception
- `system.attributes.end.value` - Endurance
- `system.attributes.cha.value` - Charisma
- `system.attributes.int.value` - Intelligence
- `system.attributes.agi.value` - Agility
- `system.attributes.luc.value` - Luck

---

## 3. Abgeleitete Statistiken

### Berechnungsformeln (aus Fallout TTRPG Quellenbuch):

**Max Health:**
- **FVTT System Formel** (aus GitHub: FalloutActor.mjs):
  ```
  Max HP = END + LCK + (Level - 1) - Radiation + health.bonus + (wellRested ? 2 : 0)
  ```
- **Komponenten:**
  - **Basis**: END + LCK
  - **Level-Progression**: (Level - 1) → +1 HP pro Level-Up
  - **Radiation-Penalty**: Aktuelle Strahlung reduziert max HP
  - **Health Bonus**: `system.health.bonus` (von Perks/Items)
  - **Well Rested**: `system.conditions.wellRested` gibt **+2 HP** wenn true

- **Beispiel (Ellie, Level 4):**
  - Basis: END 4 + LCK 4 = 8
  - Level-Ups: (4 - 1) = +3
  - Radiation: 0
  - health.bonus: 0
  - **Well Rested: true → +2 HP** ✓
  - **Total: 8 + 3 + 0 + 0 + 2 = 13 HP** ✓ (stimmt mit Screenshot überein!)

- **JSON-Felder:**
  - `system.health.max` - Berechneter Wert (oft 0 im Export)
  - `system.health.value` - Aktuelle HP
  - `system.health.bonus` - Bonus von Perks/Items
  - `system.radiation` - Aktuelle Strahlung (reduziert max HP!)
  - `system.conditions.wellRested` - Boolean (gibt +2 HP wenn true)

**Defense:**
- **Formel:** `1 if AGI ≤ 8, else 2 if AGI ≥ 9`
- Beispiel (Ellie): AGI 6 → Defense 1 ✓
- JSON: `system.defense.value` (oft 0)
- JSON: `system.defense.bonus`

**Initiative:**
- **Formel:** `PER + AGI`
- Beispiel (Ellie): PER 8 + AGI 6 = 14 ✓
- JSON: `system.initiative.value` (oft 0)
- JSON: `system.initiative.bonus`

**Melee Damage:**
- **Formel:** `STR 7-8: +1, STR 9-10: +2, STR 11+: +3, sonst 0`
- Beispiel (Ellie): STR 4 → +0 ✓
- JSON: `system.meleeDamage.value` (oft 0)
- JSON: `system.meleeDamage.bonus`

**Carry Weight:**
- **FVTT Formel:** `(STR × 10) + settings-based capacity` (Standard: 150 lbs)
- Beispiel (Ellie): 150 + (4 × 10) = 190 lb ✓
- **Encumbrance Level**: Wird basierend auf Verhältnis von aktuellem Gewicht zu max capacity berechnet
- JSON: `system.carryWeight.total` (oft 0, wird berechnet)
- JSON: `system.carryWeight.base` - Basis-Kapazität
- JSON: `system.carryWeight.mod` - Modifikatoren
- JSON: `system.carryWeight.value` - Aktuelles Gewicht
- JSON: `system.carryWeight.encumbranceLevel` - Belastungsstufe
- **Aktuelles Gewicht**: Summe aller `items[].system.weight * quantity`

**Next Level XP:**
- **FVTT Formel:** `(nextLevel × currentLevel ÷ 2) × 100`
- Beispiel (Ellie Level 4→5): (5 × 4 ÷ 2) × 100 = 1000 XP ✓
- JSON: `system.level.nextLevelXP` (oft 0, wird berechnet)
- JSON: `system.level.currentXP` - Aktuell gesammelte XP
- JSON: `system.level.rewardXP` - Belohnungs-XP
- JSON: `system.level.value` - Aktuelles Level

### Weitere Statistiken:
- `system.radiation` - Aktuelle Radiation (direkt)
- `system.resistance` - Globale Resistenzen (physical, energy, radiation, poison)

---

## 4. Body Parts (Körperteile)

**Struktur für alle 6 Teile** (`armL`, `armR`, `head`, `torso`, `legL`, `legR`):

Jedes Teil hat:
- `system.body_parts.{part}.injuries[]` - Array von 5 Injury-Werten (0-5)
- `system.body_parts.{part}.injuryOpenCount` - Anzahl offener Verletzungen
- `system.body_parts.{part}.injuryTreatedCount` - Anzahl behandelter Verletzungen
- `system.body_parts.{part}.status` - Status ("healthy", etc.)
- `system.body_parts.{part}.resistance.physical` - Physische Resistenz
- `system.body_parts.{part}.resistance.energy` - Energie-Resistenz
- `system.body_parts.{part}.resistance.poison` - Gift-Resistenz
- `system.body_parts.{part}.resistance.radiation` - Strahlungs-Resistenz

**Wichtig**: In Screenshots wird für jedes Body Part angezeigt:
- Injury-Nummernbereich (z.B. "Head 1-2", "Torso 3-8")
- 4 Icons mit Zahlen für die Resistenzen

---

## 5. Conditions & Status

### Conditions:
- `system.conditions.alcoholic` - Boolean
- `system.conditions.fatigue` - Wert
- `system.conditions.intoxication` - Wert
- `system.conditions.wellRested` - Boolean
- `system.conditions.hunger` - Wert (nicht in Screenshots sichtbar, aber vorhanden!)
- `system.conditions.thirst` - Wert (nicht in Screenshots sichtbar, aber vorhanden!)
- `system.conditions.sleep` - Wert
- `system.conditions.lastChanged` - Timestamps für hunger/sleep/thirst

### Andere Status-Felder:
- `system.bodyType` - "humanoid" oder andere
- `system.immunities.poison` - Boolean
- `system.immunities.radiation` - Boolean

### Conditions in FVTT UI:
Im Screenshot "CONDITIONS" Dropdown werden angezeigt: Full, Quenched, Rested (basierend auf hunger/thirst/sleep Werten)

---

## 6. Skills (17 Skills in items[])

**Jedes Skill-Item hat**:
- `name` - Skill-Name (z.B. "Medicine", "Science", "Athletics")
- `type` - "skill"
- `system.value` - Rank/Level des Skills
- `system.tag` - Boolean (ob getaggt)
- `system.defaultAttribute` - Zugehöriges S.P.E.C.I.A.L. ("str", "int", "per", etc.)
- `system.description` - HTML-Beschreibung des Skills
- `system.favorite` - Boolean
- `system.source` - "core_rulebook"
- `system.summary` - Meist leer

**Skill-Tags System**:
- `system.skill.tags.max` - Max Anzahl Tags (z.B. 3)
- `system.skill.tags.bonus` - Tag-Bonus
- `system.skill.tags.additionalTags` - Array zusätzlicher Tags

**Alle Skills müssen auf Charakterbogen**, gruppiert nach Attribut, mit Tag-Markierung und Rank.

---

## 7. Trait (1 Trait in items[])

**Trait-Item**:
- `name` - Trait-Name (z.B. "Vault Kid")
- `type` - "trait"
- `system.description` - Vollständige HTML-Beschreibung mit Mechanics und Flavor Text
- `system.favorite` - Boolean
- `system.source` - "core_rulebook"

**WICHTIG**: Trait muss mit vollständiger Beschreibung auf Charakterbogen!

---

## 8. Perks (4 Perks in items[] bei Ellie)

**Perk-Item Struktur**:
- `name` - Perk-Name (z.B. "Chemist", "Medic", "Intense Training", "Robotics Expert")
- `type` - "perk"
- `system.description` - HTML-Beschreibung inkl. Requirements-Text
- `system.rank.value` - Aktueller Rank
- `system.rank.max` - Maximaler Rank
- `system.requirements` - Text-Requirements (meist leer)
- `system.requirementsEx` - Detailliertes Requirements-Objekt:
  - `level` - Min Level
  - `levelIncrease` - Level-Increase bei jeder Rank
  - `attributes.{attr}.value` - Min Attribut-Werte (für alle 7 S.P.E.C.I.A.L.)
  - `isCompanion` - Boolean
  - `magazineUuids` - Array
  - `notGhoul`, `notHuman`, `notRadiationImmune`, `notRobot`, `notSupermutant` - Exclusions
- `system.favorite` - Boolean
- `system.source` - "core_rulebook"

**WICHTIG**: Perks mit Rank, vollständiger Beschreibung UND parsed Requirements müssen auf Charakterbogen!

**Perk-Namen mit Rang-Anzeige**: "Robotics Expert (2)" bedeutet max rank ist 2 oder mehr - muss aus der Beschreibung oder levelIncrease erkannt werden.

---

## 9. Weapons (3 Weapons bei Ellie)

**Weapon-Item - Sehr komplexe Struktur**:

### Basis-Daten:
- `name` - Waffen-Name
- `type` - "weapon"
- `system.description` - HTML-Beschreibung inkl. Mod-Listen
- `system.favorite` - Boolean (zeigt "Favorite Weapons" an)
- `system.equipped` - Boolean
- `system.quantity` - Anzahl
- `system.weight` - Gewicht
- `system.cost` - Wert in Caps
- `system.rarity` - Seltenheit (1-4)

### Damage:
- `system.damage.rating` - **Haupt-Schadenswert** (z.B. 4)
- `system.damage.damageType.physical` - Boolean
- `system.damage.damageType.energy` - Boolean
- `system.damage.damageType.poison` - Boolean
- `system.damage.damageType.radiation` - Boolean

### Damage Effects:
- `system.damage.damageEffect.{effect}.rank` - Rank des Effekts
- Mögliche Effekte: piercing_x, burst, arc, freeze, persistent, radioactive, spread, stun, tranquilize_x, vicious, breaking
- **Nur Effekte mit rank > 0 anzeigen** (z.B. "Piercing 1")

### Weapon Qualities:
- `system.damage.weaponQuality.{quality}.value` - Wert der Quality
- Mögliche Qualities: accurate, close_quarters, concealed, reliable, two_handed, suppressed, blast, inaccurate, unreliable, etc.
- **Nur Qualities mit value > 0 anzeigen** (z.B. "Close Quarters", "Reliable")

### Combat Stats:
- `system.fireRate` - Feuerrate (z.B. 2)
- `system.range` - Range ("close", "medium", "long")
- `system.ammo` - Munitionstyp (z.B. "10mm Round")
- `system.ammoPerShot` - Munition pro Schuss
- `system.melee` - Boolean (Nahkampfwaffe?)
- `system.weaponType` - Waffentyp ("smallGuns", "bigGuns", "energyWeapons", "meleeWeapons", "unarmed", "explosives", "throwing")

### Mods:
- `system.mods.installedMods` - Installierte Mods
- `system.mods.current` - Anzahl aktueller Mods
- `system.mods.max` - Max Mods
- `system.mods.modded` - Boolean

**Screenshot zeigt**: Damage (mit Icon), Type Icon, Fire Rate, Range, Qualities (als Text-Liste), Effects

---

## 10. Ammo (1 Ammo bei Ellie)

**Ammo-Item**:
- `name` - Munitionsname (z.B. "10mm Round")
- `type` - "ammo"
- `system.quantity` - Anzahl (z.B. 10)
- `system.description` - Beschreibung
- `system.weight` - Gewicht
- Weitere Felder analog zu Items

---

## 11. Apparel (6 Apparel-Items bei Ellie)

**Apparel-Item Struktur**:
- `name` - Kleidungs-/Rüstungsname
- `type` - "apparel"
- `system.description` - HTML-Beschreibung inkl. Special-Effekte
- `system.weight` - Gewicht
- `system.cost` - Wert
- `system.quantity` - Anzahl
- `system.equipped` - Boolean

### Apparel-Kategorie:
- `system.appareltype` - "armor", "clothing", "headgear", "outfit", "powerArmor"

### Locations:
- `system.bodyParts.head` - Boolean
- `system.bodyParts.torso` - Boolean
- `system.bodyParts.armL` - Boolean
- `system.bodyParts.armR` - Boolean
- `system.bodyParts.legL` - Boolean
- `system.bodyParts.legR` - Boolean

**In Screenshot als Abkürzungen**: "AL AR LL LR T" oder "H"

### Resistances:
- `system.resistance.physical` - Physischer Schutz
- `system.resistance.energy` - Energie-Schutz
- `system.resistance.poison` - Gift-Schutz
- `system.resistance.radiation` - Strahlungs-Schutz

**In Screenshot**: 3 Icons mit Zahlen (Energy, Physical, Poison - Radiation wird separat oder zusammen gezeigt)

### Mods:
- `system.mods` - Ähnliche Struktur wie bei Waffen

**WICHTIG**: Beschreibung enthält oft "Special:" Texte die geparst werden müssen!

---

## 12. Apparel Mods (5 Apparel-Mods bei Ellie)

**Apparel-Mod-Item**:
- `name` - Mod-Name
- `type` - "apparel_mod"
- `system.description` - Beschreibung
- `system.quantity` - Anzahl
- Weitere Details zu analysieren

---

## 13. Consumables (4 Consumables bei Ellie)

**Consumable-Item**:
- `name` - Name (z.B. "Stimpak", "RadAway", "Mentats", "Purified Water")
- `type` - "consumable"
- `system.quantity` - Anzahl
- `system.description` - HTML-Beschreibung mit Effekten
- `system.weight` - Gewicht
- `system.cost` - Wert

**Effekt-Texte** müssen aus Description geparst werden (z.B. "Heals 4 HP", "Re-roll 1d20 on PER and INT tests")

**Im Screenshot**: Quantity links, Name, Effekt-Beschreibung (kurz)

---

## 14. Books & Magazines (1 bei Ellie)

**Book-Item**:
- `name` - Titel (z.B. "Apotheker von Gestern Band I")
- `type` - "books_and_magz"
- `system.quantity` - Anzahl
- `system.description` - Beschreibung/Effekt
- Weitere Felder analog

---

## 15. Miscellany (7 Miscellany-Items bei Ellie)

**Miscellany-Item**:
- `name` - Item-Name (z.B. "Doctor's Bag", "First Aid Kit", "Multi-Tool", "Pip-Boy", etc.)
- `type` - "miscellany"
- `system.quantity` - Anzahl
- `system.description` - HTML-Beschreibung mit Effekten/Verwendung
- `system.weight` - Gewicht
- `system.cost` - Wert
- `system.rarity` - Seltenheit

**Effekte** aus Description parsen (z.B. "Reduce the difficulty of Medicine tests by 1")

---

## 16. Currency & Materials

### Currency:
- `system.currency.caps` - Anzahl Caps
- `system.currency.other` - Freitext für andere Währung/Wertgegenstände

### Materials:
- `system.materials.junk` - Junk-Material-Anzahl
- `system.materials.common` - Common-Material-Anzahl
- `system.materials.uncommon` - Uncommon-Material-Anzahl
- `system.materials.rare` - Rare-Material-Anzahl

---

## 17. Effects (Bei Ellie leer, aber Struktur vorhanden)

**Effects in `effects[]` Array**:
- Temporary Effects
- Passive Effects
- Inactive Effects

Jedes Effect hätte:
- `name` - Effekt-Name
- Source - Quelle
- Duration - Dauer
- Weitere Modifikatoren

**In Screenshots**: Separate Kategorien für Temporary/Passive/Inactive

---

## 18. Addictions & Diseases

**Vermutlich** als Effekte oder spezielle Item-Typen gespeichert.

Im Screenshot sichtbar aber bei Ellie leer - muss bei anderen Charakteren analysiert werden.

---

## 19. Power Armor

**Power Armor Health** ist ein eigenes Feld, bei Ellie leer.

Vermutlich:
- `system.powerArmorHealth` oder ähnlich
- Power Armor als spezielle Apparel-Items

---

## Kritische Erkenntnisse für das Script:

### 1. Berechnete Werte
Das Script MUSS folgende Werte berechnen können, da sie oft 0 in JSON sind:

**Bestätigte Formeln (aus Fallout 2d20 Quellenbuch + FVTT System Code):**
- **Max Health**: `END + LCK + (Level - 1) - Radiation + health.bonus + (wellRested ? 2 : 0)`
  - Basis bei Level 1: END + LCK
  - Jedes Level-Up: +1 HP
  - Radiation reduziert max HP
  - Well Rested Status: +2 HP
  - ✓ Bei Ellie: 4+4+3+0+0+2 = 13 HP (korrekt validiert!)
- **Defense**: `1 if AGI ≤ 8, else 2`
- **Initiative**: `PER + AGI`
- **Melee Damage**: `STR 7-8: +1, STR 9-10: +2, STR 11+: +3, sonst 0`
- **Carry Weight**: `150 + (STR × 10)` lbs
- **Aktuelles Gewicht**: Summe aller `items[].system.weight * quantity`

**Zusätzliche Erkenntnisse:**
- **Next Level XP**: ✓ Formel gefunden: `(nextLevel × currentLevel ÷ 2) × 100`
- **Encumbrance Level**: ✓ Wird aus Verhältnis aktuelles/max Gewicht berechnet
- **Body Resistances**: Werden aus equipped Armor/Clothing/PowerArmor aggregiert
- **Action Points (AP)**: Nicht persistent - nur während Combat relevant

**Alle Formeln stammen aus**: [FVTT Fallout System - FalloutActor.mjs](https://github.com/Muttley/foundryvtt-fallout/blob/main/system/src/documents/FalloutActor.mjs)

### 2. HTML-Parsing
Viele Felder enthalten HTML:
- `system.biography` - Strukturiertes HTML mit Headers
- `system.description` in allen Items - HTML mit Formatting
- **Special**-Markierungen in Beschreibungen müssen erkannt werden

### 3. Qualities & Effects mit Werten
Bei Weapons und anderen Items:
- Nur Qualities/Effects mit `value > 0` oder `rank > 0` sind aktiv
- Format: "Quality Name" wenn value=1, "Quality Name (X)" wenn rank=X

### 4. Item-Kategorisierung
Items müssen nach `type` UND zusätzlichen Kriterien gruppiert werden:
- Apparel nach `appareltype` (armor/clothing/headgear/outfit/powerArmor)
- Weapons nach `weaponType` oder `favorite`

### 5. Body Part Injury Ranges
Body Parts haben feste Nummernbereiche:
- Head: 1-2
- Torso: 3-8
- Left Arm: 9-11
- Right Arm: 12-14
- Left Leg: 15-17
- Right Leg: 18-20

Diese müssen im Layout angezeigt werden.

### 6. Icon-Mapping
Resistance-Typen und Damage-Typen brauchen Icon-Representation:
- Physical (skull/fist icon)
- Energy (lightning icon)
- Poison (biohazard icon)
- Radiation (radiation icon)

### 7. Leer vs. 0 vs. Nicht vorhanden
Das Script muss unterscheiden:
- Feld existiert nicht
- Feld ist leer string ""
- Feld ist 0 (könnte berechnet sein!)
- Feld ist false vs. nicht vorhanden

---

## Zusammenfassung: Erwartungen an das Script

**Das `analyze_character.py` Script muss:**

1. **Alle Top-Level Felder extrahieren**:
   - name, type, img, system.*

2. **Alle Items durchgehen** und nach Typ gruppieren:
   - skills (17x), perks, trait, weapons, ammo, apparel, apparel_mod, consumable, books_and_magz, miscellany

3. **Für jeden Item-Typ** die relevanten Felder dokumentieren:
   - Nicht nur flache Felder, sondern auch:
   - Nested Objects (damage.damageEffect.*, damage.weaponQuality.*, etc.)
   - Arrays (injuries[], magazineUuids[], etc.)

4. **Berechnete Felder identifizieren**:
   - Welche Felder sind oft 0 und müssen berechnet werden?

5. **HTML-Felder markieren**:
   - Welche Felder enthalten HTML das geparst werden muss?

6. **Value-basierte Felder**:
   - Bei Qualities/Effects: nur aktive (value > 0) sind relevant

7. **Datentypen erfassen**:
   - String, Number, Boolean, Object, Array
   - Bei Numbers: Beispielwerte-Range

8. **Output generieren**:
   - `extracted_fields.json` - Vollständige maschinelle Struktur
   - `FIELD_INVENTORY.md` - Menschenlesbare Tabelle mit:
     - JSON-Pfad
     - Datentyp
     - Beispielwert(e)
     - Häufigkeit (in wie vielen Items kommt es vor?)
     - Notizen (z.B. "HTML", "oft 0", "berechnet?")

---

## Nächste Schritte

1. Script `analyze_character.py` implementieren basierend auf diesen Erwartungen
2. Auf Ellie's JSON ausführen
3. Output `FIELD_INVENTORY.md` prüfen
4. Mit Screenshots abgleichen
5. Missing Fields identifizieren
6. Berechnungsformeln recherchieren/dokumentieren
