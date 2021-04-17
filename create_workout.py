import random, os
from gtts import gTTS
from pydub import AudioSegment


COMB_ID = 0
SEED = 0
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
        random.seed(SEED+i)
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


def text_to_speech(text):
    filename = "tmp.mp3"
    gTTS(text=text, lang="en", slow=False).save(filename)
    sound = AudioSegment.from_mp3(filename)
    os.remove(filename)
    return sound


def create_mp3(workout, combinations):
    # combs must be unique
    assert len(set([comb["id"] for comb in combinations])) == len(combinations)
    get_combination_by_id = lambda id_: [comb for comb in combinations if comb["id"] == id_][0]
    get_blank = lambda: AudioSegment.from_mp3("sfx/template.mp3")[0]
    get_bell = lambda: AudioSegment.from_mp3("sfx/bell.mp3")
    
    final_workout = get_blank()
    
    flag = EMPTY_PLACEHOLDER
    for idx, char in enumerate(workout):
        if char == EMPTY_PLACEHOLDER:
            flag = EMPTY_PLACEHOLDER
            final_workout += get_blank() * 1000
            continue
        if flag == char: continue
        
        comb_id = ord(char) - ASCII_OFFSET

        # when round begins or ends
        if comb_id == 0:
            final_workout += get_bell()
            flag = char
            continue

        combination = get_combination_by_id(comb_id)
        text = combination["name"]
        
        voice = text_to_speech(text)
        final_workout += voice + get_blank() * (combination["time"] * 1000 - len(voice))
        flag = char
        
    return final_workout
