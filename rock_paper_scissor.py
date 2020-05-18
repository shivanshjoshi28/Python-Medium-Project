import random
name = input("Enter your name: ")
print(f"Hello, {name}")
handtype = input().split(',')
print("\nOkay, let's start")


# Making a list and corresponding dictionary ... here handtype is the user input given by the keyboard
# and compwins is the condition for the computer to win
if handtype == ['']:
    handtype = ['rock', 'paper', 'scissors']
    compwins = {'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'}
else:
    compwins = dict()
    for i in range(len(handtype)):
        A = (len(handtype)-1)//2
        if A+i >= len(handtype):
            li = [handtype[j]for j in range(i+1, len(handtype))]
            [li.append(handtype[j])for j in range(A-len(li))]
            compwins[handtype[i]] = li

        else:
            compwins[handtype[i]] = [handtype[j] for j in range(i+1, i+1+A)]
inp = input()

# Here The file is being processed to get the score of a person if present
ratingfile = open("rating.txt", 'r')
t = ratingfile.read()
if(name not in t):
    score = 0
else:
    ratingfile.seek(t.index(name)+len(name)+1)
    score = int(ratingfile.readline().strip('\n'))


# Main game logic is here
while(inp != '!exit'):
    if inp == '!rating':
        print(score)
    elif inp not in handtype:
        print("Invalid input")
    else:
        orginalind = handtype.index(inp)
        guessind = random.randint(0, len(handtype)-1)
        if handtype[guessind] in compwins[handtype[orginalind]]:
            print(f"Sorry, but computer chose {handtype[guessind]}")
        elif(handtype[guessind] == handtype[orginalind]):
            print(f"There is a draw ({handtype[orginalind]})")
            score += 50
        else:
            print(f"Well done. Computer chose {handtype[guessind]} and failed")
            score += 100
    inp = input()
