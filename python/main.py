from database.db_connection import get_connection


def main():
    conn = get_connection()

    if conn:
        print("Database is ready!")
        conn.close()
        print("Connection closed.")


if __name__ == "__main__":
    main()