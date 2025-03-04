import duckdb
import uuid

CON = duckdb.connect(database="test_db.duckdb")

def create_user(name, address, email, phone, ssn):
    result = CON.execute(
        "INSERT INTO user (name, address, email, phone, ssn) VALUES (?, ?, ?, ?, ?);", (
            name, address, email, phone, ssn)
    ).fetchone()

    return result
