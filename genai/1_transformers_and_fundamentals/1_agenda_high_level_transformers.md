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
    - 