from pynput import keyboard
import os
import engine

area = engine.Area(width=20, height=20, texture='~', layer=1)

player_1 = engine.Player(area, texture='@', y=10, x=10, width=3, height=3)
player_2 = engine.Player(area, texture='%', layer=1, y=5, x=10, width=3, height=3)

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
        player_1.move(key)

    elif key in allowed_keys_2:
        player_2.move(key)

    elif key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_release=pressed) as listener:
    listener.join()