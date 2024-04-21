# BOTW Presets

See [Config](#config) for what to include in `project.yaml` to use these presets

See [Usage](#usage) for how to use the presets in the route

## Config

### Example
Here is an example of a typical `project.yaml` that uses BOTW presets:

**Make sure you add the `variables` and `botw-ability-unstable` plugins for the counters and fury/gale to work properly!!!** See [below](#champion-abilities) for how fury/gale works
```yaml
# project.yaml
title: Example Route
version: 1.0
route:
  ...
config:
# See `Layers` below on what to use here
# `full` includes everything. Most routes can use `most`, which is `full` without koroks
- use: Pistonight/celer-presets/botw/full.yaml
- plugins:
  - use: variables             # required
  - use: botw-ability-unstable # required
```

### Layers
The presets are provided in 4 layers. 
You can choose to only include the layer that has the things you want.
Each layer also includes everything in the previous layer

1. `map`: Includes just the botw map
    ```yaml
    - use: Pistonight/celer-presets/botw/map.yaml
    ```
2. `mini` Includes:
    - The map
    - Tags:
        - item
        - loc
        - npc
        - rune
        - boss
        - enemy
        - important
        - dir
        - terrain
    - [Time of Day (Tod)](#tod)
    - [Chest](#chest)
    - [Equipment](#equipment)
    - [Shop](#shop)
    - [Npc](#npc)
    - [Cook](#cook)
    - [Discover](#discover)
    - [Snap](#snap)
    - [Material](#material)
    ```yaml
    - use: Pistonight/celer-presets/botw/mini.yaml
    ```
3. `most` Includes:
    - Everything in `mini`
    - [Bosses](#boss)
    - [Shrines](#shrine)
    - [Towers](#tower)
    - [Memories](#memory)
    - [Warp](#warp)
    ```yaml
    - use: Pistonight/celer-presets/botw/most.yaml
    ```
4. `full` Includes:
    - Everything in `most`
    - [Koroks](#korok)
    ```yaml
    - use: Pistonight/celer-presets/botw/full.yaml
    ```

## Usage

### Presets
#### `Korok`
Provides korok ID, type, and movements. Some koroks have a comment hinting the location.
Also displays the number of koroks collected.
```yaml
# Simple usage
- _Korok::A12

# If you can get a korok from far away, you can use the ::Away suffix and give a color
# of the line. For example, shooting a balloon from far away
- _Korok::W33::Away<white>

# Race/Flower koroks have ::Start and ::End coordinates available separately
- Start A05:
    movements:
    - _Korok::A05::Start
- Do stuff during the race
- _Korok::A05:
    movements:
    - _Korok::A05::End

# A04 is a flower korok. Just do this will fill in the movements from start to end
- _Korok::A04
```

The Korok preset also increments the `korok-seed` variable. You can use this to track if you have enough seeds for inventory upgrade every time you visit hestu:
```yaml
- spend 5 seeds:
    notes: .var(korok-seed) seeds left
    vars:
      korok-seed: .sub(5)
```
#### `Memory`
Provides memory location, coordinates and title (in game name of the memory). Also displays the number of memories collected.
```yaml
# Memories are identified by the landmark/location
- _Memory::LanayruRoad
```
See [here](./memories.yaml) for the full list of memories
#### `Tower`
```yaml
# Towers are identified by the region
- _Tower::GreatPlateau
```
See [here](./towers.yaml) for the full list of towers
#### `Shrine`
Provides shrine name and coordinates and displays the number of shrines completed.
```yaml
# Shrines are identified by the (English) name without spaces or apostrophes (')
- _Shrine::OwaDaim
# DLC shrines are also available
- _Shrine::KamiaOmuna
```
#### `Warp`
Provides coordinates for all warp points available. Also displays the number of warps
executed.
```yaml
# Warping to a shrine
- _Warp::Shrine::OwaDaim
# Warping to a tower
- _Warp::Tower::Akkala
# Warping to a divine beast
- _Warp::Beast::Ruta
# Warping to tech labs
- _Warp::TechLab::Hateno
- _Warp::TechLab::Akkala
# Warping to SoR
- _Warp::SOR
# Warping to travel medallion. Coordinates are X,Z
- _Warp::TravelMedallion<123.45,678.90>
```
#### `Boss`
Provides presets for all types of overworld bosses. Also displays the number of bosses of that type defeated. Currently does not provide the coordinates for each boss
```yaml
- _Boss::Talus::Stone
- _Boss::Talus::Luminous
- _Boss::Talus::Rare
- _Boss::Talus::Igneo
- _Boss::Talus::Frost
- _Boss::Hinox::Red
- _Boss::Hinox::Blue
- _Boss::Hinox::Black
- _Boss::Hinox::Stal
- _Boss::Stalnox # same as _Boss::Hinox::Stal
- _Boss::Molduga
# DLC bosses are supported too. However they won't be counted towards the molduga/talus count
- _Boss::Talus::Igneo::Titan
- _Boss::Molduking
```
#### `Tod`
Provides presets for passing time at a campfire.
```yaml
- _Tod::Morning
- _Tod::Noon
- _Tod::Night
```
#### `Chest`
2 presets for chest icon + item name
```yaml
- _Chest<Some Item>
- _Chest::Special<Some Special Item>
```
#### `Equipment`
Presets for equipment icon + item name
```yaml
- _Equipment::Bow<Some Bow>
- _Equipment::Shield<Some Shield>
- _Equipment::Weapon<Some Weapon>
```
#### `Shop`
Preset for shop icon + shop name
```yaml
- _Shop<Some Shop>
```
#### `Npc`
Preset for NPC icon. Currently does not provide coordinates for each NPC.
```yaml
- _Npc<Cherry>
- _Npc::Rito<Kass>
- _Npc::Goron<Bludo>
- _Npc::Gerudo<Riju>
- _Npc::Sheika::Male<Pumpkin>
- _Npc::Sheika::Female<Impa>
- _Npc::Zora::Male<Muzu>
- _Npc::Zora::Female<Mipha>
```
#### `Cook`
Preset for a cook icon
```yaml
- _Cook<Fried Egg>
```
#### `Discover`
Reminder for discovering a location. Currently does not track the number of locations discovered.
```yaml
- _Discover<Some Location>
```
#### `Snap`
Preset for taking picture of something
```yaml
- _Snap<Guardians>
```
#### `Material`
Preset for collecting materials
```yaml
- _Material<Apple>
# To also track the material count:
# the example below adds 10 to the `material<Lizalfos Tail>` variable
- _Material::Counted<Lizalfos Tail, 10>
```

### Champion Abilities
The presets uses a plugin to automatically manage fury/gale counts (and cooldown if needed). By default, it does not estimate cooldowns for you and it assumes the cooldown is instant. It will be up to you to make sure you don't use an ability when it's on cooldown.

#### Counts
Examples:
```yaml
- Examples:
  - do something # 3 furies and 3 gales here
  - use .gale(1) # displays `use GALE 1`, 2 gales left

  # can also use the old celer format by specifying the count with a property
  # this is only for compability, the new format is recommended
  - use .gale(): 
      gale: 2    # displays `use GALE 2-3`, no gales left
  
  # IMPORTANT: different from old celer, if you have more than 1 .gale() or .fury(), all occruences will use the ability
  # the line below will be `use FURY 1 here then FURY 2-3 there`
  - use .fury(1) here then .fury(2) there

  # if you are trying to use more than you have, there will be a warning
  - use .fury(1)
  - use .fury(3) # warning! only 2 furies left
  
```
#### Cooldown estimate
If you want the plugin to also estimate cooldown and give warning when the ability may not be ready, you need to turn it on in the config:
```yaml
plugins:
- use: botw-ability-unstable
  with:
    estimate-recharge: true
    # optionally, you can give a multiplier for the recharge
    # - use number greater than one if your execution is slower than estimate
    # - (unlikely, but) use number less than one if your execution is faster than estimate
    # for example, 2.0 means abilities recharges twice as fast
    multiplier: 1.0 # 1.0 is default
```
Shrines and koroks have a predefined "time passed" based on their type. Each step also costs time based on the number of `dir` tags in them.

If you need to override the time for a step, use the `time-override` property to specify the seconds the step should take.
```yaml
- Example:
  - this step takes 5 minutes:
      time-override: 300
```

###### Castle
The abilities recharge 3x as fast in Hyrule Castle. The plugin automatically handles that using the coordinates.

###### DLC Upgrades
Use `gale-plus: true` or `fury-plus: true` on the line when you obtain the upgraded ability.
```yaml
- Example:
  - get gale plus:
      gale-plus: true
  - get fury plus:
      fury-plus: true

```
This will cut down the cooldown of the abilities by 1/3 just like the game