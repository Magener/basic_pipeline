import requests
import matplotlib.pyplot as plt
import pandas as pd

from presenter.consts import BOOKS_PRESENTED, API_ENDPOINT

data = requests.get(url=f"{API_ENDPOINT}/api/books").json()[0:BOOKS_PRESENTED] # TODO: do filteration & ordering on API_ENDPOINT side, not client.

df = pd.DataFrame(data)

plt.bar(df['book_id'], df['avg_score'], color='skyblue')

plt.xlabel('book_id')
plt.ylabel('avg_score')


plt.title(f'Top {BOOKS_PRESENTED} Books by Rating')

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()