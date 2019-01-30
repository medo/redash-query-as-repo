# Redash Queries

This repo helps you download your redash (https://redash.io) queries so that you can manage and version control your quereis. The queries are structure in directory strcture
based on the query name as follows "[Directory] query name"

The suggest workflow:

- Pull branch master from your clone of this repo
- Write your query on redash then save it
- Run `python [main.py](http://main.py)` to sync the queries locally
- Commit only the queries you changed, and create a PR.


## Setup

```
pip install -r requirements.txt
```

## Pull redash queries

```
python main.py
```
