import psycopg2
import sqlalchemy
from query import Query
import sys
import json
from typing import List, Dict

class Redash(object):

    def __init__(self):
        self.load_config()
        self.create_connection()

    def load_config(self):
        raw_config = ""
        with open("connection.json") as f:
            raw_config = f.read()
        try:
            self.config = json.loads(raw_config)
        except:
            sys.stderr.write("Syntax error in config.json")


    def create_connection(self):
        eng = sqlalchemy.create_engine("postgresql+psycopg2://%s:%s@%s/%s" % (\
            self.config['user'], self.config['password'], self.config['host'], self.config['dbname']
        ))
        self._con = eng.connect()

    def close_connection(self):
        self._con.close()

    def get_queries(self) -> List[Query]:
        sql: str = """select id, name, description, query, data_source_id from queries"""
        result = self._con.execute(sql)
        queries = [Query(id=r[0], name=r[1], description=r[2], query=r[3], data_source_id=r[4]) for r in result]
        return queries


    def update_quereis(self, queries: List[Query]):
        sql: str = """update queries set query = '%s' where id = %s"""
