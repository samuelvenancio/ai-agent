from dotenv import load_dotenv
from google.genai import types
from google import genai
import argparse
import os

def main():
    load_dotenv()
    api_key = os.environ.get('GEMINI_API_KEY')
    if api_key is None:
        raise RuntimeError("GEMINI_API_KEY is missing from the environment")
    client = genai.Client(api_key=api_key)
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    messages: list[types.Content] = [
        types.Content(role="user", parts=[types.Part(text=args.user_prompt)])
    ]
    response = generate_content(client=client, messages=messages)
    if response is None:
        raise RuntimeError("Failed API request")
    print(response.text)
    if args.verbose:
        print(f'User prompt: {messages}')
        print(f'Prompt tokens: {response.usage_metadata.prompt_token_count}')
        print(f'Response tokens: {response.usage_metadata.candidates_token_count}')

def generate_content(client: genai.Client, messages: list[types.Content]) -> types.GenerateContentResponse:
    return client.models.generate_content(
        model='gemini-2.5-flash',
        contents=messages
    )

if __name__ == "__main__":
    main()
