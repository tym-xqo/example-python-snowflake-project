# Snowflake Python connection example

Simple example of connecting to Snowflake and executing a query using Python and [`sqla-raw`](https://github.com/nerium-data/sqla-raw). 

Once dependencies are properly installed and `$DATABASE_URL` configured in the environment, `snowflake-sample-query.py` prints out the 10 most recently created users as a list of dictionaries with `id`, `created_at`, `email`, and `name` of each user.

For Jupyter notebook users, `snowflake-sample-notebook.ipynb` provides the same results as tabular display from a Pandas DataFrame.

## Installation

- `git clone` this repo and `cd` into working directory
- create virtual environment and install dependencies:

```
$ python -m venv .venv
$ source /.venv/bin/activate
$ python -m pip install -r requirements.txt
```

## Script usage

- copy `.env.example` to  `.env` and edit with appropriate username and password values
- source the `.env` file to set `$DATABASE_URL` in the environment: `set -a; source .env; set +a`
- run `python snowflake-sample-query.py` 🎉

## Jupyter notebook usage

- Follow installation above
- Ensure `$DATABASE_URL` is [set in the local environment](https://analyzingalpha.com/jupyter-notebook-environment-variables-tutorial): `set -a; source .env; set +a`
  - Alternatively, set the connection URL inline and call `db.engine()` as described in comments in the sample notebook itself
- open your Jupyter server from there

  ```
  $ ipython kernel install --user --name=.venv
  $ jupyter notebook
  ```
  - Or otherwise choose `example-python-snowflake-project/.venv` as your active Jupyter kernel
  - Or use whatever kernel is most convenient, and ensure `sqla-raw` and `snowflake-sqlalchemy` libraries are installed within your kernel
- Open `snowflake-sample-notebook.ipynb` in Jupyter
- Run all cells and see result of query in table at the end! 🎉
