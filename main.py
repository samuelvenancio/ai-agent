from dotenv import load_dotenv
from google import genai
import os

def main():
    load_dotenv()
    api_key = os.environ.get('GEMINI_API_KEY')
    if api_key is None:
        raise RuntimeError('GEMINI_API_KEY is missing from the environment')
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents='Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.'
    )
    if response is None:
        raise RuntimeError('Failed API request')
    print(f'Prompt tokens: {response.usage_metadata.prompt_token_count}')
    print(f'Response tokens: {response.usage_metadata.candidates_token_count}')
    print(response.text)


if __name__ == "__main__":
    main()
