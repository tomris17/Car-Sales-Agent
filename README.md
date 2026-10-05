# Car Salesman & Inventory Assistant Agent

[![Python](https://img.shields.io/badge/Python-3.13%2B-blue.svg)](https://www.python.org/)
[![ChromaDB](https://img.shields.io/badge/ChromaDB-VectorSearch-orange.svg)](https://www.trychroma.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)](https://streamlit.io/)

This project builds an intelligent car sales agent that uses semantic search and structured filtering on the OLX car dataset to assist customers in natural language[cite: 19].

---

## Project Workflow
1. **Database Initialization**: Setting up a persistent ChromaDB client and collection (`car_collection`) for inventory documents[cite: 19].
2. **Semantic Search Function**: Querying the vector database to retrieve the top matching vehicle documents based on user goals[cite: 19].
3. **AI Agent Generation**: Utilizing Google GenAI and Gemini models with specialized prompts to generate professional, persuasive, and structured responses to customers[cite: 19].
4. **Web Application**: Interactive user deployment interface built with Streamlit.

---

## Getting Started & Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/car-sales-agent.git](https://github.com/YOUR_USERNAME/car-sales-agent.git)
   cd car-sales-agent
