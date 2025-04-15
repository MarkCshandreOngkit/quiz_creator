import os
from tkinter import *

#constants
WINDOW_HEIGHT = 300
WINDOW_WIDTH = 300
WINDOW_TITLE = "Quiz Creator"
WINDOW_BACKGROUND = "#FFFFFF"
BUTTON_COLOR = "#000000"
TEXT_COLOR = "#FFFFFF"

#initialization
iteration = 1
exit_decision = False

#functions
def exit():
#ask decision if exit
    global exit_decision
    #asking if continue
    ask_exit = input("Exit?(Y/N):\n>").lower()

    if ask_exit in ("y", "yes", "exit"):
        exit_decision = True
    elif ask_exit in ("n", "no", "continue"):
        exit_decision = False
    else:
        exit()

def check_file():
#check if file exist
    global file_name
    if os.path.exists(file_name):
        ask_overwrite = input("The file name you choose already exist. Overwrite it?(Y/N):\n> ")
        if ask_overwrite in ("y", "yes", "overwrite"):
            os.remove(file_name)
        elif ask_overwrite in ("n", "no"):
            file_name = input("File Name:\n> ") + ".txt"
            check_file()

def create_quiz():         
#create file
    with open("temp.txt", "a") as file:

        #loop
        while True:
            #ask for a question and write in file
            question = input("Question:\n> ")
            file.write(f"Question {iteration}: " + question + "\n")

            #ask for 4 answers and write in file
            answer_a = input("Answer A:\n> ")
            file.write("A: " + answer_a + "\n")

            answer_b = input("Answer B:\n> ")
            file.write("B: " + answer_b + "\n")

            answer_c = input("Answer C:\n> ")
            file.write("C: " + answer_c + "\n")

            answer_d = input("Answer D:\n> ")
            file.write("D: " + answer_d + "\n")

            #ask for correct answer and write in file
            correct_answer = input("Correct Answer:\n> ")
            file.write("Correct Answer: " + correct_answer + "\n")
            
            exit()

            if exit_decision == True:
                break
    #create file name
        file_name = input("File Name:\n> ") + ".txt"
        check_file()
    os.rename("temp.txt", file_name)

main_window = Tk()

main_window.title(WINDOW_TITLE)
main_window.resizable(False, False)
main_window.config(bg=WINDOW_BACKGROUND)

screen_width = main_window.winfo_screenwidth()
screen_height = main_window.winfo_screenheight()

screen_position_x = int((screen_width / 2) - (WINDOW_WIDTH / 2)) 
screen_position_y = int((screen_height / 2) - (WINDOW_HEIGHT / 2)) - 20

main_window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{screen_position_x}+{screen_position_y}")

create_button = Button(main_window, text="Create New Quiz", command=create_quiz)
create_button.config(bg=BUTTON_COLOR, fg=TEXT_COLOR, relief=SUNKEN)
create_button.config(font=("Arial", 20, "bold"))
create_button.place(x=30, y=60)

read_button = Button(main_window, text="Read Quiz File", command=create_quiz, state=DISABLED)
read_button.config(bg=BUTTON_COLOR, fg=TEXT_COLOR, relief=SUNKEN)
read_button.config(font=("Arial", 20, "bold"))
read_button.place(x=40, y=180)

main_window.mainloop()
             
