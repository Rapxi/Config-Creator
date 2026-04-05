### Set up

1. Download the .zip and extract it into the AIO folder
2. Run install_deps.bat
3. Run launch_app.bat


### Tutorial

#### Firstly
Get an Api Key and paste it into the Text Box and save.

#### Secondly
Select the Gamemode on the first options list and then the Map to the Gamemode.

Optionally assign Unit names to the Slots, please keep in mind its from left to right to left to right.

####  Thirdly
1. Create an prompt, each prompt should have atleast 3 Key Values those are: 
- Slot (could be Unit name if you assigned) (1-6, None)
- Unit (1-5, None)
- Action (None, Place, Special Ability, Restart, Ability 1, Ability 2, VSJW 1, VSJW 2, VSJW 3, Swap, Sell)

2. Optionally you can also assign:
- Upgrade(0-14, Max, Auto, Same)
- Priority(None, Same, Bosses, Closest, First, Last, Strongest, Weakest)
- Delay <- 0 by default, recommended
- Wave <- 0 by default, recommended


As an example a prompt to place 3 speedwagons, 1 taka and 3 alucards and max upg them.

- Slot 1: Alucard
- Slot 2: Speed
- Slot 3: Taka
- (- This is in the Slot Context (optional))

- The "," are optional
- Place unit 1-3 speed, place unit 1 taka, place unit 1-3 alucard, upgrade unit 1-3 speed max, upgrade unit 1 taka max, upgrade unit 1-3 alucard max.

Output:
- Slot 2|Unit 1|0|None|Place|0|0
- Slot 2|Unit 2|0|None|Place|0|0
- Slot 2|Unit 3|0|None|Place|0|0
- Slot 3|Unit 1|0|None|Place|0|0
- Slot 1|Unit 1|0|None|Place|0|0
- Slot 1|Unit 2|0|None|Place|0|0
- Slot 1|Unit 3|0|None|Place|0|0
- Slot 2|Unit 1|Max|None|None|0|0
- Slot 2|Unit 2|Max|None|None|0|0
- Slot 2|Unit 3|Max|None|None|0|0
- Slot 3|Unit 1|Max|None|None|0|0
- Slot 1|Unit 1|Max|None|None|0|0
- Slot 1|Unit 2|Max|None|None|0|0
- Slot 1|Unit 3|Max|None|None|0|0


#### Fourth 
If youre fine with the output press "Save Config" Button below output