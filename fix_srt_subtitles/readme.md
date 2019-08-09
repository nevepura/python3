# Purpose
This script was created to have working .srt subtitles on Chrome extension Substitial.
The extension seems to have troubles processing -srt subtitle that have multiple lines in the same time interval: the subs go out of timing.

This scripts takes an .srt file and creates a copy having totally time-separated subs: where you have two overlapping lines, the previous is cut where the current begins: the result is that some line are cut, but you can still listen  to everything on time.

# Usage
Input: `file_name.srt`\
output: `file_name_edited.srt`\
From terminal run: `$ python3 fix_srt.subtitles.py file_name.srt`
