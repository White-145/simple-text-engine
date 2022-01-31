from pynput import keyboard
import os
import engine

def translate_keys(func):

    keys_up = {keyboard.Key.up, engine.key('w')}
    keys_down = {keyboard.Key.down, engine.key('s')}
    keys_left = {keyboard.Key.left, engine.key('a')}
    keys_right = {keyboard.Key.right, engine.key('d')}

    def wrapper(entity, key):
        if key in keys_up:
            key = 'up'
        elif key in keys_down:
            key = 'down'
        elif key in keys_left:
            key = 'left'
        elif key in keys_right:
            key = 'right'

        func(entity, key)

    return wrapper

@translate_keys
def move(entity, key):
    if key == 'up':
        entity.y += 1
    elif key == 'down':
        entity.y -= 1

    elif key == 'left':
        entity.x -= 1
    elif key == 'right':
        entity.x += 1

    area.show()

area = engine.Area(width=20, height=20, texture='~', layer=0)

player_1 = engine.Entity(area, texture='@', y=10, x=10, width=3, height=3)
player_2 = engine.Entity(area, texture='%', layer=1, y=5, x=10, width=3, height=3)

wall = engine.Entity(area, texture='/', layer=2, y=2, x=2, width=4, height=4)
platform = engine.Entity(area, texture='\\', layer=-1, y=4, x=4, width=4, height=4)

area.show()

allowed_keys_1 = {
    keyboard.Key.up,
    keyboard.Key.down,
    keyboard.Key.left,
    keyboard.Key.right
}

allowed_keys_2 = {
    engine.key('w'),
    engine.key('s'),
    engine.key('a'),
    engine.key('d')
}

def pressed(key):
    if key in allowed_keys_1:
        move(player_1, key)

    elif key in allowed_keys_2:
        move(player_2, key)

    elif key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_release=pressed) as listener:
    listener.join()