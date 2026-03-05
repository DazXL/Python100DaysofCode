from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"

class QuizInterface():
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        #window
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        #score label
        self.score = Label(text=f"Score: {self.quiz.score}",fg="white", bg=THEME_COLOR)
        self.score.grid(row=0, column=1)

        #canvas
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=00)
        self.question_label = self.canvas.create_text(150, 125, text=f"Question Here", width=300, font=("arial", 20, "italic"), fill="black")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        #buttons
        true_image = PhotoImage(file="Images/true.png")
        self.button_true = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.button_true.grid(row=2, column=0)

        false_image = PhotoImage(file="Images/false.png")
        self.button_false = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.button_false.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_label, text=q_text)
        else:
            self.button_false.config(state="disabled")
            self.button_true.config(state="disabled")
    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))


    def give_feedback(self, answer):
        if answer:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000,self.get_next_question)