import math
import random
from .models import HighScore

# All coordinates are stored as tuples of (x, y)
# x is east-west with east being positive
# y is north-south with north being positive


MARS_URL = (
    "https://api.nasa.gov/insight_weather/?api_key=DEMO_KEY&feedtype=json&ver=1.0"
)


def get_current_weather(request):
    """
    If user reloads the page, used cached data instead of making call to API again.
    """
    is_cached = "weather_data" in request.session

    if not is_cached:
        response = requests.get(MARS_URL)
        request.session["weather_data"] = response.json()

    weather_data = request.session["weather_data"]

    current_sol = weather_data["sol_keys"][-1]

    context = dict.fromkeys(["AT", "PRE", "HWS"])

    for measurement in context.keys():
        if weather_data["validity_checks"][current_sol][measurement]["valid"]:
            context[measurement] = weather_data[current_sol][measurement]

    context["season"] = weather_data[current_sol]["Season"]

    return context


def new_game(request):
    """
    Generates a new game, resetting the location of all components and the rover.
    """

    game_data = {
        "initials": "",
        "input_len": 16,
        "getting_score": False,
        "score": 0,
        "rover": (0, 0),
        "battery": 100,
        "power_usage": 5,
        "is_stuck": False,
        "plutonium": (7, 5),
        "has_plutonium": False,
        "solar_panels": (-3, 2),
        "has_solar_panels": False,
        "wind": (-1, 0),
        "temperature": get_current_weather(request)["AT"]["av"],
        "obstacles": {"dust_storm": (0, 2), "small_crater": (-4, -3),},
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

    randomize_positions(game_data)
    return game_data


def randomize_positions(game_data):
    """
    Randomizes the loacation of parts and obstacles
    """

    game_data.update(
        {
            "plutonium": (random.randint(-8, 8), random.randint(-8, 8)),
            "solar_panels": (random.randint(-3, 3), random.randint(-3, 3)),
        }
    )
    game_data["obstacles"].update(
        {
            "dust_storm": (random.randint(-5, 5), random.randint(-5, 5)),
            "small_crater": (random.randint(-3, 3), random.randint(-3, 3)),
        }
    )


def get_game(request):
    """
    Attempt to retrieve the current game from sessions. If no game is found,
    generate a new game.
    """

    is_cached = "game_data" in request.session
    if not is_cached:
        game_data = new_game(request)
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
            "message": "Be careful of your surroundings, Mars is a hazardous planet.",
        },
        {
            "from_rover": False,
            "message": "Your score is based on your battery life multiplied by the temperature on Mars.",
        },
        {
            "from_rover": False,
            "message": "If you want a higher score play on a colder day.",
        },
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

    # check if current position contains an obstacle
    for obstacle in game_data["obstacles"]:
        if (
            game_data["obstacles"][obstacle][0] == old_position[0]
            and game_data["obstacles"][obstacle][1] == old_position[1]
        ):
            # if the obstacle is a dust stom there is a 50% chace power comsumption will increase
            if obstacle == "dust_storm":
                if random.randint(1, 10) > 5:
                    game_data["power_usage"] += 5
                    game_data["messages"].append(
                        {
                            "from_rover": False,
                            "message": f"Sand has gotten stuck in the treads. Moving becomes less efficient.",
                        }
                    )
            # if the obstacle is a small crater there is a 50% chance to get stuck
            if obstacle == "small_crater":

                # In not already stuck there is a chance to become stuck
                if not game_data["is_stuck"]:
                    if random.randint(1, 10) > 5:
                        game_data["is_stuck"] = True
                        game_data["messages"].append(
                            {"from_rover": False, "message": f"You are stuck!",}
                        )

                # If you are stuck there is a chance to become unstuck
                else:
                    if random.randint(1, 10) > 5:
                        game_data["is_stuck"] = False
                        game_data["messages"].append(
                            {
                                "from_rover": False,
                                "message": f"You are no longer stuck.",
                            }
                        )
                    else:
                        game_data["messages"].append(
                            {"from_rover": False, "message": f"You are stuck!",}
                        )

    # Attempt to move the rover
    if not game_data["is_stuck"]:
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
    else:
        success = False

    # If stuck depleat the battery
    if game_data["is_stuck"]:
        game_data["battery"] = game_data["battery"] - game_data["power_usage"]
        if game_data["has_solar_panels"]:
            game_data["battery"] = game_data["battery"] + 2

    # If successfully moved depleat battery, handel components, and update position
    if success:

        # depleat battery
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
                {
                    "from_rover": False,
                    "message": f"You have retrieved the solar panels!",
                }
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
    checks direction for parts and obstacles
    """
    new_message = []

    # list of items on the map
    check_list = [
        "dust_storm",
        "plutonium",
        "solar_panels",
        "small_crater",
    ]
    obstacles_list = [
        "dust_storm",
        "small_crater",
    ]

    # rover position
    rover = game_data["rover"]

    # check the angle of each item
    for item in check_list:
        if item in obstacles_list:
            x_dis = abs(rover[0] - game_data["obstacles"][item][0])
            y_dis = abs(rover[1] - game_data["obstacles"][item][1])
            item_pos = game_data["obstacles"][item]
        else:
            x_dis = abs(rover[0] - game_data[item][0])
            y_dis = abs(rover[1] - game_data[item][1])
            item_pos = game_data[item]

        if x_dis == 0:
            angle = 0
        else:
            angle = math.tan(y_dis / x_dis)

        # if the angle is 0 check if the camera is facing the right direction
        d = ""  # the direction that the item is in
        if angle == 0:
            if rover[0] > item_pos[0]:
                d = "w"
            elif rover[0] < item_pos[0]:
                d = "e"
            elif rover[1] > item_pos[1]:
                d = "s"
            elif rover[1] < item_pos[1]:
                d = "n"

        # if the item is in the right direction update the messages
        if direction == d:
            if x_dis == 1 or y_dis == 1:
                new_message.append(
                    {"from_rover": False, "message": game_data["item_messages"][item]}
                )
            else:
                new_message.append(
                    {"from_rover": False, "message": game_data["item_messages"][item]}
                )

    # If no new_message is added use this default message.
    if new_message == []:
        new_message = [
            {
                "from_rover": False,
                "message": "The barren wasteland of Mars stretches out to the horizon.",
            }
        ]

    game_data["messages"] = game_data["messages"] + new_message
    return game_data


def save_score(s, i):
    HighScore.objects.create(score=s, initials=i)


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
        game_data = new_game(request)
        request.session["game_data"] = new_game(request)

    # Win if plutonium was retrieved
    if game_data["has_plutonium"] and not game_data["victorious"]:
        game_data["victorious"] = True
        game_data["game_over"] = True
        game_data["score"] = int(
            game_data["battery"] * abs(game_data["temperature"]) // 10
        )
        game_data["messages"].append({"from_rover": False, "message": ""})
        game_data["messages"].append(
            {"from_rover": False, "message": "CONGRATULATIONS!"}
        )
        game_data["messages"].append(
            {
                "from_rover": False,
                "message": f"Your rover was able to reconnect its power supply!",
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

    # Direct player to start new game and save score
    if game_data["game_over"]:
        if game_data["victorious"]:
            if game_data["getting_score"]:
                game_data["initials"] = command
                HighScore.objects.create(score=game_data["score"], initials=command)
                game_data["input_len"] = 16
                game_data["getting_score"] = False
                game_data["messages"].append(
                    {"from_rover": False, "message": "Your score has been recorded."}
                )
                game_data["messages"].append(
                    {
                        "from_rover": False,
                        "message": 'Type "new game" to start a new game.',
                    }
                )
            elif command.startswith("save") and game_data["initials"] == "":
                game_data["input_len"] = 3
                game_data["messages"].append(
                    {"from_rover": False, f"message": "Enter initials."}
                )
                game_data["getting_score"] = True
            else:
                score = game_data["score"]
                game_data["messages"].append(
                    {"from_rover": False, "message": f"Your score is {score}."}
                )
                if game_data["messages"] == "":
                    game_data["messages"].append(
                        {
                            "from_rover": False,
                            "message": 'Type "save" to save your score.',
                        }
                    )
                game_data["messages"].append(
                    {
                        "from_rover": False,
                        "message": 'Type "new game" to start a new game.',
                    }
                )
        else:
            game_data["messages"].append(
                {"from_rover": False, "message": 'Type "new game" to start a new game.'}
            )

    request.session["game_data"] = game_data
    return game_data
