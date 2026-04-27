import os
from transformers import pipeline

def load_text_from_file(filename="article.txt"):
    """Reads the long text from a file."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
            # Basic validation to ensure the text isn't too short
            if len(text.split()) < 50:
                 print("Warning: The text is quite short. The summary might not be optimal.")
            return text
    except FileNotFoundError:
        print(f"Error: Could not find '{filename}'. Please create it and paste your text inside.")
        return None

def main():
    print("Loading the text from article.txt...")
    original_text = load_text_from_file()
    
    if not original_text:
        return

    print("\nInitializing the AI Summarizer... (This may take a moment if downloading the model for the first time)")
    # We use facebook/bart-large-cnn as it is heavily optimized for abstractive summarization
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

    print("\nGenerating summary...")
    # Generate the summary. We set limits to ensure it condenses the text effectively.
    # You can adjust max_length and min_length based on your needs.
    summary = summarizer(original_text, max_length=130, min_length=30, do_sample=False)

    print("\n" + "="*50)
    print("📰 ORIGINAL TEXT (First 500 characters):")
    print("="*50)
    print(original_text[:500] + "...\n")

    print("✨ AI GENERATED SUMMARY:")
    print("="*50)
    # The pipeline returns a list of dictionaries, we extract the text
    print(summary[0]['summary_text'])
    print("="*50 + "\n")

if __name__ == '__main__':
    main()
