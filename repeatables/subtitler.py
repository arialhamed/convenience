from googletrans import Translator, constants
from tqdm import tqdm
import os, sys

# Create variables
name_output = sys.argv[1].rsplit('.', 1)[0] + " (full sub)." + sys.argv[1].rsplit('.', 1)[1] if len(sys.argv) == 2 else sys.argv[2]
array_command = [[],[],[]]
translator = Translator()
lang_out = "eng" 
code_dict = {
    "af": "afr", "sq": "sqi", "am": "amh", "ar": "ara", "hy": "hye", "az": "aze", "eu": "eus", "be": "bel", "bn": "ben",
    "bs": "bos", "bg": "bul", "ca": "cat", "ny": "nya", "zh-cn": "zho", "co": "cos", "hr": "hrv", "cs": "ces",
    "da": "dan", "nl": "nld", "eo": "epo", "et": "est", "tl": "tir", "fi": "fin", "fr": "fra", "fy": "fry", "gl": "glg",
    "ka": "kat", "de": "deu", "el": "ell", "gu": "guj", "he": "heb", "hi": "hin",
    "hu": "hun", "is": "isl", "id": "ind", "ga": "gle", "it": "ita", "ja": "jpn", "kn": "kan",
    "kk": "kaz", "km": "khm", "ko": "kor", "ku": "kur", "ky": "kir", "lo": "lao", "la": "lat", "lv": "lav", "lt": "lit",
    "lb": "ltz", "mk": "mkd", "mg": "mlg", "ms": "msa", "ml": "mal", "mi": "mal", "mr": "mar", "mn": "mon",
    "my": "mya", "ne": "nep", "no": "nor", "or": "ori", "ps": "pus", "fa": "fas", "pl": "pol", "pt": "por", "pa": "pan",
    "ro": "ron", "ru": "rus", "sm": "smo", "gd": "gla", "sr": "srp", "st": "sot", "sn": "sna", "sd": "snd", "si": "sin",
    "sk": "slk", "sl": "slv", "so": "som", "es": "spa", "su": "sun", "sw": "swa", "sv": "swe", "tg": "tgk", "ta": "tam",
    "te": "tel", "th": "tha", "tr": "tur", "uk": "ukr", "ur": "urd", "ug": "uig", "uz": "uzb", "vi": "vie", "cy": "cym",
    "xh": "xho", "yi": "yid", "yo": "yor", "zu": "zul"
}

print(f"Input video: \"{sys.argv[1]}\"\nOutput video: \"{name_output}\"\n\nInput language: {lang_out}")

# Loops through language codes
for lang in tqdm([x for x in list(constants.LANGUAGES.keys()) if x in list(code_dict.keys())]):

	# Reads source & writes destination
	with open(f"{code_dict[lang]}.srt", "a", encoding="utf-8") as file_output, open(f"{lang_out}.srt", "r") as file_input:

		# Loops through lines of source
		for i in tqdm(file_input.read().split("\n"), leave=False):
			while True:
				try: # WARNING: This will render Ctrl+C to be useless
					verse = translator.translate(i, src="en", dest=lang).text if i != "" and "-->" not in i and not(i.isnumeric()) else i
					file_output.write(f"{verse}\n")
					break
				except:
					pass


# Build FFMPEG command
for n, i in enumerate([x for x in os.listdir() if x.endswith(".srt")]):
	array_command[0].append(f" -i {i}")
	array_command[1].append(f" -map {n+1}")
	array_command[2].append(f" -metadata:s:s:{n} language={i[:-4]}")
final_command = f"ffmpeg -i \"{sys.argv[1]}\"" + "".join([x for x in array_command[0]]) + " -c:v copy -c:a copy -c:s " + ("mov_text" if sys.argv[1].endswith(".mp4") else "srt") + " -map 0:v -map 0:a" + "".join([x for x in array_command[1]]) + "".join([x for x in array_command[2]]) + f" \"{name_output}\" -hide_banner -loglevel error"

# Execute command
os.system(final_command)
print(final_command)

# Since the IO mode here uses "a", we would unfortunately need to clear all except the source language
for i in [x for x in os.listdir() if x.endswith(".srt") and not(x.startswith(lang_out))]:
	os.remove(i)