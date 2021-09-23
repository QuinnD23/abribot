from data.config import userc, passc, hostc

import psycopg2.extras


async def create_db():
    conn = psycopg2.connect(dbname="postgres", user=userc, password=passc, host=hostc)

    with conn:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            # -----
            try:
                cur.execute("CREATE TABLE forms18 (index serial primary key,"
                            "nick varchar default 0,"
                            "message varchar default 0,"
                            "photo_id varchar default 0);")
            except:
                pass
            # -----
            try:
                cur.execute("CREATE TABLE forms (index serial primary key,"
                            "nick varchar default 0,"
                            "message varchar default 0,"
                            "photo_id varchar default 0);")
            except:
                pass
            # -----
            try:
                cur.execute("CREATE TABLE users (user_id varchar primary key,"
                            "user_num serial,"
                            "user_name varchar default 0,"
                            "reg_date varchar default 0,"
                            "status varchar default 0,"
                            "status18 varchar default 0,"
                            "help varchar default 0);")
            except:
                pass
            # -----
            try:
                cur.execute("CREATE TABLE admin (user_id varchar primary key,"
                            "user_name varchar default 0,"
                            "table_name varchar default 0,"
                            "help varchar default 0,"
                            "count18 integer default 0,"
                            "count integer default 0);")
            except:
                pass

    conn.close()
