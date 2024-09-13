from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

app = Flask(__name__)

# Database setup
Base = declarative_base()

class Movie(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    rating = Column(Float)
    num_ratings = Column(Integer)
    last_updated = Column(DateTime, default=datetime.utcnow)

# IMDb Scraper
class IMDbScraper:
    def __init__(self):
        self.base_url = "https://www.imdb.com"

    def fetch_movie_data(self, movie_id):
        url = f"{self.base_url}/title/{movie_id}/"
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.find('h1').text.strip()
            rating = float(soup.find('span', class_='AggregateRatingButton__RatingScore').text.strip())
            num_ratings = int(soup.find('div', class_='AggregateRatingButton__TotalRatingAmount').text.strip().replace(',', ''))
            return {'title': title, 'rating': rating, 'num_ratings': num_ratings}
        return None

# Claude API Integration
class ClaudeAnalyzer:
    def __init__(self, api_key):
        self.api_url = "https://api.anthropic.com/v1/messages"
        self.headers = {"Content-Type": "application/json", "X-API-Key": api_key}

    def analyze_movie(self, movie_data):
        prompt = f"Analyze the following movie: {movie_data['title']}"
        payload = {
            "model": "claude-3.5-sonnet",
            "messages": [{"role": "user", "content": prompt}]
        }
        response = requests.post(self.api_url, headers=self.headers, json=payload)
        return json.loads(response.json()['content'])

# Recommendation Algorithm
class MovieRecommender:
    def __init__(self, db_session):
        self.db_session = db_session

    def get_recommendations(self, user_preferences):
        movies = self.db_session.query(Movie).all()
        scored_movies = []
        for movie in movies:
            score = self.calculate_score(movie, user_preferences)
            scored_movies.append((movie, score))
        return sorted(scored_movies, key=lambda x: x[1], reverse=True)[:10]

    def calculate_score(self, movie, user_preferences):
        # Simplified scoring function
        genre_score = 0.5  # Placeholder for genre matching
        popularity_score = (movie.rating / 10) * 0.3
        recency_score = 0.2  # Placeholder for recency calculation
        return genre_score + popularity_score + recency_score

# Flask routes
@app.route('/recommend', methods=['POST'])
def recommend_movies():
    user_preferences = request.json
    recommendations = recommender.get_recommendations(user_preferences)
    return jsonify([{'title': movie.title, 'score': score} for movie, score in recommendations])

@app.route('/update_movie/<string:movie_id>', methods=['POST'])
def update_movie(movie_id):
    movie_data = scraper.fetch_movie_data(movie_id)
    if movie_data:
        movie = Movie(**movie_data)
        db_session.add(movie)
        db_session.commit()
        return jsonify({"message": "Movie updated successfully"}), 200
    return jsonify({"error": "Failed to fetch movie data"}), 400

if __name__ == '__main__':
    # Database setup
    db_engine = create_engine(os.getenv('DATABASE_URL', 'postgresql://username:password@localhost/moviedb'))
    Base.metadata.create_all(db_engine)
    Session = sessionmaker(bind=db_engine)
    db_session = Session()

    # Initialize components
    scraper = IMDbScraper()
    claude_analyzer = ClaudeAnalyzer(os.getenv('CLAUDE_API_KEY'))
    recommender = MovieRecommender(db_session)

    # Run the Flask app
    app.run(debug=True)
