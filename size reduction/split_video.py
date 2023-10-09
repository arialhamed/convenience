#!/usr/bin/env python3

import os
# from tqdm import tqdm

deans_list = [x for x in os.popen('f(){ find "$@" -type f -size +100M ; unset -f f; }; f').read().split('\n') if os.path.isfile(x)]
for i in [x for x in deans_list if x.endswith(".mp4") or x.endswith(".mkv")]:
	print(f"CONSOLE: PROCESSING \"{i}\"")
	os.system(f"mkvmerge -o \"{i.rsplit('.',1)[0]} (split).{i.rsplit('.',1)[-1]}\" --split 93M \"{i}\"")
	os.system(f"rm -rf \"{i}\"")

os.system("notify-send \"File finished\" --urgency=critical")
