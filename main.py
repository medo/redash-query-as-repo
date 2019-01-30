from redash import Redash
import local


def main():
    red = Redash()
    try:
        queries = red.get_queries()
        local.persist_queries(queries)
    finally:
        red.close_connection()


if __name__ == '__main__':
    main()
