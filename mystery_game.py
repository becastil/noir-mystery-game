class Room: 
    def __init__(self, name, description, contents, exits):
        self.name = name
        self.description = description
        self.contents = contents # List of items or clues
        self.exits = exits # Dict: direction -> room name
        self.visited = False

        
