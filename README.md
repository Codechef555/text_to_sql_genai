🧠 Text-to-SQL AI System
📘 Overview

The Text-to-SQL AI System enables users to interact with databases using natural language. By leveraging Google Gen AI (Gemini) and SQLite3, this project converts plain English queries into structured SQL commands, executes them, and returns the relevant data — all through an intuitive Streamlit web interface.

This project demonstrates the integration of Large Language Models (LLMs) with traditional databases, bridging the gap between human-friendly text and machine-readable queries.

🚀 Features

🗣 Text-to-SQL Conversion: Converts natural language queries into SQL commands using Google Gen AI.

🗃 SQLite Database Integration: Uses a lightweight and self-contained database for simplicity.

💻 Web Interface: Built using Streamlit for easy interaction.

⚙️ Automated Database Setup: Automatically generates and populates a local database (student.db).

🔍 Dynamic Query Execution: Retrieves and displays database results in real-time.

📂 text-to-sql/
│
├── app.py                # Main Streamlit app file (UI + query logic)
├── sql.py                # Database setup and sample data insertion
├── student.db            # SQLite database file (auto-created)
├── requirements.txt      # List of required Python packages
└── DOCUMENTATION.md      # Project documentation


🧩 System Requirements
🔧 Dependencies

Make sure you have Python 3.8+ installed, then install all required libraries:
pip install -r requirements.txt

📦 Required Packages
Your requirements.txt should include (example):
streamlit
sqlite3
google-generativeai

⚙️ How It Works

Database Creation (sql.py):

Uses sqlite3 to create a local database named student.db.

Defines sample tables and inserts sample records.

Validates data by running a basic SQL query.

Model Integration (app.py):

Loads the Google Gemini API key.

Uses Gemini to interpret natural text and generate SQL queries.

Executes the query on the local SQLite database.

Displays the query results on a Streamlit interface.

User Interface (Streamlit):

Allows users to enter plain English questions (e.g., “Show all students with marks above 80”).

Displays the translated SQL query and the result table.

Instructions to run:
pip install -r requirements.txt -> To install the necessary libraries

python sql.py -> To setup the local database and load the information

python app.py --> To run the main source file 

streamlit run app.py --> To run the main web interface of the application. 


💡 Future Enhancements

Add support for multiple databases (PostgreSQL, MySQL).

Enhance query accuracy using fine-tuned prompt engineering.

Include authentication for secure access.

Improve UI with better data visualization (charts, filters, etc.).


🧑‍💻 Author

Developed by: Md.Karaamathullah sheriff
Purpose: To explore and demonstrate how AI and natural language processing can simplify database interactions.
Acknowledgment: This project was built as part of a personal learning journey into AI-driven data systems.

📜 License

This project is released under the MIT License.
You are free to use, modify, and distribute it, provided proper credit is given.
