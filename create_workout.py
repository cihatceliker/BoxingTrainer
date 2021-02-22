import random

COMB_ID = 0
ASCII_OFFSET = 399
EMPTY_PLACEHOLDER = "_"

def create_combination(name, expected_time):
    global COMB_ID
    COMB_ID += 1
    return {
        "name": name,
        "time": expected_time,
        "id": COMB_ID
    }

def create_workout(num_rounds, round_time, rest_time, comb_gap, combinations):
    workout = []
    for i in range(num_rounds):
        schedule = [EMPTY_PLACEHOLDER] * round_time
        second = comb_gap
        while second < round_time:
            combination = random.choice(combinations)
            for i in range(second, min(second+combination["time"], round_time)):
                schedule[i] = chr(ASCII_OFFSET+combination["id"])
            second += combination["time"] + comb_gap
        schedule[::len(schedule)-1] = [chr(ASCII_OFFSET)]*2
        workout = [*workout, *schedule] + [EMPTY_PLACEHOLDER]*rest_time
    return workout[:-rest_time]