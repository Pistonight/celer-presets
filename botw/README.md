# BOTW Presets

See [Config](#config) for what to include in `project.yaml` to use these presets

See [Usage](#usage) for how to use the presets in the route

**Parity Notice**
The following features from the old celer do not work yet:
- [ ] Champion ability/time estimation

## Config

### Example
Here is an example of a typical `project.yaml` that uses BOTW presets:
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
plugins:
- variables # required
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
    - Time of Day (Tod)
    - Chest
    - Equipment
    - Shop
    - Npc
    - Cook
    - Discover
    - Snap
    - Material
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
- _Boss::Molduga
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
- _Npc::SheikaMale<Pumpkin>
- _Npc::SheikaFemale<Impa>
- _Npc::ZoraMale<Muzu>
- _Npc::ZoraFemale<Mipha>
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
