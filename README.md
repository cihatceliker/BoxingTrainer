# Boxing Workout Creator

Randomized boxing workout creator inspired from the [video](https://www.youtube.com/watch?v=Vpis08_FL3k) by [Precision Striking channel](https://www.youtube.com/channel/UC4PwJo76WpTOk-3N8dazt1A). The concept of the video is simple, he says the combination name and you do it.
#
The goal here is to make it flexible so that you can create your own customized workouts with any combination you want, with any intensity you want.
****
#### An example usage:
```python
from create_workout import *

COMBINATIONS = [
    create_combination("up and around", 3),
    create_combination("slip and go", 4),
    create_combination("hook body", 4),
    create_combination("angles", 2),
    create_combination("double up", 4)
]

workout = create_workout(num_rounds=3, 
                         round_time=60, 
                         rest_time=30, 
                         comb_gap=2, 
                         combinations=COMBINATIONS)

final_workout = create_mp3(workout, COMBINATIONS)
final_workout.export("workout.mp3", format="mp3")
```
- The function `create_workout` takes 5 arguments and creates a string representing the workout. Later, this string is passed to `create_mp3` function to create the mp3 file.
1. num_rounds   : Total number of rounds.
1. round_time   : Length of a round.
1. rest_time    : Length of the time between rounds.
1. comb_gap     : Length of the default gap between combinations.
1. combinations : A list of combinations, where each combination has name and length. The name of the combination will be vocalized using the [gtts: Google-Text2Speech](https://pypi.org/project/gTTS/) library. The length is the preserved time for that combination. 
