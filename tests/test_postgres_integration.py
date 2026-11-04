
import os
import psycopg
import pytest


@pytest.mark.integration
def test_insert_order():
    database_url = os.environ["TEST_DATABASE_URL"]

    with psycopg.connect(database_url) as conn:
        with conn.cursor() as cursor:

            cursor.execute("""
                CREATE TEMP TABLE orders (
                    order_id INTEGER PRIMARY KEY,
                    amount NUMERIC NOT NULL
                )
            """)

            cursor.execute(
                "INSERT INTO orders VALUES (%s, %s)",
                (1, 100)
            )

            cursor.execute(
                "SELECT amount FROM orders WHERE order_id = %s",
                (1,)
            )

            result = cursor.fetchone()

            assert result[0] == 100

        conn.rollback()
