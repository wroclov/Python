import tkinter as tk
from tkinter import messagebox
import random
import json


# Load questions from JSON file
def load_questions(filename):
    with open(filename, "r") as file:
        return json.load(file)


class QuizGame:
    def __init__(self, root, questions):
        self.root = root
        self.root.title("Python Quiz Game")

        # Initialize variables
        self.score = 0
        self.current_question_index = 0

        # Shuffle the questions and select the first 8 unique questions
        random.shuffle(questions)
        self.selected_questions = questions[:20]  # Select 8 unique questions after shuffling
        self.user_answers = []  # Store user's answers

        # UI Components
        self.question_number_label = tk.Label(root, text="", font=("Arial", 12))
        self.question_number_label.pack(pady=10)

        self.question_label = tk.Label(root, text="", wraplength=400, font=("Arial", 14))
        self.question_label.pack(pady=10)

        self.options_frame = tk.Frame(root)
        self.options_frame.pack(pady=10, anchor="w")

        self.selected_option = tk.StringVar(value=None)
        self.option_buttons = []
        for i in range(4):
            button = tk.Radiobutton(
                self.options_frame, text="", variable=self.selected_option, value="", font=("Arial", 12), anchor="w",
                justify="left", padx=20, command=self.check_answer
            )
            button.pack(anchor="w", pady=2)
            self.option_buttons.append(button)

        self.next_button = tk.Button(root, text="Next", command=self.next_question, state="disabled")
        self.next_button.pack(pady=20)

        self.load_question()

    def load_question(self):
        if self.current_question_index < len(self.selected_questions):
            question = self.selected_questions[self.current_question_index]
            self.question_number_label.config(
                text=f"Question {self.current_question_index + 1} of {len(self.selected_questions)}"
            )
            self.question_label.config(text=question["question"])

            # Shuffle options while keeping track of the correct answer
            options = question["options"][:]
            random.shuffle(options)
            self.correct_answer = question["answer"]
            self.shuffled_answer_mapping = {option: (option == self.correct_answer) for option in options}

            self.selected_option.set(None)  # Reset selected option
            for i, option in enumerate(options):
                self.option_buttons[i].config(text=option, value=option)
                self.option_buttons[i].pack(anchor="w", pady=2)

            # Hide unused buttons
            for i in range(len(options), 4):
                self.option_buttons[i].pack_forget()

            self.next_button.config(state="disabled")
        else:
            self.show_results()

    def check_answer(self):
        if self.selected_option.get():
            self.next_button.config(state="normal")

    def next_question(self):
        selected_option = self.selected_option.get()
        question = self.selected_questions[self.current_question_index]
        correct_answer = question["answer"]

        # Record the user's answer
        self.user_answers.append({
            "question": question["question"],
            "options": question["options"],
            "user_answer": selected_option,
            "correct_answer": correct_answer
        })

        if selected_option == correct_answer:
            self.score += 1

        self.current_question_index += 1
        self.load_question()

    def show_results(self):
        # Clear current UI
        for widget in self.root.winfo_children():
            widget.destroy()

        # Pagination variables
        self.results_per_page = 4
        self.current_results_page = 0
        self.total_results_pages = (len(self.user_answers) - 1) // self.results_per_page + 1

        def display_results_page(page):
            # Clear current UI
            for widget in self.root.winfo_children():
                widget.destroy()

            start_idx = page * self.results_per_page
            end_idx = start_idx + self.results_per_page
            answers_to_display = self.user_answers[start_idx:end_idx]

            # Display results for the current page
            tk.Label(self.root, text="Quiz Results", font=("Arial", 16, "bold")).pack(pady=10)

            # Create a canvas for scrollable results
            canvas = tk.Canvas(self.root)
            canvas.pack(fill="both", expand=True, pady=20)

            # Create a scrollable frame inside the canvas
            scrollable_frame = tk.Frame(canvas)
            canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

            # Add a scrollbar that spans the entire height
            scrollbar = tk.Scrollbar(self.root, orient="vertical", command=canvas.yview)
            scrollbar.pack(side="right", fill="y")

            # Configure canvas scroll region
            canvas.config(yscrollcommand=scrollbar.set)

            # Display results
            for idx, answer in enumerate(answers_to_display, start=start_idx + 1):
                question_label = tk.Label(scrollable_frame, text=f"Q{idx}: {answer['question']}", font=("Arial", 12))
                question_label.pack(anchor="w", padx=10, pady=5)

                for option in answer["options"]:
                    if option == answer["correct_answer"]:
                        color = "green"  # Correct answer
                    elif option == answer["user_answer"]:
                        color = "red"  # Wrong answer selected by user
                    else:
                        color = "black"  # Neutral

                    option_label = tk.Label(scrollable_frame, text=option, font=("Arial", 11), fg=color)
                    option_label.pack(anchor="w", padx=30)

            # Update the scrollable frame's scroll region
            scrollable_frame.update_idletasks()
            canvas.config(scrollregion=canvas.bbox("all"))

            # Navigation buttons
            nav_frame = tk.Frame(self.root)
            nav_frame.pack(pady=20)

            if page > 0:
                tk.Button(nav_frame, text="Previous", command=lambda: display_results_page(page - 1)).pack(side="left",
                                                                                                           padx=10)
            if page < self.total_results_pages - 1:
                tk.Button(nav_frame, text="Next", command=lambda: display_results_page(page + 1)).pack(side="left",
                                                                                                       padx=10)

            # Display final score on the last page
            if page == self.total_results_pages - 1:
                tk.Label(self.root, text=f"Your Score: {self.score}/{len(self.selected_questions)}",
                         font=("Arial", 14, "bold")).pack(pady=20)

                # Exit button
                tk.Button(self.root, text="Exit", command=self.root.destroy).pack(pady=10)

        # Show the first page of results
        display_results_page(self.current_results_page)


# Main application
if __name__ == "__main__":
    questions = load_questions("questions.json")
    root = tk.Tk()
    app = QuizGame(root, questions)
    root.mainloop()
