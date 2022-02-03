# About
 Engine for simple text "games" in the terminal

 I use this project to test my OOP skills
 
 to use you need to install pynput:
 
 `pip install pynput`
 
 # Area
 `class Area(width: int=5, height: int=5, texture: str='_', layer: int=None, id: [int, str]=0)`
 
 Arguments:
 * width - area width (Default 5)
 * height - area height (Default 5)
 * texture - area back texture symbol (Default '_')
 * layer - area layer (Default None)
 * id - area id (Default next unassigned)

 example:
 `area = Area(width=10, height=10, texture='-')`
 
 Show area:
 `area.show()` or `show(area)`

 # Entity
 An entity is an object with its own texture located on the area.
 
 `class Entity(area, texture: str='#', layer: int=0, y: int=0, x: int=0, width: int=1, height: int=1, id: [int, str]=0)`
 
 Arguments:
 * area - the area on which the entity is located
 * texture - entity texture symbol (Default '#')
 * layer - entity layer (Default 0)
 * y - the y coordinate the player is on (Default 0)
 * x - the x coordinate the player is on (Default 0)
 * width - entity width (Default 1)
 * height - entity height (Default 1)
 * id - entity id (Default next unassigned)
 
 example:
 `entity = entity(area, texture='@', y=2, x=2)`
 
 Methods:
 `def move_to_area(area)`
 
 Arguments:
 * area - area for move entity to

 example:
 `entity.move_to_area(area)`

