from pynput import keyboard
import os
import typing

key = lambda key: keyboard.KeyCode.from_char(key)  # function to get text key

# get argument
def set_arg(arg, args, rtype, default):
    argument = args.pop(arg, None)
    if argument is not None:
        if not isinstance(argument, rtype):
            raise TypeError(f'{arg} must be None or a {rtype}')
    else:
        return default
    return argument

# string to texture
def fix_texture(texture):
    if texture == '':
        return '_'
    elif texture[0] in {'\a', '\b', '\f', '\n', '\r', '\t', '\v'}:
        return '_'
    else:
        return texture[0]

def update_next_id(cls, entries):
    def check(check_id):
        for entry in entries:
            if entry.id == check_id:
                break
        else:
            return check_id
        return check(check_id + 1)

    cls.next_id = check(cls.next_id + 1)

class Area:
    areas = []  # list of all areas
    next_id = 0

    def __init__(self, **kwargs):
        # throw error if extra args given
        if list(filter(lambda x: x not in {"width", "height", "layer", "texture", "id"}, kwargs)):
            raise TypeError("invalid keyword arguments to Area()")

        clamp = lambda x, l: max(1, min(x, l))

        # set variables
        self.width = clamp(set_arg("width", kwargs, int, 5), 120)
        self.height = clamp(set_arg("height", kwargs, int, 5), 29)
        self.layer = set_arg('layer', kwargs, int, None)
        self.texture = fix_texture(set_arg('texture', kwargs, str, '_'))

        area_id = set_arg('id', kwargs, typing.Union[int, str], None)
        if area_id == None:
            area_id = self.__class__.next_id
            update_next_id(self.__class__, self.__class__.areas)
        else:
            if isinstance(area_id, int):
                if area_id == self.__class__.next_id:
                    update_next_id(self.__class__, self.__class__.areas)
            for area in self.__class__.areas:
                if area.id == area_id:
                    raise ValueError("Area with given id already exists")

        self.id = area_id

        self.entities = []  # all entities on area
        self.__class__.areas.append(self)  # add area to all areas

    def show(self):
        os.system('cls')  # clear terminal (windows)

        area_full = [[self.texture for _ in range(self.width)] for _ in range(self.height)]
        area_layers = [[self.layer for _ in range(self.width)] for _ in range(self.height)]

        for entity in self.entities:
            for i in entity.covers:
                if area_layers[i[0]][i[1]] != None:
                    if area_layers[i[0]][i[1]] > entity.layer:
                        continue

                area_full[i[0]][i[1]] = entity.texture
                area_layers[i[0]][i[1]] = entity.layer

        print('\n'.join([''.join(area_full[self.height - x - 1]) for x in range(self.height)]))

    def __str__(self):
        return f'area {self.texture} ID {self.id} with {len(self.entities)} entities'

class Entity:
    entities = []  # list of all entities
    next_id = 0

    def __init__(self, area, **kwargs):
        # throw error if area not given
        if not isinstance(area, Area):
            raise TypeError("area must be an instance of Area class")

        # throw error if extra args given
        if list(filter(lambda x: x not in {"texture", "layer", 'y', 'x', "width", "height", "id"}, kwargs)):
            raise TypeError("invalid keyword arguments to Entity()")

        limit = lambda x: 1 if x < 1 else x

        # set variables
        self.area = area
        
        self.texture = fix_texture(set_arg("texture", kwargs, str, '#'))
        self.layer = set_arg("layer", kwargs, int, 0)
        self.y = set_arg('y', kwargs, int, 0)
        self.x = set_arg('x', kwargs, int, 0)
        self.width = limit(set_arg('width', kwargs, int, 1))
        self.height = limit(set_arg('height', kwargs, int, 1))

        entity_id = set_arg('id', kwargs, typing.Union[int, str], None)
        if entity_id == None:
            entity_id = self.__class__.next_id
            update_next_id(self.__class__, self.__class__.entities)
        else:
            if isinstance(entity_id, int):
                if entity_id == self.__class__.next_id:
                    update_next_id(self.__class__, self.__class__.entities)
            for entity in self.__class__.entities:
                if entity.id == entity_id:
                    raise ValueError("Entity with given id already exists")

        self.id = entity_id

        area.entities.append(self)  # add entity to area
        self.__class__.entities.append(self)  # add entity to all entities

    # get all covers
    @property
    def covers(self):
        is_on_area = lambda loc: 0 <= loc[0] < self.area.height and 0 <= loc[1] < self.area.width

        all_covers = [(self.y + y_offset, self.x + x_offset) for y_offset in range(self.height) for x_offset in range(self.width)]
        covers = tuple(filter(is_on_area, all_covers))

        return covers

    def move_to_area(self, area, **kwargs):
        # throw error if area not given
        if not isinstance(area, Area):
            raise TypeError("area must be an instance of Area class")

        # throw error if extra args given
        if list(filter(lambda x: x not in {'y', 'x'}, kwargs)):
            raise TypeError("invalid keyword arguments to Entity().move_to_area()")

        # update area
        self.area.entities.pop(self.area.entities.index(self))
        self.area = area
        area.entities.append(self)

        self.y = set_arg('y', kwargs, int, self.y)
        self.x = set_arg('x', kwargs, int, self.x)

    def __str__(self):
        return f'entity {self.texture} ID {self.id}'
