<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD004 -->
<!-- markdownlint-disable MD040 -->

# Embeddings

What are embeddings?

- Vector representations of tokens that become numerical inputs to deep neural networks for encoding / decoding more complex or simple information
- Very useful for understanding how text data can be applied to a variety of problems and can also make its way into other typse of data modalities

Types of Embeddings

- Similar to different levels of tokenization, there are different types of embeddings that can be used to represent text data such as word embeddings or sentence embeddings.

## Token

A token is a chunk of text — typically a word, part of a word, or even a character.
Example:

```
Sentence: "Cats sleep."

Tokens: ["Cats", "sleep", "."]
```

## Vector Representation

Each token gets turned into a vector — a list of numbers that represents the meaning or usage of that token.

Example:

```
Token: "sleep" → Vector: [0.2, -0.1, 0.7, ..., 0.05]
```

These vectors are often dense, meaning every position in the vector has a non-zero value, and they carry semantic meaning — similar words have similar vectors.

- Vector representations of tokens that become numerical inputs to deep neural networks for encoding / decoding more complex or simple information.
- Very useful for understanding how text data can be applied to a variety of problems and can also make its way into other types of data modalities.

## Why Are These Used in Deep Neural Networks?

Neural networks work on numbers. So to make them understand language, we:

1. Encode text into vector representations (numerical inputs).
1. Use those vectors as input to the neural network model.
1. The network then decodes or processes those numbers to:
    - Understand context
    - Predict the next word
    - Translate languages
    - Answer questions, etc.

## Simple vs Complex Information

- Simple Info: “The cat is black.”
    → Easily encoded with basic vectors capturing subject-verb-object.

- Complex Info: “Despite the rain, the crowd stayed, hoping for a glimpse of the star.”
    → Requires richer vectors that capture long-distance dependencies, nuance, and layered meaning.

## Types of Embeddings

- Similar to different levels of tokenization, there are different types of embeddings that can be used to represent text data such as word embeddings or sentence embeddings.

## How to get there

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

### Example Word Embedding Algorithms

- Word2Vec - was a premier, that temp changed the field. Symantic relationships
- GloVe

#### Summary

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
