# Install before running
# pip install gensim matplotlib scikit-learn

# Import libraries
import gensim.downloader as api
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA

# Load model
print("Loading model...\n")

model = api.load("word2vec-google-news-300")

print("Model loaded\n")

# Technology words
words = [
    "computer",
    "internet",
    "software",
    "hardware",
    "keyboard",
    "mouse",
    "server",
    "network",
    "programming",
    "database"
]

# Get vectors
vec = []

for word in words:

    vec.append(model[word])

# PCA
pca = PCA(n_components=2)

new_vec = pca.fit_transform(vec)

# Similar words
input_word = "computer"

result = model.most_similar(
    input_word,
    topn=5
)

# Print output
print("Top 5 words similar to",
      input_word, "\n")

for word, score in result:

    print(word, ":",
          round(score, 4))

# Draw graph
plt.figure(figsize=(8,6))

for i in range(len(words)):

    plt.scatter(new_vec[i,0],
                new_vec[i,1])

    plt.text(new_vec[i,0],
             new_vec[i,1],
             words[i])

plt.title("PCA Word Embeddings")

plt.xlabel("PC1")

plt.ylabel("PC2")

plt.grid()

plt.show()