import requests
import csv

# Ask for user input
query = input("Enter a keyword to search for: ")
num_articles = int(input("Enter the number of articles to retrieve: "))

# Replace YOUR_API_KEY with your actual NewsAPI key
url = f"https://newsapi.org/v2/everything?q={query}&pageSize=100&page=1&apiKey=8f89582e7ffc45f1b73faeca278f87e5"

articles = []

# Retrieve the specified number of articles (up to 500, the max allowed by NewsAPI)
for i in range((num_articles-1)//100 + 1):
    response = requests.get(url.format(i + 1))
    if response.status_code == 200:
        data = response.json()
        articles += data["articles"]
    else:
        print("Error:", response.status_code)
        break

# Save data to a CSV file
filename = input("Enter a filename to save the CSV data: ")
with open(f"{filename}.csv", "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["title", "description"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for article in articles:
        writer.writerow({"title": article["title"], "description": article["description"]})

print(f"{len(articles)} articles saved to {filename}.csv")
