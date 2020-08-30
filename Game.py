import pygame
import sys
import random
import time

#minmax algorithm
def maximum_val(x,o,a):
    val1=[]
    temp="x"
    if (a[0] == temp and a[1] == temp and a[2] == temp) or (
            a[3] == temp and a[4] == temp and a[5] == temp) or (
            a[6] == temp and a[7] == temp and a[8] == temp) or (
            a[0] == temp and a[3] == temp and a[6] == temp) or (
            a[1] == temp and a[4] == temp and a[7] == temp) or (
            a[2] == temp and a[5] == temp and a[8] == temp) or (
            a[0] == temp and a[4] == temp and a[8] == temp) or (
            a[2] == temp and a[4] == temp and a[6] == temp):
        if x == True:
            val1.append(1)
        else:
            val1.append(-1)
    elif "" not in a:
        val1.append(0)
    elif "" in a:
        x=False
        o=True
        org_a = list(a)
        player = "o"
        for i in range(9):
            a = list(org_a)
            if a[i] == "":
                a[i] = player
                val1.append(minimum_val(x, o, a))
    return(min(val1))
def minimum_val(x,o,a):
    val2=[]
    temp = "o"
    if (a[0] == temp and a[1] == temp and a[2] == temp) or (
            a[3] == temp and a[4] == temp and a[5] == temp) or (
            a[6] == temp and a[7] == temp and a[8] == temp) or (
            a[0] == temp and a[3] == temp and a[6] == temp) or (
            a[1] == temp and a[4] == temp and a[7] == temp) or (
            a[2] == temp and a[5] == temp and a[8] == temp) or (
            a[0] == temp and a[4] == temp and a[8] == temp) or (
            a[2] == temp and a[4] == temp and a[6] == temp):
        if x == True:
            val2.append(1)
        else:
            val2.append(-1)
    elif "" not in a:
        val2.append(0)
    elif "" in a:
        x = True
        o = False
        org_a = list(a)
        player = "x"
        for i in range(9):
            a = list(org_a)
            if a[i] == "":
                a[i] = player
                val2.append(maximum_val(x, o, a))
    return(max(val2))
def calculate(x,o,a):
    org_a=list(a)
    next_x_move=[]
    next_o_move=[]
    pos_mov_point1=[]
    pos_mov_point2=[]
    start=0
    start1=0
    same_val=[]
    if x==True:
        for i in range(9):
            a = list(org_a)
            if a[i]=="":
                a[i]="x"
                next_x_move.append(i)
                pos_mov_point1.append(maximum_val(x, o, a))
        max_temp = pos_mov_point1[0]
        for i in pos_mov_point1:
            if i>=max_temp:
                max_temp = pos_mov_point1[start]
                final_move=start
            start+=1
        for i in pos_mov_point1:
            if i == max_temp:
                same_val.append(start1)
            start1+=1
        if final_move in same_val:
            final_move=random.choice(same_val)
        return(next_x_move[final_move])
    else:
        for i in range(9):
            a = list(org_a)
            if a[i]=="":
                a[i]="o"
                next_o_move.append(i)
                pos_mov_point2.append(minimum_val(x,o,a))
        min_temp = pos_mov_point2[0]
        for i in pos_mov_point2:
            if i <= min_temp:
                min_temp = pos_mov_point2[start]
                final_move = start
            start += 1
        for i in pos_mov_point2:
            if i == min_temp:
                same_val.append(start1)
            start1 += 1
        if final_move in same_val:
            final_move = random.choice(same_val)
        return(next_o_move[final_move])

#main game loop
while 1:
    x = True
    o = False

    turn=random.choice(["ai","human"])

    pygame.init()

    screen = pygame.display.set_mode((300, 300))

    myFont = pygame.font.Font("freesansbold.ttf", 30)
    cross_wins = myFont.render("X wins", 1, (255, 255, 255))
    circle_wins = myFont.render("O wins", 1, (255, 255, 255))
    draw = myFont.render("DRAW", 1, (255, 255, 255))

    cross = pygame.image.load("cross.jpg")
    cross = pygame.transform.scale(cross, (99, 99))
    circle = pygame.image.load("circle.jpg")
    circle = pygame.transform.scale(circle, (99, 99))

    pygame.draw.line(screen, (255, 255, 255), (100, 0), (100, 300), 2)
    pygame.draw.line(screen, (255, 255, 255), (200, 0), (200, 300), 2)
    pygame.draw.line(screen, (255, 255, 255), (0, 100), (300, 100), 2)
    pygame.draw.line(screen, (255, 255, 255), (0, 200), (300, 200), 2)

    li1 = []
    li2 = []
    li3 = []
    li4 = []
    li5 = []
    li6 = []
    li7 = []
    li8 = []
    li9 = []

    checked=[False,False,False,False,False,False,False,False,False]

    boxval=["","","","","","","","",""]

    for i in range(100):
        for j in range(100):
            li1.append((i, j))
    for i in range(101, 200):
        for j in range(0, 100):
            li2.append((i, j))
    for i in range(201, 300):
        for j in range(0, 100):
            li3.append((i, j))
    for i in range(100):
        for j in range(101, 200):
            li4.append((i, j))
    for i in range(101, 200):
        for j in range(101, 200):
            li5.append((i, j))
    for i in range(201, 300):
        for j in range(101, 200):
            li6.append((i, j))
    for i in range(0, 100):
        for j in range(201, 300):
            li7.append((i, j))
    for i in range(101, 200):
        for j in range(201, 300):
            li8.append((i, j))
    for i in range(201, 300):
        for j in range(201, 300):
            li9.append((i, j))

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if pygame.mouse.get_focused() and (pygame.mouse.get_pressed() == (1, 0, 0)) and turn=="human":#human turn
                if pygame.mouse.get_pos() in li1 and checked[0] == False:
                    checked[0] = True
                    if x == True:
                        screen.blit(cross, (0, 0))
                        x = False
                        o = True
                        boxval[0] = 'x'
                        turn = "ai"
                    elif o == True:
                        screen.blit(circle, (0, 0))
                        o = False
                        x = True
                        boxval[0] = 'o'
                        turn = "ai"
                elif pygame.mouse.get_pos() in li2 and checked[1] == False:
                    checked[1] = True
                    if x == True:
                        screen.blit(cross, (101, 0))
                        x = False
                        o = True
                        boxval[1] = 'x'
                        turn = "ai"
                    elif o == True:
                        screen.blit(circle, (101, 0))
                        o = False
                        x = True
                        boxval[1] = 'o'
                        turn = "ai"
                elif pygame.mouse.get_pos() in li3 and checked[2] == False:
                    checked[2] = True
                    if x == True:
                        screen.blit(cross, (201, 0))
                        x = False
                        o = True
                        boxval[2] = 'x'
                        turn = "ai"
                    elif o == True:
                        screen.blit(circle, (201, 0))
                        o = False
                        x = True
                        boxval[2] = 'o'
                        turn = "ai"
                elif pygame.mouse.get_pos() in li4 and checked[3] == False:
                    checked[3] = True
                    if x == True:
                        screen.blit(cross, (0, 101))
                        x = False
                        o = True
                        boxval[3] = 'x'
                        turn = "ai"
                    elif o == True:
                        screen.blit(circle, (0, 101))
                        o = False
                        x = True
                        boxval[3] = 'o'
                        turn = "ai"
                elif pygame.mouse.get_pos() in li5 and checked[4] == False:
                    checked[4] = True
                    if x == True:
                        screen.blit(cross, (101, 101))
                        x = False
                        o = True
                        boxval[4] = 'x'
                        turn = "ai"
                    elif o == True:
                        screen.blit(circle, (101, 101))
                        o = False
                        x = True
                        boxval[4] = 'o'
                        turn = "ai"
                elif pygame.mouse.get_pos() in li6 and checked[5] == False:
                    checked[5] = True
                    if x == True:
                        screen.blit(cross, (201, 101))
                        x = False
                        o = True
                        boxval[5] = 'x'
                        turn = "ai"
                    elif o == True:
                        screen.blit(circle, (201, 101))
                        o = False
                        x = True
                        boxval[5] = 'o'
                        turn = "ai"
                elif pygame.mouse.get_pos() in li7 and checked[6] == False:
                    checked[6] = True
                    if x == True:
                        screen.blit(cross, (0, 201))
                        x = False
                        o = True
                        boxval[6] = 'x'
                        turn = "ai"
                    elif o == True:
                        screen.blit(circle, (0, 201))
                        o = False
                        x = True
                        boxval[6] = 'o'
                        turn = "ai"
                elif pygame.mouse.get_pos() in li8 and checked[7] == False:
                    checked[7] = True
                    if x == True:
                        screen.blit(cross, (101, 201))
                        x = False
                        o = True
                        boxval[7] = 'x'
                        turn = "ai"
                    elif o == True:
                        screen.blit(circle, (101, 201))
                        o = False
                        x = True
                        boxval[7] = 'o'
                        turn = "ai"
                elif pygame.mouse.get_pos() in li9 and checked[8] == False:
                    checked[8] = True
                    if x == True:
                        screen.blit(cross, (201, 201))
                        x = False
                        o = True
                        boxval[8] = 'x'
                        turn = "ai"
                    elif o == True:
                        screen.blit(circle, (201, 201))
                        o = False
                        x = True
                        boxval[8] = 'o'
                        turn = "ai"

            elif turn=="ai":#ai turn
                turn="human"
                move=calculate(x,o,boxval)
                checked[move]=True
                if move==0:
                    x_pos=0
                    y_pos=0
                elif move==1:
                    x_pos = 101
                    y_pos = 0
                elif move==2:
                    x_pos = 201
                    y_pos = 0
                elif move==3:
                    x_pos = 0
                    y_pos = 101
                elif move==4:
                    x_pos = 101
                    y_pos = 101
                elif move==5:
                    x_pos = 201
                    y_pos = 101
                elif move==6:
                    x_pos = 0
                    y_pos = 201
                elif move==7:
                    x_pos = 101
                    y_pos = 201
                elif move==8:
                    x_pos = 201
                    y_pos = 201
                if x == True:
                    screen.blit(cross, (x_pos, y_pos))
                    x = False
                    o = True
                    boxval[move] = 'x'
                elif o == True:
                    screen.blit(circle, (x_pos, y_pos))
                    o = False
                    x = True
                    boxval[move] = 'o'
        if (boxval[0] == "x" and boxval[1] == "x" and boxval[2] == "x") or (
                boxval[3] == "x" and boxval[4] == "x" and boxval[5] == "x") or (
                boxval[6] == "x" and boxval[7] == "x" and boxval[8] == "x") or (
                boxval[0] == "x" and boxval[3] == "x" and boxval[6] == "x") or (
                boxval[1] == "x" and boxval[4] == "x" and boxval[7] == "x") or (
                boxval[2] == "x" and boxval[5] == "x" and boxval[8] == "x") or (
                boxval[0] == "x" and boxval[4] == "x" and boxval[8] == "x") or (
                boxval[2] == "x" and boxval[4] == "x" and boxval[6] == "x"):
            win = "x"
            break
        elif  (boxval[0] == "o" and boxval[1] == "o" and boxval[2] == "o") or (
                boxval[3] == "o" and boxval[4] == "o" and boxval[5] == "o") or (
                boxval[6] == "o" and boxval[7] == "o" and boxval[8] == "o") or (
                boxval[0] == "o" and boxval[3] == "o" and boxval[6] == "o") or (
                boxval[1] == "o" and boxval[4] == "o" and boxval[7] == "o") or (
                boxval[2] == "o" and boxval[5] == "o" and boxval[8] == "o") or (
                boxval[0] == "o" and boxval[4] == "o" and boxval[8] == "o") or (
                boxval[2] == "o" and boxval[4] == "o" and boxval[6] == "o"):
            win = "o"
            break
        elif (checked[0] == True) and (checked[1] == True) and (checked[2] == True) and (checked[3] == True) and (
                checked[4] == True) and (checked[5] == True) and (checked[6] == True) and (checked[7] == True) and (
                checked[8] == True):
            win = ""
            break
        pygame.display.update()
    pygame.display.update()
    time.sleep(1)
    screen.fill((0, 0, 0))
    if win == "x":
        screen.blit(cross_wins, (110, 110))
    elif win == "o":
        screen.blit(circle_wins, (110, 110))
    else:
        screen.blit(draw, (110, 110))
    pygame.display.update()
    time.sleep(1)