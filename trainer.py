import random, sys
from pydub import AudioSegment
from google_speech import Speech

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

def create_round(id, time, gap, combinations):
    schedule = [EMPTY_PLACEHOLDER] * time
    second = gap
    while second < time:
        combination = random.choice(combinations)
        for i in range(second, min(second+combination["time"], time)):
            schedule[i] = chr(ASCII_OFFSET+combination["id"])
        second += combination["time"] + gap
    return schedule


class Workout:

    def __init__(self, num_rounds, round_time, rest_time, comb_gap, combinations):
        self.rounds = []
        self.round_time = round_time
        self.rest_time = rest_time
        self.comb_gap = comb_gap
        self.combinations = combinations
        self.output_fname = "output.mp3"
        for i in range(num_rounds):
            round = create_round(id=i+1, time=round_time, gap=comb_gap, combinations=combinations)
            self.rounds.append(round)

    def __iter__(self):
        for round in self.rounds:
            yield round
    
    def get_combination_by_id(self, id):
        for combination in self.combinations:
            if combination["id"] == id:
                return combination

    def add_sound(self, sound):
        previous_sound = AudioSegment.from_mp3(self.output_fname)
        (previous_sound + sound).export(self.output_fname, format="mp3")

    def create_mp3(self):
        all_workout = [EMPTY_PLACEHOLDER] * (
            len(self.rounds) * self.round_time + (len(self.rounds)-1) * self.rest_time
        )
        idx = 0
        for round_ in self.rounds:
            all_workout[idx:idx+self.round_time] = round_
            idx += self.rest_time + self.round_time
        
        flag = False
        for idx, second in enumerate(all_workout):
            if second == EMPTY_PLACEHOLDER:
                flag = False
                continue
            if flag: continue

            comb_id = ord(second) - ASCII_OFFSET

            combination = self.get_combination_by_id(comb_id)
            text = combination["name"]
            
            fname = "tmp"+str(comb_id)+".mp3"
            Speech(text, "en").save(fname)

            speech_sound = AudioSegment.from_mp3(fname) + 10
            silent_gap = AudioSegment.silent(self.comb_gap * 1000)
            
            latest_sound = silent_gap + speech_sound
            latest_sound += AudioSegment.silent((combination["time"]*1000 - len(speech_sound)))
            self.add_sound(latest_sound)

            flag = True
            
            if idx % self.round_time == 0:
                # adding bell sound after each round
                self.add_sound(AudioSegment.from_mp3("bell.mp3"))


combinations=[
    create_combination("up and around", 3),
    create_combination("slip and go", 4),
    create_combination("hook body", 4),
    create_combination("angles", 2),
    create_combination("double up", 4)
]

workout = Workout(num_rounds=1, round_time=180, rest_time=60, comb_gap=3, combinations=combinations)
#for round in workout: print(round)

workout.create_mp3()
