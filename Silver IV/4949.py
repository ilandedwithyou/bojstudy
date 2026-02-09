def f(x):
    l = len(x)
    c = []
    for i in range(l):
        if x[i] == '(' or x[i] == '[':
            c.append(x[i])

        elif x[i] == ')':
            if len(c) == 0 or c[-1] != '(':
                return 0
            c.pop()

        elif x[i] == ']':
            if len(c) == 0 or c[-1] != '[':
                return 0
            c.pop()

    
    if(len(c) == 0 ):
        return 1
    else:
        return 0

while(1):
    s = input()

    if(s == '.'):
        break

    if(f(s) == 1):
        print("yes")
    else:
        print("no")

