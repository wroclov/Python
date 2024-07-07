import json
import random
import tkinter as tk
from tkinter import messagebox

# Load country data from a JSON file
def load_country_data(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        countries = json.load(file)
    return countries

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Country Capitals Quiz")
        self.country_data = load_country_data('countries.json')
        self.questions = random.sample(self.country_data, 20)
        self.score = 0
        self.current_question = 0

        # Determine maximum width needed for Radiobuttons
        max_country_length = max(len(country["name"]) for country in self.country_data)
        self.radiobutton_width = max_country_length + 10  # Adjust multiplier as needed

        self.create_widgets()
        self.show_question()

    def create_widgets(self):
        self.score_label = tk.Label(self.root, text=f"Score: {self.score}/20", font=('Helvetica', 16))
        self.score_label.pack(pady=10)

        self.question_label = tk.Label(self.root, text="", font=('Helvetica', 18, 'bold'), fg='blue',width=self.radiobutton_width)
        self.question_label.pack(pady=20)

        self.options = tk.StringVar()
        self.option_buttons = []
        for i in range(4):
            btn = tk.Radiobutton(self.root, text="", variable=self.options, value="", font=('Helvetica', 14),
                                 anchor='w', justify=tk.LEFT, fg='green')
            btn.pack(fill='x', padx=40, pady=5)
            self.option_buttons.append(btn)

        self.submit_button = tk.Button(self.root, text="Submit", command=self.check_answer, font=('Helvetica', 14))
        self.submit_button.pack(pady=20)

    def show_question(self):
        if self.current_question < len(self.questions):
            country_info = self.questions[self.current_question]
            country = country_info["name"]
            correct_capital = country_info["capital"]

            all_capitals = [info["capital"] for info in self.country_data if info["capital"] != correct_capital]
            options = random.sample(all_capitals, 3) + [correct_capital]
            random.shuffle(options)

            self.question_label.config(text=f"What is the capital of {country}?")
            self.options.set(None)
            for i, option in enumerate(options):
                self.option_buttons[i].config(text=f"    {option}", value=option)

        else:
            self.show_results()

    def check_answer(self):
        selected_capital = self.options.get()
        if selected_capital:
            correct_capital = self.questions[self.current_question]["capital"]
            if selected_capital == correct_capital:
                self.score += 1
            self.current_question += 1
            self.score_label.config(text=f"Score: {self.score}/20")
            self.show_question()
        else:
            messagebox.showwarning("Selection Error", "Please select an answer.")

    def show_results(self):
        messagebox.showinfo("Quiz Results", f"Your score: {self.score} out of 20")
        self.root.destroy()

def main():
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
