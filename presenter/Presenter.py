import requests
import matplotlib.pyplot as plt
import pandas as pd

from presenter.consts import BOOKS_PRESENTED

data = requests.get(url="http://127.0.0.1:8001/api/books").json()[0:BOOKS_PRESENTED]

df = pd.DataFrame(data)

plt.bar(df['book_id'], df['avg_score'], color='skyblue')

plt.xlabel('book_id')
plt.ylabel('avg_score')


plt.title(f'Top {BOOKS_PRESENTED} Books by Rating')

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()