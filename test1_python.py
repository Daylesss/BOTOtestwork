import psycopg2 as pc2
import numpy as np
from config import host, user, password, db_name

def courses_for_employee(employee):

    try:
        # connection to DB
        connection =pc2.connect(
            host=host,
            user=user,
            password=password,
            database= db_name)
        # extraction data
        with connection.cursor() as cursor:
            cursor.execute(f'SELECT * FROM empl_post_grades WHERE empl_post_grades.employee =\'{employee}\'')
            employee_inf=cursor.fetchone()       # information about employee
        
            cursor.execute(f'SELECT course FROM c_course ORDER BY course')
            all_courses=tuple(np.concatenate(cursor.fetchall()))        # tuple of all available courses

            cursor.execute(f'SELECT * FROM c_post WHERE post=\'{employee_inf[1]}\'')
            required_competencies = cursor.fetchone()[1:]         #required competencies for employee's post

            cursor.execute(f'SELECT * FROM course_post WHERE post=\'{employee_inf[1]}\'')
            compulsory_courses = cursor.fetchone()[1:]        # compulsory courses for employee's post (tuple of boolean values)

            employee_competencies= employee_inf[2:]         # extracting employee's competences
            competencies_to_study=[]             # list of competencies that need to be improved
            for i in range(len(employee_competencies)): 
                if (employee_competencies[i] and required_competencies[i]):     # exclussion of 'None' values
                    if employee_competencies[i] < required_competencies[i]:     # comparison of competencies
                        competencies_to_study.append(i)
                elif employee_competencies==None and required_competencies!=None:
                    competencies_to_study.append(i)
                else:
                    continue # ignoring 'None' values
            

            cursor.execute(f'SELECT column_name FROM information_schema.columns WHERE table_schema =\'public\' AND table_name= \'c_course\'')
            competencies_names=tuple(np.concatenate(cursor.fetchall()))[1:]     #extracting names of competencies to use them in SQL queries.

            competence_building_courses=[]
            for competence in competencies_to_study:
                cursor.execute(f'SELECT course FROM c_course WHERE {competencies_names[competence]}= TRUE') # using names of competencies to extract courses we need
                competence_building_courses.extend(cursor.fetchone())

            required_courses=[all_courses[i] for i in range(len(all_courses)) if compulsory_courses[i]]   # difinition of list with requered curses (compulsory curses is tuple with boolean values)


    except Exception as ex:     # exception handling
        print( 'ERROR while working PostgreeSQL', ex)
    finally:
        if connection:
            connection.close()
            print('Connection closed')

        courses_for_employee = set(competence_building_courses + required_courses) # combining courses that an employee must take 
                                                                                   # (using the set to exclude duplicated valuse )
    return courses_for_employee
    

print(courses_for_employee('e1'))
