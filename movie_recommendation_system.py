from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_restful import Api, Resource
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

app = Flask(__name__)
CORS(app)  # This allows all origins
api = Api(app)

# Database setup
Base = declarative_base()

class Movie(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    rating = Column(Float)
    num_ratings = Column(Integer)
    last_updated = Column(DateTime, default=datetime.utcnow)

# ... (IMDbScraper, ClaudeAnalyzer, and MovieRecommender classes remain the same)

class RecommendationResource(Resource):
    def post(self):
        user_preferences = request.json
        recommendations = recommender.get_recommendations(user_preferences)
        return jsonify([{'title': movie.title, 'score': score} for movie, score in recommendations])

class MovieResource(Resource):
    def post(self, movie_id):
        movie_data = scraper.fetch_movie_data(movie_id)
        if movie_data:
            movie = Movie(**movie_data)
            db_session.add(movie)
            db_session.commit()
            return {"message": "Movie updated successfully"}, 200
        return {"error": "Failed to fetch movie data"}, 400

    def get(self, movie_id):
        movie = db_session.query(Movie).filter_by(id=movie_id).first()
        if movie:
            return {
                "id": movie.id,
                "title": movie.title,
                "rating": movie.rating,
                "num_ratings": movie.num_ratings,
                "last_updated": movie.last_updated.isoformat()
            }
        return {"error": "Movie not found"}, 404

api.add_resource(RecommendationResource, '/recommend')
api.add_resource(MovieResource, '/movie/<string:movie_id>')

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
