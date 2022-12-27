# importing Flask and other modules
from flask import Flask, request, render_template
import commons, constants
from flask_mysqldb import MySQL
from distutils.util import strtobool

# from sqlalchemy import text
# import dao

# Flask constructor
app = Flask(__name__)

app.config['MYSQL_HOST'] = constants.HOST
app.config['MYSQL_USER'] = constants.USERNAME
app.config['MYSQL_PASSWORD'] = constants.PASSWORD
app.config['MYSQL_DB'] = constants.DB_NAME
mysql = MySQL(app)


# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods=["GET", "POST"])
@app.route('/table', methods=["GET", "POST"])
def gfg():
    if request.method == "POST":
        post_name = request.form.get("Post_Name")
        print(post_name)
        age = request.form.get("Age")
        preferences = request.form.get("Preferences")
        min_degree = request.form.get("Min_Degree")
        max_degree = request.form.get("Max_Degree")
        specialisation = request.form.getlist("Specialisation")
        percentage = request.form.getlist("Percentage")
        designation = request.form.getlist("Designation")
        print(designation[0])
        #print(designation[1])
        #responsibilities = request.form.get("Responsibilities")
        total_experience = request.form.getlist("Total_Experience")
        skills = request.form.get("Skills")
        skills_exp = request.form.get("Experience_in_Skill")
        print(skills_exp[0])
        cursor = mysql.connection.cursor()
        # get constraints
        query = commons.get_applicant_ids_query_as_per_skill(skills)
        print(query)
        cursor.execute(query)
        result = cursor.fetchall()
        applicant_ids =[]
        for row in result:
            applicant_ids.append(row[0])
        exp_query = commons.filter_applicant_ids_as_per_skill_exp(skills_exp)
        print(exp_query)
        cursor.execute(exp_query)
        result = cursor.fetchall()
        exp_applicant_ids = []
        for row in result:
            exp_applicant_ids.append(row[0])
        common_applicant_ids = set(applicant_ids).intersection(set(exp_applicant_ids))
        query1 = commons.get_filter_query(post_name, age, preferences, min_degree, max_degree, specialisation,
                                         percentage, designation,  total_experience) #responsibilities,
        cursor.execute(query1)
        result = cursor.fetchall()
        selected_applicant_ids = []
        for row in result:
            selected_applicant_ids.append(row[0])
        common_applicant_ids = set(common_applicant_ids).intersection(set(selected_applicant_ids))
        print(common_applicant_ids)
        field_map = {1: 'Applicant_Id', 3: 'Post_Name', 4: 'Full_Name', 6: 'Age', 9: 'Preferences', 10: 'Qualification',
                     11: 'Degree',
                     13: 'Percentage', 14: 'Designation', 15: 'Qual_Experience',
                     16: 'Skills_with_exp(months)'}  # 43: 'Responsibilities',
        result_html_code = '<html>'
        if len(common_applicant_ids) == 0:
            print("No records found. Please reduce the constraints")
            result_html_code = result_html_code + '<h1 align=center>No records found. Please reduce the constraints</h1>'
        else:
            result_html_code = result_html_code + '<h1 align=center>Filtered Records</h1><table border=2><tr><th>S.No.</th>'
            for key in field_map:
                result_html_code = result_html_code + '<th>' + field_map[key] + '</th>'
            result_html_code = result_html_code + '</tr>'
            result_html_code = result_html_code + '<tr>'
            final_query = "Select * from candidates where "
            for applicant_id in common_applicant_ids:
                final_query = final_query + "ApplicantId = "+str(applicant_id)+" or "
            final_query = final_query[:final_query.rfind("or")] + ";"
            print(final_query)
            cursor.execute(final_query)
            result = cursor.fetchall()
            print(result)
            count = 0
            for row in result:
                count = count + 1
                result_html_code = result_html_code + '<td>' + str(count) + '</td>'
                for key in field_map.keys():
                    if key == 16:
                        skill_with_exp = str(row[key-1]).replace(" -",":")
                        result_html_code = result_html_code + '<td>' + skill_with_exp + '</td>'
                    else:
                        result_html_code = result_html_code + '<td>' + str(row[key - 1]) + '</td>'
                result_html_code = result_html_code + '</tr><tr>'
            ind = result_html_code.rfind('<tr>')
            result_html_code = result_html_code[:ind]
        result_html_code = result_html_code + '</table></html>'
        show_result(result_html_code)
        cursor.close()
        return render_template("table.html", tables=[result_html_code], titles=[''])
    return render_template("guestFacultyfilter.html")




@app.route('/table', methods=["GET", "POST"])
def show_result(result_html_code):
    return render_template("table.html", tables=[result_html_code], titles=[''])


if __name__ == '__main__':
    app.run()
