#initialization
iteration = 1
ask_exit = ""

#functions
def exit():
    #asking if continue
        ask_exit = input("Exit?(Y/N):\n>").lower()
        if ask_exit in ("y", "yes"):
            return True
        elif ask_exit in ("n", "no"):
            return False
        else:
            exit()

#create file
with open("quiz.txt", "a") as file:

    #loop
    while True:
        #ask for a question and write in file
        question = input("Question:\n>")
        file.write(f"Question {iteration}: " + question + "\n")

        #ask for 4 answers and write in file
        answer_a = input("Answer A:\n>")
        file.write("A: " + answer_a + "\n")

        answer_b = input("Answer B:\n>")
        file.write("B: " + answer_b + "\n")

        answer_c = input("Answer C:\n>")
        file.write("C: " + answer_c + "\n")

        answer_d = input("Answer D:\n>")
        file.write("D: " + answer_d + "\n")

        #ask for correct answer and write in file
        correct_answer = input("Correct Answer:\n>")
        file.write("Correct Answer: " + correct_answer + "\n")
        
        exit = exit()

        if exit == True:
            break
            
             
