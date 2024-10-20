import csv
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Read data from CSV file
with open('cross.csv', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    text = ""
    for row in reader:
        text += row['description'] + " "

# Generate word cloud
wordcloud = WordCloud(width=800, height=800, background_color='white').generate(text)

# Display the generated wordcloud image
plt.figure(figsize=(8,8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()