import whisper_timestamped as whisper
import sys
from datetime import timedelta
from time import time
clockStart = time()

audio = whisper.load_audio(sys.argv[1])
model = whisper.load_model("base")

result = whisper.transcribe(model, audio, language="en")

with open("eng.srt", "w") as f:
	for i, segment in enumerate(result['segments']):
		# start, end = segment['start'], segment['end']
		start, end = [z[:-3].replace(".",",") for z in [(y + '.000000' if '.' not in y else y) for y in [str(timedelta(seconds=float(x))) for x in (segment['start'], segment['end'])]]]
		f.write(f"{i}\n")
		f.write(f"{start} --> {end}\n")
		f.write(f"{segment['text'].strip()}\n")
		f.write("\n")

print(f"Elapsed: {time() - clockStart}")