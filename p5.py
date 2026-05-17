# Install before running
# pip install gensim

import gensim.downloader as api

# Load model
print("Loading model...\n")

model = api.load("glove-wiki-gigaword-100")

print("Model loaded\n")

# Get similar words
def similar(word):

    try:

        result = model.most_similar(
            word.lower(),
            topn=5
        )

        return [w[0] for w in result]

    except:

        return []

# Create paragraph
def paragraph(word, words):

    text = word + " is an important field. "

    text += "It is related to "

    text += ", ".join(words)

    text += ". "

    text += "It helps in solving real world problems."

    return text

# Input word
seed = input("Enter a seed word: ")

# Similar words
words = similar(seed)

print("\nSimilar Words:\n")

print(words)

# Paragraph
print("\nGenerated Paragraph:\n")

print(paragraph(seed, words))