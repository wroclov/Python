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

        self.score = 0
        self.current_question_index = 0
        random.shuffle(questions)
        self.selected_questions = questions[:20]
        self.user_answers = []

        self._initialize_ui()
        self.load_question()

    def _initialize_ui(self):
        """Initialize the user interface components."""
        self.question_number_label = tk.Label(self.root, text="", font=("Arial", 12))
        self.question_number_label.pack(pady=10)

        self.question_label = tk.Label(self.root, text="", wraplength=400, font=("Arial", 14))
        self.question_label.pack(pady=10)

        self.options_frame = tk.Frame(self.root)
        self.options_frame.pack(pady=10, anchor="w")

        self.selected_option = tk.StringVar(value=None)
        self.option_buttons = self._create_option_buttons()

        self.next_button = tk.Button(self.root, text="Next", command=self.next_question, state="disabled")
        self.next_button.pack(pady=20)

    def _create_option_buttons(self):
        """Create option buttons for the quiz."""
        buttons = []
        for _ in range(4):
            button = tk.Radiobutton(
                self.options_frame, text="", variable=self.selected_option, value="", font=("Arial", 12),
                anchor="w", justify="left", padx=20, command=self.check_answer
            )
            button.pack(anchor="w", pady=2)
            buttons.append(button)
        return buttons

    def load_question(self):
        """Load the current question and display options."""
        if self.current_question_index < len(self.selected_questions):
            question = self.selected_questions[self.current_question_index]
            self._update_question_ui(question)
            self._shuffle_options_and_reset()
        else:
            self.show_results()

    def _update_question_ui(self, question):
        """Update UI elements to display the current question."""
        self.question_number_label.config(
            text=f"Question {self.current_question_index + 1} of {len(self.selected_questions)}"
        )
        self.question_label.config(text=question["question"])

    def _shuffle_options_and_reset(self):
        """Shuffle options and reset the UI for a new question."""
        options = self.selected_questions[self.current_question_index]["options"][:]
        random.shuffle(options)

        self.correct_answer = self.selected_questions[self.current_question_index]["answer"]
        self.shuffled_answer_mapping = {option: (option == self.correct_answer) for option in options}

        self.selected_option.set(None)
        for i, option in enumerate(options):
            self.option_buttons[i].config(text=option, value=option)
            self.option_buttons[i].pack(anchor="w", pady=2)

        self._hide_unused_buttons(options)
        self.next_button.config(state="disabled")

    def _hide_unused_buttons(self, options):
        """Hide any unused buttons based on the number of options."""
        for i in range(len(options), 4):
            self.option_buttons[i].pack_forget()

    def check_answer(self):
        """Enable the 'Next' button when an option is selected."""
        if self.selected_option.get():
            self.next_button.config(state="normal")

    def next_question(self):
        """Record the user's answer and load the next question."""
        selected_option = self.selected_option.get()
        question = self.selected_questions[self.current_question_index]
        self._record_answer(question, selected_option)

        if selected_option == question["answer"]:
            self.score += 1

        self.current_question_index += 1
        self.load_question()

    def _record_answer(self, question, selected_option):
        """Store the user's answer to the current question."""
        self.user_answers.append({
            "question": question["question"],
            "options": question["options"],
            "user_answer": selected_option,
            "correct_answer": question["answer"]
        })

    def show_results(self):
        """Display the results after the quiz is finished."""
        for widget in self.root.winfo_children():
            widget.destroy()

        self.results_per_page = 4
        self.current_results_page = 0
        self.total_results_pages = (len(self.user_answers) - 1) // self.results_per_page + 1
        self.display_results_page(self.current_results_page)

    def display_results_page(self, page):
        """Display a specific results page based on the page number."""
        self._clear_ui()

        start_idx, end_idx = self._get_pagination_indices(page)
        print(start_idx,end_idx)
        answers_to_display = self.user_answers[start_idx:end_idx]

        self._display_results_header()
        self._create_scrollable_results_frame(answers_to_display, start_idx)
        self._create_navigation_buttons(page)

    def _clear_ui(self):
        """Clear the current UI components."""
        for widget in self.root.winfo_children():
            widget.destroy()

    def _get_pagination_indices(self, page):
        """Return the start and end indices for pagination."""
        start_idx = page * self.results_per_page
        end_idx = start_idx + self.results_per_page
        return start_idx, end_idx

    def _display_results_header(self):
        """Display the results header."""
        tk.Label(self.root, text="Quiz Results", font=("Arial", 16, "bold")).pack(pady=10)

    def _create_scrollable_results_frame(self, answers_to_display, start_idx):
        """Create a scrollable frame to display the results."""
        canvas = tk.Canvas(self.root)
        canvas.pack(fill="both", expand=True, pady=20)

        scrollable_frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

        scrollbar = tk.Scrollbar(self.root, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")

        canvas.config(yscrollcommand=scrollbar.set)

        for idx, answer in enumerate(answers_to_display, start=start_idx+1):
            self._display_answer(scrollable_frame, idx, answer)

        scrollable_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

    def _display_answer(self, frame, idx, answer):
        """Display the answer for a question with its options and colors."""
        question_label = tk.Label(frame, text=f"Q{idx}: {answer['question']}", font=("Arial", 12))
        question_label.pack(anchor="w", padx=10, pady=5)

        for option in answer["options"]:
            color = self._get_option_color(option, answer)
            option_label = tk.Label(frame, text=option, font=("Arial", 11), fg=color)
            option_label.pack(anchor="w", padx=30)

    def _get_option_color(self, option, answer):
        """Return the color for an option based on correctness."""
        if option == answer["correct_answer"]:
            return "green"
        elif option == answer["user_answer"]:
            return "red"
        return "black"

    def _create_navigation_buttons(self, page):
        """Create the navigation buttons for pagination."""
        nav_frame = tk.Frame(self.root)
        nav_frame.pack(pady=20)

        if page > 0:
            tk.Button(nav_frame, text="Previous", command=lambda: self.display_results_page(page - 1)).pack(side="left", padx=10)
        if page < self.total_results_pages - 1:
            tk.Button(nav_frame, text="Next", command=lambda: self.display_results_page(page + 1)).pack(side="left", padx=10)

        if page == self.total_results_pages - 1:
            tk.Label(self.root, text=f"Your Score: {self.score}/{len(self.selected_questions)}", font=("Arial", 14, "bold")).pack(pady=20)
            tk.Button(self.root, text="Exit", command=self.root.destroy).pack(pady=10)


# Main application
if __name__ == "__main__":
    questions = load_questions("questions.json")
    root = tk.Tk()
    app = QuizGame(root, questions)
    root.mainloop()
