# CLASSES AND METHODS
class Person():
    def __init__(self, name, bio, age):
        # your code goes here!
        self.name = name
        self.bio = bio
        self.age = age

        
class Club():
    def __init__(self, name, description,member_list):
        # your code goes here!
        self.name = name
        self.description = description
        self.member_list = member_list
        #self.NumMem = len(member_list)


    def assign_president(self, person):
        # your code goes here!
        self.member_list.append(person)


    def recruit_member(self, person):
        # your code goes here!
        self.member_list.append(person)

    def print_member_list(self,my_age,condition):
        # your code goes here!
        avg = []
        count = 0
        for i in self.member_list:
            avg.append(int(i.age))
            count += int(i.age)
            print("- %s (%s years old) - %s\n" % (i.name,i.age,i.bio))

        if condition == False:
            print("The average age in this club is: %.2f yr" % float(count/len(avg)))
        else:
            print("The average age in this club is: %.2f yr" % float((count)/(len(avg))))
            #print("The average age in this club is: %.2f yr" % float((count+int(my_age))/(len(avg)+1)))
        print("-----------------------------------------")
