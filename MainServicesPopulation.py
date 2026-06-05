import psycopg2
from datetime import datetime



DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "databasename"
DB_USER = "postgres"
DB_PASS = "abcddddd"

try:
    data = [
        {"title": "Educational Counselling", "short_text": "Guidance for study destinations abroad", "icon": "GraduationCap"},

        {"title": "Preparation Classes - IELTS", "short_text": "Intensive training for IELTS exam success", "icon": "BookOpen"},
        {"title": "Preparation Classes - TOEFL", "short_text": "Focused preparation for TOEFL test takers", "icon": "BookOpen"},
        {"title": "Preparation Classes - GRE", "short_text": "Coaching for GRE analytical and verbal skills", "icon": "BookOpen"},
        {"title": "Preparation Classes - GMAT", "short_text": "Preparation for GMAT business school entry", "icon": "BookOpen"},
        {"title": "Preparation Classes - SAT", "short_text": "Exam readiness for SAT college admissions", "icon": "BookOpen"},
        {"title": "Preparation Classes - PTE", "short_text": "Practice sessions for PTE language test", "icon": "BookOpen"},
        {"title": "Preparation Classes - Medical Entrance", "short_text": "Coaching for medical entrance examinations", "icon": "BookOpen"},
        {"title": "Preparation Classes - Public Service", "short_text": "Preparation for public service commission exams", "icon": "BookOpen"},
        {"title": "Preparation Classes - Nursing", "short_text": "Exam prep for nursing entrance tests", "icon": "BookOpen"},
        {"title": "Preparation Classes - MBA", "short_text": "Preparation for MBA entrance examinations", "icon": "BookOpen"},
        {"title": "Preparation Classes - Bridge Course", "short_text": "Bridge course for academic transition support", "icon": "BookOpen"},
        {"title": "Preparation Classes - CMAT", "short_text": "Focused training for CMAT management test", "icon": "BookOpen"},
        {"title": "Preparation Classes - KUMAT", "short_text": "Preparation for KUMAT university entrance exam", "icon": "BookOpen"},
        {"title": "Preparation Classes - ACCA", "short_text": "Coaching for ACCA professional qualification", "icon": "BookOpen"},
        {"title": "Preparation Classes - GNK", "short_text": "Exam prep for GNK specialized tests", "icon": "BookOpen"},
        {"title": "Preparation Classes - Botany", "short_text": "Subject-specific coaching in Botany", "icon": "BookOpen"},
        {"title": "Preparation Classes - Physics", "short_text": "Subject-specific coaching in Physics", "icon": "BookOpen"},
        {"title": "Preparation Classes - Maths", "short_text": "Subject-specific coaching in Mathematics", "icon": "BookOpen"},
        {"title": "Preparation Classes - Standardized Tests", "short_text": "Training for general standardized exams", "icon": "BookOpen"},

        {"title": "Language Teaching - Japanese", "short_text": "Learn Japanese for study and work", "icon": "Languages"},
        {"title": "Language Teaching - English", "short_text": "Master English for global communication", "icon": "Languages"},
        {"title": "Language Teaching - German", "short_text": "Learn German for academic and career growth", "icon": "Languages"},
        {"title": "Language Teaching - Korean", "short_text": "Learn Korean for cultural and professional use", "icon": "Languages"},
        {"title": "Language Teaching - French", "short_text": "Learn French for international opportunities", "icon": "Languages"},
        {"title": "Language Teaching - Chinese", "short_text": "Learn Chinese for business and education", "icon": "Languages"},
        {"title": "Language Teaching - Spanish", "short_text": "Learn Spanish for global communication", "icon": "Languages"},
        {"title": "Language Teaching - Hebrew", "short_text": "Learn Hebrew for cultural and academic purposes", "icon": "Languages"},
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
