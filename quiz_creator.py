import os
from tkinter import *

#constants
WINDOW_HEIGHT = 300
WINDOW_WIDTH = 300
SUBWINDOW_HEIGHT = 600
SUBWINDOW_WIDTH = 800
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

def create_quiz_creation_window():
#create quiz writing window
    main_window.destroy()
    write_window = Tk()
    write_window.title(WINDOW_TITLE)
    write_window.resizable(False, False)
    write_window.config(bg=WINDOW_BACKGROUND)

#centralizing window
    screen_position_x = int((screen_width / 2) - (SUBWINDOW_WIDTH / 2)) 
    screen_position_y = int((screen_height / 2) - (SUBWINDOW_HEIGHT / 2)) - 20

    write_window.geometry(f"{SUBWINDOW_WIDTH}x{SUBWINDOW_HEIGHT}+{screen_position_x}+{screen_position_y}")

#inputs
    quiz_problem_label = Label(write_window, text=f"Question {iteration}:", font=("Arial", 15, "bold"), bg="#FFFFFF")
    quiz_problem_label.place(x=0, y=0)
    quiz_problem = Text(font=("Arial", 15), width=72, height=4)
    quiz_problem.place(x=0, y=30)
    
    answer_a_label = Label(write_window, text=f"Answer A:", font=("Arial", 15, "bold"), bg="#FFFFFF")
    answer_a_label.place(x=0, y=130)
    answer_a = Entry(font=("Arial", 15), width=72)
    answer_a.place(x=0, y=160)

    answer_b_label = Label(write_window, text=f"Answer B:", font=("Arial", 15, "bold"), bg="#FFFFFF")
    answer_b_label.place(x=0, y=190)
    answer_b = Entry(font=("Arial", 15), width=72)
    answer_b.place(x=0, y=220)

    answer_c_label = Label(write_window, text=f"Answer C:", font=("Arial", 15, "bold"), bg="#FFFFFF")
    answer_c_label.place(x=0, y=250)
    answer_c = Entry(font=("Arial", 15), width=72)
    answer_c.place(x=0, y=290)

    answer_d_label = Label(write_window, text=f"Answer D:", font=("Arial", 15, "bold"), bg="#FFFFFF")
    answer_d_label.place(x=0, y=325)
    answer_d = Entry(font=("Arial", 15), width=72)
    answer_d.place(x=0, y=355)

    correct_answer_label = Label(write_window, text=f"Correct Answer:", font=("Arial", 15, "bold"), bg="#FFFFFF")
    correct_answer_label.place(x=0, y=385)
    correct_answer = Entry(font=("Arial", 15), width=72)
    correct_answer.place(x=0, y=415)
    
    write_window.mainloop()

#interface window
main_window = Tk()

main_window.title(WINDOW_TITLE)
main_window.resizable(False, False)
main_window.config(bg=WINDOW_BACKGROUND)

#process of centralizing window
screen_width = main_window.winfo_screenwidth()
screen_height = main_window.winfo_screenheight()

screen_position_x = int((screen_width / 2) - (WINDOW_WIDTH / 2)) 
screen_position_y = int((screen_height / 2) - (WINDOW_HEIGHT / 2)) - 20

main_window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{screen_position_x}+{screen_position_y}")

#buttons
create_button = Button(main_window, text="Create New Quiz", command=create_quiz_creation_window)
create_button.config(bg=BUTTON_COLOR, fg=TEXT_COLOR, relief=SUNKEN)
create_button.config(font=("Arial", 20, "bold"))
create_button.place(x=30, y=60)

read_button = Button(main_window, text="Read Quiz File", command=create_quiz, state=DISABLED)
read_button.config(bg=BUTTON_COLOR, fg=TEXT_COLOR, relief=SUNKEN)
read_button.config(font=("Arial", 20, "bold"))
read_button.place(x=40, y=180)

main_window.mainloop()
             
