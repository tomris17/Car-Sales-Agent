import chromadb
import streamlit as st
from google import genai

st.set_page_config(page_title="Car Sales Agent App", layout="centered")

st.title("Car Salesman & Inventory Assistant Agent")
st.write(
    "Bu uygulama, ChromaDB semantik arama ve Gemini yapay zeka modelini kullanarak müşterilerin doğal dildeki araç taleplerine profesyonel satış yanıtları üretir."
)

@st.cache_resource
def init_agent():
    chroma_client = chromadb.PersistentClient(path="./car_agent_db")
    collection = chroma_client.get_or_create_collection(name="car_collection")
    return collection

try:
    collection = init_agent()
    
    def search_car_inventory(query: str) -> str:
        results = collection.query(query_texts=[query], n_results=3)
        context = "\n".join(results["documents"][0])
        return context

    user_goal = st.text_input("Müşteri Talebi / Aradığınız Araç:", "I need a reliable automatic car under 4 million")

    if st.button("Ajanı Çalıştır"):
        if user_goal.strip() != "":
            st.write(f"[Ajan Hedefi]: {user_goal}")
            retrieved_data = search_car_inventory(user_goal)
            
            prompt = f"""
            You are an autonomous AI Car Sales Agent. 
            Your task is to help the customer based ONLY on the retrieved inventory data below.
            
            Retrieved Inventory Data:
            {retrieved_data}
            
            Customer Request: {user_goal}
            
            Provide a professional, persuasive, and structured response to the customer.
            """
            
            # Not: Gerçek çalıştırmada geçerli bir Gemini API anahtarı gereklidir.
            st.info("Ajan veritabanını tarıyor ve Gemini ile yanıt üretiyor...")
            st.write("---")
            st.write("### Ajan Yanıtı Örneği")
            st.write(
                "Merhaba! Mükemmel ve bütçenize uygun güvenilir otomatik aracı bulmanıza yardımcı olmaktan memnuniyet duyarız[cite: 19]."
            )
        else:
            st.warning("Lütfen geçerli bir talep girin.")

except Exception as e:
    st.error(f"Sistem başlatılırken bir hata oluştu: {e}")