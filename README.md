# Flazh

Flazh is a simple flashnote reminder app for linux. It pushses you a qquestion every 15 minutes with options.


## Installation

At this stage the way to run the app is by cloning the repo.

```bash
git clone https://github.com/amanasci/flazh-linux.git
```

Then run using python.

```bash
python appv2.py
```



> Use only appv2.py for the actual app.

> app.py is the cli version.

## Install dependencies

- Python 3.x is required.
- Ensure zenity and notify-send are installed on your system. Most Linux distributions have these tools available.
```bash
sudo apt-get install zenity
sudo apt-get install libnotify-bin
```

## Add Data

Add Questions to the data.json file.

## Data Structure

The questions are stored in a JSON file, data.json, with each question entry having the following structure:

```json
{
    "question": "What is the Cauchy-Riemann equation in Cartesian coordinates?",
    "options": [
        "∂u/∂x = ∂v/∂y and ∂u/∂y = -∂v/∂x",
        "∂u/∂x = ∂v/∂x and ∂u/∂y = ∂v/∂y",
        "∂u/∂x + ∂v/∂x = 0",
        "∂u/∂y = ∂v/∂y and ∂u/∂x = ∂v/∂x"
    ],
    "correct_answer": "∂u/∂x = ∂v/∂y and ∂u/∂y = -∂v/∂x"
}
```

- question: The question text.
- options: A list of four options.
- correct_answer: The correct answer, which matches one of the options.

## Customization
- Change Question Frequency: To adjust the interval between questions, change the sleep time in the time.sleep(900) line in `appv2.py`. For example, to show a question every 10 minutes, set it to time.sleep(600).

- Add More Questions: Open data.json and add more entries in the format described above.


## Contributing

Contributions are welcome! If you want to add questions or improve the app:

1. Fork the repository.
2. Add your changes.
3. Submit a pull request.

Make sure that the data.json file is properly formatted and follows the structure specified.


## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
