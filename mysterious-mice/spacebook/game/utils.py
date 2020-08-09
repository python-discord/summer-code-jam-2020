import math
import random
from .models import HighScore
from mars_weather.services import get_week_weather


# All coordinates are stored as tuples of (x, y)
# x is east-west with east being positive
# y is north-south with north being positive
def new_game(request):
    """
    Generates a new game, resetting the location of all components and the rover.
    """

    # Attempt to pull the weather for the current sol
    # If weather data is missing for current sol, get data for previous sol
    # If data is still missing, use default values
    week_weather = get_week_weather(request)
    for sol in range(-1, -3, -1):
        sol_weather = week_weather["weekly_weather"][sol]
        sol_weather_key = list(sol_weather.keys())[0]
        sol_weather_data = sol_weather[sol_weather_key]
        if "HWS" in sol_weather_data and "AT" in sol_weather_data:
            wind_speed = sol_weather_data["HWS"]["av"]
            temperature = sol_weather_data["AT"]["av"]
            break
    if wind_speed is None or wind_speed == "":
        wind_speed = 6
    if temperature is None or temperature == "":
        temperature = -60

    # Get wind direction
    wind_direction = (random.randint(-1,1), random.randint(-1,1))


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
        "wind": wind_direction,
        "wind_speed": wind_speed,
        "temperature": temperature,
        "obstacles": {
            "dust_storm": (0, 2),
            "small_crater": (-4, -3),
            "large_rock": (0, 1),
        },
        "item_messages": {
            "plutonium": [
                "There is a plume of smoke in the distance.",
                "The plutonium module is smoking!",
                "The plutonium module is in front of you and it's not even damaged.",
            ],
            "solar_panels": [
                "There is an object reflecting light in the distance.",
                "The solar panel is in front of you.",
                "The solar panel is in front of you and it's not even damaged.",
            ],
            "dust_storm": [
                "A dust storm billows in the distance.",
                "A dust storm billows in front of you.",
                "The winds of the storm are shaping sand dunes, that's good data!",
            ],
            "small_crater": [
                "There is a small crater in the distance.",
                "There is a small crater in front of you.",
                "A frozen rock is in the crater, that's good data!",
            ],
            "large_rock": [
                "There is a large rock in the distance.",
                "There is a large rock in front of you.",
                "The rock seems to be eroded by water, that's good data!",
            ],
        },
        "item_msg_selector": 0,
        "found": {
            "plutonium": False,
            "solar_panels": False,
            "dust_storm": False,
            "small_crater": False,
            "large_rock": False,
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
            {"from_rover": False, "message": "Good luck!", },
            {"from_rover": False, "message": "", },
        ],
        "ground_descriptions": [
            "Red sand coveres the ground",
            "There are little rocks every where.",
            "A more efficient path has been found.",
        ],
        "ground_desc_selector": 0,
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
            "large_rock": (random.randint(-3, 3), random.randint(-3, 3)),
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


def on_object(rover, object):
    return rover[0] == object[0] and rover[1] == object[1]


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
        {"from_rover": False, "message": ">> move n", },
        {"from_rover": False, "message": ">> move north", },
        {"from_rover": False, "message": ""},
        {
            "from_rover": False,
            "message": "Look around for hints of where the components might be. Examples of valid commands:",
        },
        {"from_rover": False, "message": ">> look n", },
        {"from_rover": False, "message": ">> look north", },
        {"from_rover": False, "message": ">> look down", },
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
        {
            "from_rover": False,
            "message": 'Weather can be checked by typing "weather".',
        },
        {
            "from_rover": False,
            "message": "Additional points can be found by looking around a lot.",
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
        if on_object(old_position, game_data["obstacles"][obstacle]):
            # if the obstacle is a dust stom there is a 50% chace power comsumption will increase
            if obstacle == "dust_storm":
                if random.randint(1, 10) > 5:
                    game_data["power_usage"] += int(game_data["wind_speed"])
                    game_data["messages"].append(
                        {
                            "from_rover": False,
                            "message": "Sand has gotten stuck in the treads. Moving becomes less efficient.",
                        }
                    )
            # if the obstacle is a small crater there is a 50% chance to get stuck
            if obstacle == "small_crater":

                # In not already stuck there is a chance to become stuck
                if not game_data["is_stuck"]:
                    if random.randint(1, 10) > 5:
                        game_data["is_stuck"] = True
                        game_data["messages"].append(
                            {"from_rover": False, "message": "You are stuck!", }
                        )

                # If you are stuck there is a chance to become unstuck
                else:
                    if random.randint(1, 10) > 5:
                        game_data["is_stuck"] = False
                        game_data["messages"].append(
                            {
                                "from_rover": False,
                                "message": "You are no longer stuck.",
                            }
                        )
                    else:
                        game_data["messages"].append(
                            {"from_rover": False, "message": "You are stuck!", }
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
        if on_object(new_position, game_data["obstacles"]["large_rock"]):
            new_position = old_position
            success = False
            game_data["messages"].append(
                {"from_rover": False, "message": "You cannot move there.", }
            )
    else:
        success = False

    # If stuck depleat the battery
    if game_data["is_stuck"]:
        game_data["battery"] = game_data["battery"] - game_data["power_usage"]
        if game_data["has_solar_panels"]:
            game_data["battery"] = game_data["battery"] + 2

    # If successfully moved depleat battery, handel components, and update position
    if success:

        # Move dust storm
        cur_dust = game_data['obstacles']['dust_storm']
        cur_dust[0] += game_data['wind'][0]
        cur_dust[1] += game_data['wind'][1]
        game_data['obstacles'].update({"dust_storm": cur_dust})
        # depleat battery
        game_data["battery"] = game_data["battery"] - game_data["power_usage"]
        if game_data["has_solar_panels"]:
            game_data["battery"] = game_data["battery"] + 2

        # Change ground description text
        game_data["ground_desc_selector"] = random.randint(
            0, len(game_data["ground_descriptions"]) - 1
        )

        # Change close up text
        game_data["item_msg_selector"] = random.randint(
            1, len(game_data["item_messages"]["plutonium"]) - 1
        )

        # Move components with rover
        if game_data["has_solar_panels"]:
            game_data["solar_panels"] = new_position
        if game_data["has_plutonium"]:
            game_data["plutonium"] = new_position

        # Pick up components
        if on_object(new_position, game_data["solar_panels"]) and not game_data["has_solar_panels"]:
            game_data["has_solar_panels"] = True
            game_data["messages"].append(
                {
                    "from_rover": False,
                    "message": "You have retrieved the solar panels!",
                }
            )
            game_data["messages"].append(
                {
                    "from_rover": False,
                    "message": "It will take less energy to traverse the terrain of Mars now!",
                }
            )
        if on_object(new_position, game_data["plutonium"]) and not game_data["has_plutonium"]:
            game_data["has_plutonium"] = True
            game_data["messages"].append(
                {"from_rover": False, "message": "You have retrieved the plutonium!"}
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
        "large_rock",
    ]
    obstacles_list = [
        "dust_storm",
        "small_crater",
        "large_rock",
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
        d = None  # the direction that the item is in
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

            # if the object is right in front the message may be different
            if x_dis == 1 or y_dis == 1:
                new_message.append(
                    {
                        "from_rover": False,
                        "message": game_data["item_messages"][item][
                            game_data["item_msg_selector"]
                        ],
                    }
                )
                if (game_data["item_msg_selector"] == len(game_data["item_messages"]["plutonium"]) - 1):
                    if not game_data["found"][item]:
                        game_data["score"] += 50
                        game_data["found"][item] = True
            else:
                new_message.append(
                    {
                        "from_rover": False,
                        "message": game_data["item_messages"][item][0],
                    }
                )

    # Special commands

    # give more detailed description for ground
    if direction in ["d", "down"] or "ground" in direction:
        message = game_data["ground_descriptions"][game_data["ground_desc_selector"]]
        new_message.append({"from_rover": False, "message": message})

        # if the last option is chosen the battery is increased
        if (game_data["ground_desc_selector"] == len(game_data["ground_descriptions"]) - 1):
            game_data["battery"] += 3

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


def command_weather(game_data):
    game_data["messages"].append(
        {
            "from_rover": False,
            "message": f"Current temperature: {game_data['temperature']} deg C",
        }
    )
    game_data["messages"].append(
        {
            "from_rover": False,
            "message": f"Current wind speed: {game_data['wind_speed']} meters per second",
        }
    )
    return game_data


def calculate_score(game_data):
    """
    Score is equal to remaining battery times (mars temperature divided by 10) plus accumulated score.
    """
    bat_score = int(game_data["battery"] * (abs(game_data["temperature"]) // 10))
    return game_data["score"] + bat_score


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
        elif command.startswith("score"):
            game_data["messages"].append(
                {"from_rover": False, "message": calculate_score(game_data)}
            )
        elif command == "weather":
            game_data = command_weather(game_data)
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
        game_data["score"] = calculate_score(game_data)
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
    if (game_data["battery"] <= 0 and not game_data["game_over"] and not game_data["victorious"]):
        game_data["battery"] = 0
        game_data["messages"].append({"from_rover": False, "message": ""})
        game_data["messages"].append({"from_rover": False, "message": "GAME OVER!"})
        game_data["game_over"] = True

    # Direct player to start new game and save score
    if game_data["game_over"]:

        # if the player was victorious they get the option to save their score
        if game_data["victorious"]:

            # When getting the score the input field will be limited to 3 characters
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
                    {"from_rover": False, "message": "Enter initials."}
                )
                game_data["getting_score"] = True
            else:
                score = game_data["score"]
                game_data["messages"].append(
                    {"from_rover": False, "message": f"Your score is {score}."}
                )
                if game_data["initials"] == "":
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
