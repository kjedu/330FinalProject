to_do = [] #stores task from users

def options(): #define statement for options that users want
        print(" " "To-Do List" " ") #Title of list
        print("1, Add Task") #option to add a task
        print("2, Delete Task") #option to delete a task
        print("3, Display Task") #option to display all task added to list
        print("4, Mark Complete") #option to mark task complete
        print("5, Exit") #option to exit if no more adds,delete, displays or mark completes.

def add_task(): #define statement for adding task to list
    task = input("Enter task: ") #allows users to input the task description
    to_do.append({'Task': task, 'Complete': False}) #adds task to list as incomplete for default
    print(f'{task}' ' :Has been added to your To-Do List!') #confirmation that a task has been added.
    dis_play()

def delete_task(): #define statement for deleting task in list
    dis_play() #shows current to-do list items
    num = int(input('Enter number task you wish to delete: ')) #prompts user to input the number of the task need to be deleted.
    if 1 <= num <= len(to_do): #makes sure that number is vaild
        del_task = to_do.pop(num - 1) #removes task from list
        print(f"'{del_task['Task']}' :Has been removed from your To-Do List!") #confirmation that task has been deleted.
    else:
        print("Error") #if user inputs an invalid number this will execute.
    dis_play()

def dis_play(): #define statement for displaying list
    if not to_do: #checks to-do list if empty
        print('No task To-Do.') #will execute if list is empty.
    else:
        print("Your To-Do List: ") #will execute if there is items in list.
        for display, item in enumerate(to_do, 1): #lists each task while displaying number option in front of task.
            status = "Complete" if item['Complete'] else 'Incomplete' #checks if task is complete or incomplete
            print(f"{display}. {item['Task']} - {status}") #this will display the task with its status of incomplete or complete.


def mark_complete(): #define function of marking a task complete
    dis_play() #shows the current to-do list
    num = int(input("Enter the number of task that is complete: ")) #user will input the task number that needs to be marked complete
    if 1 <= num <= len(to_do): #makes sure the number user inputed aligns with the to-do list numbers.
        to_do[num - 1]['Complete'] = True #changes incomplete to complete
        print(f"'{to_do[num - 1]['Task']}' :Has been checked off as Complete.") #confirmation that a change has been made to user task status.
    else:
        print('Error') #will execute if number input is not aligned with the current to-do list
    dis_play()

def lists(): #a main function of the to-do list
    while True: #while loop statement for looping unit user inputs option 5
        options() #will display the number of options available.
        number = int(input('Enter selection 1-5: ')) #allows users to input the option they want
        if number == 1: #adds task
            add_task()
        elif number == 2: #deletes task
            delete_task()
        elif number == 3: #displays task
            dis_play()
        elif number == 4: #marks completion of task
            mark_complete()
        elif number == 5: #exit to-do list
            print('Exiting To-Do List.') #confirmation of option 5
            break
        else:
            print('Error') #prints if user input an invalid option number

lists() #calls on def lists() to allow loop to start.