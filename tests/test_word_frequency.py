# tests/test_word_frequency.py
import unittest
from faker import Faker
from src.word_frequency import WordFrequency
import os

class TestWordFrequency(unittest.TestCase):

    def setUp(self):
        self.faker = Faker()

        # Create a temporary file with random text for testing
        self.test_file_path = "test_file.txt"
        with open(self.test_file_path, 'w') as file:
            file.write(self.faker.text(max_nb_chars=1000))  # Generate 1000 characters of random text

    def tearDown(self):
        # Remove the test file after each test
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)

    def test_word_frequency(self):
        # Create an instance of WordFrequencyCounter with the test file
        word_frequency = WordFrequency(self.test_file_path)

        # Get the word frequencies
        result = word_frequency.counter()

        # Check if result is a list and not empty
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)

        # Check if the word frequencies are tuples of (word, frequency)
        for word, count in result:
            self.assertIsInstance(word, str)
            self.assertIsInstance(count, int)

    def test_empty_file(self):
        # Create an empty file
        empty_file_path = "empty_file.txt"
        with open(empty_file_path, 'w') as file:
            pass

        word_frequency = WordFrequency(empty_file_path)
        result = word_frequency.counter()

        # Check that the result is an empty list
        self.assertEqual(result, [])

        # Clean up the empty file
        os.remove(empty_file_path)

    def test_file_not_found(self):
        # Test for a non-existent file
        word_frequency = WordFrequency("non_existent_file.txt")
        with self.assertRaises(FileNotFoundError):
            word_frequency.counter()

if __name__ == '__main__':
    unittest.main()