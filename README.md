# convenience
Automation &amp; convenience tools with python, at its finest. The ones labelled with "personal" are those that I use personally (of course) though you can also use it and adjust it according to your own scope. 

### update-git.sh
Automatically updates your remote repository **&** your local repository. This is useful for me as sometimes I am just not feeling it one day, and I can't just make up of a good commit message. By default it will use the current datetime as the commit message but you can also add in your own, as such:

``` bash
./update.sh "upload something words here"
```

### timestamp.py
Automatically slaps a datetime stamp to your file. You can change how time format looks like, just download it and edit it yourself lol. This really just makes the process of creating backups so much easier. Even though there are good backup software like ZPAQ & Backups by Ubuntu, this is good for small-scale, singular files. The usage is as follows:

``` bash
python3 timestamp.py example.txt

_example.txt is renamed as [2023-01-21_21-37-49]_example.txt_
```

### video-compressor.sh
You can use `ffmpeg` yourself, but this script compresses your video into a specific size. The usage is as follows:

``` bash
./video-compressor.sh input.mkv 99
```

The line above will compress that `input.mkv` and output it as a video that is **99MB**. Change that value to however you may like it.

Source: [StackOverflow](https://stackoverflow.com/a/61146975)

Edit: It may not work for some reason.. I made it so that it works afterwards but the quality of the video ended up being really crappy :|

### start.sh (personal)
This is my personal login script that I use when I daily my Kubuntu on my X230. The script makes use of my fingerprint reader, sends a notif that it is working after I log in. After I let it read my fingerprint, it will continue to fulfil the rest of the script, which are the following functions:
- Starts Waydroid session
- Organizes and moves files from home directory & Downloads directory to other folders in the system
- Update packages (_requires internet connection_)
- Set battery start &amp; stop thresholds by **75%** &amp; **85%** _respectively_
- Rip multiple Reddit subreddits and users with [ripme.jar](https://github.com/ripmeapp/ripme) (_requires internet connection_)

### instagram_comment_purge
This is a very jank tool that clears every single comment that you have probably carelessly created at some point in the past in Instagram. Sometimes maybe you were too heated when reading a post, or you thought of a very clever but risky joke in the comments section. However, **employers can look at your internet footprint**, especially those from bigger companies. Their search engines are insane when it comes to background checks, so feel free to use this tool. 

To be honest, I am not sure if it would work for everyone, you may need to edit each XPath value again, since Meta is apparently anti-scraping. 

``` bash
python3 instagram_comment_purge.py <USERNAME> <PASSWORD>
```

This Python script expects user to be in Ubuntu 22.04 (in any flavour) and have Firefox Marionette installed, though with some minor edits this script can be used in Windows as well.

### split_video.py
This script looks at the current directory and all current subdirectories, pick out which .mp4 files are larger than 100MB, then use mkvtools's mkvmerge command to split it by 100MB. Useful for when you have videos that you want to save to a github repo but it's larger than 100MB. You can absolutely tune it to your own specifications for other purposes.

Just chmod it then run it. Note that this only works for MKVs and MP4s. 

``` bash
chmod split_video.py
./split_video.py
```

