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
# `full` includes everything. Most routes can use `most`, which is `full` without koroks
- use: Pistonight/celer-presets/totk/full.yaml
- plugins:
  - use: variables # required
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
    - [Warp](#warp)
    - [Bubbulfrogs](#bubbulfrog)
    - [Wells](#terrain)
    - [Caves](#terrain)
    - [Chasms](#terrain)
    
    ```yaml
    - use: Pistonight/celer-presets/totk/most.yaml
    ```
4. `full` Includes:
    - Everything in `most`
    - [Koroks](#korok)
    
    ```yaml
    - use: Pistonight/celer-presets/totk/full.yaml
    ```

## Usage

### Presets

#### `Korok`
Provides korok ID, type, and movements.
Also displays the number of koroks collected.
```yaml
# Simple usage
- _Korok::EC12

# Race/Flower/Target koroks have ::Start and ::End coordinates available separately
- Start GC07:
    movements:
    - _Korok::GC07::Start
- Do stuff before landing on target
- _Korok::GC07:
    movements:
    - _Korok::GC07::End

# GC14 is a flower korok. Just doing this will fill in the movements from start to end
- _Korok::GC14

# For friend koroks, just doing this will have the movements from picking up to dropping off
- _Korok::GC21
# Since friend koroks are usually far apart, there are preset texts and icons for picking up and dropping off
# The seed is counted
- _Korok::GC21::Start # Shows "Pick up GC21"
- Do other stuff
- _Korok::GC21::End # Shows "Drop off GC21"

# Note that friend koroks increase the counter by 2. This is done using the variables system internally
# if you need to change other variables in the same step, you need to manually set the korok counter
# (Only need to do this *if* you are changing `vars`)
- _Korok::GC21:
    vars:
      another-var: .add(5)
      counter-korok: .add(1) # counter is incremented by 1 automatically, need to add another 1

```
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
- _Boss::Talus::Battle
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
# Warping to a temple entrance (Wind, Fire, Water, Lightning, Spirit)
- _Warp::Temple::Wind
# Warping to tech lab (note there's no akkala tech lab warp point)
- _Warp::TechLab::Hateno
# Warping to RoA
- _Warp::RoA
# Warping to Great Abandoned Central Mine
- _Warp::Mine::Central
# Warping to travel medallion. Order of the coordinates are the same as you would enter with the `coord` property
- _Warp::TravelMedallion<X,Z,Y>
```
#### `Bubbulfrog`
Provides coordinates for all bubbulfrogs. Also displays the number of bubbulgems collected.

Bubbulfrogs are identified by the Cave name
```yaml
- _Bubbulfrog::AncientPrisonRuins
- _Bubbulfrog::KomoShorelineCave
```

### Terrain
There are additional presets for terrain features in TOTK: Wells, Caves and Chasms.

#### `Well`
Well locations and counter for how many wells discovered.
The well icon is different on the doc and map. The in-game icon is used on the map and the celer-style icon is used on the doc.
```yaml
# line with the well with icon and counter
- _Well::DronocsPass
# Move to the well location without text in the doc
# This will show the well icon on the map, but will not count towards the well counter
- Go to the well:
    movements:
    - _Well::DronocsPass
```

#### `Cave`
Cave entrances. The cave icon is different on the doc and map. The in-game icon is used on the map and the celer-style icon is used on the doc.

Each cave is identified by its name. If the name has "Cave" in it, it is omitted.
```yaml
# Enter and Exit cave text, with icons
- _Cave::Enter::LakeKilsie           # "Lake Kilsie Cave", the "Cave" is omitted
- _Cave::Exit::LakeDarmanMonsterDen  # "Lake Darman Monster Den"
- _Cave::Enter::UnderZorasDomain     # "Cave Under Zora's Domain", the "Cave" is omitted

# for caves with multiple entrances, you must use a letter to identify the right entrance
# the letter is somewhat random (sorted by id) so you will have to trial and error to find the right one starting from A
- _Cave::Enter::AncientAltarRuins::C

# Move to the cave location without text in the doc
- Go to the cave:
    movements:
    - _Cave::Enter::LakeKilsie
```

#### `Chasm`
Chasms. The chasm icon is different on the doc and map. The in-game icon is used on the map and the
celer-style icon is used on the doc.

Like caves, each chasm also comes with `Enter` and `Exit`. Since most chasms are vertical, using
`Enter` and `Exit` properly will allow the lines on the map to be drawn on the correct layer
```yaml
# Enter and Exit chasm text, with icons
- _Chasm::Enter::GerudoSummit
- _Chasm::Exit::HyruleRidge

# Enter/exit chasms without text in the doc
- enter a chasm and exit another:
    movements:
    - _Chasm::Enter::GerudoSummit
    - _Chasm::Exit::HyruleRidge
```
