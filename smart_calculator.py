import string
no = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


def checkistherenum(x):
    sum = 0
    for i in no:
        sum += x.find(str(i))
    if sum != -10:
        return 1
    else:
        return 0


def checkistherealpha(x):
    totalalpha = string.ascii_letters
    sum = 0
    for i in totalalpha:
        sum += x.find(i)
    if sum != -52:
        return 1
    else:
        return 0


a = input()
while(a != '/exit'):
    if('/'in a and a[a.index('/')+1].isalpha()):
        if(a == '/help'):
            print("The program calculates the sum and difference of numbers")
        else:
            print("Unknown command")
        a = input()
        continue
    if(a != ''):
        if a.isalpha():
            try:
                if a == 'a':
                    a = memory
                    print(eval(a))
                    a = input()
                    continue
            except:
                print("Unknown variable")
                a = input()
                continue
            try:
                print(eval(a))
            except Exception as e:
                print("Unknown variable")
        elif a.isalnum():
            print("Invalid identifier")
            a = input()
            continue
        elif '=' in a:
            beforealphastr = a[0:a.index('=')].strip(' ')
            afteralphastr = a[a.index('=')+1:].strip(' ')
            if a.count('=') > 1:
                print("Invalid assignment")
            elif checkistherenum(beforealphastr):
                print("Invalid identifier")
            elif checkistherealpha(afteralphastr) and checkistherenum(afteralphastr):
                print("Invalid assignment")
            elif beforealphastr.isalpha() and afteralphastr.isdigit():
                if beforealphastr == 'a':
                    memory = afteralphastr
                exec(a)
            elif beforealphastr.isalpha() and afteralphastr.isalpha():
                if afteralphastr == 'a':
                    a = beforealphastr+'='+memory
                try:
                    exec(a)
                except Exception as e:
                    print("Unknown variable")
            else:
                print("Youu have reached")

        else:
            try:
                wordform = a
                if 'a'in a:
                    a = int(memory)
                print(eval(wordform))
            except Exception as e:
                print("Invalid expression")
    a = input()
print('Bye!')
