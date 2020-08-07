import re


def new_game():
    # coordinates tuples of (x, y)
    # x is east-west with east being positive
    # y is north-south with north being positive

    game_data = {
        "rover": (0, 0),
        "plutonium": (7, 5),
        "solar_panels": (-3, 2),
        "wind": (-1, 0),
        "small_crater": (-4, -3),
        "messages": ["Welcome to Crash Landing!"],
    }
    return game_data


def get_game(request):
    is_cached = "game_data" in request.session
    if not is_cached:
        game_data = new_game()
    else:
        game_data = request.session["game_data"]

    return game_data


def command_move(game_data, direction):
    old_position = game_data["rover"]
    if direction in ["n", "north"]:
        new_position = (old_position[0], old_position[1] + 1)
    elif direction in ["e", "east"]:
        new_position = (old_position[0] + 1, old_position[1])
    elif direction in ["s", "south"]:
        new_position = (old_position[0], old_position[1] - 1)
    elif direction in ["w", "west"]:
        new_position = (old_position[0] - 1, old_position[1])
    else:
        new_position = old_position
    game_data["messages"].append(f"Your new location is {new_position}")
    game_data["rover"] = new_position
    return game_data

def command_look(game_data, direction):
    rover = game_data.get('rover')
    plutonium = game_data.get('plutonium')
    solar_panels = game_data.get('solar_panels')
    plutonium_message = "There is a plume of smoke in the distance."
    panel_message = "There is a plume of smoke in the distance."
    if direction in ["n", "north"]:
        if rover[0] == plutonium[0] and rover[1] < plutonium[1]: #if the rover is inline wih plutonium and plutonium is north of rover
            new_message = plutonium_message
        if rover[0] == solar_panels[0] and rover[1] < solar_panels[1]:#if the rover is inline wih solar panels and solar panels is north of rover
            new_message = panel_message
    elif direction in ["s", "south"]:
        if rover[0] == plutonium[0] and rover[1] > plutonium[1]:
            new_message = plutonium_message
        if rover[0] == solar_panels[0] and rover[1] > solar_panels[1]:
            new_message = panel_message
    elif direction in ["w", "west"]:
        if rover[1] == plutonium[1] and rover[1] < plutonium[1]:
            new_message = plutonium_message
        if rover[1] == solar_panels[1] and rover[1] < solar_panels[1]:
            new_message = panel_message
    elif direction in ["e", "east"]:
        if rover[1] == plutonium[1] and rover[1] > plutonium[1]:
            new_message = plutonium_message
        if rover[1] == solar_panels[1] and rover[1] > solar_panels[1]:
            new_message = panel_message
    game_data.messages.append(new_message)
    return game_data


def parse_command(request, game_data, command):
    game_data["messages"].append(command)
    if command != "" and command != None:
        command = command.replace(" ", "").lower()
        if command.startswith("move"):
            game_data = command_move(game_data, command[4:])
        elif command.startswith("look"):
            game_data = command_look(game_data, command[4:])
        elif command == "help":
            pass
        elif command == "newgame":
            game_data = new_game()
            request.session["game_data"] = new_game()
        else:
            game_data["messages"].append(f"Command not understood: {command}")
    request.session["game_data"] = game_data
    return game_data
