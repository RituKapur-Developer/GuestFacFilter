import constants
import dao, commons, normalizeSkills


def fetch_and_display_existing_data(conn):
    filter_fields_1 = ['Post_Name','Age', 'Preferences', 'Degree' ] #PostName in DB
    filter_fields_4 = ['Specialisation', 'Percentage',  'Designation']
    filter_fields_3 = ['Total_Experience','Skills'] #QualifyingExperience in DB
    filter_fields_5 = ['Experience_in_Skill']

    html_code = commons.read_file_as_string(constants.STARTING_HTML_CODE)
    for field in filter_fields_1:
        if field == "Degree":
            html_code = html_code + '<th> Minimum Degree </th> <th> Highest Degree </th>'
        else:
            html_code = html_code + '<th>' + field + '</th>'
    html_code = html_code + '</tr><tr>'
    for field in filter_fields_1:
        field_values_list = dao.fetch_field_values(conn, field)
        html_code = html_code + commons.create_field_html_code(field, field_values_list)
    html_code = html_code + '</tr></table><table><tr>'
    #table 4
    for field in filter_fields_4:
        html_code = html_code + '<th>' + field + '</th>'
    html_code = html_code + '</tr><tr>'
    for field in filter_fields_4:
        field_values_list = dao.fetch_field_values(conn, field)
        html_code = html_code + commons.create_field_html_code(field, field_values_list)
    html_code = html_code + '</tr></table><table><tr>'
    #table 3 for space
    for field in filter_fields_3:
        html_code = html_code + '<th>' + field + '</th>'
    html_code = html_code + '</tr><tr>'
    for field in filter_fields_3:
        field_values_list = dao.fetch_field_values(conn, field)
        html_code = html_code + commons.create_field_html_code(field, field_values_list)

    for field in filter_fields_5:
        html_code = html_code + '<th> Experience_in_Skill </th>'
    html_code = html_code + '</tr><tr>'
    for field in filter_fields_5:
        html_code = html_code + commons.create_field_html_code(field, field_values_list)
    html_code = html_code + '</tr></table><input type=submit></div></form></body></html>'
    return html_code




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    conn = dao.est_connection()
    html_code = fetch_and_display_existing_data(conn)
    commons.write_code_to_file(constants.HTML_FILE, html_code)
    conn.close()
    #dao.create_one_time_tables() #run this first then flask and run once
    #dao.insert_once_skill_exp_range()
    #normalizeSkills.normalize_skill()


