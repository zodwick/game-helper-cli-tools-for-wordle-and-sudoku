
#inputing board

print(' Please Enter your sudoku from left to right top to bottom')
print('Use 0 to mark blank spaces')
print('Do not use comma or spaces in between numbers')
x=input()
if len(x)!=81:
    print("ERROR u didnt input the entire 9*9 sudoku")
board=[]
for j in range(8,81,9):
    y=x[j-8:j+1]
    l = []
    for i in y:
        l.append(eval(i))
    board.append(l)



def solve(sudo):

    position=find_empty(sudo)
    if not position:
        return True

    for i in  range(1,10):
        if valid_check(i,position,sudo):
            sudo[position[0]][position[1]]=i

            if solve(sudo):
                return True

        sudo[position[0]][position[1]] = 0

    return False





def valid_check(num,pos,sudo):
    #chck row
    for i in range(len(sudo[0])):
        if sudo[pos[0]][i]==num and i!=pos[1]:
            return False


    #check coloumn

    for i in range(len(sudo)):
        if sudo[i][pos[1]]==num and i!=pos[0]:
            return False

    #check sqr thingy
    x=pos[0]//3
    y=pos[1]//3
    for i in range(x*3,x*3+3):
        for j in range(y*3,y*3+3):
            if sudo[i][j]==num and pos!=(i,j):
                return False

    return True

def find_empty(sudo):

    for i in range(len(sudo)):

        for j in range(len(sudo[0])):
            if sudo[i][j]==0:
                return (i,j)
                        #i=row , j=col
    return None




def print_sudo(sud):

    for i in range(len(sud)):
        if i%3==0 and i!=0:
            print("---------------------------------")

        for j in range(len(sud[0])):
            if j%3==0 and  j!=0:
                print("|"," ",end='')

            print(sud[i][j]," " ,end='')


            if j==8:
                print()

print_sudo(board)
solve(board)

print('......................................'
      '.....................................')
print_sudo(board)




