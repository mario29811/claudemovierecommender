# Movie Recommendation System

## Overview

This project is a full-stack application for a movie recommendation system that combines a Flask-based REST API backend with a React frontend. It utilizes IMDb data scraping, Claude AI for analysis, and a custom recommendation algorithm to provide personalized movie suggestions.

## Features

- Flask-based REST API backend
- React frontend for user interaction
- Real-time data scraping from IMDb
- Integration with Claude AI for deep movie content analysis
- Personalized movie recommendations based on user preferences
- PostgreSQL database for efficient data storage

## Components

1. Backend:
   - Flask REST API
   - IMDb Scraper
   - Claude Analyzer
   - SQLAlchemy Database Model
   - Recommendation Algorithm

2. Frontend:
   - React-based user interface

## Prerequisites

- Python 3.8+
- Node.js and npm
- PostgreSQL
- Claude AI API key

## Installation

### Backend

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/movie-recommendation-system.git
   cd movie-recommendation-system/backend
   ```

2. Install required packages:
   ```
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   ```
   export DATABASE_URL='postgresql://username:password@localhost/moviedb'
   export CLAUDE_API_KEY='your_api_key_here'
   ```

### Frontend

1. Navigate to the frontend directory:
   ```
   cd ../frontend
   ```

2. Install dependencies:
   ```
   npm install
   ```

## Usage

1. Start the backend server:
   ```
   cd backend
   python app.py
   ```

2. In a new terminal, start the frontend development server:
   ```
   cd frontend
   npm start
   ```

3. Open your browser and navigate to `http://localhost:3000`

## API Endpoints

- `POST /recommend`: Get movie recommendations
- `POST /movie/<imdb_movie_id>`: Update movie data
- `GET /movie/<imdb_movie_id>`: Get movie details

## Configuration

Adjust the following environment variables:

- `DATABASE_URL`: Your PostgreSQL database connection string
- `CLAUDE_API_KEY`: Your Claude AI API key

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

This project is for educational purposes only. Ensure you comply with IMDb's terms of service when scraping their website.

## Future Enhancements

- Implement user authentication
- Add support for TV shows and series
- Integrate with additional movie databases
- Implement collaborative filtering
- Enhance the frontend with more interactive features

## Contact

For any queries, please open an issue on this repository.
