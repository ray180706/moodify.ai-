from flask import Flask, render_template, request, redirect, url_for, session, flash
from textblob import TextBlob
import json
import random
import os

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem
app.config["SECRET_KEY"] = "moodify_secret_key"

# Load music recommendations data
def load_music_data():
    try:
        with open('music_data.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return {
            "happy": [
                {
                    "genre": "Pop Upbeat",
                    "description": "De la musique pop énergique pour célébrer votre bonne humeur!",
                    "spotify_url": "https://open.spotify.com/playlist/37i9dQZF1DX0hWmn8d5pRe"
                },
                {
                    "genre": "Dance & Électro",
                    "description": "Des rythmes électroniques pour maintenir votre énergie positive!",
                    "spotify_url": "https://open.spotify.com/playlist/37i9dQZF1DX8tZsk68tuDw"
                }
            ],
            "neutral": [
                {
                    "genre": "Indie Chill",
                    "description": "De la musique indie relaxante qui vous accompagne sans vous distraire.",
                    "spotify_url": "https://open.spotify.com/playlist/37i9dQZF1DWWpVs4onVKxP"
                },
                {
                    "genre": "Jazz Ambiance",
                    "description": "Du jazz doux pour une ambiance détendue.",
                    "spotify_url": "https://open.spotify.com/playlist/37i9dQZF1DX4wta20PHgwo"
                }
            ],
            "sad": [
                {
                    "genre": "Ballades Émotionnelles",
                    "description": "Des ballades qui comprennent vos émotions et vous réconfortent.",
                    "spotify_url": "https://open.spotify.com/playlist/37i9dQZF1DWZqdNJKTRBst"
                },
                {
                    "genre": "Soul & R&B",
                    "description": "De la soul profonde pour exprimer et transformer vos émotions.",
                    "spotify_url": "https://open.spotify.com/playlist/37i9dQZF1DX2SK4ytI2KAZ"
                }
            ]
        }

def analyze_mood(text):
    """Analyze text and determine mood based on polarity score"""
    analysis = TextBlob(text)

    # Get polarity score (-1 to 1)
    polarity = analysis.sentiment.polarity

    # Determine mood based on polarity
    if polarity > 0.1:
        mood = "happy"
    elif polarity < -0.1:
        mood = "sad"
    else:
        mood = "neutral"

    return mood, polarity

def get_emoji_for_mood(mood):
    """Return appropriate emoji for the given mood"""
    if mood == "happy":
        return "😊"
    elif mood == "sad":
        return "😢"
    else:
        return "😐"

def get_recommendation(mood):
    """Get music recommendation based on mood"""
    music_data = load_music_data()
    print(f"Loaded music data: {music_data}") 
    if mood in music_data:
        # Choose a random recommendation for the mood
        recommendations = music_data[mood]
        recommendation = random.choice(recommendations)
        return recommendation

    # Fallback if mood not found
    return {"genre": "Variety", "description": "Music for all moments",
            "spotify_url": "https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M"}

# Routes
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get user text input
        user_text = request.form.get("user_text")

        if not user_text:
            flash("Please enter some text to analyze your mood", "warning")
            return redirect("/")

        # Analyze mood
        mood, score = analyze_mood(user_text)

        # Get music recommendation
        recommendation = get_recommendation(mood)

        return render_template(
            "index.html",
            user_text=user_text,
            mood=mood,
            emoji=get_emoji_for_mood(mood),
            score=score,
            recommendation=recommendation
        )

    # If GET request, just show the form
    return render_template("index.html")

@app.route("/reset", methods=["POST"])
def reset():
    """Reset the form"""
    return redirect("/")

# Custom filter
app.jinja_env.filters["format_score"] = lambda score: f"{abs(round(score * 100))}%"

if __name__ == "__main__":
    app.run(debug=True)
