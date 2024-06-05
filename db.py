from db_connect import connect_db


def test_conn():
    with connect_db() as conn:
        cur = conn.cursor()
        select_statement = """
        SELECT * FROM Test1;
        """
        cur.execute(select_statement)
        res = cur.fetchall()
        print(res)
    return res
