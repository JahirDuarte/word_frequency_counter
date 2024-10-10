# Word Frequency Counter

## Description

- Project developed as a coding test for Cart.com.
- This Python project counts the frequency of words in a text file.
- Words are treated case-insensitively.
- Punctuation is ignored, and words are sorted by frequency in descending order.
- The code is structured in a class, and a set of automated tests is included.
- The code has been implemented following the PEP 8 style guide for Python code formatting.

## Project Architechture
- src/word_frequency.py: Main file containing the WordFrequencyCounter class.
- tests/test_word_frequency.py: Test file using unittest and Faker to test various use cases.

## Requirements.txt

- Python 3.8 or higher
- Additional packages:
  - faker (to generate random texts for testing)
  - unittest (Python's standard library for testing)

### Virtual Environment Setup
- You can create and activate a virtual environment using the following commands (Linux):

    ```bash
    $ python3 -m venv env
    $ source env/bin/activate
    $ pip install -r requirements.txt

## Program Usage
- Place the text file you want to analyze in the project's root directory or any other location.
- Run the program from the command line, providing the path to the text file as an argument.
- Example:

    - Input
    $ python src/word_frequency.py src/sample.txt

    - Output
    test: 3
    a: 2
    is: 2
    this: 2
    only: 1

- To run the script that generates random words and paragraphs, use the following command in the terminal:
    ```bash
    $ python src/faker_util.py

## Automated tests
- To run all tests, navigate to the project's root directory and use the following command: 
    $ python -m unittest discover tests