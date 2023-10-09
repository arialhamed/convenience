#!/usr/bin/env python3

'''
This script moves duplicate files to a folder named "DUPES". You may modify this script to delete (with `os.remove`) but use at your own risk.
Having Git installed and selecting True to whatever option that allows some Linux tools to be usable in Windows shells (PowerShell & Command Line).
This was ran and tested in PowerShell, with Python 3.11.4 in Revision OS (Windows 11).
The MIT License applies to this script, such as the repository this originates from. Search it up.
'''

# Libraries
import os, asyncio, time, shelve, ctypes, sys
# `os` for basic operating functions
# `asyncio` for multi-threaded performance (speedy boi)
# `time` for performance measurement
# `shelve` for persistant storage recording hash algorithms of files
# `ctypes` to hide `shelve` database folder in Windows)
# `sys` to detect current operating system (to avoid ctypes error)

# I may add third-party libraries for greater features, such as `plyer` for notifications.

# Get current list (only reads files, not directories)
listcwd = [x for x in list(filter(os.path.isfile, os.listdir())) if not x.endswith(".py")]

# Initialize folder for duplicates & count of duplicates
dupeDirectory = "DUPES"
dupeCountNew = 0 # Count of new duplicates
dupeCountExisting = 0 # Count of existing duplicates
if os.path.exists(dupeDirectory):
	dupeCountExisting += len(os.listdir(dupeDirectory))
else:
	os.system(f"mkdir {dupeDirectory}")

# Initialize multi-platform variable
linux = sys.platform.lower() == "linux"
slash = "/" if linux else "\\"

# Shelve Database
shelveDirectory = (os.path.expanduser('~') if linux else os.getcwd().split("\\")[0]) + f"{slash}.dedup" + slash
print(shelveDirectory)
if not os.path.exists(shelveDirectory):
	os.system(f"mkdir {shelveDirectory}")
	if linux:
#		os.system(f"touch {shelveDirectory}{slash}db")
		pass
	else:
		ctypes.windll.kernel32.SetFileAttributesW(shelveDirectory, 0x02)

# Async function to ensure that CPU doesn't get overloaded with too many processes
# Looking at the last line of the `main` function within the open shelve, the number
async def gather_with_concurrency(n, *coros):
	semaphore = asyncio.Semaphore(n)
	async def sem_coro(coro):
		async with semaphore:
			return await coro
	return await asyncio.gather(*(sem_coro(c) for c in coros))

# Initialize `dedup_db` with shelve
print(f"Reading from `{shelveDirectory}db`")
with shelve.open(f"{shelveDirectory}db", "c") as db: # TODO: make Linux alternative for this line (using `platform` module (`platform.system()`))

	# Checks if `file_in` sha256sum
	async def getsha(file_in):
		global db, dupeCountNew
		# if db.get(file_in) == None: # TODO: don't execute next line if `file_in` in `db`
		proc = await asyncio.create_subprocess_shell( # Real process (don't touch)
			f"sha256sum \"{file_in}\"",
			stderr=asyncio.subprocess.PIPE,
			stdout=asyncio.subprocess.PIPE
		)
		stdout, stderr = await proc.communicate() # `stdout` is where the results come from
		sha256sum_result = stdout.decode().split(" ")[0] # Splice the `stdout` string
		if sha256sum_result in db: # If HASH exists in `db`
			if db[sha256sum_result] != file_in: # If INPUT FILE does not match existing INPUT FILE
				os.system(f"mv \"{file_in}\" \"{dupeDirectory}{slash}{file_in}\"") # Script's purposed execution
				dupeCountNew += 1 # Increase `dupeCountNew`
		else: # If HASH doesn't exist, add it in with INPUT FILE
			db[sha256sum_result] = file_in
		print(f"{sha256sum_result} : {file_in}")

	# Main for `asyncio.run`
	async def main(the_list):
		tasklist_in = [getsha(x) for x in the_list] # Create list of tasks
		# await asyncio.gather(*tasklist_in) # Classic method (causes overloading)
		await gather_with_concurrency(60, *tasklist_in)

	# Performance measure & execution
	timer_start = time.perf_counter()
	asyncio.run(main(listcwd))

print(f"\
Performed deduping in... {time.perf_counter() - timer_start:0.4f} seconds\n\
New duplicate files found and moved to {dupeDirectory}: {dupeCountNew}\n\
Existing duplicate files in {dupeDirectory}: {dupeCountExisting}\n\
Total duplicate files: {dupeCountNew+dupeCountExisting}"
)

if linux:
	os.system("notify-send \"dedup.py complete\" --urgency=critical")
else:
	os.system("pause") # This is if you're running this in regards to the shebang
