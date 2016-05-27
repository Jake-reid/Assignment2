"""Jake Reid Williams  4/11/16 Items for hire https://github.com/Jake-reid/CP1404ASSIGNMENT1"""

print ('Items for hire - Jake Reid-Williams')
# Welcome message

def display_item (rowinfo, rownumber):
    descsize = rowinfo[0] + rowinfo[1]
    space_num = 50 - len(descsize)
    in_out = ""
    if rowinfo[3] == 'out':
           in_out = "*"
    # set a * beside a rented item
    print(rownumber, ' - ', rowinfo[0], ',', rowinfo[1], ' ' * space_num, '= $', rowinfo[2], in_out)
    #this will have the prices lined up neatly
    return
#function to display the information for individual items
import csv

Name = ''
Description = ''
Cost = 0.00
Location = []
TakeOut = 0

ReturnItem = 0
itemout = 0
NewItem = []
row_info = []
MenuChoice = ''
writelist = []
writedict = {}
def read_write_csv(readwrite, list):
    with open('C:\Python34\items.csv', readwrite, newline='') as csvfile:

        if readwrite == 'r':
            useCSV = csv.reader(csvfile, delimiter=',')
            dataLines = [line for line in useCSV]
            return dataLines
        if readwrite == 'w':
            useCSV = csv.writer(csvfile, delimiter=',')
            useCSV.writerows(list)

dataLines = read_write_csv('r',[])
while MenuChoice != 'q':
    MenuChoice = input('(L)ist all items \n(H)ire an item \n(R)eturn an item \n(A)dd an item \n(Q)uit \n')
    MenuChoice = MenuChoice.lower()
    while len(MenuChoice) != 1:
        print('Incorrect entry')
        MenuChoice = input('(L)ist all items \n(H)ire an item \n(R)eturn an item \n(A)dd an item \n(Q)uit \n')
        MenuChoice = MenuChoice.lower()
    while MenuChoice not in 'lhraq':
        print('Incorrect entry')
        MenuChoice = input('(L)ist all items \n (H)ire an item \n (R)eturn an item \n (A)dd an item \n (Q)uit \n')
        MenuChoice = MenuChoice.lower()
#error check the menu input
    i=0
    j=0
    if MenuChoice == 'l':
        print('All items on file')
        for i in range(0,len(dataLines),1):

            display_item(dataLines[i], i)



    elif MenuChoice == 'h':
        i = 0
        print('All available items on file')
        for i in range(0,len(dataLines),1):
            if dataLines[i][3] == 'in':
                display_item(dataLines[i], i)
        TakeOut = input('Which item do you want to Hire(0, 1, 2...)')
        itemout = int(TakeOut)
        while itemout > i:           #check this logic
            print('Invalid input')
            TakeOut = input('Which item do you want to hire')
            itemout = int(TakeOut)
        dataLines[itemout][3] = 'out'




    elif MenuChoice == 'r':
        i = 0
        j = 0
        print('All items currently hired')
        for i in range(0,len(dataLines),1):
            if dataLines[i][3] == 'out':
                display_item(dataLines[i], i)
        ReturnItem = input('Which item to you wish to return')
        itemout = int(ReturnItem)
        while itemout > i:
            print('Invalid input')
            ReturnItem = input('Which item to you wish to return')
            itemout = int(ReturnItem)
        dataLines[itemout][3] = 'in'




    elif MenuChoice == 'a':
        Name = input('Please enter the name of the new item')
        print("Characters remaining:", 50 - len(Name))
        Description = input('Please enter a brief description of an item')
        while (len(Name) + len(Description)) >50:
            print("please keep the name and description under 50 characters")
            Name = input('Please enter the name of the new item')
            print("Characters remaining:", 50 - len(Name))
            Description = input('Please enter a brief description of an item')
        Cost = input('Please enter the cost in $AUD')
        NewItem.append(Name)
        NewItem.append(Description)
        NewItem.append(Cost)
        NewItem.append('in')
        dataLines.append(NewItem)


read_write_csv('w', dataLines)



