from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains.summarize import load_summarize_chain
from langchain.docstore.document import Document
from dotenv import load_dotenv
import os

# Load API key from .env
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

def summarize_text(text):
    # Initialize Groq LLM
    llm = ChatGroq(
        groq_api_key=groq_api_key,
        model_name="llama3-8b-8192",
        temperature=0
    )

    # Wrap text in a Document
    docs = [Document(page_content=text)]

    # Use map-reduce summarization chain
    chain = load_summarize_chain(llm, chain_type="map_reduce")
    summary = chain.run(docs)
    return summary
