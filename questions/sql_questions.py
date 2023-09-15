import sqlite3

def get_test_ids_by_status(connection, status):
    try:
        print(connection)
        conn = sqlite3.connect(connection)
        cursor = conn.cursor()
        cursor.execute(f"SELECT DISTINCT test_id FROM status WHERE status = {status}")
        result = cursor.fetchall()

        return result
    finally:
        cursor.close()
        conn.close()

def get_min_max_date_for_test_id_and_status(connection,test_id,status):
    try:
        conn = sqlite3.connect(connection)
        cursor = conn.cursor()

        #Select min and max date where test_id is 1 and status is true
        cursor.execute(f"SELECT MIN(date) AS min_date, MAX(date) AS max_date FROM status WHERE test_id = {test_id} AND status = {status};")
        result = cursor.fetchall()

        return result 

    finally:
        cursor.close()
        conn.close()

# connection = './databases/mydatabase.sqlite'
# print(get_test_ids_by_status(connection, False))
# print(get_min_max_date_for_test_id_and_status(connection, 1, True))