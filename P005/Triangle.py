import turtle
input_number_1 = int(input('enter the number: '))
square = turtle.Turtle()
for f in range(0,input_number_1):
    square.left(90)
    square.forward(input_number_1*30)
    square.backward(input_number_1*30)
    square.right(90)
    square.forward(30)
square.left(90)
for g in range(0,input_number_1):
    square.forward(30)
    square.left(90)
    square.forward(input_number_1*30)
    square.backward(input_number_1*30)
    square.right(90)
input_number_2 = input('player: ').split(',')
player = turtle.Turtle()
player.shape('circle')
player.shapesize(2,1,1)
player.color('red')
player.penup()
player.goto(int(input_number_2[0])*30,int(input_number_2[1])*30)
input_number_3 = input('ball: ').split(',')
Ball = turtle.Turtle()
Ball.shape('circle')
Ball.color('green')
Ball.penup()
Ball.goto(int(input_number_3[0])*30,int(input_number_3[1])*30)
check = turtle.Turtle()
input_number_4 = input('football gate: ').split(' ')
football_gate_0_input = input_number_4[0].split(',')
football_gate_0=(int(football_gate_0_input[0]),int(football_gate_0_input[1]))
check.goto(football_gate_0[0]*30,football_gate_0[1]*30)
check.color('blue')
football_gate_1_input = input_number_4[1].split(',')
football_gate_1 = (int(football_gate_1_input[0]),int(football_gate_1_input[1]))
check.goto(football_gate_1[0]*30,football_gate_1[1]*30)
subtract = ((int((football_gate_1[0]-football_gate_0[0])/2)+football_gate_0[0])*30,(int((football_gate_1[1]-football_gate_0[1])/2)+football_gate_0[1])*30)
ball_position_0 = Ball.position()
P_position_0 = player.position()
if football_gate_0[0] == football_gate_1[0]:
    if subtract[1] > ball_position_0[1]:
        for go_2 in range(P_position_0[1],ball_position_0[1]-60,-30):
            player.goto(P_position_0[0],go_2)
    else:
        for go_1 in range(P_position_0[1],ball_position_0[1]+60,30):
            player.goto(P_position_0[0],go_1)
    P_position_1 = player.position()
    if ball_position_0[0] < P_position_0[0]:
        for go_3 in range(P_position_0[0],ball_position_0[0]-30,-30):
            player.goto(go_3,P_position_1[1])
    if ball_position_0[0] > P_position_0[0]:
        for go_4 in range(P_position_1[0],ball_position_0[0]+30,30):
            player.goto(go_4,P_position_1[1])
    if ball_position_0[1]<subtract[1]:
        for walk_together_1 in range(ball_position_0[1],subtract[1]+30,30):
            ball_position_1 = Ball.position()
            player.goto(ball_position_1[0],walk_together_1-30)
            Ball.goto(ball_position_0[0],walk_together_1)
    else:
        for walk_together_2 in range(ball_position_0[1],subtract[1]-30,-30):
            ball_position_2 = Ball.position()
            player.goto(ball_position_2[0],walk_together_2+30)
            Ball.goto(ball_position_2[0],walk_together_2)
    ball_pos = Ball.position()
    P_position_4=player.position()
    if ball_pos[1]>P_position_4[1]:
        player.goto(ball_pos[0]+30,ball_pos[1])
    else:
        player.goto(ball_pos[0]+30,ball_pos[1])
    input()
    if subtract[0]>ball_pos[0]:
        for finish_1 in range(ball_pos[0],subtract[0]+30,30):
            player.goto(finish_1-30,ball_pos[1])
            Ball.goto(finish_1,ball_pos[1])
    if subtract[0]<ball_pos[0]:
        for finish_2 in range(ball_pos[0],subtract[0]-30,-30):
            player.goto(finish_2+30,ball_pos[1])
            Ball.goto(finish_2,ball_pos[1])
else:
    print(subtract[0],ball_position_0[0])
    if subtract[0] > ball_position_0[0]:
        for go_5 in range(P_position_0[0],ball_position_0[0]-60,-30):
            player.goto(go_5,P_position_0[1])
    else:
        for go_6 in range(P_position_0[0],ball_position_0[0]+60,30):
            player.goto(go_6,P_position_0[0])
    a = input()
    P_position_2 = player.position()
    if ball_position_0[1] < P_position_2[1]:
        for go_3 in range(P_position_0[1],ball_position_0[1]-30,-30):
            player.goto(P_position_2[0],go_3)
    if ball_position_0[1] > P_position_2[1]:
        for go_4 in range(P_position_0[1],ball_position_0[1]+30,30):
            player.goto(P_position_2[0],go_4)
    a = input()
    if ball_position_0[0]<subtract[0]:
        for walk_together_1 in range(ball_position_0[0],subtract[0]+30,30):
            ball_position_3 = Ball.position()
            player.goto(walk_together_1-30,ball_position_3[1])
            Ball.goto(walk_together_1,ball_position_3[1])
    else:
        for walk_together_2 in range(ball_position_0[0],subtract[0]-30,-30):
            ball_position_2 = Ball.position()
            player.goto(walk_together_2+30,ball_position_2[1])
            Ball.goto(walk_together_2,ball_position_2[1])
    a = input()
    ball_pos = Ball.position()
    if subtract[0]>ball_pos[0]:
        player.goto(ball_pos[0],ball_pos[1]+30)
    else:
        player.goto(ball_pos[0],ball_pos[1]-30)
    if subtract[1]>ball_pos[1]:
        for finish_1 in range(ball_pos[1],subtract[1]+30,30):
            player.goto(ball_pos[0],finish_1)
            Ball.goto(ball_pos[0]+30,finish_1)
    else:
        for finish_2 in range(ball_pos[1],subtract[1]-30,-30):
            player.goto(ball_pos[0],finish_2)
            Ball.goto(ball_pos[10]+30,finish_2)
input()