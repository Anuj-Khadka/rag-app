import streamlit as st

st.set_page_config(layout="wide", page_title="Project Documentation", page_icon="📄")


st.title("📄 Project Documentation")


st.header("📚 RAG Application with LLaMA 3.1, ChromaDB, and Streamlit")

st.header("🛠 Tech Stack Used")
st.markdown("""
- **Frontend:** Streamlit
- **LLM Backend:** Ollama (Self-hosted models)
- **Vector Database:** ChromaDB
- **Dockerized Services:** Docker, docker-compose
- **Language:** Python
""")

st.header("⚙️ Setup Instructions")
st.markdown("""
1. Install Docker
2. Clone the repository
3. Run `pip install -r requirements.txt`
4. Run `docker-compose up --build`
5. Open your browser at `localhost:8501`
""")

st.header("🔗 Resources")
st.markdown("""
- [Ollama Documentation](https://ollama.ai)
- [ChromaDB Documentation](https://docs.trychroma.com/)
- [Streamlit Documentation](https://docs.streamlit.io)
- [Docker Documentation](https://docs.docker.com/)
""")
