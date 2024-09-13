# Movie Recommendation System

## Overview

This project is a Python-based movie recommendation system that combines data from IMDb with AI-powered analysis to provide personalized movie suggestions. It utilizes web scraping, machine learning techniques, and the Claude AI API to create a robust recommendation engine.

## Features

- Real-time data scraping from IMDb
- Integration with Claude AI for deep movie content analysis
- Personalized movie recommendations based on user preferences
- PostgreSQL database for efficient data storage
- Customizable user preferences and filters

## Components

1. IMDb Scraper: Fetches current movie data from IMDb
2. Claude Analyzer: Integrates with Claude AI for movie content analysis
3. Database Model: Stores movie information and user preferences
4. Recommendation Algorithm: Generates personalized movie suggestions

## Prerequisites

- Python 3.8+
- PostgreSQL
- Claude AI API key

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/movie-recommendation-system.git
   cd movie-recommendation-system
   ```

2. Install required packages:
   ```
   pip install -r requirements.txt
   ```

3. Set up the PostgreSQL database and update the connection string in `movie_recommendation_system.py`.

4. Set your Claude AI API key as an environment variable:
   ```
   export CLAUDE_API_KEY='your_api_key_here'
   ```

## Usage

Run the main script:

```
python movie_recommendation_system.py
```

## Configuration

Adjust the following parameters in `movie_recommendation_system.py`:

- `DB_CONNECTION_STRING`: Your PostgreSQL database connection string
- `CLAUDE_API_URL`: The endpoint for Claude AI API (if different from default)
- `NUM_RECOMMENDATIONS`: Number of movie recommendations to generate

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

This project is for educational purposes only. Ensure you comply with IMDb's terms of service when scraping their website.

## Future Enhancements

- Implement a web-based user interface
- Add support for TV shows and series
- Integrate with additional movie databases
- Implement collaborative filtering for improved recommendations

## Contact

For any queries, please open an issue on this repository.
