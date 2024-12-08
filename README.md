Project Overview
The News Word Cloud Generator is a web application that allows users to fetch news articles based on a specific keyword, generate a CSV file with the article details, and create a word cloud image from the article descriptions. It combines a Flask backend for processing and a React frontend for user interaction.

Features
•	Fetch news articles using the NewsAPI.
•	Generate a CSV file with the title and description of the articles.
•	Create a visually appealing word cloud from the article descriptions.
•	User-friendly React interface for interacting with the application.

Technologies Used
•	Backend: Python, Flask, Flask-CORS
•	Frontend: React, Vite
•	Additional Libraries:
- requests for API requests
- wordcloud for generating the word cloud
- matplotlib for saving the word cloud as an image
- dotenv for managing environment variables
•	API: NewsAPI

Setup Instructions
1. Clone the Repository
$ git clone https://github.com/your-repository-url.git
$ cd my-news-app

2. Backend Setup (Flask)
•	Navigate to the server directory: $ cd server
•	Create a Python virtual environment: $ python3 -m venv venv
•	Activate the virtual environment:
- macOS/Linux: $ source venv/bin/activate
- Windows:Bash venv\Scripts\activate
•	Install the required Python libraries: $ pip install Flask Flask-CORS requests wordcloud matplotlib python-dotenv
•	Create a .env file to store your NewsAPI key: $ touch .env
•	Add your NewsAPI key to the .env file: $ NEWS_API_KEY=your_api_key_here
•	Start the Flask server:$ python server.py
- The server will run at http://127.0.0.1:5000.

3. Frontend Setup (React)
1.	Open a new terminal and navigate to the root project directory: 
$ cd my-news-app
2.	Install the frontend dependencies: $ npm install
3.	Start the React development server:$ npm run dev
- The frontend will run at http://localhost:5173.

4. Test the Application
1.	Open the React app in your browser:
Arduino http://localhost:5173
2.	Fill in the following fields in the form:
Query: The keyword to search for (e.g., "technology").
Number of Articles: The number of articles to fetch (e.g., 10).
Filename: The name of the CSV file and word cloud image (e.g., "tech_news").
3.	Click Generate Word Cloud to:
- Fetch articles from NewsAPI.
- Save the articles in a CSV file.
- Generate a word cloud image.
4.	Verify:
- The CSV file and word cloud image are created in the server directory.
- The word cloud is displayed in the React app.

Project File Structure
The application uses the NewsAPI to fetch articles. Below is a brief summary of the API used:
•	Endpoint: https://newsapi.org/v2/everything
•	Parameters:
- q: The search keyword.
- pageSize: The number of articles per request (max 100).
- apiKey: Your API key.

Example URL: https://newsapi.org/v2/everything?q=technology&pageSize=10&apiKey=your_api_key
1.	NewsAPI Usage Limits:
Free-tier accounts are limited to 100 requests per day.
2.	Word Cloud Quality:
The quality of the word cloud depends on the descriptions provided in the fetched articles.
3.	Local File Handling:
The CSV file and word cloud image are saved locally on the server.

Future Enhancements
•	Add filters for date ranges, sources, or language.
•	Allow users to download the CSV file and word cloud image directly from the React app.
•	Deploy the application to a cloud platform for public access.

![image](https://github.com/user-attachments/assets/0cd47f0e-5596-4ad3-851d-e217b57205cd)
