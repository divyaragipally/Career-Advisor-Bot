Career Advisor Bot (GenAI Powered)

An AI-powered Career Guidance Chatbot built using Python, Gemini API, and Streamlit.
The application provides personalized career suggestions, skill roadmaps, and interview preparation guidance through an interactive web interface.

🚀 Live Overview

This project demonstrates:

✅ Generative AI API integration (Gemini)

✅ Prompt Engineering

✅ Modular architecture (service layer + prompt manager)

✅ Logging implementation

✅ Streamlit-based Web UI

✅ Environment variable security using .env

🛠️ Tech Stack

Python

Streamlit (Web UI)

Google Gemini API

dotenv (Environment variable management)

Custom logging module

📂 Project Structure
Career-Advisor-Bot/
│
├── app.py                # Streamlit web application
├── gemini_service.py     # Handles Gemini API requests
├── prompt_manager.py     # Manages structured prompts
├── logger.py             # Logging configuration
├── requirements.txt      # Dependencies
├── .env                  # API key (not uploaded)
└── README.md
⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/divyaragipally/Career-Advisor-Bot.git
cd Career-Advisor-Bot
2️⃣ Create Virtual Environment (Recommended)
python -m venv venv

Activate it:

Windows

venv\Scripts\activate

Mac/Linux

source venv/bin/activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Configure Environment Variables

Create a .env file in the root directory and add:

API_KEY=your_gemini_api_key_here

⚠️ Do NOT upload .env to GitHub.

▶️ Run the Streamlit App
streamlit run app.py

The application will open in your browser at:

http://localhost:8501
💬 Example Use Cases

Suggest career paths for a CSE student

Generate a roadmap for becoming a Data Analyst

Interview preparation guidance

Skill recommendations for AI/ML roles

🧠 How It Works

User enters a career-related question in Streamlit UI

prompt_manager.py structures the prompt

gemini_service.py sends request to Gemini API

Response is displayed in the web interface

Logs are stored using logger.py

🔒 Security

API keys are stored securely using environment variables

.env file is excluded from version control
