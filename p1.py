# Install before running
# pip install gensim scipy

# Import libraries
import gensim.downloader as api
from scipy.spatial.distance import cosine

# Load Word2Vec model
print("Loading model...")

model = api.load("word2vec-google-news-300")

print("Model loaded\n")

# Word vector
print("First 10 values of 'king'\n")

print(model["king"][:10])

# Similar words
print("\nSimilar words to 'king'\n")

for word, score in model.most_similar("king", topn=10):

    print(word, ":", round(score, 4))

# Analogy 1
print("\nking - man + woman = ?\n")

result = model.most_similar(
    positive=["king", "woman"],
    negative=["man"],
    topn=1
)

print(result[0][0],
      ":",
      round(result[0][1], 4))

# Analogy 2
print("\nparis + italy - france = ?\n")

for word, score in model.most_similar(
        positive=["paris", "italy"],
        negative=["france"],
        topn=5):

    print(word, ":", round(score, 4))

# Analogy 3
print("\nwalking + swimming - walk = ?\n")

for word, score in model.most_similar(
        positive=["walking", "swimming"],
        negative=["walk"],
        topn=5):

    print(word, ":", round(score, 4))

# Cosine similarity
sim = 1 - cosine(
    model["king"],
    model["queen"]
)

print("\nSimilarity between king and queen =",
      round(sim, 4))