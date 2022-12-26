import mysql.connector
import constants


def est_connection():
    conn = mysql.connector.connect(
        host=constants.HOST,
        user=constants.USERNAME,
        password=constants.PASSWORD
    )
    return conn


def create_one_time_tables():
    conn = est_connection()
    cursor = conn.cursor()
    query0 = "create table recruit.skillExp(skillId Int, skillName varchar(100), minExp Double, maxExp Double)"
    cursor.execute(query0)
    conn.commit()
    '''
    query1 = 'create table recruit.candidate_skill_exp(recordID Int, ApplicantID Int, Skill Varchar(100), Experience Double);'
    cursor.execute(query1)
    conn.commit()
    print("Skill Table Created. Now inserting records")
    conn.commit()
    '''
    conn.close()
    return

def insert_once_skill_exp_range():
    skill_exp = {}
    conn = est_connection()
    cursor = conn.cursor()
    query = "select distinct skill, experience from recruit.candidate_skill_exp;"
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        skill_exp[row[0]] = []
    for row in results:
        for key in skill_exp.keys():
            if row[0] == key:
                skill_exp[key].append(row[1])
    print("skill exp map completed")
    query = "insert into recruit.skillExp values(%s, %s, %s, %s);"

    count = 0
    for key in skill_exp.keys():
        count = count + 1
        exp_list = skill_exp[key]
        record = (count, key, min(exp_list), max(exp_list))
        try:
            cursor.execute(query, record)
            conn.commit()
        except mysql.connector.Error as error:
            print("Failed to insert into MySQL table {}".format(error))
    conn.close()
    return


def fetch_field_values(conn, field):
    cursor = conn.cursor()
    print(field)
    if field == 'Skills':
        query = 'select distinct Skill from recruit.candidate_skill_exp;'
    elif field == 'Experience_In_Skill':
        query = 'select distinct Skill from recruit.candidate_skill_exp;'
    else:
        if field == 'Post_Name':
            field = 'PostName'
        if field == 'Total_Experience':
            field = 'QualifyingExperience'
        query = 'select distinct ' + field + ' from recruit.candidates'
    cursor.execute(query)
    results = cursor.fetchall()  # Get query response and store in variable
    field_value_list = [i for sub in results for i in sub]  # Convert to list from tuple
    return field_value_list


def fetch_selected_records(category, age):
    conn = est_connection()
    cursor = conn.cursor()
    query = 'select * from recruit.candidates where Category=' + category + ' and Age=' + age
    cursor.execute(query)
    results = cursor.fetchall()  # Get query response and store in variable
    print(results)
    conn.close()
    return results




def insert_skill_exp_range(skill_exp_range):
    conn = est_connection()
    ind = skill_exp_range.find("-")
    min_exp = int(skill_exp_range[:ind])
    max_exp = int(skill_exp_range[ind+1:])
    query = "update recruit.skillExp set maxExp = %s, minExp = %s where skillId = 1"
    record = (max_exp, min_exp)
    try:
        cursor.execute(query, record)
        conn.commit()
        #print("inserted data")
    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))
    finally:
        if conn.is_connected():
            conn.close()
    return

def get_applicant_skill_map():
    skill_map = {}
    conn = est_connection()
    cursor = conn.cursor()
    query = "select ApplicantID, Skills from recruit.candidates;"
    cursor.execute(query)
    results = cursor.fetchall()  # Get query response and store in variable
    for row in results:
        skill_map[row[0]] = row[1]
    conn.close()
    return skill_map

def insert_norm_cand_skill_exp(cand_skill_map):
    conn = est_connection()
    cursor = conn.cursor()
    query = 'insert into recruit.candidate_skill_exp values(%s, %s, %s, %s);'
    count = 0
    for key in cand_skill_map.keys():
        count = count + 1
        app_id = int(key)
        skill_exp_map = cand_skill_map[key]
        for skill in skill_exp_map.keys():
            exp = skill_exp_map[skill]
            record = (count, app_id, skill, exp)
            try:
                cursor.execute(query, record)
                conn.commit()
                # print("inserted data")
            except mysql.connector.Error as error:
                print("Failed to insert into MySQL table {}".format(error))
    conn.close()
    return


