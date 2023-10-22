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

class BackgroundElement:
    def __init__(self, element_path: str, x: int = 0, y: int = 0, transparency_index: int | None = None) -> None:
        self._bitmap_sheet, self._palette = adafruit_imageload.load(element_path, bitmap=displayio.Bitmap, palette=displayio.Palette)
        if transparency_index is not None:
            self._palette.make_transparent(transparency_index)
        self._bitmap = displayio.TileGrid(self._bitmap_sheet, 
                                          pixel_shader=self._palette)
        self._bitmap.x = x
        self._bitmap.y = y
        
        self._displayio_group = displayio.Group()
        self._displayio_group.append(self._bitmap)
        
    def get_group(self) -> displayio.Group:
        return self._displayio_group
    
    def reposition(self, x: int, y: int) -> None:
        self._bitmap.x = x
        self._bitmap.y = y
        