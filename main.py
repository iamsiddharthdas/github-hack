import os

## Number of days you want to make commits
for i in (
    1,
    3,
    6,
    9,
    5,
    6,
    13,
    12,
    14,
    16,
    18,
    10,
    17,
    23,
    16,
    19,
    12,
    18,
    33,
    46,
    52,
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
