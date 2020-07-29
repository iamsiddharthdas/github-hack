import os

## Number of days you want to make commits
for i in (
    101,
    113,
    126,
    139,
    152,
    165,
    103,
    112,
    124,
    136,
    148,
    160,
    172,
    123,
    146,
    69,
    82,
    118,
    103,
    106,
    150,
):
    d = str(i) + " day ago"
    ## Open a text file and modify it
    with open("bot.txt", "a") as file:
        file.write(d)
    ## Add bot.txt to staging area
    os.system("git add bot.txt")
    ## Commit it
    os.system('git commit --date="' + d + '" -m "first commit"')

## push the commit to github
os.system("git push -u origin master")
