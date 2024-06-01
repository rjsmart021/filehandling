import re

from typing import Tuple

positive_words = {"amazing", "enjoy", "beautiful", "wonderful", "memorable", "excellent",
                  "fantastic", "unforgettable"}
negative_words = {"bad", "disappointing", "poor", "lackluster", "scarce"}


def count_travel_blog_sentiment_words(file_path) -> Tuple[int, int]:
    """
    It will read the file and take each word and check whether it is positive or negative word and
    increase the respective word count.
    If file path not exist it will display an error message and exit.
    :param file_path: travel_blog.txt file path to open and read the contents.
    :return:
    """
    negative_word_count = 0
    positive_word_count = 0

    try:
        f = open(file_path, 'r')
        contents = f.read()
        words = contents.split()

        for word in words:
            # remove punctuation marks
            word = re.sub(r'[^\w\s]', '', word)
            if word in positive_words:
                positive_word_count += 1
            elif word in negative_words:
                negative_word_count += 1

    except FileNotFoundError:
        print(f"File not found. Please verify path: {file_path}")
        exit(0)
    return positive_word_count, negative_word_count


file_path = input("Enter travel blog contents file path: ")
positive_word_count, negative_word_count = count_travel_blog_sentiment_words(file_path)
print("The number of positive words are: ", positive_word_count)
print("The number of negative words are: ", negative_word_count)
