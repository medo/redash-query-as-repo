import query
import string
import re
import os
from typing import List

def format_filename(s):
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    filename = ''.join(c for c in s if c in valid_chars)
    filename = filename.replace(' ','_') # I don't like spaces in filenames.
    return filename

def persist_queries(queries: List[query.Query]):
    for q in queries:
        file_name = q.name
        dir_name = re.search('\[(.*)\]', file_name)
        print(file_name)
        path_to_file = query.QUERY_DIR
        if dir_name:
            dir_name = dir_name.group(1).strip().lower()
            path_to_file = "%s/%s" % (path_to_file, dir_name)
            if not os.path.exists(path_to_file):
                os.mkdir(path_to_file)
        f = open("%s/%s.sql" % (path_to_file, format_filename(q.name)), 'w')
        f.write(query.query_to_str(q))
        f.close()
