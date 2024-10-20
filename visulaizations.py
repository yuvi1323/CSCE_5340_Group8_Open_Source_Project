import csv
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import STOPWORDS

# Pie chart for the top N most common words
plt.figure(figsize=(8, 8))
plt.pie(counts, labels=words, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
plt.title(f'Word Frequency Distribution (Top {top_n} Words)')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.tight_layout()
plt.show()

# Calculate word lengths
word_lengths = [len(word) for word in filtered_words]

# Create a histogram of word lengths
plt.figure(figsize=(8, 6))
plt.hist(word_lengths, bins=range(1, max(word_lengths) + 1), color='purple', edgecolor='black')
plt.xlabel('Word Length')
plt.ylabel('Frequency')
plt.title('Histogram of Word Lengths')
plt.tight_layout()
plt.show()

# Cumulative frequency plot of the top N words
cumulative_counts = [sum(counts[:i+1]) for i in range(len(counts))]

plt.figure(figsize=(8, 6))
plt.plot(words, cumulative_counts, marker='o', color='green')
plt.xlabel('Words')
plt.ylabel('Cumulative Frequency')
plt.title('Cumulative Frequency of Top Words')
plt.grid(True)
plt.tight_layout()
plt.show()

import seaborn as sns
import numpy as np

# Create a matrix of word co-occurrences (for top N words)
co_occurrence_matrix = np.zeros((top_n, top_n))

for description in text.split('.'):
    description_words = set(description.lower().split())
    for i, word1 in enumerate(words):
        if word1 in description_words:
            for j, word2 in enumerate(words):
                if word2 in description_words:
                    co_occurrence_matrix[i][j] += 1

# Create heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(co_occurrence_matrix, xticklabels=words, yticklabels=words, cmap="YlGnBu", annot=True)
plt.title("Heatmap of Word Co-occurrences")
plt.tight_layout()
plt.show()
