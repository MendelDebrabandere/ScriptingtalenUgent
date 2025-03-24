h = int(input())
b = int(input())

goingRight = True
goingUp = True

currXPos = 0
currYPos = 0

while True:
    currXPos += 1 if goingRight else -1
    currYPos += 1 if goingUp else -1

    if (currXPos >= b or currXPos <= 0) and (currYPos >= h or currYPos <= 0):
        if goingRight:
            print(f'rechteronderpocket ({currXPos}, {currYPos})') if not goingUp else print(f'rechterbovenpocket ({currXPos}, {currYPos})')
        else:
            print(f'linkeronderpocket ({currXPos}, {currYPos})') if not goingUp else print(f'linkerbovenpocket ({currXPos}, {currYPos})')
        break

    if currXPos >= b or currXPos <= 0:
        print(f'rechterband ({currXPos}, {currYPos})') if goingRight else print(f'linkerband ({currXPos}, {currYPos})')
        goingRight = not goingRight

    if currYPos >= h or currYPos <= 0:
        print(f'bovenband ({currXPos}, {currYPos})') if goingUp else print(f'onderband ({currXPos}, {currYPos})')
        goingUp = not goingUp



