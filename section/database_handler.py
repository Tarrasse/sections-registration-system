from django.db import connection


def insert_user(name, password, sid=None):
    with connection.cursor() as cursor:
        cursor.execute('''
        INSERT INTO section_client ('sid', 'name', 'password') VALUES ('{}', '{}', '{}')'''
                       .format(sid, name, password))


def query_user(sid):
    with connection.cursor() as cursor:
        cursor.execute('''
        SELECT * FROM section_client WHERE sid = {}'''.format(sid))
        row = cursor.fetchone()
        return row


def register(section_id, student_id):
    with connection.cursor() as cursor:
        cursor.execute('''
        SELECT count(*)
        FROM section_reg
        WHERE sid={} AND section_id_id={}
        '''.format(student_id, section_id))

        rows = cursor.fetchall()
        if len(rows) == 0:
            regs = query_regs(section_id)
            if regs <= 25:
                cursor.execute('''
                INSERT INTO section_reg ('sid_id', 'section_id_id')
                VALUES ({}, {})
                '''.format(str(student_id),
                           str(section_id)))
                return True
            else:
                return False
        else:
            return True


def un_register(sid, section_id):
    with connection.cursor() as cursor:
        cursor.execute('''
             DELETE FROM section_reg
             WHERE section_reg.sid_id ={} AND section_reg.section_id_id ={}
             '''.format(
            str(sid), str(section_id)))


def query_student_sections(student_id):
    with connection.cursor() as cursor:
        cursor.execute('''
        SELECT section_section.id, date, course_id FROM section_section
        INNER JOIN section_reg
        ON section_section.id = section_Reg.section_id_id
        WHERE section_reg.sid_id = {} '''.format(student_id))
        rows = cursor.fetchall()
        names_set = set()
        course_list = []
        for row in rows:
            name = get_table_name(row[2])
            if name not in names_set:
                names_set.add(name)
            course_list.append((row[0], row[1], name))
        return course_list, names_set


def query_regs(section_id):
    with connection.cursor() as cursor:
        cursor.execute('''
        SELECT count(*)
        FROM section_reg
        WHERE section_id_id={}
        '''.format(section_id))
        rows = cursor.fetchall()
        return len(rows)


def query_sections():
    with connection.cursor() as cursor:
        cursor.execute('''
           SELECT section_section.id ,date, course_id FROM section_section
           INNER JOIN section_reg
           ON section_section.id = section_Reg.section_id_id
           ''')
        rows = cursor.fetchall()
        names_set = set()
        l = []
        for row in rows:
            name = get_table_name(row[2])
            if name not in names_set:
                names_set.add(name)
            l.append((row[0], row[1], name))
        return l, names_set


def get_table_name(course_id):
    with connection.cursor() as cursor:
        cursor.execute('''
        SELECT name FROM section_course WHERE id = {}'''.format(course_id))
        row = cursor.fetchone()
        return row[0]


def test():
    with connection.cursor() as cursor:
        cursor.execute('''
             SELECT * FROM section_reg
             WHERE section_reg.id = 5000
             ''')
        row = cursor.fetchall()
        print type(row)
