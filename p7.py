# Install before running
# pip install transformers torch sentencepiece

from transformers import pipeline

# Load summarization model
print("Loading model...\n")

model = pipeline("summarization")

print("Model loaded\n")

# Long text
text = """
Artificial Intelligence is transforming many industries.
Machine learning and natural language processing are
widely used in healthcare, education, banking,
recommendation systems and autonomous vehicles.
AI helps machines perform tasks like humans.
"""

# Generate summary
result = model(
    text,
    max_length=40,
    min_length=10,
    do_sample=False
)

# Print summary
print("Summary:\n")

print(result[0]["summary_text"])