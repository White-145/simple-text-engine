from pynput import keyboard
import os

key = lambda key: keyboard.KeyCode.from_char(key)


class Area:
    areas = []

    def __init__(self, width: int=5, height: int=5, texture: str='_'):
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
        self.entities = []

        self.__class__.areas.append(self)

    def show(self):
        os.system('cls')

        area_full = [[self.texture for _ in range(self.width)] for _ in range(self.height)]
        area_layers = [[None for _ in range(self.width)] for _ in range(self.height)]

        for entity in self.entities:
            for i in entity.get_covers():
                if area_layers[i[0]][i[1]] != None:
                    if area_layers[i[0]][i[1]] > entity.layer:
                        continue

                area_full[i[0]][i[1]] = entity.texture
                area_layers[i[0]][i[1]] = entity.layer

        for line in [''.join(area_full[self.height - x - 1]) for x in range(self.height)]:
            print(line)

        print(f'\r{self}', end='')

    def __str__(self):
        return f'area ID {self.__class__.areas.index(self)}'

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

    def get_covers(self):

        def get_covers_simple(self):
            all_covers = tuple([tuple([self.y + y_offset, self.x + x_offset]) for y_offset in range(self.height) for x_offset in range(self.width)])
            covers = []
            for cover in all_covers:
                if 0 <= cover[0] < self.area.height and 0 <= cover[1] < self.area.width:
                    covers.append(cover)

            return tuple(covers)

        # def get_covers_complex(self):
        #     area_full = [['_' for _ in range(self.width)] for _ in range(self.height)]
        #     area_layers = [[None for _ in range(self.width)] for _ in range(self.height)]

        #     for entity in self.entities:
        #         for i in entity.get_covers_area():
        #             if area_layers[i[0]][i[1]] != None:
        #                 if area_layers[i[0]][i[1]] > entity.layer:
        #                     continue

        #             area_full[i[0]][i[1]] = entity.texture
        #             area_layers[i[0]][i[1]] = entity.layer

        #     return

        return get_covers_simple(self)

    def __str__(self):
        return f'entity {self.texture} ID {self.__class__.entities.index(self)}'

class Player(Entity):

    def translate_keys(func):

        keys_up = {keyboard.Key.up, key('w')}
        keys_down = {keyboard.Key.down, key('s')}
        keys_left = {keyboard.Key.left, key('a')}
        keys_right = {keyboard.Key.right, key('d')}

        def wrapper(self, key):
            if key in keys_up:
                key = 'up'
            elif key in keys_down:
                key = 'down'
            elif key in keys_left:
                key = 'left'
            elif key in keys_right:
                key = 'right'

            func(self, key)

        return wrapper

    @translate_keys
    def move(self, key):
        if key == 'up':
            self.y += 1
        elif key == 'down':
            self.y -= 1

        elif key == 'left':
            self.x -= 1
        elif key == 'right':
            self.x += 1

        self.area.show()
