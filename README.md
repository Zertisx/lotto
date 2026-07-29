# Lotto

A small lottery game, rebuilt in Python from an old C++ school project — used as a hands-on way to learn Python, SQL, and web development properly.

## About

This started life as a lottery simulator I wrote in C++ for school. I'm rebuilding it from scratch to learn the tools behind real web apps: clean Python, automated tests, a proper database, and eventually a web interface and deployment. It's a learning project, built step by step. Each stage is committed as I go, so the history shows the progression.

## Current status

- **Done:** console version of the game, with input validation, a prize lookup, and unit tests.
- **Done:** a SQLite storage layer — saving plays, looking up users, reading history and stats.
- **In progress:** turning it into a web app.
- **Planned:** deploying it to a live URL.

## Features

- Pick six numbers (1–49) or check them against a random draw.
- Prize calculated from how many numbers match, using the original C++ project's prize table.
- Input validation: rejects duplicates, out-of-range numbers, and non-numeric input instead of crashing.
- Plays are saved to a database, with each user's history and total winnings tracked.

## How to run it

You'll need Python 3 installed.

Play the console game:

```
python Lotto.py
```

Set up the database (creates `lotto.db`):

```
python database.py
```

Run the tests:

```
python -m unittest
```

## Project structure

- `Lotto.py` — the game logic (getting numbers, drawing, calculating the prize).
- `database.py` — the storage layer: creating tables, saving plays, reading history and stats.
- `test.py` — unit tests for the prize calculation.
