# Import the Natural Language Toolkit library
import nltk

# Download the 'punkt' tokenizer models if not already available.
# This is required for both word and sentence tokenization.
nltk.download('punkt')

# --- Word Tokenization Example ---

# Define a simple sentence as a string
sentence = "The brown fox crosses the road."

# Use nltk's word_tokenize method to split the sentence into words and punctuation
word_tokens = nltk.word_tokenize(sentence)

# Print a label for clarity
print("Word Tokenizer Output:")

# Print the list of word tokens
# Output: ['The', 'brown', 'fox', 'crosses', 'the', 'road', '.']
print(word_tokens)

# --- Sentence Tokenization Example ---

# Define a block of text containing multiple sentences
text = ("The brown fox crossed the road. "
        "A man saw the fox from the other side of a bridge and started approaching it.")

# Use nltk's sent_tokenize method to split the text into individual sentences
sentence_tokens = nltk.sent_tokenize(text)

# Print a label for clarity
print("\nSentence Tokenizer Output:")

# Print the list of sentence tokens
# Output: ['The brown fox crossed the road.', 
#          'A man saw the fox from the other side of a bridge and started approaching it.']
print(sentence_tokens)
