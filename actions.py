# UTILS AND FUNCTIONALITY
from data import  population, clubs
from components import Club, Person

my_name = input("Enter your name: ")

while True:
    my_age = input("Enter Your age: ")
    try:
        if type(int(my_age)) == int:
            break
    except ValueError:
        print("~Enter an integer number to indicate you age~")
        
my_bio = input("Type a bio for yourself: ")
myself = Person(my_name, my_bio, my_age,"President")

def introduction():
    print("Hello, %s. Welcome to our portal." % my_name)
    print("-----------------------------------------")

def options():
    # your code goes here!
    while True:
        print("Would you like to:")
        print("1) Create a new club.")
        print("2) Browse and join clubs.")
        print("3) View existing clubs.")
        print("4) Display members of a club.")
        print("-1) Close application.")
        option = input("Enter an option: ")
        print("-----------------------------------------")
        if option == "1":
            create_club()
        elif option == "2":
            join_clubs()
        elif option == "3":
            view_clubs()
        elif option == "4":
            view_clubs()
            temp = input("Enter the name of the club whose members you'd like to see: ")
            while True:
                if check_name(clubs,temp)== True:
                    break
                else:
                    print("~The club name you entered doesn't match these in the list, please try again~")
                    temp = input("Enter the name of the club whose members you'd like to see: ")
            view_club_members(temp.lower())   
        elif option == "-1":
            break
        else:
            print("~The option you entered doesn't exist. Please enter the options that are shown above~")
            print("\n-----------------------------------------")

def create_club():
    # your code goes here!
    temp_name = input("Pick an name for your awesome new club: ")
    print("What is your club about?")
    temp_description = input()
    print("Enter the people you would like to recruit for your new club based")
    print("on their number shown in the bracket below.(-1 to stop)")
    print("-----------------------------------------")
    unselected = []
    selected = []
    for i in range(len(population)):
        print("[%d] %s" % (i+1,population[i].name))
        unselected.append(str(i+1))
    print("Unselected members:")
    print(unselected)
    print("selected members:")
    print(selected)
    my_members = []

    while True:
        temp = input("\nSelect a member number: ") 
        if temp in unselected and temp not in selected:
            selected.append(temp)
            unselected.remove(temp)
            print("Unselected members:")
            print(unselected)
            print("selected members:")
            print(selected)
            my_members.append(population[int(temp)-1])
        elif temp in selected:
            print("~You already selected this member, choose another one~")
        elif temp == "-1":               
            print("\nHere is your new club:")
            print("- %s (%s years old, President) - %s\n" % (myself.name,myself.age,myself.bio))
            #temp_club.print_member_list(my_age,True)
            print_members(my_members,True,myself)
            temp_club = Club(temp_name,temp_description,[])
            temp_club.member_list.append(myself)
            for i in my_members:
                temp_club.member_list.append(i)

            
            clubs.append(temp_club)
            break
        else:
            print("~The number you entered doesn't exist in the list given above~")


def view_clubs():
    # your code goes here!
    for i in clubs:
        print("NAME: %s" % i.name)
        print("DESCRIPTION: %s" % i.description)
        print("MEMBERS: %s\n" % len(i.member_list))
    
def view_club_members(club_name):
    # your code goes here!
    index = 0
    for i in clubs:
        if club_name == i.name.lower():
            print(index)
            if index > 3:
                #print("-### %s (%s years old) - %s\n" % (my_name,my_age,my_bio))
                i.print_member_list(my_age,True)
            else:
                i.print_member_list(my_age,False)
        index += 1    

def join_clubs():
    # your code goes here!
    view_clubs()
    temp = input("Enter the name of the club you'd like to join: ")
    while True:
        if check_name(clubs,temp)== True:
            for i in clubs:
                if i.name.lower() == temp.lower():
                    i.member_list.append(myself)
                    #i.NumOfMembers += 1
            print("   `%s just joined %s!`" % (my_name,i.name))
            print("-----------------------------------------")
            break
        else:
            print("~The club name you entered doesn't match these in the list, please try again~")
            temp = input("Enter the name of the club you'd like to join: ")

def application():
    introduction()
    # your code goes here!
    options()


def check_name(clubs,s_name):
    name_list = []
    for i in clubs:
        name_list.append(i.name.lower())

    if s_name in name_list:
        return True
    else:
        return False


def print_members(member_list,condition,Me):
    avg = []
    count = 0
    for i in member_list:
        avg.append(int(i.age))
        count += int(i.age)
        print("- %s (%s years old) - %s\n" % (i.name,i.age,i.bio))

    if condition == False:
        print("The average age in this club is: %.2f yr" % float(count/len(avg)))
    else:
        print("The average age in this club is: %.2f yr" % float((count+int(Me.age))/(len(avg)+1)))
    print("-----------------------------------------")
