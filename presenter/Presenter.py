import matplotlib.pyplot as plt
import pandas as pd
import requests

from presenter.consts import BOOKS_PRESENTED, API_ENDPOINT

data = requests.get(url=f"{API_ENDPOINT}/api/books?presented_amount={BOOKS_PRESENTED}").json()

df = pd.DataFrame(data)

plt.bar(df['book_id'], df['avg_score'], color='skyblue')

plt.xlabel('book_id')
plt.ylabel('avg_score')

plt.title(f'Top {BOOKS_PRESENTED} Books by Rating')

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()