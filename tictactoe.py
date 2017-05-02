import random
def inputsymbol(board,p,s):
    board[p-1]=s
def checkingwin(board,p):
    if (board[0] == p and board[1] == p and board[2] == p) or (board[3] == p and board[4] == p and board[5]==p) or (board[6]==p and board[7]==p and board[8]==p):
        return(True)
    if (board[0]==p and board[3]==p and board[6]==p) or (board[1]==p and board[4]==p and board[7]==p) or (board[2]==p and board[5]==p and board[8]==p):
        return(True)
    if (board[0]==p and board[4]==p and board[8] == p) or (board[2]== p and board[4] == p and board[6]==p):
        return(True)
    else:
        return(False)
def checkingtie(board):
    if board.count(' ')==0:
        return True
    else:
        return False
def getcopy(board):
    boardcopy=[]
    for i in board:
        boardcopy.append(i)
    return(boardcopy)
def possiblemove(bo):
    plist=[]
    for i in range(0,9):
        if bo[i]==' ':
            plist.append(int(i))
    return(plist)
def machine_move(b,s,p):
    if b.count(p)== 1:
        ini=b.index(p)
        if ini==0:
            if b[8]==' ':
                b[8]=s
                return(False)
        elif ini ==2:
            if b[6]==' ':
                b[6]=s
                return(False)
        elif ini == 6:
            if b[2]==' ':
                b[2]=s
                return(False)
        elif ini == 8:
            if b[0]==' ':
                b[0] =s
                return(False)
    for i in range(0,9):
        copy=getcopy(b)
        if copy[i]==' ':
            copy[i]=s
            if checkingwin(copy,s):
                b[i]=s
                return(True)
    for j in range(0,9):
        copy=getcopy(b)
        if copy[j]==' ':
            copy[j]=p
            if checkingwin(copy,p):
                b[j]=s
                return(False)
    possible_moves=possiblemove(b)
    corner=[]
    side=[]
    for i in possible_moves:
        if i%2==0 and i!=4:
            corner.append(i)
        if i%2!=0:
            side.append(i)
    if len(corner)!=0:
        move1=random.choice(corner)
        b[move1]=s
        return(False)
    elif b[4] == ' ':
        b[4]=s
        return(False)
    else:
        move1=random.choice(side)
        b[move1]=s
        return(False)
def printboard(board):
    print(' ','+---'*3,'+',sep='')
    print(' | ',board[0],' | ',board[1],' | ',board[2],' | ',sep='')
    print(' ','+---'*3,'+',sep='')
    print(' | ',board[3],' | ',board[4],' | ',board[5],' | ',sep='')
    print(' ','+---'*3,'+',sep='')
    print(' | ',board[6],' | ',board[7],' | ',board[8],' | ',sep='')
    print(' ','+---'*3,'+',sep='')
def sampleboard():
    print("< sample board >".center(60,'$'))
    print(' ','+---'*3,'+',sep='')
    print(' | ','1',' | ','2',' | ','3',' | ',sep='')
    print(' ','+---'*3,'+',sep='')
    print(' | ','4',' | ','5',' | ','6',' | ',sep='')
    print(' ','+---'*3,'+',sep='')
    print(' | ','7',' | ','8',' | ','9',' | ',sep='')
    print(' ','+---'*3,'+',sep='')
def getplayersymbol():
    while True:
        try:
            symbol=input("enter the your symbol ('O' or 'X')\n your symbol:")
            symbol=symbol.upper()
        except:
            print("enter correct symbol".center(60,'-'))
        else:
            if symbol!='O' and symbol!='X':
                print("enter correct symbol".center(60,'-'))
                print('try again....')
                continue
            elif symbol=='X':
                return('X','O')
            else:
                return('O','X')
            if symbol=='X' or symbol == 'O':
                break
def toss():
    turn=random.randint(0,10)
    if turn%2==0:
        turn='O'
    else:
        turn='X'
    return(turn)
def playagain():
    print("do you want to play again(y/n)")
    while True:
        try:
            try1=input("enter: ")
        except:
            print("enter the proper choice")
            continue
        else:
            if try1!='y' and try1!='n':
                print(" enter correct option-(y/n) ".center(60,'*'))
                continue
            else:
                if try1=='y':
                    tictactoe()
                else:
                    print(" exited ".center(60,'-'))
                    exit()
                    break
def tictactoe():
    board=[' ']*9
    sampleboard()
    print("game starts".center(60,'-'))
    player_symbol,machine_symbol=getplayersymbol()
    print('\n','toss begins.....')
    turn=toss()
    if turn==player_symbol:
        print('\n',' player goes first '.center(60,'*'))
    else:
        print('\n',' machine goes first '.center(60,'*'))
    while True:
        if turn==player_symbol:
            print('\n',"your turn.....")
            while True:
                try:
                    position=int(input('enter :'))
                except:
                    print(" integer only ".center(60,'-'))
                    continue
                else:
                    if position < 1 or position > 9:
                        print(" enter correct position(1-9) ".center(60,'-'))
                        sampleboard()
                        print(" try again....")
                        continue
                    elif board[position-1]!=' ':
                        print(' position is already filled ')
                        print(" try again....")
                        continue
                    else:
                        inputsymbol(board,position,player_symbol)
                        printboard(board) 
                        check1=checkingwin(board,player_symbol)
                        if check1:
                            print(" wow! you are won ".center(60,'*'))
                            playagain()
                        else:
                            tie_status=checkingtie(board)
                            if tie_status:
                                print(' match is tie '.center(60,'-'))
                                playagain()
                            else:
                                turn=machine_move
                                break
        else:
            print("machine move")
            status=machine_move(board,machine_symbol,player_symbol)
            if status:
                printboard(board)
                print(" sorry baby machine won ".center(60,'*'))
                playagain()
            else:
                printboard(board)
                tie_status=checkingtie(board)
                if tie_status:
                    print(' match is tie '.center(60,'-'))
                    playagain()
                else:
                    turn=player_symbol
print("  game is started  ".center(60,'*'))
tictactoe()
