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

from sprite import Sprite
import random

class SpriteFactory:
    def __init__(self, sprites: list = None):
        if sprites is None:
            self._sprites: list = []
        else:
            self._sprites: list = sprites
            
        self._previous_sprite: Sprite = None
            
    def add_sprite(self, sprite: Sprite) -> None:
        self._sprites.append(sprite)
    
    def get_random_sprite(self) -> Sprite:
        sprite: Sprite = random.choice(self._sprites)
        if self._previous_sprite is not None and sprite.get_id() is self._previous_sprite.get_id():
            self.get_random_sprite()
        self._previous_sprite = sprite
        return sprite