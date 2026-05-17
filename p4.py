# Install before running
# pip install gensim sentence-transformers
import gensim.downloader as api
from sentence_transformers import SentenceTransformer
from sentence_transformers import util

# Load model
print("Loading model...\n")

model = api.load("glove-wiki-gigaword-100")

print("Model loaded\n")

# Original prompt
text = "Explain benefits of exercise"

print("Original Prompt:\n")

print(text)

# Get similar words
extra = []

for word in text.lower().split():

    try:

        result = model.most_similar(
            word,
            topn=2
        )

        for w, s in result:

            extra.append(w)

    except:

        pass

# Enriched prompt
new_text = text + " " + " ".join(extra)

print("\nEnriched Prompt:\n")

print(new_text)

# Detail
print("\nOriginal Detail:",
      len(text.split()))

print("Enriched Detail:",
      len(new_text.split()))

# Relevance
sim = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

v1 = sim.encode(text,
                convert_to_tensor=True)

v2 = sim.encode(new_text,
                convert_to_tensor=True)

score = util.cos_sim(v1, v2)

print("\nRelevance Score:",
      round(score.item(),4))

# Diversity
d1 = len(set(text.split())) / len(text.split())

d2 = len(set(new_text.split())) / len(new_text.split())

print("\nOriginal Diversity:",
      round(d1,4))

print("Enriched Diversity:",
      round(d2,4))