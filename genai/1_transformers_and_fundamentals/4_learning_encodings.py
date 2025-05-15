import torch
import torch.nn as nn

# Create a class LearnedPositionEmbedding
class LearnedPositionEmbedding(nn.Module):
    # Constructor
    def __init__(self, vocab_size, embed_dim, max_seq_len):
        super(LearnedPositionEmbedding, self).__init__()
        # Create an embedding layer
        self.embedding = nn.Embedding(vocab_size, embed_dim)
        
        # Create a position embedding layer
        self.position_embedding = nn.Embedding(max_seq_len, embed_dim)
    
    # Define forward pass
    def forward(self, x):
        seq_len = x.size(1)

        # Generate position indices (e.g. [0, 1, 2, ... seq_len - 1])
        position_ids = torch.arange(seq_len, dtype=torch.long, device=x.device).unsqueeze(0).expand_as(x)

        # Embed tokens and positions
        token_embeddings = self.embedding(x)
        position_embeddings = self.position_embedding(position_ids)

        # Add the embeddings together - Concatenates the token embeddings with information about the positions of each token
        embeddings = token_embeddings + position_embeddings

        return embeddings

# Example Usage
vocab_size = 1000 # Size of the vocabulary
embed_dim = 512
max_seq_len = 100 # Max seq length

# Instantiate a model
model = LearnedPositionEmbedding(vocab_size=vocab_size, embed_dim=embed_dim, max_seq_len=max_seq_len)

# Dummy Input - Batch of 2 sentences each with 10 tokens
dummy_input = torch.randint(0, vocab_size, (2, 10))

# Output from the forward pass
output: torch.Tensor = model(dummy_input)

print(output.shape) # Should be torch.Size([2, 10, 512])
