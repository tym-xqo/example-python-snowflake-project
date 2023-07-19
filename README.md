# Snowflake Python connection example

Simple example of connecting to Snowflake and executing a query using Python and [`sqla-raw`](https://github.com/nerium-data/sqla-raw). Once dependencies are properly installed and `$DATABASE_URL` configured in the environment, `snowflake-sample-query.py` prints out the 10 most recently created users as a list of dictionaries with `id`, `created_at`, `email`, and `name` of each user.

## Installation/Usage

- `git clone` this repo and `cd` into working directory
- create virtual environment and install dependencies:

```
$ python -m venv .venv
$ source /.venv/bin/activate
$ python -m pip install -r requirements.txt
```

- copy `.env.example` to  `.env`
- source the `.env` file: `set -a; source .env; set +a`

- run `python snowflake-sample-query.py`
