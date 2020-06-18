import random
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
        return Exception("combination not found")

    def create_mp3(self):
        output_fname = "output.mp3"

        all_workout = [EMPTY_PLACEHOLDER] * (len(self.rounds) * self.round_time + (len(self.rounds)-1) * self.rest_time)
        #print("".join(all_workout))


        for i, round in enumerate(self.rounds):
            idx = (i - 1) * self.rest_time
            
            while idx < self.round_time:
                if round[idx] == EMPTY_PLACEHOLDER:
                    idx += 1
                    continue

                comb_id = ord(round[idx]) - ASCII_OFFSET

                combination = self.get_combination_by_id(comb_id)
                text = combination["name"]
                
                fname = "tmp"+str(comb_id)+".mp3"
                Speech(text, "en").save(fname)

                speech_sound = AudioSegment.from_mp3(fname)
                silent_gap = AudioSegment.silent(self.comb_gap * 1000)
                previous_sound = AudioSegment.from_mp3(output_fname)

                latest_sound = previous_sound + silent_gap + speech_sound
                latest_sound += AudioSegment.silent((combination["time"]*1000 - len(speech_sound)))
                latest_sound.export(output_fname, format="mp3")

                for j in range(idx, self.round_time):
                    if round[j] == EMPTY_PLACEHOLDER:
                        break
                idx = j


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