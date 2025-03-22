import re
import sys

def calculate_text_stats(text):
    """
    Calculate statistics about a piece of text.
    
    Args:
        text (str): The input text to analyze
        
    Returns:
        tuple: (average_word_length, word_count)
    """
    # Remove punctuation and convert to lowercase
    text = re.sub(r'[^\w\s]', '', text.lower())
    
    # Split the text into words
    words = text.split()
    
    # Filter out empty strings
    words = [word for word in words if word]
    
    # Count the number of words
    word_count = len(words)
    
    if not words:
        return 0, 0
    
    # Calculate total characters
    total_chars = sum(len(word) for word in words)
    
    # Calculate average word length
    average_length = total_chars / word_count
    
    return average_length, word_count

def main():
    # Read text from stdin until EOF
    try:
        text = sys.stdin.read()
    except KeyboardInterrupt:
        print("\nInput interrupted.")
        return
        
    # Calculate and display the results
    avg_length, word_count = calculate_text_stats(text)
    print(f"Total words: {word_count}")
    print(f"Average word length: {avg_length:.2f} characters")

if __name__ == "__main__":
    main()
