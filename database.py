import sqlite3

def connect_db():
    conn = sqlite3.connect('university.db')
    return conn

def create_tables():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            major TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS courses (
            course_id INTEGER PRIMARY KEY AUTOINCREMENT,
            course_name TEXT NOT NULL,
            instructor TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS student_courses (
            student_id INTEGER,
            course_id INTEGER,
            FOREIGN KEY (student_id) REFERENCES students (id),
            FOREIGN KEY (course_id) REFERENCES courses (course_id),
            PRIMARY KEY (student_id, course_id)
        )
    ''')
    conn.commit()
    conn.close()

def add_student(name, age, major):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO students (name, age, major) VALUES (?, ?, ?)
    ''', (name, age, major))
    conn.commit()
    conn.close()

def add_course(course_name, instructor):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO courses (course_name, instructor) VALUES (?, ?)
    ''', (course_name, instructor))
    conn.commit()
    conn.close()

def enroll_student(student_id, course_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO student_courses (student_id, course_id) VALUES (?, ?)
    ''', (student_id, course_id))
    conn.commit()
    conn.close()

def list_students():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()
    conn.close()
    return students

def list_courses():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM courses')
    courses = cursor.fetchall()
    conn.close()
    return courses

def list_students_in_course(course_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT s.id, s.name FROM students s
        JOIN student_courses sc ON s.id = sc.student_id
        WHERE sc.course_id = ?
    ''', (course_id,))
    students = cursor.fetchall()
    conn.close()
    return students

create_tables()
