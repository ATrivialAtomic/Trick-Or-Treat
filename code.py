# MIT License
# Copyright (c) 2023, Stefan Hueneke

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import displayio
import rgbmatrix
import framebufferio
import random
import time
import display_factory
from sprite_factory import SpriteFactory
from sprite import Sprite
from background_element import BackgroundElement

# Wait time in seconds between trick-or-treaters
MIN_SEC_BETWEEN_TRICK_OR_TREATERS = 3
MAX_SEC_BETWEEN_TRICK_OR_TREATERS = 10

# Configure Display
displayio.release_displays()
matrix: rgbmatrix.RGBMatrix = display_factory.get_matrix('RP2040')
display: framebufferio.FramebufferDisplay = framebufferio.FramebufferDisplay(matrix, auto_refresh=True)

# Create Group
group = displayio.Group()

background: BackgroundElement = BackgroundElement(element_path='/bmps/background.bmp')
leah: BackgroundElement = BackgroundElement(element_path='/bmps/leah_with_candy.bmp', transparency_index=0)
door: BackgroundElement = BackgroundElement(element_path='/bmps/door.bmp', transparency_index=0)
grass: BackgroundElement = BackgroundElement(element_path='/bmps/grass.bmp', x=0, y=2, transparency_index=0)
knock: BackgroundElement = BackgroundElement(element_path='/bmps/knock.bmp', x=-3, y=0, transparency_index=0)

cat: Sprite = Sprite(spritesheet_path='/bmps/cat.bmp', id='cat', width=1, height=1, tile_width=16, default_tile=0, tile_height=32, transparency_index=0)
knight: Sprite = Sprite(spritesheet_path='/bmps/knight.bmp', id='knight', width=1, height=1, tile_width=16, default_tile=0, tile_height=32, transparency_index=0)
pumpkin: Sprite = Sprite(spritesheet_path='/bmps/pumpkin.bmp', id='pumpkin', width=1, height=1, tile_width=16, default_tile=0, tile_height=32, transparency_index=0)
skeleton: Sprite = Sprite(spritesheet_path='/bmps/skeleton.bmp', id='skeleton', width=1, height=1, tile_width=16, default_tile=0, tile_height=32, transparency_index=0)
vampire: Sprite = Sprite(spritesheet_path='/bmps/vampire.bmp', id='vampire', width=1, height=1, tile_width=16, default_tile=0, tile_height=32, transparency_index=0)
witch: Sprite = Sprite(spritesheet_path='/bmps/witch.bmp', id='witch', width=1, height=1, tile_width=16, default_tile=0, tile_height=32, transparency_index=0)

background_elements: list[BackgroundElement] = [
    background,
    leah,
    door,
    knock
]

trick_or_treaters: list[Sprite] = [
    cat,
    knight,
    pumpkin,
    skeleton,
    vampire,
    witch
]

foreground_elements: list[BackgroundElement] = [
    grass
]

for element in background_elements:
    group.append(element.get_group())
    
for character in trick_or_treaters:
    group.append(character.get_group())
    
for element in foreground_elements:
    group.append(element.get_group())

# Create Sprite Factory
sprite_factory = SpriteFactory(trick_or_treaters)

# Show all layers
display.show(group)

def knock_at_door() -> None:
    for i in range(0,3):
        x: int = random.randint(37, 45)
        y: int = random.randint(10, 14)
        knock.reposition(x, y)
        time.sleep(0.3)
    knock.reposition(-3, 0)
    time.sleep(1.5)
    
def open_door() -> None:
    door.reposition(0, 32)
    
def close_door() -> None:
    door.reposition(0, 0)

def run_trick_or_treat_sequence(sprite: Sprite) -> None:
    walk_direction = random.choice(['left', 'right'])
    wait_for_door: int = random.randint(1, 3)
    at_door: int = random.randint(3, 6)
    print(f"direction = {walk_direction}")
    if walk_direction is 'left':
        sprite.walk_and_stop(80, 42, wait_for_door)
        knock_at_door()
        open_door()
        sprite.stop(at_door)
        close_door()
        time.sleep(1)
        sprite.walk(42, -16)
        
    elif walk_direction is 'right':
        sprite.walk_and_stop(-16, 24, wait_for_door)
        knock_at_door()
        open_door()
        sprite.stop(at_door)
        close_door()
        time.sleep(1)
        sprite.walk(24, 80)

# Wait before starting loop
time.sleep(2)

while True:
    sprite: Sprite = sprite_factory.get_random_sprite()
    run_trick_or_treat_sequence(sprite)
    wait_between_trick_or_treaters = random.randint(
        MIN_SEC_BETWEEN_TRICK_OR_TREATERS, 
        MAX_SEC_BETWEEN_TRICK_OR_TREATERS
        )
    time.sleep(wait_between_trick_or_treaters)
    