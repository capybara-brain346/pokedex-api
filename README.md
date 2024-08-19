<h1 align="center" id="title">pokedex-api</h1>

<p align="center"><img src="https://socialify.git.ci/capybara-brain346/pokedex-api/image?description=1&amp;font=Raleway&amp;name=1&amp;owner=1&amp;pattern=Signal&amp;theme=Dark" alt="project-image"></p>

<p id="description">pokedex-api is a Restful api to retrieve pokemon data.</p>


  
  
<h2>🧐 Features</h2>

Here're some of the project's best features:

*   Get pokemon by name ability and type
*   Get pokemon by querying its height and weight

<h2>🛠️ Installation Steps:</h2>

<p>1. Clone the repository</p>

```
git clone https://github.com/capybara-brain346/pokedex-api.git
```

<p>2. If you are using anaconda follow the below steps</p>

```
conda create -p venv python=3.10 -y
```

```
For windows:- conda activate venv/
```

```
For Linux/Mac:- source activate venv/
```

<p>5. Install dependencies</p>

```
pip install -r requirements.txt
```

<p>6. Run the main file</p>

```
fastapi dev main.py
```

<p>7. Steps to setup database (assuming you have installed sqlite3 and it is on your path variable)</p>

```
sqlite3 pokemon.db
```

```
.mode csv
```

```
.import data/final_data/pokemon_combined.csv
```

  
  
<h2>💻 Built with</h2>

Technologies used in the project:

*   Python
*   FastAPI
*   Sqlite3
*   SQL

<h2>🛡️ License:</h2>

This project is licensed under the MIT License
