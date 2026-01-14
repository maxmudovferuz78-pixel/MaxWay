from django.db import connection
from contextlib import closing


def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row)) for row in cursor.fetchall()
    ]


def dictfetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))


def get_faculties():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * from dashboard_faculty""")
        faculties = dictfetchall(cursor)
        return faculties


def get_groups():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT dashboard_group.id, dashboard_group.name, dashboard_faculty.name as faculty
         from dashboard_group left join dashboard_faculty on dashboard_group.faculty_id = dashboard_faculty.id
         """)
        groups = dictfetchall(cursor)
        return groups


def get_kafedra():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * from dashboard_kafedra""")
        kafedra = dictfetchall(cursor)
        return kafedra


def get_subject():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * from dashboard_subject""")
        subjects = dictfetchall(cursor)
        return subjects


def get_teacher():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT dashboard_teacher.id, dashboard_teacher.first_name, dashboard_teacher.last_name,
        dashboard_teacher.age, dashboard_kafedra.name as dashboard_name, dashboard_subject.name as subject_name from 
        dashboard_teacher left join dashboard_kafedra on dashboard_teacher.kafedra_id = dashboard_kafedra.id
        left join dashboard_subject on dashboard_teacher.subject_id = dashboard_subject.id""")
        teachers = dictfetchall(cursor)
        return teachers


def get_student():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT dashboard_student.id, dashboard_student.first_name, dashboard_student.last_name, 
        dashboard_student.age, 
        dashboard_group.name as group_name, dashboard_student.image as image  from dashboard_student
        left join dashboard_group on dashboard_student.group_id = dashboard_group.id""")
        student = dictfetchall(cursor)
        return student
