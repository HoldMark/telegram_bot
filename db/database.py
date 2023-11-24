import psycopg2
from config import DB_PORT, DB_PAS, DB_HOST, DB_USER

link = f"postgresql://{DB_USER}:{DB_PAS}@{DB_HOST}:{DB_PORT}"


def get_con():

    try:
        return psycopg2.connect(link)
    except Exception as e:
        print(f"DB problem: {e}")


connection = get_con()
