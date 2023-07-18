"""
Note that this file cannot be modified.
If you would like to add your own unit tests, please put these in a separate test file.
"""

import pytest

from books.books_csv_parser import BooksCSVParser
from books.bestselling_books_stats_generator import BestsellingBooksStatsGenerator

fiction_genre = "Fiction"
non_fiction_genre = "Non Fiction"
ranked_year = 2018

_bestselling_books_stats_generator_setup = BestsellingBooksStatsGenerator(BooksCsvParser())

@pytest.fixture
def bestselling_books_stats_generator_setup():
    return _bestselling_books_stats_generator_setup

def test_get_title_of_book_with_most_reviews(bestselling_books_stats_generator_setup):
    assert bestselling_books_stats_generator_setup.get_title_of_book_with_most_reviews(fiction_genre, ranked_year) == "The Wonky Donkey"

def test_get_title_of_book_with_most_reviews_2(bestselling_books_stats_generator_setup):
    assert bestselling_books_stats_generator_setup.get_title_of_book_with_most_reviews(non_fiction_genre, ranked_year) == "Becoming"

def test_get_average_reviews(bestselling_books_stats_generator_setup):
    assert bestselling_books_stats_generator_setup.get_average_reviews(fiction_genre, ranked_year) == 12710

def test_get_average_reviews_2(bestselling_books_stats_generator_setup):
    assert bestselling_books_stats_generator_setup.get_average_reviews(non_fiction_genre, ranked_year) == 14683
