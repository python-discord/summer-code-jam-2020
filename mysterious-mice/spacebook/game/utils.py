import math
import random

# All coordinates are stored as tuples of (x, y)
# x is east-west with east being positive
# y is north-south with north being positive


def new_game():
    """
    Generates a new game, resetting the location of all components and the rover.
    """

    game_data = {
        "initials": "",
        "rover": (0, 0),
        "battery": 100,
        "power_usage": 5,
        "plutonium": (random.randint(0, 10), random.randint(0, 10)),
        "has_plutonium": False,
        "solar_panels": (random.randint(0, 5), random.randint(0, 5)),
        "has_solar_panels": False,
        "dust_storm": (random.randint(0, 10), random.randint(0, 10)),
        "wind": (-1, 0),
        "small_crater": (random.randint(0, 10), random.randint(0, 10)),
        "item_messages": {
            "plutonium": "There is a plume of smoke in the distance.",
            "solar_panels": "There is an object reflecting light in the distance.",
            "dust_storm": "A dust storm billows in the distance.",
            "small_crater": "There is a small crater in the distance.",
        },
        "messages": [
            {"from_rover": False, "message": "Crash Landing!"},
            {"from_rover": False, "message": ""},
            {
                "from_rover": False,
                "message": "You play as a rover that has just had a crash landing on Mars.",
            },
            {
                "from_rover": False,
                "message": "The rover lost its two power sources in the crash.",
            },
            {
                "from_rover": False,
                "message": "Plutonium is the rover's main power source.",
            },
            {
                "from_rover": False,
                "message": "The goal of the game is to retrieve the plutonium before the battery depletes.",
            },
            {
                "from_rover": False,
                "message": "Retrieving the rover's solar panels will allow you to travel more efficiently.",
            },
            {
                "from_rover": False,
                "message": 'Type "help" at any time to review the controls.',
            },
            {"from_rover": False, "message": "Good luck!",},
            {"from_rover": False, "message": ""},
        ],
        "game_over": False,
        "victorious": False,
    }
    print("=============")
    print(game_data["plutonium"])
    print(game_data["solar_panels"])
    print(game_data["dust_storm"])
    print(game_data["small_crater"])
    return game_data


def get_game(request):
    """
    Attempt to retrieve the current game from sessions. If no game is found,
    generate a new game.
    """

    is_cached = "game_data" in request.session
    if not is_cached:
        game_data = new_game()
    else:
        game_data = request.session["game_data"]

    return game_data


def command_help(game_data):
    """
    Provide text commands to control the rover.
    """

    help_messages = [
        {"from_rover": False, "message": "Help:"},
        {"from_rover": False, "message": ""},
        {"from_rover": False, "message": "Movement:"},
        {
            "from_rover": False,
            "message": "You can move by clicking the buttons with the cardinal directions.",
        },
        {
            "from_rover": False,
            "message": "You can also move through text commands. Examples of valid commands:",
        },
        {"from_rover": False, "message": ">> move n",},
        {"from_rover": False, "message": ">> move north",},
        {"from_rover": False, "message": ""},
        {
            "from_rover": False,
            "message": "Look around for hints of where the components might be. Examples of valid commands:",
        },
        {"from_rover": False, "message": ">> look n",},
        {"from_rover": False, "message": ">> look north",},
        {"from_rover": False, "message": ""},
        {
            "from_rover": False,
            "message": 'Type "new game" at any point to start a new game.',
        },
    ]
    game_data["messages"] = game_data["messages"] + help_messages
    return game_data


def command_move(game_data, direction):
    """
    Moves the rover, depletes the battery, and picks up a component if one is found.
    """
    old_position = game_data["rover"]
    success = True

    # Attempt to move the rover
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
        success = False

    # Deplete battery if successfully moved
    if success:
        game_data["battery"] = game_data["battery"] - game_data["power_usage"]
        if game_data["has_solar_panels"]:
            game_data["battery"] = game_data["battery"] + 2

    # Move components with rover
    if game_data["has_solar_panels"]:
        game_data["solar_panels"] = new_position
    if game_data["has_plutonium"]:
        game_data["plutonium"] = new_position

    # Pick up components
    if (
        new_position[0] == game_data["solar_panels"][0]
        and new_position[1] == game_data["solar_panels"][1]
        and not game_data["has_solar_panels"]
    ):
        game_data["has_solar_panels"] = True
        game_data["messages"].append(
            {"from_rover": False, "message": f"You have retrieved the solar panels!"}
        )
        game_data["messages"].append(
            {
                "from_rover": False,
                "message": f"It will take less energy to traverse the terrain of Mars now!",
            }
        )
    if (
        new_position[0] == game_data["plutonium"][0]
        and new_position[1] == game_data["plutonium"][1]
        and not game_data["has_plutonium"]
    ):
        game_data["has_plutonium"] = True
        game_data["messages"].append(
            {"from_rover": False, "message": f"You have retrieved the plutonium!"}
        )

    game_data["messages"].append(
        {"from_rover": False, "message": f"Your new location is {new_position}"}
    )
    game_data["rover"] = new_position
    return game_data


def command_look(game_data, direction):
    """
    checks direction for parts and obsticals
    """
    new_message = []

    # list of items on the map
    check_list = [
        "plutonium",
        "solar_panels",
        "dust_storm",
        "small_crater",
    ]

    # rover position
    rover = game_data["rover"]

    # check the angle of each item
    for item in check_list:
        x_dis = abs(rover[0] - game_data[item][0])
        y_dis = abs(rover[1] - game_data[item][1])

        if x_dis == 0:
            angle = 0
        else:
            angle = math.tan(y_dis / x_dis)

        # if the angle is 0 check if the camera is facing the right direction
        d = ""  # the direction that the item is in
        if angle == 0:
            if rover[0] > game_data[item][0]:
                d = "w"
            elif rover[0] < game_data[item][0]:
                d = "e"
            elif rover[1] > game_data[item][1]:
                d = "s"
            elif rover[1] < game_data[item][1]:
                d = "n"

        # if the item is in the right direction update the messages
        if direction == d:
            new_message = [
                {"from_rover": False, "message": game_data["item_messages"][item]}
            ]

    if new_message == []:
        new_message = [
            {"from_rover": False, "message": "Red sand and rocks and more rocks."}
        ]

    game_data["messages"] = game_data["messages"] + new_message
    return game_data


def parse_command(request, game_data, command):
    """
    Parses the user's input and runs the applicable command.
    Returns game_data to the view to be displayed.
    """
    game_data["messages"].append({"from_rover": True, "message": command})
    command = command.replace(" ", "").lower()

    if not game_data["game_over"]:
        if command.startswith("move"):
            game_data = command_move(game_data, command[4:])
        elif command.startswith("look"):
            game_data = command_look(game_data, command[4:])
        elif command == "help":
            game_data = command_help(game_data)
        else:
            game_data["messages"].append(
                {"from_rover": False, "message": f"Command not understood: {command}"}
            )
    if command == "newgame":
        game_data = new_game()
        request.session["game_data"] = new_game()

    # Win if plutonium was retrieved
    if game_data["has_plutonium"] and not game_data["victorious"]:
        game_data["victorious"] = True
        game_data["game_over"] = True
        game_data["messages"].append({"from_rover": False, "message": ""})
        game_data["messages"].append(
            {"from_rover": False, "message": "CONGRATULATIONS!"}
        )
        game_data["messages"].append(
            {
                "from_rover": False,
                "message": "Your rover was able to reconnect its power supply!",
            }
        )

    # Lose if battery reaches 0, unless plutonium was found this move
    if (
        game_data["battery"] <= 0
        and not game_data["game_over"]
        and not game_data["victorious"]
    ):
        game_data["battery"] = 0
        game_data["messages"].append({"from_rover": False, "message": ""})
        game_data["messages"].append({"from_rover": False, "message": "GAME OVER!"})
        game_data["game_over"] = True

    # Direct player to start new game if
    if game_data["game_over"]:
        game_data["messages"].append(
            {"from_rover": False, "message": 'Type "new game" to start a new game.'}
        )

    request.session["game_data"] = game_data
    return game_data
