# Install before running
# pip install gensim matplotlib scikit-learn

import matplotlib.pyplot as plt

from gensim.models import Word2Vec
from sklearn.manifold import TSNE

# Medical text
text = [

    ["patient", "diabetes"],

    ["doctor", "treatment"],

    ["vaccine", "infection"],

    ["fever", "pain"],

    ["brain", "scan"],

    ["therapy", "recovery"],

    ["surgery", "doctor"],

    ["medicine", "pain"],

    ["disease", "diagnosis"]
]

# Train model
model = Word2Vec(
    text,
    vector_size=20,
    min_count=1
)

# Get words
words = model.wv.index_to_key

# Get vectors
vec = [model.wv[word]
       for word in words]

# Reduce dimensions
tsne = TSNE(
    n_components=2,
    perplexity=5
)

new_vec = tsne.fit_transform(vec)

# Graph
plt.figure(figsize=(8,6))

for i in range(len(words)):

    plt.scatter(new_vec[i][0],
                new_vec[i][1])

    plt.text(new_vec[i][0],
             new_vec[i][1],
             words[i])

plt.title("Word Embeddings")

plt.grid()

plt.show()

# Similar words
print("Words similar to treatment\n")

result = model.wv.most_similar(
    "treatment",
    topn=5
)

for word, score in result:

    print(word, ":",
          round(score,2))