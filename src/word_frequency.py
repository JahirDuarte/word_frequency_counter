# src/word_frequency.py
import re  # Importar re para expresiones regulares
from collections import Counter

class WordFrequency:
    def __init__(self, file_path):
        self.file_path = file_path

    def clean_word(self, word):
        """
        This function removes punctuation and numbers from a word and converts it to lowercase.
        """
        cleaned_word = re.sub(r'[^a-zA-Z]', '', word).lower()
        return cleaned_word

    def counter(self):
        try:
            # Open and read the file
            with open(self.file_path, 'r') as file:
                text = file.read()

            # Split the text into words, clean each word, and filter out empty words
            words = [self.clean_word(word) for word in text.split()]
            words = [word for word in words if word]  # Delete empty words

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
    # Open the script and expect one parameter (the sample text file, e.g., sample.txt)
    import sys
    if len(sys.argv) != 2:
        print("Usage: python word_frequency.py sample.txt")
        sys.exit(1)

    # Open the specified text file and count the frequency of words using the WordFrequency class
    file_path = sys.argv[1]
    word_frequency = WordFrequency(file_path)
    result = word_frequency.counter()

    for word, count in result:
        print(f"{word}: {count}")