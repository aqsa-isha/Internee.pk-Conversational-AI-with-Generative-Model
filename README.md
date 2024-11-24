# Gemini Q&A App

The **Gemini Q&A App** is a Streamlit-powered application that uses Google's **Gemini Pro** large language model (LLM) to provide intelligent, real-time responses. This app offers an intuitive interface for Q&A interactions, a visually appealing design, and easy management of chat history.

## Features

- **Real-time Q&A**: Powered by Google's **Gemini Pro** LLM for intelligent responses.
- **Chat History**: View and manage previous conversations.
- **Clear Chat**: Reset the chat history with a single click.
- **Interactive UI**: Modern design for an engaging user experience.

---

## Installation Guide

Follow these steps to set up and run the application locally:

### Prerequisites

- Python 3.9 or higher
- A valid **Google Gemini API key**

### Steps to Run

1. **Clone the repository**  
   ```bash
   git clone <repository_url>
   cd <repository_name>

Set up a virtual environment

On Windows:
bash
Copy code
python -m venv venv
venv\Scripts\activate
On macOS/Linux:
bash
Copy code
python -m venv venv
source venv/bin/activate
Install dependencies

bash
Copy code
pip install -r requirements.txt
Set up environment variables

Create a .env file in the project root directory with the following content:
makefile
Copy code
GOOGLE_API_KEY=your-google-gemini-api-key
Run the app

bash
Copy code
streamlit run app.py
