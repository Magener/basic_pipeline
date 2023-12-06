import matplotlib.pyplot as plt
import pandas as pd
import requests

from presenter.consts import API_ENDPOINT, BOOKS_PRESENTED
from presenter.GraphSynthesizer import compute_book_name_column


def present_books(book_dataframe):
    plt.bar(compute_book_name_column(book_dataframe), book_dataframe['avg_score'], color='skyblue')
    plt.xlabel('book')
    plt.ylabel('avg_score')
    plt.title(f'Top {BOOKS_PRESENTED} Books by RatingModel')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    data = requests.get(url=f"{API_ENDPOINT}/api/books?presented_amount={BOOKS_PRESENTED}").json()
    present_books(pd.DataFrame(data))
