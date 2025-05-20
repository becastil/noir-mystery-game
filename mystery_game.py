# Define the Room class
class Room:
    def __init__(self, name, description, contents, exits):
        self.name = name
        self.description = description
        self.contents = contents  # List of items or clues
        self.exits = exits        # Dict: direction -> room name
        self.visited = False      # Track if we have been here before

# Create room instances
foyer = Room(
    "Grand Foyer",
    """
    Rain drums on the tall window. The front doors are bolted. 
    A grand staircase looms overhead. Footprints muddy the marble floor.
    """,
    contents=["footprints", "dropped locket"],
    exits={"north": "Study", "east": "Library"}
)

study = Room(
    "Study",
    """
    A green desk lamp casts sickly light over the slumped figure of Victor Holloway. 
    Papers scatter the floor. A heavy iron safe sits behind the desk.
    """,
    contents=["body", "safe", "papers"],
    exits={"south": "Grand Foyer"}
)

library = Room(
    "Library",
    """
    Books tower above. A fire smolders low in the hearth. 
    You notice a book with a torn spine. Something falls off.
    """,
    contents=["cipher book", "fireplace"],
    exits={"west": "Grand Foyer"}
)

# Create the room map
rooms = {
    "Grand Foyer": foyer,
    "Study": study,
    "Library": library
}

# Set the player's starting location
current_room = "Grand Foyer"

# Initialize the detective's inventory
inventory = []


# Function to describe the current room
def enter_room(room_name):
    room = rooms[room_name]
    if not room.visited:
        print(f"\nYou enter the {room.name.strip()}.")
        print(room.description.strip())
        room.visited = True
    else:
        print(f"\nYou're back in the {room.name.strip()}.")
    print("Contents:", ", ".join(room.contents))
    print("Exits:", ", ".join(room.exits.keys()))

# Start the main game loop
while True:
    command = input("\n> ").strip().lower()

    if command.startswith("go "):
        direction = command[3:]
        current = rooms[current_room]
        if direction in current.exits:
            current_room = current.exits[direction]
            enter_room(current_room)
        else:
            print("You can't go that way.")

    elif command == "look":
        enter_room(current_room)

    elif command in ["quit", "exit"]:
        print("You tip your hat, turn from the shadows, and step into the rain. Case closed.")
        break

    elif command.startswith("take "):
        item = command[5:] # Get the item name after "take "
        current = rooms[current_room]
        if item in current.contents:
            inventory.append(item)
            current.contents.remove(item)
            print(f"You slip the {item} into your coat pocket.")
        else: 
            print(f"No sign of {item}' in this room.")

    elif command == "inventory":
        if inventory:
            print("Clues in your pocket:", ", ".join(inventory))
        else:
            print("Your pockets are empty. For now.")


    else:
        print("That doesn't make sense in this twisted place...")


