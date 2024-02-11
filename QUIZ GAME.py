import tkinter as tk
from tkinter import messagebox
import random

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.root.geometry("600x400")
        self.root.configure(bg="#FFFFCC") 

        self.questions = self.load_questions_from_file("dbms_questions.txt")
        self.current_question_index = 0
        self.score = 0

        self.selected_option = tk.StringVar()

        self.setup_ui()

    def setup_ui(self):
        self.label_question = tk.Label(self.root, text="", font=("Arial", 14), bg="#FFFFCC", wraplength=500, justify="center")
        self.label_question.pack(pady=20)

        self.option_buttons = []
        for i in range(4):
            option_button = tk.Radiobutton(self.root, text="", variable=self.selected_option, value="", font=("timesnewroman", 12), bg="#FFFFCC", activebackground="#FFD699", indicatoron=0)
            option_button.pack(pady=5)
            self.option_buttons.append(option_button)

        submit_button = tk.Button(self.root, text="Submit Answer", command=self.check_answer, font=("timesnewroman", 12), bg="#FF7043", fg="white", activebackground="#E64A19", activeforeground="white")
        submit_button.pack(pady=20)

        self.load_question()

    def load_questions_from_file(self, filename):
        return [
            {"question": "What does SQL stand for?", "options": ["Structured Query Language", "Sequential Query Language", "Standard Query Language", "Structured Question Language"], "correct_answer": "Structured Query Language"},
            {"question": "What is a primary key in a database?", "options": ["A key that uniquely identifies each record in a table", "A key that references another table's primary key", "A key used for sorting records in a table", "A key used for querying records in a table"], "correct_answer": "A key that uniquely identifies each record in a table"},
            {"question": "What is a foreign key in a database?", "options": ["A key used for sorting records in a table", "A key that references another table's primary key", "A key that uniquely identifies each record in a table", "A key used for querying records in a table"], "correct_answer": "A key that references another table's primary key"},
            {"question": "What is normalization in DBMS?", "options": ["The process of removing redundant data from a database", "The process of adding redundant data to a database", "The process of organizing data in a database", "The process of deleting data from a database"], "correct_answer": "The process of removing redundant data from a database"},
            {"question": "What is a view in DBMS?", "options": ["A virtual table based on the result of a SELECT query", "A physical table in the database", "A key that uniquely identifies each record in a table", "A key used for sorting records in a table"], "correct_answer": "A virtual table based on the result of a SELECT query"}
        ]

    def load_question(self):
        if self.current_question_index < len(self.questions):
            question_data = self.questions[self.current_question_index]
            self.label_question.config(text=question_data["question"])

            options = question_data["options"]
            random.shuffle(options)

            for i in range(4):
                self.option_buttons[i].config(text=options[i], value=options[i], bg="#FFFFCC", activebackground="#FFD699")

            self.selected_option.set("")
        else:
            self.show_final_results()

    def check_answer(self):
        user_answer = self.selected_option.get()
        correct_answer = self.questions[self.current_question_index]["correct_answer"]

        if user_answer == correct_answer:
            self.score += 1

        self.show_feedback(correct_answer, user_answer)

        self.current_question_index += 1
        self.load_question()

    def show_feedback(self, correct_answer, user_answer):
        msg = f"Correct Answer: {correct_answer}\nYour Answer: {user_answer}"
        if user_answer == correct_answer:
            msg += "\nCorrect!"
        else:
            msg += "\nIncorrect!"
        messagebox.showinfo("Feedback", msg, parent=self.root)

    def show_final_results(self):
        messagebox.showinfo("Quiz Completed", f"Your final score is: {self.score} out of {len(self.questions)}", parent=self.root)

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizGame(root)
    root.mainloop()
