import time

class QuizApp:
    def __init__(self):
        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
                "answer": "C"
            },
            {
                "question": "Which language is primarily used for web pages' styling?",
                "options": ["A. Python", "B. CSS", "C. Java", "D. C++"],
                "answer": "B"
            },
            {
                "question": "What is the result of 5 + 3 * 2?",
                "options": ["A. 16", "B. 11", "C. 13", "D. 10"],
                "answer": "B"
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["A. Earth", "B. Venus", "C. Mars", "D. Jupiter"],
                "answer": "C"
            },
            {
                "question": "Who wrote 'Romeo and Juliet'?",
                "options": ["A. Charles Dickens", "B. William Shakespeare", "C. Mark Twain", "D. Leo Tolstoy"],
                "answer": "B"
            }
        ]
        self.score = 0

    def run(self):
        print("=== Welcome to the Quiz Application ===")
        name = input("Enter your name: ").strip()
        print(f"\nGood luck, {name}! There are {len(self.questions)} questions.\n")
        time.sleep(1)

        for i, q in enumerate(self.questions, start=1):
            print(f"Q{i}. {q['question']}")
            for option in q["options"]:
                print(f"   {option}")

            user_answer = input("Your answer (A/B/C/D): ").strip().upper()

            if user_answer == q["answer"]:
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Wrong! The correct answer is {q['answer']}.\n")

        self.show_result(name)

    def show_result(self, name):
        total = len(self.questions)
        percentage = (self.score / total) * 100

        print("=== Quiz Result ===")
        print(f"Name: {name}")
        print(f"Score: {self.score}/{total}")
        print(f"Percentage: {percentage:.2f}%")

        if percentage >= 80:
            print("Grade: Excellent!")
        elif percentage >= 60:
            print("Grade: Good")
        elif percentage >= 40:
            print("Grade: Average")
        else:
            print("Grade: Needs Improvement")

if __name__ == "__main__":
    quiz = QuizApp()
    quiz.run()