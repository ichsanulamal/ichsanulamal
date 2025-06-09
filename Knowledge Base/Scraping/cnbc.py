import requests
from bs4 import BeautifulSoup
import pendulum
import pandas as pd
from sqlalchemy import create_engine

db_params = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "postgres",
    "host": "127.0.0.1",  # Change to your database host
    "port": "5432",  # Change to your database port
}
db_url = f"postgresql://{db_params['user']}:{db_params['password']}@{db_params['host']}:{db_params['port']}/{db_params['dbname']}"
engine = create_engine(db_url)


def get_articles(url, page_date, page_index, category_name, category_id):
    print(url)
    res = []

    response = requests.get(url)
    html_code = response.text
    soup = BeautifulSoup(html_code, "html.parser")

    articles = soup.find_all("article")

    for article in articles:
        title = article.find("h2").text.strip()
        href = article.find("a")["href"]
        img_url = article.find("img")["src"]

        data = {
            "article_date": page_date,
            "article_page_index": page_index,
            "article_title": title,
            "article_href": href,
            "article_img": img_url,
            "category_name": category_name,
            "category_id": category_id,
        }

        res.append(data)
    return res


categories = [
    ["market", "5"],
    ["news", "3"],
    ["entrepreneur", "9"],
    ["syariah", "10"],
    ["tech", "12"],
    ["lifestyle", "11"],
    ["opini", "13"],
    ["mymoney", "71"],
    ["cuap-cuap-cuan", "78"],
    ["research", "127"],
]

df = []
for cat in categories:
    category_name, category_id = cat[0], cat[1]

    base_url = f"https://www.cnbcindonesia.com/{category_name}/indeks/{category_id}/"
    start_date = pendulum.parse("2024-05-09")
    end_date = pendulum.parse("2024-05-17")

    current_date = start_date
    while current_date <= end_date:
        index = 1
        while True:
            url = f'{base_url}{index}?date={current_date.format("YYYY/MM/DD")}'
            articles = get_articles(
                url=url,
                page_date=current_date.format("YYYY-MM-DD"),
                page_index=index,
                category_name=category_name,
                category_id=category_id,
            )
            if not articles:
                print(f"Not found: {category_name} - {current_date} - {index}")
                break
            else:
                print(
                    pd.DataFrame(articles).to_sql(
                        name="cnbc_indonesia",
                        con=engine,
                        schema="personal",
                        if_exists="append",
                        method="multi",
                        index=False,
                    )
                )
            index += 1
        current_date = current_date.add(days=1)
