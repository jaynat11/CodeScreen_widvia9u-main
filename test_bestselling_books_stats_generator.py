import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "books")))

from bestselling_books_stats_generator import BestsellingBooksStatsGenerator
from books_csv_parser import BooksCSVParser

fiction_genre = "Fiction"
non_fiction_genre = "Non Fiction"
ranked_year = 2018

@pytest.fixture
def bestselling_books_stats_generator_setup():
    csv_parser = BooksCSVParser('C:/Users/jayad/git_repo/CodeScreen_widvia9u-main/books')
    return BestsellingBooksStatsGenerator(csv_parser)

def test_get_title_of_book_with_most_reviews(bestselling_books_stats_generator_setup):
    csv_parser = bestselling_books_stats_generator_setup
    result = csv_parser.get_title_of_book_with_most_reviews(fiction_genre, ranked_year)
    print(f"Title of the book with most reviews in {fiction_genre} genre and {ranked_year}: {result}")

def test_get_title_of_book_with_most_reviews_2(bestselling_books_stats_generator_setup):
    csv_parser = bestselling_books_stats_generator_setup
    result = csv_parser.get_title_of_book_with_most_reviews(non_fiction_genre, ranked_year)
    print(f"Title of the book with most reviews in {non_fiction_genre} genre and {ranked_year}: {result}")

def test_get_average_reviews(bestselling_books_stats_generator_setup):
    csv_parser = bestselling_books_stats_generator_setup
    result = csv_parser.get_average_reviews(fiction_genre, ranked_year)
    print(f"Average reviews for books in {fiction_genre} genre and {ranked_year}: {result}")

def test_get_average_reviews_2(bestselling_books_stats_generator_setup):
    csv_parser = bestselling_books_stats_generator_setup
    result = csv_parser.get_average_reviews(non_fiction_genre, ranked_year)
    print(f"Average reviews for books in {non_fiction_genre} genre and {ranked_year}: {result}")

if __name__ == "__main__":
    pytest.main()
