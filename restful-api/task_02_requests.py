import requests

URL = "https://jsonplaceholder.typicode.com/posts"

def fetch_and_print_posts():
    response = requests.get(URL)

    print("Status Code:", response.status_code)

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])

import csv

def fetch_and_save_posts():
    response = requests.get(URL)

    if response.status_code == 200:
        posts = response.json()

        with open("posts.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames =["id", "title", "body"])
            writer.writeheader()

            for post in posts:
                writer.writerow
                ({
                    "id": post["id"],
                    "title": post["title"],
                    "body": post["body"]
                })
