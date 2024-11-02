import json
import random
import time
import subprocess

def load_questions(filename='data.json'):
    with open(filename, 'r') as f:
        return json.load(f)

def send_notification(message):
    subprocess.call(['notify-send', message])

def ask_question(question_data):
    question = question_data['question']
    options = question_data['options']
    correct_answer = question_data['correct_answer']

    print(f"\n{question}\n")
    for idx, option in enumerate(options, 1):
        print(f"{idx}. {option}")

    while True:
        try:
            choice = int(input("\nSelect an option (1-{}): ".format(len(options))))
            if 1 <= choice <= len(options):
                break
            else:
                print("Please enter a number between 1 and {}.".format(len(options)))
        except ValueError:
            print("Invalid input. Please enter a number.")

    selected_option = options[choice - 1]
    if selected_option == correct_answer:
        print("\n✅ Correct!")
        send_notification("Correct! Great job.")
    else:
        print(f"\n❌ Incorrect. The correct answer is:\n{correct_answer}")
        send_notification(f"Incorrect. The correct answer was:\n{correct_answer}")

def main():
    questions = load_questions()
    try:
        while True:
            question_data = random.choice(questions)
            ask_question(question_data)
            print("\nNext question in 15 minutes...")
            time.sleep(900)  # Wait for 15 minutes
    except KeyboardInterrupt:
        print("\nQuiz terminated.")

if __name__ == "__main__":
    main()
