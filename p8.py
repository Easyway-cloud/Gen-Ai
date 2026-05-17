# Install before running
# pip install langchain-cohere langchain-community cohere

from langchain_cohere import ChatCohere

# Enter your Cohere API key
api_key = "YOUR_API_KEY"

# Load model
model = ChatCohere(
    cohere_api_key=api_key
)

# Create text
text = """
Artificial Intelligence is changing the world.
Machine learning helps computers learn from data.
AI is used in healthcare, education and banking.
"""

# Prompt
prompt = f"""
Read the text and give:

1. Summary
2. Key Points
3. Conclusion

Text:
{text}
"""

# Generate output
result = model.invoke(prompt)

# Print output
print(result.content)