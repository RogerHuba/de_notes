import math
import torch
import torch.nn as nn

# Class - FixedPositionalEncoding
class FixedPositionalEncoding(nn.Module):
    # Constructor
    def __init__(self, embed_dim, max_seq_len):

        # Apply super()
        super(FixedPositionalEncoding, self).__init__()

        # Create a matrix (max_seq_len, embed_dim)
        position_enc = torch.zeros(max_seq_len, embed_dim)

        position = torch.arange(0, max_seq_len, dtype=torch.float).unsqueeze(1)

        # Division Term
        div_term = torch.exp(torch.arange(0, embed_dim, 2).float() * (-math.log(10000.0) / embed_dim))

        # Apply updates to the position_enc by odd or even indices

        # Even - sin() function
        position_enc[:, 0::2] = torch.sin(position * div_term)

        # Odd - cos() function
        position_enc[:, 1::2] = torch.cos(position * div_term)

        # Register a buffer so then there's no update to these positions during training
        self.register_buffer('positional_encoding', position_enc.unsqueeze(0))

    # Forward Pass
    def forward(self, x):
        seq_len = x.size(1)

        # Comes from the registered buffer
        return self.positional_encoding[:, :seq_len, :]
    

# Example Usage
embed_dim = 512
max_seq_len = 100

# Define pos_encoding
pos_encoding = FixedPositionalEncoding(embed_dim=embed_dim, max_seq_len=max_seq_len)

# Dummy Input
dummy_input = torch.zeros(2, 10, embed_dim)

# Add positional encodings
output: torch.Tensor = dummy_input + pos_encoding(dummy_input)

print(output.shape)
