// App.js
import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [preferences, setPreferences] = useState({
    favorite_genres: [],
    preferred_years: []
  });
  const [recommendations, setRecommendations] = useState([]);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setPreferences({
      ...preferences,
      [name]: value.split(',').map(item => item.trim())
    });
  };

  const getRecommendations = async () => {
    try {
      const response = await axios.post('http://localhost:5000/recommend', preferences);
      setRecommendations(response.data);
    } catch (error) {
      console.error('Error fetching recommendations:', error);
    }
  };

  return (
    <div className="App">
      <h1>Movie Recommendation System</h1>
      <div>
        <label>
          Favorite Genres (comma-separated):
          <input
            type="text"
            name="favorite_genres"
            onChange={handleInputChange}
          />
        </label>
      </div>
      <div>
        <label>
          Preferred Years (comma-separated):
          <input
            type="text"
            name="preferred_years"
            onChange={handleInputChange}
          />
        </label>
      </div>
      <button onClick={getRecommendations}>Get Recommendations</button>
      <div>
        <h2>Recommendations:</h2>
        <ul>
          {recommendations.map((movie, index) => (
            <li key={index}>{movie.title} (Score: {movie.score.toFixed(2)})</li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default App;
