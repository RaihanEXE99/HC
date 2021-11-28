import os,time

colors = ['\033[95m','\033[94m','\033[96m','\033[92m','\033[93m','\033[91m']
space1=" "*16
head1=",,,,,,,,,,---''"
space2 = "      "
head2 = "--''''''''"+"-"*10+"````|"

body =[
    "                           _:'''':.",
    " _                  .,---------------.",
    " \\    / _________./  |[__]|    ]|\"\"\"\"\\__",
    "  \\============:;    |____|[____|''''/_/')",
    "     /            `'-,._____===\=_____.,-'",
    "                          \         \     ",
    "                    \"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\""
]

flag = True
space,c = 0,0
while True:
    space = space+1 if space<119 else 0
    print("\n"*3)
    if flag==True:
        print(" "*space+space1+" "*15+head1[::-1])
        print(" "*space+space2+head2)
        
    else:
        print(" "*space + space1+head1)
        print(" "*space + space2+" "*25+head2[::-1])

    for b in body:
        print(colors[c]+" "*space+ b)

    print(colors[int(space/20)]+"\n"*5+"HELICOPTER!!!HELICOPTER")
    time.sleep(.005)
    flag = False if flag == True else True
    c = 0 if c==5 else c+1
    os.system('clear')
