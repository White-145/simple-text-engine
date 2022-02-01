from pynput import keyboard
import os
import main

# Functions used to move player entities
def translate_keys(func):
    keys_up = {keyboard.Key.up, main.key('w')}
    keys_down = {keyboard.Key.down, main.key('s')}
    keys_left = {keyboard.Key.left, main.key('a')}
    keys_right = {keyboard.Key.right, main.key('d')}

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
    print(f'\r{area}', end='')

# Setup area
area = main.Area(width=20, height=20, texture='-', layer=0)

# Create entities
player_1 = main.Entity(area, texture='@', y=10, x=10, width=3, height=2)
player_2 = main.Entity(area, texture='%', layer=1, y=5, x=10, width=3, height=3)

wall = main.Entity(area, texture='/', layer=2, y=2, x=2, width=4, height=4)
platform = main.Entity(area, texture='\\', layer=-1, y=4, x=4, width=4, height=4)  # This entity will be hidden due of highter area layer

# Show area and area info
area.show()
print(f'\r{area}', end='')

# Move players
keys_1 = {
    keyboard.Key.up,
    keyboard.Key.down,
    keyboard.Key.left,
    keyboard.Key.right
}

keys_2 = {
    main.key('w'),
    main.key('s'),
    main.key('a'),
    main.key('d')
}

def pressed(key):
    if key in keys_1:
        move(player_1, key)

    elif key in keys_2:
        move(player_2, key)

    elif key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_release=pressed) as listener:
    listener.join()