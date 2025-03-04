import os
import uuid

from flask_test import main

import duckdb
import pytest


@pytest.fixture(scope="session")
def db_connection():
    """Provides an in-memory DuckDB connection for tests."""
    con = duckdb.connect(database="test_db.duckdb")
    con.sql(
        "CREATE TABLE user (uuid UUID PRIMARY KEY DEFAULT UUID(), name string, address string, email string, ssn string)"
    )
    con.sql(
        """CREATE TABLE loan_application (uuid UUID PRIMARY KEY DEFAULT UUID(), user_uuid
        FORIEGN KEY, loan_amount integer, status string, interest_rate integer, months integer, monthly_payment integer)
        """
    )

    yield con

    if os.path.exists("test_db.duckdb"):
        os.remove("test_db.duckdb")

    con.close()  # Cleanup after tests


@pytest.fixture
def client():
    with main.app.test_client() as client:
        yield client


@pytest.fixture
def create_fixture(db_connection):
    #con = duckdb.connect(database="test_db.duckdb")
    def blah(status):
        result = db_connection.execute(
            "INSERT INTO test (status) VALUES (?) RETURNING (uuid);",
            (status,),
        ).fetchone()
        return str(result[0])

    return blah
