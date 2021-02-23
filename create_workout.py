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
    get_available_combs = lambda remaining_seconds: [comb for comb in combinations
                                                     if comb["time"] < remaining_seconds]
    for i in range(num_rounds):
        remaining_seconds = round_time - 4
        combs = []
        while len(available_combs:=get_available_combs(remaining_seconds)) > 0:
            combs.append(random.choice(available_combs))
            remaining_seconds -= combs[-1]["time"] + comb_gap
        second = 3 # for bell sound
        schedule = [EMPTY_PLACEHOLDER] * round_time
        for comb in combs:
            for i in range(comb["time"]):
                schedule[i+second] = chr(ASCII_OFFSET+comb["id"])
            second += comb["time"] + comb_gap
        schedule[:3] = chr(ASCII_OFFSET)*3
        schedule[-1] = chr(ASCII_OFFSET)
        schedule += chr(ASCII_OFFSET)*2
        workout = [*workout, *schedule] + [EMPTY_PLACEHOLDER]*(rest_time-2)
    return workout[:-rest_time]