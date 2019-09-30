#!/bin/bash
# H  = Commit hash
# an = Author name
# cn = Committer name
# cd = Commit date
# s  = Subject (which dir was edited)

currentDir=$(pwd)
cd ..
git log --decorate=full --pretty=format:"%H|%an|%cn|%cd|%s" > "$currentDir/log.txt" 2>&1
git log --name-only --pretty=format:"#%H|%an|%cn|%cd" > "$currentDir/stat.txt" 2>&1
cd "$currentDir"
python format_log.py
python format_stat.py

exit
