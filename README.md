# Text_to_sql_genai
A Streamlit-based application that converts natural language queries into SQL commands using Google Gemini and retrieves results from a SQLite database.
Overview
The Text-to-SQL AI System enables users to interact with databases using natural language. By leveraging Google Gen AI (Gemini) and SQLite3, this project converts plain English queries into structured SQL commands, executes them, and returns the relevant data — all through an intuitive Streamlit web interface.
This project demonstrates the integration of Large Language Models (LLMs) with traditional databases, bridging the gap between human-friendly text and machine-readable queries.
Features
•	Text-to-SQL Conversion: Converts natural language queries into SQL commands using Google Gen AI.
•	SQLite Database Integration: Uses a lightweight and self-contained database for simplicity.
•	Web Interface: Built using Streamlit for easy interaction.
•	Automated Database Setup: Automatically generates and populates a local database (student.db).
•	Dynamic Query Execution: Retrieves and displays database results in real-time.
Project Structure
app.py                - Main Streamlit app file (UI + query logic)
sql.py                - Database setup and sample data insertion
student.db            - SQLite database file (auto-created)
requirements.txt      - List of required Python packages
DOCUMENTATION.md      - Project documentation
System Requirements
Ensure Python 3.8+ is installed and all dependencies are available.
Install dependencies:
•	pip install -r requirements.txt
Required packages:
streamlit
sqlite3
google-generativeai
How It Works
1.	Database Creation (sql.py): Uses sqlite3 to create a local database named student.db, defines tables, and inserts data.
2.	Model Integration (app.py): Loads Gemini API key, converts text to SQL queries, executes, and displays output.
3.	User Interface (Streamlit): Users enter natural language queries, view SQL translation, and see results instantly.
Example Usage
1. Setup the Database: python sql.py
2. Run the Application: streamlit run app.py
3. Use the Web App: Open the Streamlit URL and type natural queries like 'Show all students with marks above 85'.
API Key Configuration
Obtain a Google Gemini API key from Google AI Studio. Add it to app.py or set as an environment variable:
export GOOGLE_API_KEY='your_api_key_here'
Troubleshooting
Common Issues:
•	Issue: student.db not found — Solution: Run python sql.py first
•	Issue: API key error — Solution: Check your Gemini API key setup
•	Issue: Streamlit not running — Solution: Reinstall packages with pip install -r requirements.txt
Future Enhancements
•	Add support for multiple databases (PostgreSQL, MySQL).
•	Enhance query accuracy using prompt engineering.
•	Include authentication for secure access.
•	Improve UI with visualizations (charts, filters, etc.).
Author
Developed by: [Your Name]
Purpose: To explore how AI and NLP can simplify database interactions.
Acknowledgment: Built as a personal learning project in AI-driven data systems.
License
Released under the MIT License. You may use, modify, and distribute it with proper credit.
