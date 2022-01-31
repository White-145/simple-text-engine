# simple text engine
 Engine for simple text "games" in the terminal

 I use this project to test my OOP skills
 
 to use you need to install pynput:
 
 `pip install pynput`
 
 Add area:
 
 `area = engine.Area(width: int=5, height: int=5, texture: str='_', layer: [None, int]=None)`
 Arguments:
 * width - area width (Default 5)
 * height - area height (Default 5)
 * texture - area back texture symbol (Default '_')
 * layer - area layer (Default None)

 An entity is an object with its own texture located on the area.
 Add entity:
 
 `entity = engine.Entity(area, texture: str='#', layer: int=0, y: int=0, x: int=0, width: int=1, height: int=1)`
 Arguments:
 * area - the area on which the entity is located
 * texture - entity texture symbol (Default '#')
 * layer - entity layer (Default 0)
 * y - the y coordinate the player is on (Default 0)
 * x - the x coordinate the player is on (Default 0)
 * width - entity width (Default 1)
 * height - entity height (Default 1)

A player is an entiti that can be controlled by simple commands (most likely to be removed soon due to easy replacement).
Player requires the same arguments as the entity

