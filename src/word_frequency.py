# src/word_frequency.py
import string
from collections import Counter

class WordFrequency:
    def __init__(self, file_path):
        self.file_path = file_path

    def clean_word(self, word):
        """
        This function removes punctuation from a word and converts it to lowercase.
        """
        return word.strip(string.punctuation).lower()

    def counter(self):
        try:
            # Open and read the file
            with open(self.file_path, 'r') as file:
                text = file.read()

            # Split the text into words and clean each word
            words = [self.clean_word(word) for word in text.split() if word]

            # Count the frequency of each word
            word_count = Counter(words)

            # Sort words by frequency (descending) and alphabetically for ties
            sorted_word_count = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))

            # Return the sorted words and frequencies
            return sorted_word_count

        except FileNotFoundError:
            raise FileNotFoundError(f"Error: File '{self.file_path}' not found.")
        except Exception as e:
            raise Exception(f"An error occurred: {e}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python word_frequency.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    word_frequency = WordFrequency(file_path)
    result = word_frequency.counter()

    for word, count in result:
        print(f"{word}: {count}")
