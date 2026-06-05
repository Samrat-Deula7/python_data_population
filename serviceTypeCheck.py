import psycopg2

DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "databasename"
DB_USER = "postgres"
DB_PASS = "abcddddd"

try:

    def check(service_short_text):
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        cur = conn.cursor()

        value = service_short_text

        cur.execute("SELECT id FROM services WHERE short_text = %s;",(value,))
        idRow = cur.fetchone()[0]
        print(idRow)
        return idRow

    check("Exam prep for GRE")
except Exception as e:
    print("Error occurred while connecting to the database:", e)
