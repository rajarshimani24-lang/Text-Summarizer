# Text-Summarizer
This project implements an Abstractive Text Summarizer using Natural Language Processing (NLP). It leverages Hugging Face's Transformers library and a pre-trained BART model (`facebook/bart-large-cnn`) to generate concise, human-like summaries of long text documents.   Developed as part of an internship project for Codec Technologies.
## 🚀 Overview
Unlike extractive summarizers that simply pull existing sentences, this model uses abstractive summarization to actually understand the context and generate *new* sentences to capture the core meaning of the original text.

## 🛠️ Tech Stack
* **Language:** Python
* **Machine Learning Framework:** PyTorch
* **NLP Library:** Hugging Face `transformers`
* **Model:** `facebook/bart-large-cnn`

## ⚙️ How to Run
1. Clone this repository to your local machine.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
