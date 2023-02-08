# OpenAI API Document Embedding (Semantic Search & Q&A) prototype for Enterprise customers

For internal purposes:This project aims to provide an alternative to full text and keyword search through a GenerativeAI approach. This implementation leverages OpenAI's Embeddings model `ada` to improve search with more contextual relevance, improved accuracy, and natural language intent understanding.

## Requirements

- Python 3.7 or higher
- pandas
- openai
- tiktoken

## Usage

1. First, install the required packages using `pip install -r requirements.txt`.
2. Load your document data into a pandas dataframe with a single column called `vscontent`.
3. Run the `compute_doc_embeddings` function, passing in your dataframe, to generate the embeddings.
4. Use the `order_document_sections_by_query_similarity` function, passing in your query and the document embeddings, to find the most relevant documents.
5. Finally, use the `construct_prompt` function to generate a prompt containing the relevant document sections concatenated together, along with your original query.

## Example

```python
import pandas as pd
import openai
import tiktoken

# Load the sample vSTART document data into a dataframe
df = pd.read_csv("vstart.csv")

# Compute the embeddings for each document
document_embeddings = compute_doc_embeddings(df)

# Find the most relevant documents for a given query
relevant_documents = order_document_sections_by_query_similarity("Name a tenet of prioritization", document_embeddings)

# Generate a prompt containing the relevant document sections concatenated together, along with your original query
prompt = construct_prompt("Name a tenet of prioritization", document_embeddings, df)

```

## Contributing

If you would like to learn more about applying this prototype to meet your program needs or to contribute to this project, please reach out to Noble for more information.

## Maintainers

Noble Ackerson nackerson@ventera.com
