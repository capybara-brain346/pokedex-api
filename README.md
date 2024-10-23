<img src="https://github.com/user-attachments/assets/de7f2289-5809-4126-8432-5fcd1e625c5a" alt="Features Screenshot" width="full">

# Pokedex-API

This project is a RESTful API developed with FastAPI that provides detailed data on over 1,000 Pokémon. It allows users to query various Pokémon attributes such as name, species, abilities, type, and combat stats. The API integrates an SQLite database to store and manage Pokémon data scraped from external sources.

## Features
- **Comprehensive Pokémon Data:**
  - Data scraped from [pokemondb.net](https://pokemondb.net) for 1,015 Pokémon.
  - Data stored in CSV files and imported into an SQLite database for persistence.
  - Uploaded to Kaggle as an open-source dataset, receiving over 1,100 downloads and 5,000 views.

- **API Endpoints:**
  - Query Pokémon by different attributes such as name, abilities, type, size, species, growth rate, catch rate, friendship, and experience.

- **Automated Workflows:**
  - GitHub Actions configured for Continuous Integration (CI) to automate linting with Pylint and building the application inside a container.

## Technology Stack

- **Python:** Core programming language for developing the API and scraping Pokémon data.
- **FastAPI:** Framework used to build the RESTful API server.
- **SQLite:** Embedded database for storing Pokémon data.
- **Scrapy:** For scraping Pokémon data from external sources.
- **GitHub Actions:** Automates linting and container builds.

## Dataset

The dataset contains information about:
- Pokémon Name
- Species
- Type(s)
- Abilities
- Base Stats (HP, Attack, Defense, etc.)
- Size (Height, Weight)
- Growth Rate
- Catch Rate
- Base Friendship
- Base Experience

The dataset is publicly available on [Kaggle](https://www.kaggle.com/datasets/crinklybrain2003/pokmon-base-stats-dataset).

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/capybara-brain346/pokedex-api.git
   cd pokedex-api
   ```

2. **Set up a virtual environment (optional but recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the FastAPI server:**
   ```bash
   uvicorn app.main:app --reload
   ```

5. **Access the API:**
   - Once the server is running, navigate to `http://127.0.0.1:8000` to access the API.
   - Use the interactive API documentation provided by FastAPI at `http://127.0.0.1:8000/docs`.

## API Endpoints

### Pokémon Attributes

- **GET /pokemons/name/{name}:**  
  Fetch Pokémon data by name.
  
- **GET /pokemons/abilities/{abilities}:**  
  Query Pokémon by their abilities.

- **GET /pokemons/type/{pokemon_type}:**  
  Query Pokémon by their type (e.g., Water, Fire, etc.).

- **GET /pokemons/size:**  
  Query Pokémon by size (height and/or weight). Pass values like `>2.5` for height or `<=50` for weight.

- **GET /pokemons/species/{pokemon_species}:**  
  Query Pokémon by species.

- **GET /pokemons/growth_rate/{pokemon_growth_rate}:**  
  Query Pokémon by growth rate (e.g., Fast, Slow).

- **GET /pokemons/catch_rate:**  
  Query Pokémon by catch rate. Pass values like `>=45`.

- **GET /pokemons/base_friendship:**  
  Query Pokémon by base friendship. Pass values like `>=50`.

- **GET /pokemons/base_experience:**  
  Query Pokémon by base experience. Pass values like `>=100`.

## CI/CD with GitHub Actions

The project utilizes GitHub Actions for automating:
- **Linting:** Pylint is used to maintain code quality.
- **Containerization:** GitHub Actions automatically builds the app inside a container for deployment.

## Future Improvements

- Add more nuanced filtering options (e.g., multi-type filtering, ability combinations).
- Implement caching for frequently queried data to improve response time.
- Add support for more detailed Pokémon statistics and movesets.

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or find issues, feel free to open a pull request or submit an issue.
