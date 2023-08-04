# warbler

A Social media app (twitter-clone) made in Flask.

## Getting Started

```bash

# Clone the repo then
cd warbler
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Create the database
# Make sure you have postgresql installed
createdb warbler
python seed.py # To seed the database

# Run the app
flask run
```

if all goes well you should see something like this:

```bash
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

if you get any errors, make sure you have all the dependencies installed
with the right versions.

ps: I'm using python 3.10 in this run. if any errors open an issue.
