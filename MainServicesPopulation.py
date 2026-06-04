import psycopg2
from datetime import datetime



DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "databasename"
DB_USER = "postgres"
DB_PASS = "abcddddd"

try:
    data = [
        {"title": "Educational Counselling", "short_text": "Guides students to right study destinations abroad", "icon": "GraduationCap"},
        {"title": "Preparation Classes", "short_text": "Exam prep for IELTS", "icon": "BookOpen"},
        {"title": "Preparation Classes", "short_text": "Exam prep for TOEFL", "icon": "BookOpen"},
        {"title": "Preparation Classes", "short_text": "Exam prep for GRE", "icon": "BookOpen"},
        {"title": "Preparation Classes", "short_text": "Exam prep for GMAT", "icon": "BookOpen"},
        {"title": "Preparation Classes", "short_text": "Exam prep for SAT", "icon": "BookOpen"},
        {"title": "Preparation Classes", "short_text": "Exam prep for PTE", "icon": "BookOpen"},
        {"title": "Preparation Classes", "short_text": "Exam prep for MEDICAL ENTRANCE", "icon": "BookOpen"},
        {"title": "Preparation Classes", "short_text": "Exam prep for PUBLIC SERVICE", "icon": "BookOpen"},
        {"title": "Preparation Classes", "short_text": "Exam prep for NURSING", "icon": "BookOpen"},
        {"title": "Preparation Classes", "short_text": "Exam prep for MBA", "icon": "BookOpen"},
        {"title": "Preparation Classes", "short_text": "Exam prep for BRIDGE COURSE", "icon": "BookOpen"},
        {"title": "Preparation Classes", "short_text": "Exam prep for CMAT", "icon": "BookOpen"},
        {"title": "Preparation Classes", "short_text": "Exam prep for KUMAT", "icon": "BookOpen"},
        {"title": "Preparation Classes", "short_text": "Exam prep for ACCA", "icon": "BookOpen"},
        {"title": "Preparation Classes", "short_text": "Exam prep for GNK", "icon": "BookOpen"},
        {"title": "Preparation Classes", "short_text": "Exam prep for BOTANY", "icon": "BookOpen"},
        {"title": "Preparation Classes", "short_text": "Exam prep for PHYSICS", "icon": "BookOpen"},
        {"title": "Preparation Classes", "short_text": "Exam prep for MATHS", "icon": "BookOpen"},
        {"title": "Preparation Classes", "short_text": "Trains students for standardized tests and exams", "icon": "BookOpen"},
        {"title":"Japanese Language Teaching","short_text":"Teaches Japanese language","icon":"Languages"},
        {"title":"English Language Teaching","short_text":"Teaches English language","icon":"Languages"},
        {"title":"German Language Teaching","short_text":"Teaches German language","icon":"Languages"},
        {"title":"Korean Language Teaching","short_text":"Teaches Korean language","icon":"Languages"},
        {"title":"French Language Teaching","short_text":"Teaches French language","icon":"Languages"},
        {"title":"Chinese Language Teaching","short_text":"Teaches Chinese language","icon":"Languages"},
        {"title":"Spanish Language Teaching","short_text":"Teaches Spanish language","icon":"Languages"},
        {"title":"Hebrew Language Teaching","short_text":"Teaches Hebrew language","icon":"Languages"},
    ]

    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )
    cur = conn.cursor()

    insert_query = """
    INSERT INTO services (title, short_text, icon, created_at, updated_at)
    VALUES (%s, %s, %s, %s, %s)
    RETURNING id;
    """

    for item in data:
        values = (
            item["title"],
            item["short_text"],
            item["icon"],
            datetime.now(),
            datetime.now()
        )
        cur.execute(insert_query, values)
        new_id = cur.fetchone()[0]
        print(f"Inserted row with id: {new_id}")

    # Commit once after all inserts
    conn.commit()

    # Verify insertion
    cur.execute("SELECT * FROM services;")
    rows = cur.fetchall()
    for row in rows:
        print(row)

        cur.close()
        conn.close()

except Exception as e:
    print("Error occurred while connecting to the database:", e)
