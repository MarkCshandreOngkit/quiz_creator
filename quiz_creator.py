import os
from tkinter import *

#constants
WINDOW_HEIGHT = 300
WINDOW_WIDTH = 300
WINDOW_TITLE = "Quiz Creator"
WINDOW_BACKGROUND = "#FFFFFF"
TEXT_COLOR = "#000000"

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

window = Tk()

window.title(WINDOW_TITLE)
window.resizable(False, False)

create_button = Button(window, text="Create New Quiz")
create_button.config(command=create_quiz)
create_button.config(font=("Arial", 25, "bold"))
create_button.pack()

canvas = Canvas(window, bg=WINDOW_BACKGROUND, height=WINDOW_HEIGHT, width=WINDOW_WIDTH)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x_position = int((screen_width / 2) - (window_width / 2)) 
y_position = int((screen_height / 2) - (window_height / 2)) - 20

window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

window.mainloop()
             
