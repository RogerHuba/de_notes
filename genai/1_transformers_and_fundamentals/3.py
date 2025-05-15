# Big Picture: What is this script doing?
# You're taking a sentence and:
# 1. Breaking it into words (tokenizing).
# 2. Giving each word a unique ID (vocabulary).
# 3. Turning those word IDs into vectors (embeddings) using PyTorch.
# This is foundational in NLP because neural networks can’t understand text directly — they need numbers, and embeddings are how we turn words into meaningful numbers.

# Import PyTorch for tensor operations and building neural network components
import torch

# Import NLTK's word tokenizer
from nltk import word_tokenize

# --- Function: Tokenize a sentence into words ---
def tokenize_sentence(sentence: str) -> list[str]:
    """
    This function checks if the sentence contains a period (basic sentence check),
    removes it, and tokenizes the sentence into individual words.
    """
    # Check if the input contains a period (basic sentence format validation)
    if '.' in sentence:
        # Remove the period so it doesn't become its own token
        sentence = sentence.replace('.', '')
    else:
        # If no period, raise an error to enforce sentence formatting
        raise ValueError("The input text is not a sentence.")

    # Use NLTK to split the sentence into individual word tokens
    return word_tokenize(sentence)

# --- Function: Create a vocabulary from word tokens ---
def create_word_vocab(tokens: list[str]) -> dict:
    """
    This function takes a list of tokens (words) and assigns a unique index
    to each word using a Python dictionary.
    """
    # Use set() to get unique words, then assign each a number using enumerate
    return {token: idx for idx, token in enumerate(set(tokens))}

# --- Function: Generate embeddings using PyTorch ---
def generate_embedding(vocab: dict, tokens: list[str], embedding_dim: int = 5) -> torch.Tensor:
    """
    This function converts words into numerical indices based on the vocab,
    then uses a PyTorch Embedding layer to convert those indices into dense vectors.
    """

    # Convert each word token into its corresponding numerical index
    token_indices = [vocab[token] for token in tokens]

    # Convert the list of indices into a PyTorch tensor
    input_tensor = torch.tensor(token_indices)

    # Create a PyTorch embedding layer:
    # - num_embeddings = total number of unique words (vocab size)
    # - embedding_dim = number of features in each word vector
    embedding_layer = torch.nn.Embedding(num_embeddings=len(vocab), embedding_dim=embedding_dim)

    # Pass the input tensor into the embedding layer to get vector representations
    embedded_output: torch.Tensor = embedding_layer(input_tensor)

    # Print the generated word embeddings (random values unless trained)
    print(f"Word Embeddings: {embedded_output}")

    # Print the shape: (number of words, embedding dimension)
    print(f"Shape of the embeddings: {embedded_output.shape}")

    # Return the tensor containing word embeddings
    return embedded_output

# ---------------- Main Program Flow ----------------


sentence = 'Deep learning models are powerful.'
# Step 1: Define a sentence to process

tokens = tokenize_sentence(sentence=sentence)
# Step 2: Tokenize the sentence into words
# Output: ['Deep', 'learning', 'models', 'are', 'powerful']

vocab = create_word_vocab(tokens=tokens)
# Step 3: Create a vocabulary from the tokens
# Example: {'Deep': 0, 'learning': 1, 'models': 2, 'are': 3, 'powerful': 4}

embedding_output = generate_embedding(vocab=vocab, tokens=tokens, embedding_dim=5)
# Step 4: Generate embeddings for each word in the sentence
# Output: Tensor with shape [5 words, 5-dimensional vectors]
# ExampleEmbedding Output: tensor(
    # [
    #     [ 0.9435,  0.0287,  0.5086,  1.1486, -0.4988],
    #     [-0.5176,  1.3344,  0.6804, -0.0417,  0.7454],
    #     [ 0.9118, -0.3946, -0.7673,  0.1083,  0.5649],
    #     [-0.8922, -1.0466, -1.3613,  0.8851, -0.5393],
    #     [-0.2567,  1.0250,  0.3129,  1.7350, -0.9159]
    # ],
    #    grad_fn=<EmbeddingBackward0>)
    
# This is a 5×5 tensor, meaning:
# There are 5 rows → each one corresponds to a word in your input sentence.
# There are 5 columns → each number in a row is one dimension of the word's embedding vector.
# So each word is represented by a 5-dimensional vector of real numbers.
# You chose embedding_dim=5, so each word is mapped to 5 learned (currently random) features.

# Word	    Embedding Vector (5 values)
# Deep	    [0.9435, 0.0287, 0.5086, 1.1486, -0.4988]
# learning	[-0.5176, 1.3344, 0.6804, -0.0417, 0.7454]
# models	[0.9118, -0.3946, -0.7673, 0.1083, 0.5649]
# are	    [-0.8922, -1.0466, -1.3613, 0.8851, -0.5393]
# powerful	[-0.2567, 1.0250, 0.3129, 1.7350, -0.9159]

# These values are not meaningful yet — they are randomly initialized when the Embedding layer is created. During training, these vectors get adjusted so that words with similar meanings have similar vectors.

# PyTorch randomly initializes the embedding weights for each word (token) in your vocabulary. These are not pre-trained embeddings — they’re random vectors meant to be learned during training.
# You're seeing a different output every time you run the script because:
    # A new embedding_layer is created.
    # That layer has random weights each time it's instantiated.
    # So the output vectors are random until trained.
    