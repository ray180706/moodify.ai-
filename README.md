# Moodify.ai

## Description
Moodify.ai is an interactive web application powered by archaic artificial intelligence that analyzes user-input text to detect mood, then recommends a musical style and Spotify playlist matching the emotional state.

## Key Features
I) Natural language text analysis using TextBlob
II) Mood detection: happy, neutral, or sad
III) Personalized music recommendations with direct links to Spotify
IV) Simple and responsive interface built with Flask + HTML/CSS

## Installation

1. Clone this repository:
```
git clone https://github.com/your-username/moodify.git
cd moodify
```

2. Install dependencies:
```
pip install -r requirements.txt
```

3. Download language data for TextBlob:
```
python -m textblob.download_corpora
```

4. Launch the application:
```
flask run
```
or
```
python app.py
```

5. Open your browser at http://127.0.0.1:5000

## Project Structure
```
moodify/
├── app.py                 # Main Flask application
├── static/                # Static files
│   └── styles.css         # CSS stylesheet
├── templates/             # HTML templates
│   ├── layout.html        # Base template
│   └── index.html         # Home page
├── music_data.json        # Music recommendations database
├── requirements.txt       # Project dependencies
└── README.md              # Documentation
```

## Technologies Used
* Python (Flask, TextBlob)
* HTML/CSS
* JavaScript
* Bootstrap
* JSON for music database

## How It Works
1. **User Input**: Enter your thoughts, feelings, or a description of your day
2. **AI Analysis**: TextBlob processes the text to determine sentiment polarity
3. **Mood Detection**: The system categorizes your mood as happy, neutral, or sad
4. **Music Matching**: A curated playlist is selected based on your emotional state
5. **Spotify Integration**: One-click access to music that matches your mood

## Why Moodify.ai?
The goal was to create an accessible, useful, and original AI application that combines basic natural language processing and music recommendation in a fun context. This project applies key concepts from Python, Flask, and AI while exploring the connection between emotion and technology.

## Credits
Project created as part of Harvard's CS50x course.

## License
MIT
