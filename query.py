from dataclasses import dataclass

QUERY_DIR = "queries"

@dataclass
class Query:
    id: int
    query: str
    name: str
    description: str
    data_source_id: int


QUERY_TEMPLATE = """/*
ID: {id}
Name: {name}
Data source: {data_source_id}
Description: {description}
*/

{query}
"""

def query_to_str(query: Query) -> str:
    return QUERY_TEMPLATE.format(**query.__dict__)
