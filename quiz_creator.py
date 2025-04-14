#create file
with open("quiz.txt", "a") as file:
    #loop
    while True:
        #ask for a question and write in file
        question = input("Question:\n>")
        file.write(question + "\n")

        #ask for 4 answers and write in file
        answer_a = input("Answer A:\n>")
        file.write(answer_a + "\n")

        answer_b = input("Answer B:\n>")
        file.write(answer_b + "\n")

        answer_c = input("Answer C:\n>")
        file.write(answer_c + "\n")

        answer_d = input("Answer D:\n>")
        file.write(answer_d + "\n")

        #ask for correct answer and write in file
        correct_answer = input("Correct Answer:\n>")
        file.write(correct_answer + "\n")
        break

