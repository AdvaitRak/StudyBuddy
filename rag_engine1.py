# rag_engine.py

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.chat_models import ChatOllama
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.memory import ConversationSummaryBufferMemory


def load_docs(file_path):
    loader = PyPDFLoader(file_path)
    return loader.load()


def split_docs(documents, chunk_size=1500, chunk_overlap=300):
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return splitter.split_documents(documents)


def create_vectorstore(splits):
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    vectorstore = FAISS.from_documents(splits, embeddings)
    return vectorstore


def get_chat_chain_with_memory(vectorstore):
    llm = ChatOllama(model="gemma:2b")
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    return ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=ConversationSummaryBufferMemory(llm=llm,memory_key="chat_history",return_messages=True,max_token_limit=1000 ),
        return_source_documents=False,
        output_key="answer", 
        verbose=False
    )
