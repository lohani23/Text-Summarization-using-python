from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

# Choose the language for summarization (e.g., English)
language = "english"

# Initialize the summarizer algorithm (LexRank in this case)
summarizer = LexRankSummarizer()
text = """
This is the long text that you want to summarize. It can have multiple sentences and paragraphs. 
The purpose of text summarization is to extract the most important information and generate a concise summary.
There are different techniques and algorithms for text summarization, including extractive and abstractive methods.
Extractive summarization involves selecting the most relevant sentences or phrases from the original text,
while abstractive summarization aims to generate new sentences that capture the essence of the original text.
In this example, we will use the LexRank algorithm provided by the sumy library for extractive summarization.
"""

# Initialize a plaintext parser with the given text
parser = PlaintextParser.from_string(text, Tokenizer(language))

# Set the number of sentences in the summary
num_sentences = 3  # Adjust this value based on your desired summary length
# Use the summarizer to get the summary
summary_sentences = summarizer(parser.document, num_sentences)

# Join the summary sentences into a single string
summary = " ".join([str(sentence) for sentence in summary_sentences])
print(summary)
