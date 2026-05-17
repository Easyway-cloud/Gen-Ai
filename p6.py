# Install before running
# pip install transformers

from transformers import pipeline

# Load sentiment model
model = pipeline("sentiment-analysis")

# Sentences
text = [

    "I love this mobile phone",

    "The service was terrible",

    "The movie was boring",

    "This laptop works perfectly"
]

# Find sentiment
result = model(text)

# Print output
for sentence, value in zip(text, result):

    print("Sentence:",
          sentence)

    print("Sentiment:",
          value["label"])

    print("Confidence Score:",
          round(value["score"],4))

    print()