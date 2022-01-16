import math


circle_degrees = {
        "N": math.degrees(math.pi/2),
        "NE": math.degrees(math.pi/4),
        "E": math.degrees(0 * math.pi),
        "SE": math.degrees(7 * math.pi/4),
        "S": math.degrees(3 * math.pi/2),
        "SW": math.degrees(5 * math.pi/4),
        "W": math.degrees(math.pi),
        "NW": math.degrees(3 * math.pi/4)
    }


def direction(facing, turn):
    try:
        if facing not in circle_degrees.keys():
            raise KeyError(f"Dictinary does not contain such key '{facing}'")
        if turn % 45 != 0:
            raise ValueError("Turn value must be a multiple of 45")
        res = circle_degrees[facing] - (turn // 45) * math.degrees(math.pi) / 4
        if res < 0 or res >= 360:
            res = res % 360
        return list(circle_degrees.keys())[list(circle_degrees.values()).index(res)]
    except KeyError as e:
        print(e)
    except ValueError as e:
        print(e)
