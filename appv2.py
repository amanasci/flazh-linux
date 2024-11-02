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

    # Construct the zenity command
    cmd = [
        'zenity', '--list', '--radiolist', '--width=600', '--height=400',
        '--title=Quiz Question', '--text', question,
        '--column', '', '--column', 'Options'
    ]

    # Add options to the zenity command
    # The first column is for the radio button selection (TRUE/FALSE), second is the option text
    for idx, option in enumerate(options):
        # Set all options to FALSE initially
        cmd.extend(['FALSE', option])

    try:
        selected_option = subprocess.check_output(cmd, text=True).strip()
    except subprocess.CalledProcessError:
        # User closed the dialog or did not make a selection
        send_notification('No selection made.')
        return

    # Check if the selected option matches the correct answer
    if selected_option == correct_answer:
        send_notification('✅ Correct! Great job.')
    else:
        send_notification(f'❌ Incorrect.\nThe correct answer was:\n{correct_answer}')

def main():
    questions = load_questions()
    try:
        while True:
            question_data = random.choice(questions)
            ask_question(question_data)
            # Wait for 15 minutes before showing the next question
            time.sleep(900)
    except KeyboardInterrupt:
        send_notification('Quiz terminated.')

if __name__ == '__main__':
    main()
