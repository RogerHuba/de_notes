<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD004 -->

# NLTK in Python Explained

Tokenization is splitting the input into some form or data structure. Such as splitting text into letters, words, sentences, word pairings. This can include puctuation.

Want to make sure to test this in virtual environemnts.

For this test we will the nltk library
It is best to use a requirements.txt to handle dependencies
This allows for good tracking. This is a good time to remember the pip freeze to export to requrements.txt

## Example

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
