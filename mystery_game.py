class Room: 
    def __init__(self, name, description, contents, exits):
        self.name = name
        self.description = description
        self.contents = contents # List of items or clues
        self.exits = exits # Dict: direction -> room name
        self.visited = False # Track if we have been here before

foyer = Room(
    """
    
    Grand Foyer
    
    """,
    """
    
    "Rain drums on the tall window. The front doors are bolted. A grand staircase looms overhead. Footprints muddy the marble floor."
    
    """,
    contents = ["footprints", "dropped locket"],
    exits = {"north": "Study", "east": "Library"}
)

study = Room(
    """
    Study

    """, 
    """
    
    "A green desk lamp casts sickly light over the slumped figure of Victor Holloway. Papers scatter the floor. A heavy iron safe sits behind the desk."
    
    """,
    contents = ["body", "safe", "papers"],
    exits = {"south": "Grand Foyer"}
)

library = Room(
    """
    
    Library
    
    """,
    """
    
    Books tower above. A fire smolders low in the hearth. You notice a book with a torn spine. Something falls off.
    
    """,
    contents = ["cipher book", "fireplace"],
    exits = {"west": "Grand Foyer"}
)

        
