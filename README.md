# Halloween Trick Or Treat
Create a [Stardew Valley](https://www.stardewvalley.net/) Halloween Trick Or Treat scene using CircuitPython and hardware from Adafruit.

Characters in the scene will enter from the left or right, walk to the door, knock, receive their Halloween candy, then continue on to the next house (off screen)! 

The code is built out to randomly select a trick or treater from the pool of available character sprites, run through the trick-or-treating sequence, then exit. Modifications to the code can be made to allow you to:
- Add new characters
- Change the time characters spend at the door
- Change the interval at which a new trick or treater will arrive

---

### Hardware Used
- [Adafruit Feather RP2040](https://www.adafruit.com/product/4884)
- [Header Kit for Feather - 12-pin and 16-pin Female Header Set](https://www.adafruit.com/product/2886)
- [Adafruit RGB Matrix Featherwing Kit](https://www.adafruit.com/product/3036)
- [64x32 RGB LED Matrix - 4mm pitch](https://www.adafruit.com/product/2278)
- [Black LED Diffusion Acrylic Panel](https://www.adafruit.com/product/4749)
- [Clear Adhesive Squares - 6 pack - UGlu Dashes](https://www.adafruit.com/product/4813)
- [Adjustable Bent-Wire Stand](https://www.adafruit.com/product/1679)
- [12V 5A switching power supply](https://www.adafruit.com/product/352)

### CircuitPython Version
- [CircuitPython 8.x for RP2040](https://circuitpython.org/board/adafruit_feather_rp2040/)


## Physical Assembly Instructions
- Solder Header Pins to RP2040.
- Solder Female Header Pins, 2x8 IDC header, 2.1mm DC jack, and 5.08mm terminal block set to RGB Matrix Featherwing.
- Cut LED Matrix Plug-In Power cable to fit. Solder cables together and wrap in heat shrink tubing or electrical tape.
- Use Clear Adhesive Squares to attach Acrylic Panel to LED Panel.

## Configuration/Coding Instructions
- [Install CircuitPython on the Adafruit RP2040](https://learn.adafruit.com/adafruit-feather-rp2040-pico/circuitpython).
- Copy following directories and files to the main `CIRCUITPY` drive.
    - `/lib`
    - `/bmps`
    - `background_element.py`
    - `code.py`
    - `display_factory.py`
    - `sprite_factory.py`
    - `sprite.py`
- If everything is soldered and configured correctly, you should start to see image and characters!


## Basics of modifying the code

### Adding Sprites
The sprite sheets used assume a dimension of 112 × 96 pixels, laid out in 21 tiles.
- Tiles 0 - 6 are for right walk animations
- Tiles 7 - 13 are for left walk animations
- Tile 14 is for the backward facing animation (back to you)
- Tile 15 is for the right-facing standing animation

To create a new sprite, add the new character sheet to /bmps and modify `code.py` to initialize a new sprite (example below):

```python3
witch: Sprite = Sprite(spritesheet_path='/bmps/witch.bmp', id='witch', width=1, height=1, tile_width=16, default_tile=0, tile_height=32, transparency_index=0)
```

Then, add the character to the trick-or-treater list in `code.py`:
```python3
trick_or_treaters: list[Sprite] = [
    witch
]
```
---
### Changing the min and max time between trick or treaters
This portion of the code can be found in `code.py`:
```python3
# Wait time in seconds between trick-or-treaters
MIN_SEC_BETWEEN_TRICK_OR_TREATERS = 3
MAX_SEC_BETWEEN_TRICK_OR_TREATERS = 10
```

---
### Changing the time characters spend waiting at the door
This part of the sequence is randomized to allow some variety with each character. In order to change the time, you can go to `code.py` and look for the function `def run_trick_or_treat_sequence(sprite: Sprite) -> None`. 

Within that function, you will see two variables `wait_for_door` and `at_door`. The random integer range can be changed, or even made to just a standard integer.

```python3
# Random int between 1 and 3
wait_for_door: int = random.randint(1, 3)
# Random int between 3 and 6
at_door: int = random.randint(3, 6)


# Or, just set an integer without randomization
wait_for_door: int = 2
at_door: int = 3
```