from pynput import keyboard
from typing import Union
import os

key = lambda key: keyboard.KeyCode.from_char(key)

class Area:
    areas = []

    def __init__(self, width: int=5, height: int=5, texture: str='_', layer: Union[None, int]=None):
        if texture == '':
            self.texture = '_'
        else:
            self.texture = texture[0]

        if width < 1:
            width = 1
        elif width > 120:
            width = 120

        if height < 1:
            height = 1
        elif height > 29:
            height = 29

        self.width = width
        self.height = height
        self.layer = layer

        self.entities = []

        self.__class__.areas.append(self)

    def show(self):
        def get_covers(entity):
            all_covers = tuple([tuple([entity.y + y_offset, entity.x + x_offset]) for y_offset in range(entity.height) for x_offset in range(entity.width)])
            covers = []
            for cover in all_covers:
                if 0 <= cover[0] < entity.area.height and 0 <= cover[1] < entity.area.width:
                    covers.append(cover)

            return tuple(covers)

        os.system('cls')

        area_full = [[self.texture for _ in range(self.width)] for _ in range(self.height)]
        area_layers = [[self.layer for _ in range(self.width)] for _ in range(self.height)]

        for entity in self.entities:
            for i in get_covers(entity):
                if area_layers[i[0]][i[1]] != None:
                    if area_layers[i[0]][i[1]] > entity.layer:
                        continue

                area_full[i[0]][i[1]] = entity.texture
                area_layers[i[0]][i[1]] = entity.layer

        for line in [''.join(area_full[self.height - x - 1]) for x in range(self.height)]:
            print(line)

    def __str__(self):
        return f'area {self.texture} ID {self.__class__.areas.index(self)} with {len(self.entities)} entities'

class Entity:
    entities = []

    def __init__(self, area, texture: str='#', layer: int=0, y: int=0, x: int=0, width: int=1, height: int=1):
        if texture == '':
            self.texture = '#'
        else:
            self.texture = texture[0]

        self.y = y
        self.x = x

        self.area = area
        self.layer = layer

        self.width = width
        self.height = height

        area.entities.append(self)
        self.__class__.entities.append(self)

    def __str__(self):
        return f'entity {self.texture} ID {self.__class__.entities.index(self)}'
