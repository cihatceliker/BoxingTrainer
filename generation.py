from pydub import AudioSegment
from google_speech import Speech

text = "start"
lang = "en"
speech = Speech(text, lang)
#speech.play()
#print(speech)
speech.save("output.mp3")

"""

sound = AudioSegment.from_mp3("output.mp3")

# writing mp3 files is a one liner
two_sec_silence = AudioSegment.from_mp3("output.mp3")
sound_with_gap = sound[:500] + two_sec_silence + sound[500:]

#sound_with_gap.export("new.mp3", format="mp3")

print(len(sound_with_gap))



output_fname = "output.mp3"
text = combination["name"]
fname = "tmp"+str(combination["id"])+".mp3"
Speech(text, "en").save(fname)
speech_sound = AudioSegment.from_mp3(fname)
silent_gap = AudioSegment.silent(comb_gap * 1000)
previous_sound = AudioSegment.from_mp3(output_fname)

latest_sound = previous_sound + silent_gap + speech_sound
latest_sound += AudioSegment.silent((combination["time"]*1000 - len(speech_sound)))
latest_sound.export(output_fname, format="mp3")
"""
"""
text = "slip and go"
lang = "en"
speech = Speech(text, lang)
speech.play()

# you can also apply audio effects while playing (using SoX)
# see http://sox.sourceforge.net/sox.html#EFFECTS for full effect documentation
sox_effects = ("speed", "1.2")
speech.play(sox_effects)

# save the speech to an MP3 file (no effect is applied)
speech.save("output.mp3")
"""


"""
Open a WAV file

from pydub import AudioSegment

song = AudioSegment.from_wav("never_gonna_give_you_up.wav")

...or a mp3

song = AudioSegment.from_mp3("never_gonna_give_you_up.mp3")

... or an ogg, or flv, or anything else ffmpeg supports

ogg_version = AudioSegment.from_ogg("never_gonna_give_you_up.ogg")
flv_version = AudioSegment.from_flv("never_gonna_give_you_up.flv")

mp4_version = AudioSegment.from_file("never_gonna_give_you_up.mp4", "mp4")
wma_version = AudioSegment.from_file("never_gonna_give_you_up.wma", "wma")
aac_version = AudioSegment.from_file("never_gonna_give_you_up.aiff", "aac")

Slice audio:

# pydub does things in milliseconds
ten_seconds = 10 * 1000

first_10_seconds = song[:ten_seconds]

last_5_seconds = song[-5000:]

Make the beginning louder and the end quieter

# boost volume by 6dB
beginning = first_10_seconds + 6

# reduce volume by 3dB
end = last_5_seconds - 3

Concatenate audio (add one file to the end of another)

without_the_middle = beginning + end

How long is it?

without_the_middle.duration_seconds == 15.0

AudioSegments are immutable

# song is not modified
backwards = song.reverse()

Crossfade (again, beginning and end are not modified)

# 1.5 second crossfade
with_style = beginning.append(end, crossfade=1500)

Repeat

# repeat the clip twice
do_it_over = with_style * 2

Fade (note that you can chain operations because everything returns an AudioSegment)

# 2 sec fade in, 3 sec fade out
awesome = do_it_over.fade_in(2000).fade_out(3000)

Save the results (again whatever ffmpeg supports)

awesome.export("mashup.mp3", format="mp3")

Save the results with tags (metadata)

awesome.export("mashup.mp3", format="mp3", tags={'artist': 'Various artists', 'album': 'Best of 2011', 'comments': 'This album is awesome!'})

You can pass an optional bitrate argument to export using any syntax ffmpeg supports.

awesome.export("mashup.mp3", format="mp3", bitrate="192k")

Any further arguments supported by ffmpeg can be passed as a list in a 'parameters' argument, with switch first, argument second. Note that no validation takes place on these parameters, and you may be limited by what your particular build of ffmpeg/avlib supports.

# Use preset mp3 quality 0 (equivalent to lame V0)
awesome.export("mashup.mp3", format="mp3", parameters=["-q:a", "0"])

# Mix down to two channels and set hard output volume
awesome.export("mashup.mp3", format="mp3", parameters=["-ac", "2", "-vol", "150"])
"""