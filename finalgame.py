import os
import time

table=[[5,0,0,6,0,0,9,0,3],
       [0,3,0,0,0,1,0,7,0],
       [2,0,1,0,3,4,8,0,0],
       [0,9,3,0,0,0,0,0,6],
       [0,0,6,0,1,0,3,0,0],
       [7,0,0,0,0,0,4,9,0],
       [0,0,5,4,7,0,1,0,9],
       [0,1,0,8,0,0,0,4,0],
       [8,0,4,0,0,6,0,0,7]]

#numbers for deleting
tablefix=[[5,0,0,6,0,0,9,0,3],
         [0,3,0,0,0,1,0,7,0],
         [2,0,1,0,3,4,8,0,0],
         [0,9,3,0,0,0,0,0,6],
         [0,0,6,0,1,0,3,0,0],
         [7,0,0,0,0,0,4,9,0],
         [0,0,5,4,7,0,1,0,9],
         [0,1,0,8,0,0,0,4,0],
         [8,0,4,0,0,6,0,0,7]]

#completed board
tablefull = [[5,4,8,6,2,7,9,1,3],
             [6,3,9,5,8,1,2,7,4],
             [2,7,1,9,3,4,8,6,5],
             [1,9,3,2,4,8,7,5,6],
             [4,5,6,7,1,9,3,2,8],
             [7,8,2,3,6,5,4,9,1],
             [3,6,5,4,7,2,1,8,9],
             [9,1,7,8,5,3,6,4,2],
             [8,2,4,1,9,6,5,3,7]]

def clear():
    '''Clears the board'''
    os.system('cls' if os.name=='nt' else 'clear')

def startscreen():
   while True:
       clear()
       start=input('''This is a simple sudoku game 
       \n If you want to know more about the RULES, please enter: rules! 
       \n If you want to PLAY the game, please enter: play!
       \n If you want to EXIT from the game, please enter: exit!''') 
       start=start.lower()
       if start=="play":
           return
       if start=="rules":
           clear()
           print('''Fill a number in to every cell in the grid, using the numbers 1 to 9.
           \n You can only use each number once in each row, each column, and in each of the 3×3 boxes!''')
           time.sleep(3)
           continue
       if start=="exit":
           quit()

def finish():
    answer=input('Done? Enter yes or no!')
    if answer == "yes":
        if str(table) != str(tablefull):
            print('Sorry, You haven\'t finished yet! Try again!')
            return False
    elif str(table) == str(tablefull):
        print('Sorry, You\'ve already finished!')
        time.sleep(3)
    else:
        return False
    clear()
    print('Well done!')
    quit()

def draw():
    '''Draws the sudoku and calls the refresh function when finished'''
    clear()
    colorclose="\x1b[0m"
    colorg="\033[1;32m"
    colorw="\033[1;37m"
    colorr="\033[1;31m"
    print(colorg+"  | 1 2 3 | 4 5 6 | 7 8 9 |"+colorclose)
    print("---"*9)
    counter=1
    for row in range(0,len(table)):
        if row == 3 or row == 6:
            print("---"*9)
        print(colorg+str(counter)+colorclose+" | ",end="")
        for column in range(0,len(table[0])):
            if column == 3 or column == 6:
                print("| ",end="")
            if(tablefix[row][column] == 0):
                print(colorw+str(table[row][column])+colorclose+" ",end="")
            else:
                print(colorr+str(table[row][column])+colorclose+" ",end="")
        counter += 1
        print("|")
    print("---"*9)
    refresh()
    
def initialize():
    '''Replaces the table elements containing zero with a dot'''
    for i in range(0,9):
        for j in range(0,9):
            if table[i][j]==0:
                table[i][j]="."
    draw()
   
def userinput(rowcolnum):
    '''Fills a new list with only the int elements of the given string and returns with the list'''
    rcn_list=[]
    for i in range(len(rowcolnum)):
        if  rowcolnum[i] != " ":
            if rowcolnum[i].isdigit() != True:
                print('Please enter numbers!')
                return []
            else:
                rcn_list.append(int(rowcolnum[i]))
    return rcn_list

def inputfordelete(delete):
    '''From the given input it checks the table and deletes the element if its not a fixed one'''
    drcnlist=[]
    if delete == "N":
        return 
    elif delete == "Y":  
        drcnlist=userinput(input('Enter 2 value for delete [rows][columns]:'))
        while len(drcnlist) != 0:
            if (len(drcnlist) > 3) or (drcnlist == []) or (0 in drcnlist):
                print('Please enter 1-9 numbers!')
                drcnlist = userinput(input()) 
                continue  
            elif tablefix[drcnlist[0]-1][drcnlist[1]-1] == 0:
                table[(drcnlist[0])-1][(drcnlist[1])-1] = "."
                draw()
            else:
                print("It\'s a fix number, you can't delete that!")
                time.sleep(1)
                refresh()
    elif delete =="Q":
        quit()
    else:
        refresh()

def maininput():
    '''Checks the input and updated the table if the input is valid'''
    rcnlist=[]
    while len(rcnlist) == 0:
        inputfordelete(input('Press N to CONTINUE or Y to delete or Q to exit!'))
        rcnlist = userinput(input('Enter 3 value [rows][columns][number to write]:'))
        if (len(rcnlist) > 3) or (rcnlist == []) or (0 in rcnlist):
            print('Please enter 1-9 numbers!')
            continue 
        elif table[(rcnlist[0])-1][(rcnlist[1])-1] == ".":
            table[(rcnlist[0])-1][(rcnlist[1])-1] = rcnlist[2]
            draw()
        else:
            print('It\'s a fix number, enter another!')
            continue

def refresh():
    '''Refreshes the console output'''
    while str(table) != str(tablefull):
        x=False
        if "." not in str(table):
            x=finish()
        if x==True:
            continue
        maininput()
    finish()

'''Program starts here'''
clear()
startscreen()
initialize()