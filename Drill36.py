#7 - Use of conditional statements: if, elif, else

def demo():
    answer=input('\nWould you like to see a simple, a loop, other stuff, or exit? (simple/ loop / other/ exit):').lower()
    if answer == 'simple':
        remainder()
    elif answer == 'loop':
        while_demo()
    elif answer == 'other':
        start()
    elif answer == 'exit':
        print("\nThanks for using this demo. Good bye!")
        exit
    else:
        print("\nYou must type in 'simple, loop, other, or exit' to proceed: ")
        demo()
        

#5 - use of += operator <this is to increment by the value following the sign
#8 - use of a while loop <this is to demonstrate that as long as the value i
#    less than 100, increment by 10.

def while_demo():
    print ("\nHere's a while loop demo with a bonus of a += operator demo, incrementing your value by 10).")
    pick_First = input("\nPick a value from 1 to 10: ")
    i = int(pick_First)
    while i < 100:
        i+=10
        print (i)
    tuple_demo ()

#6 - Use of logical operators: and
#11 - Create a tuple and iterate through it using a for loop to print each item out of a new line
    
def tuple_demo ():
    print ("\nWell, that demo was boring. Let's try something else.")
    food_base = ("rice", "lettuce")
    food_fixin = ("barbacoa", "corn", "salsa")
    food_fixinExtra = ("guacamole", "cheese")
    my_preferences = food_base + food_fixin + food_fixinExtra
    base_choice = input("\nGuess what I like in my burrito bowl. If you guess correctly, my answer will be True. If incorrect, my answer will be False. What's your guess for my base?: ")
    fixin_choice1 = input("\nWhat's my must have item in my order?: ")
    fixin_choice2 = input("\nOkay, might as well make another guess. Anything else in my burrito bowl?: ")
                    
    make_food = (base_choice in food_base) and ((fixin_choice1 in food_fixin) or (fixin_choice2 in food_fixin))
    print ("nYour guess?", make_food)
    print ("\nFor my burrito bowl, I like: ")
    for my_preference in my_preferences:
        print(my_preference)
    
    
    demo()
        

#1 - Assign an integer to a variable
#2 - Assign a string to a variable
#5 - use of % operator
#12 - Define a function that returns a string variable
        
def remainder():
    print ("\nThis is a very simple demo, showing you the remainder when you divide something")
    pick_Second = input ("\nPlease enter your first number that's not a zero: ")
    pick_Second = int(pick_Second)                   
    pick_Third = input ("\nNow enter your second number that's not a zero: ")
    pick_Third = int(pick_Third)
    result = pick_Second%pick_Third
    print ("When you divide "+str(pick_Second)+" by "+str(pick_Third)+" ,the remainder is: "+str(result))
    demo()



names = ["Peter","Paul","Mary"]
current_GPAs = [3.0,1.0,3.75]
percentages = [85,65,95]


#9 - For loop
#10 - create a list and iterate through that list using a for loop to print each item out on a new line

def start():
    print ("\nYou currently have "+str(len(names))+" students.")
    names_str=", ".join(names)
    print("\nThey are: "+names_str)
    current_students = {}
    for name, current_GPA, percentage in zip(names, current_GPAs, percentages):
        current_students[name]=current_GPA, percentage
    print("\nBelow are records of your current students: ")
    for key, value in current_students.items():
        print(key, value)
    register_student()


#1 - Assigning integer to a variable
#2 - Assigning string to a variable
#3 - Assigning float to a variable
#5 - use of operators *, +, /, -, =
#7 - use of conditional statement if, else
#12 - Define a function that returns a string variable
    
#Please note that I cannot figure out why the format() notation in the def score_calc() does not work.


def score_calc(percent=0, GPA=0):
        full_score = input("\nPlease enter the full score: ")
        full_score = int(full_score)
        student_score = input("Please enter the {}'s score: ".format(new_studentName))
        student_score = int(student_score)
        extraCredit = input("Please enter any applicable extra credit: ")
        extraCredit = int(extraCredit)
        percent = round(float(100*((student_score+extraCredit)/full_score)),2)
        #rounding the percent calc result to 2 decimal points
        GPA = round(((100*((student_score+extraCredit)/full_score))/20)-1,2)
        #rounding GPA calc result to 2 decimal points
        print ("The student's final percentage is: "+str(percent)+"% \nCurrent GPA is: "+str(GPA))
        percentages.append(percent)
        current_GPAs.append(GPA)
        return percent, GPA


#4- Use the print function and .format() notation to print out the variable "new_studentName"

def register_student():
    print ("{} is now registered.".format(new_studentName()))
    print ("\nYou now have "+str(len(names))+" students.")
    names_str=", ".join(names)
    print("\nThey are: "+names_str)
    percent = score_calc()
    current_students = {}
    for name, current_GPA, percentage in zip(names, current_GPAs, percentages):
        current_students[name]=current_GPA, percentage
    print ("\nBelow are records of your current students: ")
    for key, value in current_students.items():
        print(key, value)
    register_more()



def new_studentName():
    new_studentName = input("\nTo register new student, please enter a name: ").capitalize()
    names.append(new_studentName)
    return new_studentName


def register_more():
    register_more = input("\nWould you like to register more students? y/n: ").lower()
    if register_more == "y":
        register_student()
#    if register_more == "n":
    else:
        print ("Have a great day!")
    demo()
    

if __name__=="__main__":
    demo()
   
