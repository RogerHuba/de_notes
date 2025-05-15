<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD004 -->

# Transformers

## Agenda

1. Use Cases
1. High-Level Architecture
1. Tokenization
1. Attention Mechanisms
1. Position Embeddings
1. Project 1 - Sentiment Analysis with Transformer from Scratch via PyTorch
1. Popular Variants - BERT and RoBERTa
1. Project 2 - Text Summarization with BERT Models from HuggingFace
1. Knowledge Distillation
1. Popular Variants - DistilBERT
1. Increasing Context Windows - RoPE and Flash Attention
1. Fine-tuning
1. Efficient Fine-tuning with Low Rank Adaptation (LoRa)
1. Popular Variants - T5
1. Project 3 - Fine-tuning T5 for Named Entity Recognition (NER) with Autotrain
1. Generalized Pretrained Transformer (GPT)
1. Project 4 - Building GPT from Scratch with PyTorch and Lightning AI
1. Alignment - RLHF and DPO
1. Project 5 - Improving GPT Responses with DPO
1. Large Language Models (LLMs)
1. Popular Variants - Llama Architecture
1. Project 6 - Fine-tuning Llama 3.3 8B for Medical Question-Answering with LitGPT
1. Popular Variants - DeepSeek
1. Alignment Variant - GRPO
1. Project 7 - Conducting Local Inference with DeepSeek via Ollama

## Use Cases

1. Machine Translation
    - Translating spoken / written languages.
    - Converting one programming language to another.
1. Question Answering
    - Answering questions based on a given context.
1. Text Generation
    - Generating text based on a given prompt.
    - Summarizing long texts.
1. Classification
    - Classifying text into categories.
    - Sentiment analysis.
1. Named Entity Recognition
    - Identifying and classifying entities in text.

## Transformer Architecture

![Credits: Dive into Deep Learning](https://d2l.ai/_images/transformer.svg)

1. Encoder
    - **Input**: Sequence of tokens from your data.
    - **Output**: Sequence of embeddings to provide context to the decoder.
1. Decoder
    - **Input**: Sequence of tokens from your data.
    - **Output**: Sequence of tokens to generate text or probability score for a given task.

## Tokenization

1. Tokenization
    - Splitting text into tokens.
    - Converting tokens into embeddings.
1. What is a token?
    - A token is a word or a subword or a character in language modeling.
1. What is an embedding?
    - An embedding is a vector representation of a token in language modeling.
![ ](https://miro.medium.com/v2/resize:fit:1050/1*6ttE_KrYJ9iPdBEfa-Qj2g.png)
![ ](https://i0.wp.com/eastgate-software.com/wp-content/uploads/2024/08/Blogs-photos-2.jpg?resize=978%2C551&ssl=1)
1. Tokenizer
    - A tokenizer is a function that converts text into tokens.
1. Popular Tokenizers
    - Word Tokenizers
    - Sentence Tokenizers
    - Byte Pair Encoding (BPE)

## Python Examples

1. `nltk` tokenization
    - Word Tokenizer
    - Sentence Tokenizer
1. `PyTorch` implementation of `Byte Pair Encoding`

## Attention Mechanisms

1. Self Attention
    - A mechanism to allow the model to focus on different positions of the input sequence.
1. Multi-head Attention
    - A mechanism to allow the model to focus on different positions of the input sequence, but with multiple attention heads for parallelization.
1. Masked Multi-head Attention
    - Contrasts multi-head attention by introducing a mask to prevent the model from attending to future tokens.

### NLTK in Python Explained

Tokenization is splitting the input into some form or data structure. Such as splitting text into letters, words, sentences, word pairings. This can include puctuation.

Want to make sure to test this in virtual environemnts.

For this test we will the nltk library
It is best to use a requirements.txt to handle dependencies
This allows for good tracking. This is a good time to remember the pip freeze to export to requrements.txt

#### Example

```python
import nltk

# Example Sentence
sentence = "The quick brown fox jumped over the lazy sleeping dog."
sentences = "The fox was brown. The rat was white. They faught. The rat won."

# NLTK method to seperate by word
word_token = nltk.word_tokenize(sentence)

# NLTK method to seperate by sentence
sentence_token = nltk.snet_tokenize(sentences)
print("Word Tokens:")
print(word_token)

print("Sentence Tokens:")
print(sentence_token)
```

### Embeddings

#### Token

A token is a chunk of text — typically a word, part of a word, or even a character.
Example:

Sentence: "Cats sleep."

Tokens: ["Cats", "sleep", "."]

#### Vector Representation

Each token gets turned into a vector — a list of numbers that represents the meaning or usage of that token.

Example:

Token: "sleep" → Vector: [0.2, -0.1, 0.7, ..., 0.05]

These vectors are often dense, meaning every position in the vector has a non-zero value, and they carry semantic meaning — similar words have similar vectors.

- Vector representations of tokens that become numerical inputs to deep neural networks for encoding / decoding more complex or simple information.
- Very useful for understanding how text data can be applied to a variety of problems and can also make its way into other types of data modalities.

#### Why Are These Used in Deep Neural Networks?

Neural networks work on numbers. So to make them understand language, we:

1. Encode text into vector representations (numerical inputs).
1. Use those vectors as input to the neural network model.
1. The network then decodes or processes those numbers to:
    - Understand context
    - Predict the next word
    - Translate languages
    - Answer questions, etc.

#### Simple vs Complex Information

- Simple Info: “The cat is black.”
    → Easily encoded with basic vectors capturing subject-verb-object.

- Complex Info: “Despite the rain, the crowd stayed, hoping for a glimpse of the star.”
    → Requires richer vectors that capture long-distance dependencies, nuance, and layered meaning.

#### Types of Embeddings

- Similar to different levels of tokenization, there are different types of embeddings that can be used to represent text data such as word embeddings or sentence embeddings.

#### How to get there

"Deep learning models are powerful"

tokenize will yield a list of words.
Look at unique words, or a vocabulary - length of unique - make a set.
    - By converting to a set, we remove any duplicates of the words
    - Remember that set is not ordered.
    - The lenth of the set gives us the total number of unique words: Vocabulary
Our Vocabulary Size is 5
Now we look at how to numberically encode
Take each word and give an index, maybe the position in the list to give an initial value
"deep" goes into a value of 0
"powerful" goes to index 4
We turn this into a {key:value} pair

```json
{"Deep":0, "learning":1, "models":2, "are":3, "powerful":4}
```

embeding size can be whatever we like. Depedning on how we choose, canget rich or poor.
The more the size, the more matrix and time to computate the word embeddings
Our embedding size: 5

So our Vector:

`[0] = "deep"`
`[2] = "models"`
`[1] = "learning"`
`[4] = "powerful"`
`[3] = "are"`

##### Example Word Embedding Algorithms

- Word2Vec - was a premier, that temp changed the field. Symantic relationships
- GloVe

###### Summary

|Term | Meaning|
|---|---|
|Token | A word or character chunk from text|
|Vector | A numerical form of a token|
|Embedding Size| |
|Encoding | Turning text into vectors|
|Input Size | Embedding Size |
|Decoding | Turning vectors back into text or meaning|
|Purpose | To let neural networks process language as numbers|
|Vocabulary Size | |
