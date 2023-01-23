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
- Disable keyring module in Python (_does not work, for now_)
- Update packages (_requires internet connection_)
- Set battery start &amp; stop thresholds by **75%** &amp; **85%** _respectively_
- Rip _r/thinkpad_ with [ripme.jar](https://github.com/ripmeapp/ripme) (_requires internet connection_)
