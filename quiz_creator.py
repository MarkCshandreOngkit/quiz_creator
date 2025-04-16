import os
from tkinter import *
from tkinter import messagebox

#constants
MAIN_WINDOW_HEIGHT = 300
MAIN_WINDOW_WIDTH = 300
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 800
SUBWINDOW_WIDTH = 250
SUBWINDOW_HEIGHT = 150
WINDOW_TITLE = "Quiz Creator"
WINDOW_BACKGROUND = "#000000"
BUTTON_COLOR = "#FFFFFF"
TEXT_COLOR = "#000000"
LABEL_COLOR = "#000000"
FONT_1 = ("Arial", 15, "bold")
ENTRY_FONT = ("Arial", 15)

#initialization
iteration = 1
exit_decision = False

#quiz creation window
def save_quiz_file_creation_window():
    #functions
    def submit():
        global question, answer_a, answer_b, answer_c, answer_d, correct_answer
        question = quiz_problem.get("1.0", "end-1c")
        answer_a = answer_a_entry.get()
        answer_b = answer_b_entry.get()
        answer_c = answer_c_entry.get()
        answer_d = answer_d_entry.get()
        correct_answer = correct_answer_entry.get()
        print(question, answer_a, answer_b, answer_c, answer_d, correct_answer)
    
    def save_quiz_file():         
    #create file
        with open("temp.txt", "a") as file:

            #ask for a question and write in file
            submit()

            file.write(f"Question {iteration}: " + question + "\n")

            #ask for 4 answers and write in file
            file.write("A: " + answer_a + "\n")

            file.write("B: " + answer_b + "\n")

            file.write("C: " + answer_c + "\n")

            file.write("D: " + answer_d + "\n")

            #ask for correct answer and write in file
            file.write("Correct Answer: " + correct_answer + "\n")
    
    def file_naming():
        def name_submit():
            global file_name
            file_name = file_name_entry.get()
            if file_name == "":
                file_name = "QuizFile.txt"
            else:
                file_name += ".txt"
            file_name_window.destroy()


        global file_name

        file_name_window = Toplevel(bg=WINDOW_BACKGROUND)
        screen_position_x = int((screen_width / 2) - (SUBWINDOW_WIDTH / 2)) 
        screen_position_y = int((screen_height / 2) - (SUBWINDOW_HEIGHT / 2)) - 20
        file_name_window.geometry(f"{SUBWINDOW_WIDTH}x{SUBWINDOW_HEIGHT}+{screen_position_x}+{screen_position_y}")
        file_name_window.focus()

        file_name_label = Label(file_name_window, text=f"Name your file:", font=FONT_1, fg="#FFFFFF", bg=LABEL_COLOR)
        file_name_label.place(x=0, y=0)
        check_string = StringVar(master=file_name_window)
        check_string.set("")
        file_name_entry = Entry(file_name_window, font=ENTRY_FONT, width=22, textvariable=check_string)
        file_name_entry.place(x=0, y=30)

        name_submit_button = Button(file_name_window, text="Submit", command=lambda:[name_submit(), check_overwrite_file()], font=("Arial", 15, "bold"), fg=TEXT_COLOR, bg=BUTTON_COLOR)
        name_submit_button.place(x=85, y=80)

    def check_overwrite_file():
        #check if file exist
        if os.path.exists(file_name):
            if messagebox.askyesno(message="The file name you picked already exist, Overwrite it?"):
                os.remove(file_name)
                os.rename("temp.txt", file_name)
            else:
                pass
        else:
            os.rename("temp.txt", file_name)
          
    def exit():
        #ask decision if exit
        if messagebox.askyesno(message="Do you want to exit the program?"):
            write_window.destroy()
        else:
            write_window.destroy()
            save_quiz_file_creation_window()


    #create quiz writing window
    main_window.destroy()
    write_window = Tk()
    
    write_window.title(WINDOW_TITLE)
    write_window.resizable(False, False)
    write_window.config(bg=WINDOW_BACKGROUND)

    #centralizing window
    screen_position_x = int((screen_width / 2) - (WINDOW_WIDTH / 2)) 
    screen_position_y = int((screen_height / 2) - (WINDOW_HEIGHT / 2)) - 20

    write_window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{screen_position_x}+{screen_position_y}")

    #inputs
    quiz_problem_label = Label(write_window, text=f"Question {iteration}:", font=FONT_1, fg="#FFFFFF", bg=LABEL_COLOR)
    quiz_problem_label.place(x=0, y=0)
    quiz_problem = Text(font=ENTRY_FONT, width=72, height=4, bg="#D3D3D3")
    quiz_problem.place(x=0, y=30)
    
    answer_a_label = Label(write_window, text=f"Answer A:", font=FONT_1, fg="#FFFFFF", bg=LABEL_COLOR)
    answer_a_label.place(x=0, y=130)
    answer_a_entry = Entry(font=ENTRY_FONT, width=72, bg="#D3D3D3")
    answer_a_entry.place(x=0, y=160)

    answer_b_label = Label(write_window, text=f"Answer B:", font=FONT_1, fg="#FFFFFF", bg=LABEL_COLOR)
    answer_b_label.place(x=0, y=190)
    answer_b_entry = Entry(font=ENTRY_FONT, width=72, bg="#D3D3D3")
    answer_b_entry.place(x=0, y=220)

    answer_c_label = Label(write_window, text=f"Answer C:", font=FONT_1, fg="#FFFFFF", bg=LABEL_COLOR)
    answer_c_label.place(x=0, y=250)
    answer_c_entry = Entry(font=ENTRY_FONT, width=72, bg="#D3D3D3")
    answer_c_entry.place(x=0, y=290)

    answer_d_label = Label(write_window, text=f"Answer D:", font=FONT_1, fg="#FFFFFF", bg=LABEL_COLOR)
    answer_d_label.place(x=0, y=325)
    answer_d_entry = Entry(font=ENTRY_FONT, width=72, bg="#D3D3D3")
    answer_d_entry.place(x=0, y=355)

    correct_answer_label = Label(write_window, text=f"Correct Answer:", font=FONT_1, fg="#FFFFFF", bg=LABEL_COLOR)
    correct_answer_label.place(x=0, y=385)
    correct_answer_entry = Entry(font=ENTRY_FONT, width=72, bg="#D3D3D3")
    correct_answer_entry.place(x=0, y=415)

    submit_button = Button(write_window, text="Submit", command=lambda:[save_quiz_file(), file_naming()], font=("Arial", 25, "bold"), fg=TEXT_COLOR, bg=BUTTON_COLOR)
    submit_button.place(x=int(WINDOW_WIDTH / 2) - 75, y=485)
    
    write_window.mainloop()

def check_overwrite_file():
    #check if file exist
    global file_name
    if os.path.exists(file_name):
        ask_overwrite = input("The file name you choose already exist. Overwrite it?(Y/N):\n> ")
        if ask_overwrite in ("y", "yes", "overwrite"):
            os.remove(file_name)
        elif ask_overwrite in ("n", "no"):
            file_name = input("File Name:\n> ") + ".txt"
            check_overwrite_file()

#interface window

main_window = Tk()

main_window.title(WINDOW_TITLE)
main_window.resizable(False, False)
main_window.config(bg=WINDOW_BACKGROUND)

#process of centralizing window
screen_width = main_window.winfo_screenwidth()
screen_height = main_window.winfo_screenheight()

screen_position_x = int((screen_width / 2) - (MAIN_WINDOW_WIDTH / 2)) 
screen_position_y = int((screen_height / 2) - (MAIN_WINDOW_HEIGHT / 2)) - 20

main_window.geometry(f"{MAIN_WINDOW_WIDTH}x{MAIN_WINDOW_HEIGHT}+{screen_position_x}+{screen_position_y}")

#buttons
create_button = Button(main_window, text="Create New Quiz", command=save_quiz_file_creation_window)
create_button.config(bg=BUTTON_COLOR, fg=TEXT_COLOR, relief=SUNKEN)
create_button.config(font=("Arial", 20, "bold"))
create_button.place(x=30, y=60)

read_button = Button(main_window, text="Read Quiz File", state=DISABLED)
read_button.config(bg=BUTTON_COLOR, fg=TEXT_COLOR, relief=SUNKEN)
read_button.config(font=("Arial", 20, "bold"))
read_button.place(x=40, y=180)

main_window.mainloop()
             
