import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv('.env')
# Initialize the OpenAI client with the API key from environment variables
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))


# Function to summarize text using the OpenAI API
def summarize_text(text: str) -> str:
    # Create a completion request to the OpenAI API
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You're a business assistant. "
                           "Your task is to make a summary of the PDF content"
            },
            {
                "role": "user",
                "content": f"Summarize the following text:\n\n{text}"
            }
        ]
    )
    # Return the content of the first choice from the completion response
    return completion.choices[0].message.content
