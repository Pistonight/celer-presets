# TOTK Presets

See [Config](#config) for what to include in `project.yaml` to use these presets

See [Usage](#usage) for how to use the presets in the route

## Config

### Example
Here is an example of a typical `project.yaml` that uses TOTK presets:
```yaml
# project.yaml
title: Example Route
version: 1.0
route:
  ...
config:
# See `Layers` below on what to use here
# `full` includes everything. Most routes can use `most`, which is `full` without koroks and bubbulfrogs
- use: Pistonight/celer-presets/totk/full.yaml
plugins:
- variables # required
```

### Layers
The presets are provided in 4 layers. 
You can choose to only include the layer that has the things you want.
Each layer also includes everything in the previous layer

1. `map`: Includes just the totk map
    ```yaml
    - use: Pistonight/celer-presets/totk/map.yaml
    ```
2. `mini` Includes:
    - The map
    - Basic tags in the [BOTW presets](../botw/README.md#layers)
    ```yaml
    - use: Pistonight/celer-presets/totk/mini.yaml
    ```
3. `most` Includes:
    - Everything in `mini`
    - [Shrines](#shrine)
    - [Lightroots](#lightroot)
    - [Towers](#tower)
    - [Tears](#tear)
    - [Bosses](#boss)
    - [Warp](#warp) TODO
    - [Wells](#well) TODO
    - [Caves](#cave) TODO
    - [Chasms](#chasm) TODO
    ```yaml
    - use: Pistonight/celer-presets/totk/most.yaml
    ```
4. `full` Includes:
    - Everything in `most`
    - [Koroks](#korok) TODO
    - [Bubbulfrogs](#bubbulfrog) TODO
    
    ```yaml
    - use: Pistonight/celer-presets/totk/full.yaml
    ```

## Usage

### Presets

#### `Korok`
TODO
#### `Tear`
TODO
#### `Shrine`
Provides shrine name and coordinates and displays the number of shrines completed.
Shrines on the Surface, in the Sky, and in a cave have different colored-icons.
Blessings, Proving Grounds and Combat Trainings are also indicated with different icons.
```yaml
# Shrines are identified by the (English) name without hyphens ('-')
- _Shrine::Mayachin # Mayachin Shrine
- _Shrine::Oogim    # O-ogim Shrine
```
#### `Lightroot`
Provides lightroot name and coordinates and displays the number of lightroots completed.
```yaml
# Lightroots are identified by the (English) name without hyphens ('-')
- _Lightroot::Nihcayam # Nihcayam Lightroot
- _Lightroot::Migoo    # Migo-o Lightroot
```
#### `Tower`
Provides coordiantes for all towers. Each tower is identified by its English name without spaces or apostrophes.
```yaml
- _Tower::LindorsBrow # Lindor's Brow Tower
```
#### `Tear`
Tears are identified by their numbers (01 to 12) in the game.
```yaml
- _Tear::01
```
#### `Boss`
Provides presets for Talus/Hinox/Molduga/Frox/Flux Constructs/Gleeoks. Also displays the number of bosses defeated for each type.
```yaml
# The general syntax is _Boss::[Type]::[Variant][::[Depth]]

# Talus, Hinox and Moldugas are the same as BOTW
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

# You can also add ::Depth to have the depth style icon and text.
# (except for Moldugas)
- _Boss::Talus::Stone::Depth
- _Boss::Hinox::Red::Depth
- _Boss::Stalnox::Depth

# Flux Constructs
- _Boss::FluxConstruct::I
- _Boss::FluxConstruct::II
- _Boss::FluxConstruct::III
- _Boss::FluxConstruct::I::Depth
- _Boss::FluxConstruct::II::Depth
- _Boss::FluxConstruct::III::Depth

# Frox
- _Boss::Frox
- _Boss::Frox::Obsidian
- _Boss::Frox::BlueWhite

# Gleeok
- _Boss::Gleeok::Flame
- _Boss::Gleeok::Frost
- _Boss::Gleeok::Thunder
- _Boss::Gleeok::King
```
#### `Warp`
Provides coordinates for all warp points available. Also displays the number of warps
executed.
```yaml
# Warping to a shrine
- _Warp::Shrine::Kudanisar
# Warping to a lightroot
- _Warp::Lightroot::Rasinaduk
# Warping to a tower
- _Warp::Tower::LindorsBrow
# Warping to a temple TODO
# Warping to tech labs TODO
# Warping to RoA TODO
# Warping to travel medallion. Coordinates are X,Y,Z TODO
```
#### `Boss`
TODO

