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

import adafruit_imageload
import displayio
import time

class Sprite:
    def __init__(self, spritesheet_path: str, id: str,
                 width: int, height: int, tile_width: int, tile_height: int, 
                 default_tile: int = 0, x: int = -16, y: int = 0, transparency_index: int | None = None) -> None:
        self._spritesheet, self._palette = adafruit_imageload.load(spritesheet_path, bitmap=displayio.Bitmap, palette=displayio.Palette)
        if transparency_index is not None:
            self._palette.make_transparent(transparency_index)
        self._sprite = displayio.TileGrid(self._spritesheet, 
                                          pixel_shader=self._palette,
                                 width=width, height=height, tile_width=tile_width, tile_height=tile_height, default_tile=default_tile)
        self._id = id
        self._sprite.x = x
        self._sprite.y = y

        self._displayio_group = displayio.Group()
        self._displayio_group.append(self._sprite)

        self._CONSTANT_TIME: int = 0
        self._GRID_BOX: int = 0
    
    def get_group(self) -> displayio.Group:
        return self._displayio_group
    
    def get_id(self) -> str:
        return self._id
    
    def walk(self, x_start: int, x_end: int) -> None:
        self._sprite.x = x_start
        
        # Default to left->right
        direction: str = 'r'
        sprite_animation_box_start: int = 0
        sprite_animation_box_end: int = 6
        
        # Set right->left
        if self._sprite.x > x_end:
            direction: str = 'l'
            sprite_animation_box_start = 7
            sprite_animation_box_end = 13
        
        while self._sprite.x != x_end:
            time.sleep(0.17)
            print(f"self._sprite.x: {self._sprite.x}")
            self._sprite[0] = self._GRID_BOX
            print(f"self._GRID_BOX: {self._GRID_BOX}")
            self._GRID_BOX += 1
            
            if self._GRID_BOX > sprite_animation_box_end:
                self._GRID_BOX = sprite_animation_box_start
                
            if direction is 'r':
                self._sprite.x += 2
                
                if self._sprite.x > x_end:
                    self._sprite.x = x_end
                    self.stop()
                    return
                
            else:
                self._sprite.x -= 2
                
                if self._sprite.x < x_end:
                    self._sprite.x = x_end
                    self.stop()
                    return    

    def stop(self, seconds_to_wait: float = 0.00) -> None:
        self._sprite[0] = 14
        time.sleep(seconds_to_wait)
        
    def walk_and_stop(self, x_start: int, x_end: int, seconds_to_wait: float = 0.00) -> None:
        self.walk(x_start=x_start, x_end=x_end)
        self.stop(seconds_to_wait=seconds_to_wait)
        
        