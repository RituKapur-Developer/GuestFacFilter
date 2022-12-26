import dao, math

max_skills_exp = 0


def split_string_with_commas_and_remove_whitespace(my_str):
    return [x.strip() for x in my_str.split(',')]


def get_unique_values_list(field_val_list):
    return list(set(field_val_list))


def remove_none_values_from_list(field_val_list):
    return [i for i in field_val_list if i is not None]


def get_unique_preference_list(preference_options):
    preference_list = []
    for item in preference_options:
        preference_list.append(split_string_with_commas_and_remove_whitespace(item))
    return get_unique_values_list(combine_list_of_lists(preference_list))


def combine_list_of_lists(list_of_lists):
    return [elem for sublist in list_of_lists for elem in sublist]


def get_skill_exp_range(skill_exp_list):
    global max_skills_exp
    max_skills_exp = max(skill_exp_list)
    min_exp = min(skill_exp_list)
    exp_range = str(min_exp) + "-" + str(max_skills_exp)
    dao.insert_skill_exp_range(exp_range)
    return



def get_html_code_for_skills(html_code, field_value_list):
    # print(field_value_list)
    skills_left = []
    skill_set = get_unique_values_list(field_value_list)
    skill_set.sort()
    #security
    css_str = 'CSS'
    java_str = 'Java'
    html_str = 'HTML'
    hibernate_str = 'Hibernate'
    php_str = 'PHP'
    sql_str = 'SQL/ Microsoft SQL Server 2008 /2012/2018'
    android_str = 'Android/ Hybrid Mobile application'
    data_struct = 'Data Structures'
    net_str = 'ASP.NET/ .NET'
    comnet_str = 'Computer Networks/ Wireless Communication'
    aws_str = 'AWS/ Web services/ Cloud Computing'
    python_str = 'Python Frameworks'
    pro_str = 'Project Management/ Project Tracking/ Project Delivery/ Monthly MIS/ Jenkins'
    csharp_str = 'C#/ C/ C++'
    machlear_str = 'Machine Learning (ML)/ Artificial Intelligence (AI)/ Hardware Accelerators/ Natural Language Processing (NLP)'
    exec_str = 'Excellent verbal and written communication/ Ability to inspire and convince others/ Presentation skills'
    soft_str = 'Software development Methodology/ Software Development Life Cycle (SDLC)/ Automation/ MVC/ DevOps tools-CICD/ Agile Methodology/ ' \
               'Performance Testing/ Quality Assurance (QA)'
    web_app_str = 'Web applications/ RESTFUL API' #/ NodeJS/ Client Side Technologies/ Frontend Development'
    crypto_str = 'Cryptography/ Cyber Security '
    augment_str = 'Augmented Reality/ virtual reality/ 3D Technology'
    image_str = 'Image Processing/ Matlab/ PCB Design'
    signal_str = 'Signal Integrity/Power Integrity analysis tools'
    admin_str = 'Administration/ Database Administration/ System Administration'
    prod_dev_str = 'Electronics Product Development Cycle/ VLSI/ '
    big_data = 'Big Data analytics'
    os_str = 'Operaing System'
    #os_data os +computer architec
    for i in skill_set:
        skill = i.lower().strip()

        if skill.find("java") >= 0 or skill.find("oop") >= 0 or skill.find("object oriented programming") >= 0:
            if skill != 'java' and skill != 'javascript':
                java_str = java_str + "/ " + i

        elif skill.find("big data") >= 0 or skill == "r" or skill.find("r programming") >= 0:
            if skill != 'big data analytics':
                big_data = big_data + "/ " + i

        elif skill.find("linux") >= 0 or skill.find("windows") >= 0 or skill.find("operating") >= 0 or skill.find("os") >= \
                0 or skill.find("computer arch") >= 0 or skill.find("unix") >= 0 or skill.find("risc") >= 0:
            if skill != 'operating system':
                os_str = os_str + "/ " + i


        elif skill.find("css") >= 0:
            if skill != "css":
                css_str = css_str + "/ " + i

        elif skill.find("html") >= 0:
            if skill != "html":
                html_str = html_str + "/ " + i

        elif skill.find("hibernate") >= 0 or skill.find("spring") >= 0:
            if skill != "hibernate" and skill != "spring":
                hibernate_str = hibernate_str + "/ " + i

        elif skill.find("php") >= 0:
            if skill != "php":
                php_str = php_str + "/ " + i

        elif skill.find("sql") >= 0 or skill.find("mongo") >= 0 or skill.find("dbms") >= 0:
            if skill != "sql":
                sql_str = sql_str + "/ " + i

        elif skill.find("data structure") >= 0:
            if skill != "data structure" and skill != "data structures":
                data_struct = data_struct + "/ " + i

        elif skill.find("android") >= 0 or skill.find("hybrid mobile application") >= 0:
            if skill != "android" and skill != "hybrid mobile application":
                android_str = android_str + "/ " + i

        elif skill.find(".net") >= 0 or skill.find("visual") >= 0 :
            if skill != ".net":
                net_str = net_str + "/ " + i

        elif skill.find("network") >= 0 or skill.find("communication") >= 0 or skill.find("legal") >= 0 or skill.find("3g") >= 0 or skill.find("switch")\
                >= 0 or skill.find("4g") >= 0 or (skill.find("wi") >= 0 and skill.find("fi") >= 0) or skill.find("5g") >= 0 or \
                skill.find("wire") >= 0 or skill.find("ipv") >= 0 or skill.find("tcp") >= 0 or skill.find("ethernet") >= 0\
                or skill.find("safety") >= 0 or skill.find("security") >= 0 or skill.find("forensic") >= 0 or skill.find("rules and regulations") >= 0:
            if skill != "computer networks" and skill != "wireless communication":
                comnet_str = comnet_str + "/ " + i

        elif skill.find("aws") >= 0 or skill.find("web services") >= 0 or skill.find("cloud computing") >= 0:
            if skill != "aws" and skill != "web services" and skill != "cloud Computing":
                aws_str = aws_str + "/ " + i

        elif skill.find("python") >= 0:
            if skill != "python":
                python_str = python_str + "/ " + i

        elif skill.find("project management") >= 0 or skill.find("team management") >= 0 or skill.find("building management") >= 0 or\
                skill.find("project delivery") >= 0 or (skill.find("program") >= 0 and skill.find("management") >= 0) or skill.find(
                "event management") >= 0 or skill.find("jenkins") >= 0 or skill.find("project planning") >= 0 or skill.find("site support") >= 0\
                or skill.find("customer interaction") >= 0 or skill.find("project tracking") >= 0  or skill.find("product planning") >= 0:
            if skill != "project management" and skill != "project delivery" and skill != "event management" and skill != "jenkins":
                pro_str = pro_str + "/ " + i

        elif skill == "c#" or skill == "c" or skill == "c++":
            continue

        elif skill.find("machine learning") >= 0 or skill.find(
                "artificial intelligence") >= 0 or skill == "ml" or skill == "ai" or skill == "dl" or skill.find("hardware") >= 0 or \
                skill.find("accelerators") >= 0 or skill.find("deep") >= 0 or skill.find("natural language") >= 0 or skill.find("speech") >= 0\
                or skill.find("model") >= 0 or skill.find("decision making") >= 0 or skill.find("data clean") >= 0 or skill.find("data min") >= 0\
                or skill.find("data clean") >= 0 or skill.find("writ") >= 0 or skill.find("audio") >= 0 or skill.find("video") >=\
                0 or skill.find("soft comput") >= 0:
            if skill != "machine learning (ml)" and skill != "Natural Language Processing (NLP)" and skill != "artificial intelligence(ai)" and skill != "hardware accelerators" and skill != "ml" and skill != "ai":
                machlear_str = machlear_str + "/ " + i

        elif skill.find("excellent verbal and written communication") >= 0 or skill.find("interpersonal") >= 0 or skill.find(
                "ability to inspire and convince others") >= 0 or skill.find("content") >= 0 or skill.find("writ") >= 0\
                or skill.find("presentation") >= 0 or skill.find("leadership") >= 0 or skill.find("mentoring") >= 0  or skill.find("documentation") >= 0:
            if skill != "excellent verbal and written communication" and skill != "ability to inspire and convince others":
                exec_str = exec_str + "/ " + i

        elif skill.find("software") >= 0 or skill.find("servlet") >= 0 or skill.find("struts") >= 0  or skill.find("kuberne") >= 0 or skill.find("parallel programming") >= 0 or skill.find("development") >= 0 or skill.find("techno") >= 0 or skill.find(
                "nodejs") >= 0 or skill.find("app") >= 0 or skill.find("microserv") >= 0 or skill.find("jquery") >= 0 or \
                skill.find("software development life cycle") >= 0 or skill.find("sdlc") >= 0 or skill.find("coding") >= 0 or skill.find(
            "Automation") >= 0 or skill.find("MVC") >= 0 or skill.find("DevOps") >= 0 or skill.find("docker") >= 0 or \
                skill.find("angular") >= 0 or skill.find("cicd") >= 0 or skill.find("ui/ux") >= 0 or skill.find("ci/cd") >= 0 or skill.find(
            "performance testing") >= 0 or skill.find("quality assurance") >= 0 or skill.find("django") >= 0 or skill.find("pytorch") >= 0\
            or skill.find("high performance") >= 0 or skill.find("flask") >= 0 or skill.find("flutter") >= 0 or (skill.find("requirement") >= 0 and
                                                                                                                 skill.find(
                                                                                                                     "document") >= 0)        \
                or skill == "qa" or skill.find("restful api") >= 0 or skill.find("eclipse") >= 0 or (skill.find("system") >= 0 and \
                                                                                                     (skill.find("architecture") >= 0 or skill.find("design")
                                                                                                      >= 0)) or skill.find("pandas") >= 0 or skill.find("json") >= 0 :
            if skill != "software development methodology" and skill != "Software Development Life Cycle (SDLC)" and skill != "SDLC" and skill != "Automation" and skill != "MVC" and \
                    skill != "DevOps tools-CICD" and skill != "angular" and skill != "performance testing" and skill != "quality assurance (qa)" and skill != "restful api":
                soft_str = soft_str + "/ " + i

        elif skill.find("cryptography") >= 0 or skill.find("cyber security") >= 0:
            if skill != "cryptography" and skill != "cyber security":
                crypto_str = crypto_str + "/ " + i

        elif skill.find("web") >= 0  or skill.find("rest") >= 0 or skill.find("nodejs") >= 0 or skill.find("react") >= 0 or skill.find("bootstrap") >= 0 or skill.find("client") >= 0 or skill.find("frontend") >= 0:
            if skill != 'Web applications' and skill != 'RESTFUL API':
                web_app_str = web_app_str + "/ " + i

        elif skill.find("electro") >= 0 or skill.find("vlsi") >= 0 or skill.find("analog") >= 0 or skill.find("digital") >= 0 or skill.find("embed") >= 0 \
                or skill.find("fpga") >= 0 or skill.find("circuit") >= 0 or skill.find("hdl") >= 0 or \
                skill.find("microproce") >= 0 or skill.find("aurdino") >= 0 or skill.find("rtos") >= 0 or skill.find("arm") >= 0 or skill.find("verilog") >= 0\
             or skill.find("Xilinx") >= 0  or skill.find("board") >= 0 or skill.find("robot") >= 0 or skill.find("signal") >= 0 \
                or skill.find("sensor") >= 0 or skill.find("vehicle") >= 0 or skill.find("power") >= 0 or skill.find("iot") >= 0\
                or skill.find("internet of things") >= 0 or skill.find("raspberry") >= 0 or  skill.find("microcontrol") >= 0 :
            if skill != 'Electronics Product Development Cycle' and skill != 'VLSI':
                prod_dev_str = prod_dev_str + "/ " + i

        elif skill.find("image") >= 0 or skill.find("matlab") >= 0 or skill.find("pcb") >= 0 or skill.find("simulation") >= 0:
            if skill != 'Image Processing' and skill != 'Matlab' and skill != 'PCB Design':
                image_str = image_str + "/ " + i
        elif skill.find("admin") >= 0:
            if skill != 'Administration':
                admin_str = admin_str + "/ " + i
        else:
            skills_left.append(skill)
    print("here----------------------"+str(skills_left))

    html_code = html_code + '<option value="select" selected>Select</option>' \
                            '<option value="' + java_str + '">' + java_str + '</option>' + '<option value="' + css_str + '">' + css_str + \
                '</option>' + '<option value="' + html_str + '">' + html_str + '</option>' + '<option value="' + hibernate_str + '">' + hibernate_str + \
                '</option>' + '<option value="' + php_str + '">' + php_str + '</option>' + '<option value="' + data_struct + '">' + data_struct + \
                '</option>' + '<option value="' + sql_str + '">' + sql_str + '</option>' + '<option value="' + android_str + '">' + android_str + \
                '<option value="' + net_str + '">' + net_str + '</option>' + '<option value="' + comnet_str + '">' + comnet_str + '</option>' + \
                '<option value="' + aws_str + '">' + aws_str + '</option>' + '<option value="' + python_str + '">' + python_str + '</option>' + \
                '<option value="' + pro_str + '">' + pro_str + '</option>' + '<option value="' + csharp_str + '">' + csharp_str + '</option>' + \
                '<option value="' + machlear_str + '">' + machlear_str + '</option>' + '<option value="' + exec_str + '">' + exec_str + '</option>' + \
                '<option value="' + soft_str + '">' + soft_str + '</option>' + \
                '<option value="' + crypto_str + '">' + crypto_str + '</option>' + '<option value="' + augment_str + '">' + augment_str + '</option>' + \
                '<option value="' + image_str + '">' + image_str + '</option>' + '<option value="' + signal_str + '">' + signal_str + '</option>' + \
                '<option value="' + admin_str + '">' + admin_str + '</option>' + \
                '<option value="' + web_app_str + '">' + web_app_str + '</option>' + \
                '<option value="' + prod_dev_str + '">' + prod_dev_str + '</option>' + \
                '<option value="' + admin_str + '">' + admin_str + '</option>' + '<option value="' + big_data + '">' + big_data + '</option>' + \
                '<option value="' + os_str + '">' + os_str + '</option>'


    unique_skills_left = get_unique_values_list(skills_left).sort()
    #print(skills_left)

    for skill in skills_left:#unique_skills_left:
        html_code = html_code + '<option value="' + skill + '">' + skill + '</option>'

    return html_code


def create_field_html_code(field, field_value_list):
    field_value_list = remove_none_values_from_list(field_value_list)
    # print(field)
    html_code = ''
    if field != "Degree" and field != "Skills" and field != "Age" and field != "Preferences":
        prefix = '<td><select name="' + field + '">'
        html_code = prefix
    # fetch_filtered_data("'+field+'",this.value)
    if field == "Age":
        prefix = '<td style="width:5%"><select name="' + field + '">'
        html_code = prefix
        html_code = html_code + '<option value="select" selected>Select</option>' \
                                '<option value="below-20">below 20</option><option value="21-25">' \
                                '21-25</option><option value="26-30">26-30</option><option value="31-35">31-35</option>' \
                                '<option value="36-40">36-40</option><option value="41-45">41-45</option><option ' \
                                'value="46-50">46-50</option><option value="51-55">51-55</option><option value="56-60">' \
                                '56-60</option><option value="above-60">above-60</option>'
    elif field == "Preferences":
        prefix = '<td style="width:15%"><select name="' + field + '">'
        html_code = prefix
        preference_list = get_unique_preference_list(field_value_list)
        field_value_list = preference_list
        html_code = html_code + '<option value="select" selected>Select</option>'
        for i in field_value_list:
            if i != "Others" and i != "TVM" and i != "Thiruvananthapuram":
                html_code = html_code + '<option value="' + str(i) + '">' + str(i) + '</option>'
        html_code = html_code + '<option value="Thiruvanthapuram">Thiruvananthapuram (TVM)</option>'
        html_code = html_code + '<option value="Others">Others</option>'
    elif field == "Skills":
        prefix = '<td width="100px"><select size="10" name="' + field + '" >'
        html_code = prefix
        html_code = get_html_code_for_skills(html_code, field_value_list)
    elif field == "Degree":
        degree_code_str = '<option value="select" selected>Select</option>' \
                          '<option value="B.E./B.Tech.">B.E./B.Tech.</option>' \
                          '<option value="B.A.">B.A.</option>' \
                          '<option value="B.Com.">B.Com.</option>' \
                          '<option value="B.B.A.">B.B.A.</option>' \
                          '<option value="B.Sc.">B.Sc.</option>' \
                          '<option value="B.C.A.">B.C.A.</option>' \
                          '<option value="B.Ed.">B.Ed.</option>' \
                          '<option value="M.E./M.Tech.">M.E./M.Tech.</option>' \
                          '<option value="M.A.">M.A.</option>' \
                          '<option value="M.Com.">M.Com.</option>' \
                          '<option value="M.C.A.">M.C.A.</option>' \
                          '<option value="M.Sc.">M.Sc.</option>' \
                          '<option value="M.B.A">M.B.A.</option>' \
                          '<option value="M.Phil">M.Phil.</option>' \
                          '<option value="Ph.D.">Ph.D.</option>' \
                          '<option value="Others">Others</option>'
        html_code = '<td><select name="Min_' + field + '">' + degree_code_str + '</select></td>' + '<td><select name="Max_' + field + \
                    '">' + degree_code_str
    elif field == "Percentage":
        prefix = '<td><select size="10" multiple name="' + field + '" >'
        html_code = prefix
        html_code = html_code + '<option value="select" selected>Select</option>' \
                                '<option value="below 60%">below 60%</option><option value="60%-65%">' \
                                '60%-65%</option><option value="65%-70%">65%-70%</option><option value="70%-75%">70%-75%</option>' \
                                '<option value="75%-80%">75%-80%</option><option value="80%-85%">80%-85%</option><option ' \
                                'value="85%-90%">85%-90%</option><option value="90%-95%">90%-95%</option><option value="95%-100%">' \
                                '95%-100%</option>'
    elif field == "Designation":
        # print(field_value_list)
        cmpl_design_list = get_cmpl_designation_list(field_value_list)
        prefix = '<td><select size="10" name="' + field + '" >'
        html_code = prefix
        html_code = html_code + '<option value="select" selected>Select</option>'
        for item in cmpl_design_list:
            html_code = html_code + '<option value="' + str(item) + '">' + str(item) + '</option>'
        html_code = html_code + '<option value="Others">Others</option>'

    elif field == "Total_Experience":
        prefix = '<td><select size="7" name="' + field + '" >'
        html_code = prefix
        html_code = html_code + '<option value="select" selected>Select</option>' \
                                '<option value="No Experience">No Experience</option><option value="0-3year(s)">' \
                                '0-3year(s)</option><option value="3year(s)-7year(s)">3year(s)-7year(s)</option><option ' \
                                'value="7year(s)-9year(s)">7year(s)-9year(s)</option>' \
                                '<option value="9year(s)-15year(s)">9year(s)-15year(s)</option><option value="above-15' \
                                'above">15year(s)-above</option> '
    elif field == "Experience_in_Skill":
        prefix = '<td><select size="10" name="Experience_in_Skill" >'
        html_code = prefix + '<option value="select" selected>Select</option>' \
                                '<option value="No Experience">No Experience</option><option value="0-3">' \
                                '0-3year(s)</option><option value="3-7">3year(s)-7year(s)</option><option ' \
                                'value="7-9">7year(s)-9year(s)</option>' \
                                '<option value="9-15">9year(s)-15year(s)</option><option value="15-above"' \
                             '>15year(s) and above</option> '
    else:
        # print("here"+field)
        if field == "Post_name":
            prefix = '<td style="width:10%"><select name="' + field + '" >'
            html_code = prefix
        if field == "Specialisation":
            prefix = '<td style="width:46%"><select size="10" multiple name="' + field + '" >'
            html_code = prefix
        if len(field_value_list) > 1:
            field_value_list.sort()
        html_code = html_code + '<option value="select" selected>Select</option>'
        field_list = []
        for i in field_value_list:
            field_val = i.lower()
            if field_val == "na":
                continue
            if len(field_val) > 1:
                clubbed_spec = get_clubbed_spec(field_val, i)
                field_list.append(clubbed_spec)
        unique_field_list = get_unique_values_list(field_list)
        for val in unique_field_list:
            if val != "Others":
                html_code = html_code + '<option value="' + val + '">' + val + '</option>'
        html_code = html_code + '<option value="Others">Others</option>'
    html_code = html_code + '</select></td>'
    return html_code


def get_cmpl_designation_list(designation_list):
    new_field_value_list = []
    for i in designation_list:
        field_value: object = i.lower()
        # print(field_value)
        if len(field_value) <= 1:
            continue
        if field_value.find("--") >= 0:
            continue

        if field_value == "na" or field_value == "nothing" or field_value == "nill" or field_value == "nil" or field_value == "no" or field_value == "n/a" \
                or field_value == "n.a" or field_value == "none":
            continue
            # asst/asso.professor

        elif field_value.find("a.p") >= 0 or field_value.find("ap") >= 0 or field_value.find("hod") >= 0 or (
                (field_value.find("assi") >= 0 or \
                 field_value.find("asso") >= 0 or field_value.find("asst") >= 0) and field_value.find(
            "prof") >= 0) or field_value.find("prof") >= 0:
            new_field_value_list.append("Assistant Professor/ Associate Professor/ A.P.")

            # manager/knowlwdge
        elif field_value.find("manager") >= 0 or field_value.find("mang") >= 0 or field_value.find(
                "pm") >= 0 or field_value.find("kp") >= 0 or \
                field_value.find("pgr") >= 0 or field_value.find("mgr") >= 0 or field_value.find("pdm") >= 0 or \
                field_value.find("bm") >= 0 or field_value.find("bim") >= 0 or field_value.find("agm") >= 0 or \
                (field_value.find("kno") >= 0 and field_value.find("part") >= 0) or field_value.find("man") >= 0 or \
                field_value.find("sme") >= 0 or field_value.find("rm") >= 0 or field_value.find("fms") >= 0 or \
                field_value.find("yp") >= 0 or field_value.find("young") >= 0 or field_value.find("gm") >= 0 or \
                field_value.find("dgm") >= 0 or field_value.find("am") >= 0 or field_value.find("dmii") >= 0:
            new_field_value_list.append("Project Manager/ Knowledge Partner")

            # leader/Senior
        elif field_value.find("lead") >= 0 or field_value.find("spe") >= 0 or (field_value.find("ml") >= 0 and not (
                field_value.find("mach") >= 0 and field_value.find("lear") >= 0)) or (
                field_value.find("eng") >= 0 and (field_value.find("sr") >= 0 or field_value.find("sen") >= 0)):
            new_field_value_list.append("Project Lead/ Module Lead/ Senior Project Engineer")

            # knowledge asso.
        elif field_value.find("kn") >= 0 and field_value.find("asso") >= 0 or field_value.find("assco") >= 0:
            new_field_value_list.append("Knowledge Associate")

            # expert
        elif field_value.find("exp") >= 0 or field_value.find("sde") >= 0:
            new_field_value_list.append("Expert")

            # Engineer/software
        elif field_value.find("software") >= 0 or field_value.find("developer") >= 0 or field_value.find(
                "programmer") >= 0 \
                or field_value.find("eng") >= 0 or field_value.find("enig") >= 0 or field_value.find(
            "cod") >= 0 or field_value.find("pe") >= 0 or \
                field_value.find("dba") >= 0 or field_value.find("arch") >= 0 or field_value.find("computer") >= 0 or \
                field_value.find("ui") >= 0 or field_value.find("ux") >= 0 or field_value.find(
            "test") >= 0 or field_value.find("cyber") >= 0 or \
                field_value.find("cloud") >= 0 or field_value.find("it") >= 0 or field_value.find(
            "desi") >= 0 or field_value.find("cse") >= 0 or \
                field_value.find("ase") >= 0 or field_value.find("fse") >= 0 or field_value.find("p.e") >= 0 or \
                field_value.find("ae") >= 0 or field_value.find("nyv") >= 0 or field_value.find("se") >= 0 or \
                field_value.find("jse") >= 0 or field_value.find("dbor") >= 0 or field_value.find("j.e") >= 0:
            new_field_value_list.append("Software Developer/ Programmer/ Engineer")

            # Accountant
        elif field_value.find("acc") >= 0 or field_value.find("cash") >= 0 or field_value.find(
                "purc") >= 0 or field_value.find("nse") >= 0 or field_value.find("prod") >= 0 or field_value.find(
            "sale") >= 0 or \
                field_value.find("ci") >= 0 or field_value.find("swo") >= 0 or field_value.find(
            "cmt") >= 0 or field_value.find("mark") >= 0:
            new_field_value_list.append("Accountant/ Account Technician/ Cashier/ Cashier")

            # Faculty/Leacturer
        elif ((field_value.find("ad") >= 0 or field_value.find("gues") >= 0 or field_value.find("temp") >= 0 or
               field_value.find("visit") >= 0) and (
                      field_value.find("hoc") >= 0 or field_value.find("faculty") >= 0)) or \
                field_value.find("lect") >= 0 or field_value.find("teach") >= 0 or field_value.find(
            "educa") >= 0 or field_value.find("oper") >= 0 or field_value.find("tgt") >= 0 or field_value.find(
            "pgt") >= 0 or \
                field_value.find("tut") >= 0 or field_value.find("inst") >= 0 or field_value.find(
            "dse") >= 0 or field_value.find("pg") >= 0 or field_value.find("gat") >= 0:
            new_field_value_list.append(" (Ad. hoc./ Temporary/ Visiting/ Guest) Lecturer/ Faculty/ Teacher/ Trainer")

            # Counseller
        elif field_value.find("couns") >= 0:
            new_field_value_list.append("Counsellor")

            # admin
        elif field_value.find("admin") >= 0 or (
                field_value.find("data") >= 0 and (field_value.find("entry") >= 0 or field_value.find("proc") >= 0)) or \
                field_value.find("mis") >= 0 or field_value.find("plan") >= 0 or field_value.find(
            "rdo") >= 0 or field_value.find("deo") >= 0 or field_value.find("ert") >= 0 or field_value.find("sso") >= 0:
            new_field_value_list.append(" Admin/ Data Entry operator/ MIS/ Administrator")

            # Advisor
        elif field_value.find("advi") >= 0 or field_value.find("cons") >= 0:
            new_field_value_list.append("Advisor/ Consultant")

            # HR
        elif field_value.find("hr") >= 0 or field_value.find("human") >= 0 or field_value.find(
                "resource") >= 0 or field_value.find("relationship") >= 0:
            new_field_value_list.append("Human Resource/ Aftercare and Relationship Expert/ HR")

            # analyst
        elif field_value.find("anal") >= 0 or field_value.find("bda") >= 0 or field_value.find(
                "dba") >= 0 or field_value.find("qa") >= 0:
            new_field_value_list.append("Analyst/ Quality Assurance")

            # apprentice
        elif field_value.find("trainee") >= 0 or field_value.find("apprent") >= 0 or field_value.find("intern") >= 0 or \
                field_value.find("enter") >= 0 or field_value.find("appr") >= 0 or field_value.find(
            "get") >= 0 or field_value.find("ta") >= 0:
            new_field_value_list.append("Trainee/ Apprentice/ Intern")

            # assistant
        elif field_value.find("assi") >= 0:
            new_field_value_list.append("Assistant")

            # associate
        elif field_value.find("asso") >= 0 or field_value.find("pa") >= 0:
            new_field_value_list.append("Associate")

            # officer
        elif field_value.find("offic") >= 0 or field_value.find("cto") >= 0 or field_value.find("cco") >= 0:
            new_field_value_list.append("Officer")

            # scientist
        elif field_value.find("sci") >= 0 or field_value.find("research") >= 0 or field_value.find("jrf") >= 0 or \
                field_value.find("srf") >= 0 or field_value.find("fellow") >= 0 or field_value.find("ml") >= 0 or \
                field_value.find("ai") >= 0 or field_value.find("mach") >= 0 or field_value.find(
            "ra") >= 0 or field_value.find("stat") >= 0:
            new_field_value_list.append("Scientist/ JRF/ SRF/ RA/ Statistics")

            # director
        elif field_value.find("direc") >= 0 or field_value.find("dir") >= 0:
            new_field_value_list.append("Director")

            # vp
        elif field_value.find("vp") >= 0:
            new_field_value_list.append("VP/ AVP")

        # project support staff/executive
        elif field_value.find("staff") >= 0 or field_value.find("support") >= 0 or field_value.find("exe") >= 0 or \
                field_value.find("invi") >= 0 or field_value.find("inac") >= 0 or field_value.find("inch") >= 0 or \
                field_value.find("chie") >= 0 or field_value.find("exc") >= 0 or field_value.find("proj") >= 0 or \
                field_value.find("proc") >= 0 or field_value.find("jto") >= 0 or field_value.find("inve") >= 0 or \
                field_value.find("age") >= 0 or field_value.find("tm") >= 0 or field_value.find("track") >= 0 or \
                field_value.find("fts") >= 0 or field_value.find("jcp") >= 0 or field_value.find("helpdesk") >= 0:
            new_field_value_list.append("Project Support Staff/ Executive")

            # coordinator
        elif field_value.find("coor") >= 0 or field_value.find("co-or") >= 0 or field_value.find("fac") >= 0 or \
                field_value.find("info") >= 0 or field_value.find("supe") >= 0 or field_value.find("tech") >= 0 or \
                field_value.find("sdo") >= 0 or field_value.find("sto") >= 0 or field_value.find(
            "sdf") >= 0 or field_value.find("sse") >= 0:
            new_field_value_list.append("Coordinator/ Facilitator/ Informatics Officer/ Supervisor/ ERP and Production")

            # clerk
        elif field_value.find("clerk") >= 0 or field_value.find("ldc") >= 0 or field_value.find("udc") >= 0:
            new_field_value_list.append("Clerk")

            # CEO
        elif field_value.find("ceo") >= 0 or field_value.find("co") >= 0 or field_value.find("foun") >= 0 or \
                field_value.find("own") >= 0 or field_value.find("amba") >= 0 or field_value.find(
            "led") >= 0 or field_value.find("head") >= 0:
            new_field_value_list.append("CEO, Co-founder/ Co- Founder/ Co-ordinator/CO-FOUNDER/ co-owner")
        else:  # others
            continue
    unique_val_list = get_unique_values_list(new_field_value_list)  # removing duplicates
    unique_val_list.sort()
    return unique_val_list


def get_clubbed_spec(field_val, i):
    if field_val == "science" or field_val == "physics" or field_val == "chemistry" or field_val == "biology":
        field_val = "Science/ Physics/ Chemistry/ Biology"
    elif field_val.find("computer") >= 0 or field_val.find("software") >= 0 or field_val.find("network") >= 0 or field_val.find("cs") >= 0:
        field_val = "Computer Science/ Computer/ Information Science/ Software Engineering/ Network Security"
    elif field_val.find("electronics") >= 0 or field_val.find("telecommunication") >= 0 or field_val.find(
            "communication") >= 0 or field_val.find("vlsi") >= 0 or field_val.find("instrumentation") >= 0 or field_val.find("control") >= 0:
        field_val = "Electronics &/ Communication/ &/ Instrumentation &/ Electrical &/ Telecommunication " \
                    "&/ Information Science &/ Nanotechnology &/ Control Engineering" \
                    "/ Power Electronics/ VLSI &/ Embedded System"
    elif field_val.find("management") >= 0:
        field_val = "Material Management/ General Management/ Operational Management/ " \
                    "Business Management/ Purchase Management "
    elif field_val.find("information") >= 0:
        field_val = "Information Science and Engineering/ Information Technology"
    elif field_val.find("mach") >= 0 or \
            (field_val.find("data") >= 0 and field_val.find("science") >= 0) or \
            (field_val.find("artificial") >= 0 and field_val.find("intelligence") >= 0) or \
            field_val.find("ml") >= 0 or field_val.find("ai") >= 0 or field_val.find("machine") >= 0:
        field_val = "Machine Learning/ Artificial Intelligence/ Data Science/ Machine Learning and Data " \
                    "Science/ ML/ AI"
    elif field_val.find("civil") >= 0:
        field_val = "Civil Engineering /Civil"
    elif field_val.find("ocean") >= 0:
        field_val = "Oceanography/ Ocean Science"
    elif field_val.find("bioinformatics") >= 0:
        field_val = "Bioinformatics Engineering/ Bioinformatics"
    elif field_val.find("biotechnology") >= 0 or field_val.find("biochemistry") >= 0:
        field_val = "Biotechnology/ Biochemistry"
    elif field_val.find("geo") >= 0 and field_val.find("informatics") >= 0:
        field_val = "Geo informatics/ Geo informatics Engineering"
    elif field_val.find("atmospheric") >= 0:
        field_val = "Atmospheric Science/ Atmospheric"
    elif field_val.find("environmental") >= 0:
        field_val = "Environmental Science and Computing/ Environmental Engineering"
    elif field_val.find("finance") >= 0 or field_val.find("chartered") >= 0 or field_val.find("ca") >= 0:
        field_val = "Finance/ Chartered Accountant/ CA"
    elif field_val.find("Mechanical") >= 0:
        field_val = "Mechanical/Mechanical Engineering"
    elif field_val.find("hr") >= 0 or field_val.find("human") >= 0:
        field_val = "HR/ Human Resource"
    elif field_val.find("mis") >= 0 or field_val.find("management information system") >= 0:
        field_val = "MIS/ Management Information System"
    else:
        field_val = i
    return field_val


def read_file_as_string(file_path):
    with open(file_path, 'r') as file:
        data = file.read().replace('\n', '')
    return data


def remove_selected_keyword(field_value):
    ind = field_value.find("selected")
    new_val = 0
    if ind > 0:
        new_val = field_value[:ind]
    else:
        new_val = field_value
    return new_val


def write_code_to_file(file_path, file_content):
    f = open(file_path, "w")
    f.write(file_content)
    f.close()
    return


def fetch_age_constraint(age):
    constraint = ''
    if age != 'select':  # some age selected
        if age.find('-') >= 0:
            ind = age.find('-')
            if age.find('below') >= 0 or age.find('above') >= 0:
                age_val = age[ind + 1:]
                if age.find('below') >= 0:
                    constraint = " Age <= " + age_val + "' "
                else:
                    constraint = ' Age >= "' + age_val + '" '
            else:
                min_age = age[:ind]
                max_age = age[ind + 1:]
                constraint = ' Age >= ' + min_age + '  and Age <= ' + max_age + ' '
    else:
        print("age not selected")
    return constraint


def fetch_degree_constraint(degree_val):
    # B.E./B.Tech.
    constraint = ''
    if degree_val.find("/") >= 0:
        ind = degree_val.find("/")
        match_str1 = degree_val[:ind]  # B.E. or M.E.
        # B.E./B.Tech and M.E./M.Tech.
        if match_str1 == "B.E.":
            constraint = ' (Degree like "%tech%" or Degree like "%b%e%" or Degree like "%eng%") '
        else:
            constraint = ' (Degree like "%m%tech%" or Degree like "%m%e%" or Degree like "%eng%") '
    elif degree_val != "Others":
        match_str = '%' + degree_val.replace('.', '%')
        constraint = ' Degree like "' + match_str + '" '
    elif degree_val == "Others":  # others
        constraint = ' Degree like "%Others%" '
    else:
        print("Degree fields not selected")
    return constraint


def fetch_specialisation_constraint(specialisation_val):
    # print("here"+specialisation_val)
    constraint = ''
    if specialisation_val == "Science/ Physics/ Chemistry/ Biology":
        constraint = '( Specialisation like "%Science%" or Specialisation like "%Physics%" or Specialisation like ' \
                     '"%Chemistry%" or Specialisation like "%Biology%") '
    elif specialisation_val == "Computer Science/ Computer/ Information Science/ Software Engineering/ Network Security":
        constraint = '(Specialisation like "%Computer%" or Specialisation like "%Soft%Eng%" or Specialisation like ' \
                     '"%Network%" or Specialisation like "%Security%")'
    elif specialisation_val == "Electronics &/ Communication/ &/ Instrumentation &/ Electrical &/ Telecommunication " \
                               "&/ Information Science &/ Nanotechnology &/ Control Engineering" \
                               "/ Power Electronics/ VLSI &/ Embedded System":
        constraint = ' (Specialisation like "%Electronics%" or Specialisation like "%VLSI%" or ' \
                     ' Specialisation like %Communication% or Specialisation like "%Instrumentation%") '
    elif specialisation_val == "Material Management/ General Management/ Operational Management/ " \
                               "Business Management/ Purchase Management ":
        constraint = ' Specialisation like "%Management%"'
    elif specialisation_val == "Information Science and Engineering/ Information Technology/ Material Management":
        constraint = ' Specialisation like "%Information%"'
    elif specialisation_val == "Machine Learning/ Artificial Intelligence/ Data Science/ Machine Learning and Data " \
                               "Science/ ML/ AI":
        constraint = '(Specialisation like "%Machine%" or Specialisation like "%Data%Sc%" or Specialisation like "%Artificial%" or' \
                     ' Specialisation like "%ML%" or Specialisation like "%AI%")'
    elif specialisation_val == "Civil Engineering /Civil":
        constraint = 'Specialisation like "%Civil%"'
    elif specialisation_val == "Oceanography/ Ocean Science":
        constraint = 'Specialisation like "%Ocean%"'
    elif specialisation_val == "Bioinformatics Engineering/ Bioinformatics":
        constraint = 'Specialisation like "%Bioinformatics%"'
    elif specialisation_val == "Biotechnology/ Biochemistry":
        constraint = 'Specialisation like "%Bio%"'
    elif specialisation_val == "Geo informatics/ Geo informatics Engineering":
        constraint = 'Specialisation like "%Geo%"'
    elif specialisation_val == "Atmospheric Science/ Atmospheric":
        constraint = 'Specialisation like "%Atmospheric%"'
    elif specialisation_val == "Environmental Science and Computing/ Environmental Engineering":
        constraint = 'Specialisation like "%Environmental%"'
    elif specialisation_val == "Finance/ Chartered Accountant/ CA":
        constraint = '(Specialisation like "%Finance%" or Specialisation like "%Chartered%" or Specialisation like "%CA%")'
    elif specialisation_val == "Computer Application":
        constraint = 'Specialisation like "%Comp%Ap%"'
    elif specialisation_val == "Blockchain":
        constraint = 'Specialisation like "%Block%"'
    elif specialisation_val == "Allied Discipline":
        constraint = 'Specialisation like "%All%%Dis"'
    elif specialisation_val == "Health Informatics":
        constraint = 'Specialisation like "%Hea%Info%"'
    elif specialisation_val == "Modeling and Simulation":
        constraint = 'Specialisation like "%Mod%Sim%"'
    elif specialisation_val == "Mechanical/Mechanical Engineering":
        constraint = 'Specialisation like "%Mechanical%"'
    elif specialisation_val == "Scientific Computing":
        constraint = 'Specialisation like "%Sci%Comp%"'
    elif specialisation_val == "Medical Engineering":
        constraint = 'Specialisation like "%Med%Eng%"'
    elif specialisation_val == "Meteorology":
        constraint = 'Specialisation like "%Meteorology%"'
    elif specialisation_val == "MIS/ Management Information System":
        constraint = '(Specialisation like "%MIS%" or Specialisation like "%Manag%Inf%Sys%")'
    elif specialisation_val == "HR/ Human Resources":
        constraint = '(Specialisation like "%HR%" or Specialisation like "%Hum%Res%")'
    elif specialisation_val == "System":
        constraint = 'Specialisation like "%System%"'
    elif specialisation_val == "Mathematics":
        constraint = 'Specialisation like "%Mathematics%"'
    elif specialisation_val == "Mathematics and Computing":
        constraint = 'Specialisation like "%Math%Comp%"'
    elif specialisation_val == "Computation Biology":
        constraint = 'Specialisation like "%Comp%Bio%"'
    elif specialisation_val == "Cloud Computing":
        constraint = 'Specialisation like "%Cloud%Comp%"'
    elif specialisation_val == "Others":
        constraint = 'Specialisation like "%Others%"'
    else:  # contraint='' is returned
        print("Specialisation not selected")
    return constraint


def fetch_percent_constraint(score):
    constraint = ''
    if score.find("-") >= 0:
        ind = score.find("-")
        min_score = score[:ind].strip("%")
        max_score = score[ind + 1:].strip("%")
        constraint = " Percentage >= CAST('" + min_score + "' AS DECIMAL) and Percentage <=  CAST('" + max_score + "' AS DECIMAL) "
    elif score != "select":
        ind = score.find(" ")
        score_val = score[ind + 1:].strip("%")
        constraint = " Percentage <=  CAST('" + score_val + "' AS DECIMAL) "
    else:
        print("Percentage not selected")
    return constraint


def split_multiple_designations_form_query(designation):
    constraint = '('
    if designation.find("/") >= 0:
        designation = designation.replace("/", "-")
    if designation.find("-") >= 0:
        elements = designation.split("-")
    for elem in elements:
        elem = elem.strip()
        elem = elem.replace(" ", '%')
        constraint = constraint + '(Designation like "%' + elem + '%")' + ' or '
    ind = constraint.rfind('or')
    constraint = constraint[:ind].strip()
    constraint = constraint + ')'
    return constraint


def fetch_designation_constraint(designation):
    if designation == "Assistant Professor/ Associate Professor/ A.P.":
        constraint = '(Designation like "%a%p%" or Designation like "%ap%" or Designation like "%hod%" or Designation like "%assi%" or ' \
                     'Designation like "%asso%" or Designation like "%asst%" or Designation like "%prof%")'

    # manager/knowlwdge
    elif designation == "Project Manager/ Knowledge Partner":
        constraint = '(Designation like "%manager%" or Designation like "%mang%" or Designation like "%pm%" or Designation like "%kp%" or ' \
                     'Designation like "%pgr%" or Designation like "%mgr%" or Designation like "%pdm%" or Designation like "%bm%" or Designation like "%bim%" or ' \
                     'Designation like "%agm%" or Designation like "%kno%" or Designation like "%part%" or Designation like "%man%" or Designation like "%sme%" or ' \
                     'Designation like "%rm%" or Designation like "%fms%" or Designation like "%yp%" or Designation like "%young%" or Designation like "%gm%" or ' \
                     'Designation like "%dgm%" or Designation like "%am%" or Designation like "%%" or Designation like "%dmii%") '

    elif designation == "Analyst/ Quality Assurance":
        constraint = '(Designation like "%anal%" or Designation like "%bda%" or Designation like "%dba%" or Designation like "%qa%")'


    # apprentice
    elif designation == "Trainee/ Apprentice/ Intern":
        constraint = '(Designation like "%trainee%" or Designation like "%apprent%" or Designation like "%intern%" or Designation like "%enter%" or Designation like "%appr%" or ' \
                     'Designation like "%get%" or Designation like "%ta%")'

    # assistant
    elif designation == "Assistant":
        constraint = '(Designation like "%assi%")'

    # Associate
    elif designation == "Associate":
        constraint = '(Designation like "%asso%" or Designation like "%pa%")'

    # Officer
    elif designation == "Officer":
        constraint = '(Designation like "%offic%" or Designation like "%cto%" or Designation like "%cco%")'
    # leader/Senior
    elif designation == "Project Lead/ Module Lead/ Senior Project Engineer":
        constraint = '(Designation like "%lead%" or (Designation like "%spe%" and not(Designation like "%speci%")) or (Designation like "%ml%" and not(Designation like "%mach%") and not(Designation like "%lear%")) or ' \
                     '(Designation like "%eng%" and Designation like "%sr%" and not(Designation like "%srf%")) or (Designation like "%sen%" and not(Designation like "%anal%")))'

    # knowledge asso.
    elif designation == "Knowledge Associate":
        constraint = '(Designation like "%kn%" or Designation like "%asso%" or Designation like "%assco%")'

    # expert
    elif designation == "Expert":
        constraint = '(Designation like "%exp%" or Designation like "%sde%")'

        # "Software Developer/ Programmer/ Engineer"
    elif designation == "Software Developer/ Programmer/ Engineer":
        constraint = '(Designation like "%soft%" or Designation like "%developer%" or Designation like "%programmer%" or ' \
                     'Designation like "%eng%" or Designation like "%enig%" or Designation like "%cod%" or Designation like "%pe%" or ' \
                     'Designation like "%dba%" or Designation like "%arch%" or Designation like "%computer%" or Designation like "%ui%" or ' \
                     'Designation like "%ux%" or Designation like "%test%" or Designation like "%cyber%" or Designation like "%cloud%" or ' \
                     'Designation like "%it%" or Designation like "%desi%" or Designation like "%cse%" or Designation like "%ase%" or ' \
                     'Designation like "%fse%" or Designation like "%p%e%" or Designation like "%ae%" or Designation like "%nyv%" or ' \
                     'Designation like "%se%" or Designation like "%jse%" or Designation like "%dbor%" or Designation like "%j%e%") '

    # Accountant
    elif designation == "Accountant/ Account Technician/ Cashier/ Cashier/ cco":
        constraint = '(Designation like "%acc%" or Designation like "%cash%" or Designation like "%purc%" or Designation like "%nse%" or Designation like "%prod%" or Designation like "%sale%" or ' \
                     'Designation like "%ci%" or Designation like "%swo%" or Designation like "%cmt%" or Designation like "%mark%")'

    # Faculty/Leacturer
    elif designation == "(Ad. hoc./ Temporary/ Visiting/ Guest) Lecturer/ Faculty/ Teacher/ Trainer":
        constraint = '(Designation like "%ad%" or Designation like "%gues%" or Designation like "%temp%" or Designation like "%visit%" or Designation like "%hoc%" or Designation like "%hoc%" or ' \
                     'Designation like "%faculty%" or Designation like "%lect%" or Designation like "%teach%" or Designation like "%educa%" or Designation like "%oper%" or Designation like "%tgt%" or ' \
                     'Designation like "%pgt%" or Designation like "%tut%" or Designation like "%inst%" or Designation like "%dse%" or Designation like "%pg%" or Designation like "%gat%") '

    # Counseller
    elif designation == "Counsellor":
        constraint = 'Designation like "%couns%" '

    # admin
    elif designation == "Admin/ Data Entry operator/ MIS/ Administrator":
        constraint = '(Designation like "%admin%" or Designation like "%data%" or Designation like "%entry%" or Designation like "%proc%" or Designation like "%mis%" or Designation like "%plan%" or ' \
                     'Designation like "%deo%" or Designation like "%ert%" or Designation like "%sso%") '


    # Advisor
    elif designation == "Advisor/ Consultant":
        constraint = '(Designation like "%advi%" or Designation like "%cons%")'

    # HR
    elif designation == "Human Resource/ Aftercare and Relationship Expert/ HR":
        constraint = '(Designation like "%hr%" or Designation like "%human%" or Designation like "%resource%" or Designation like "%relationship%")'

    # analyst

    # Scientist/ JRF/ SRF/ RA/ Statistics
    elif designation == "Scientist/ JRF/ SRF/ RA/ Statistics":
        constraint = '(Designation like "%sci%" or Designation like "%research%" or Designation like "%jrf%" or Designation like "%srf%" or Designation like "%fellow%" or ' \
                     'Designation like "%ml%" or Designation like "%ai%" or Designation like "%mach%" or Designation like "%ra%" or Designation like "%stat%")'

    # director
    elif designation == "Director":
        constraint = '(Designation like "%direc%" or Designation like "%dir%")'

    # vp
    elif designation == "VP/ AVP":
        constraint = 'Designation like "%vp%"'

    # coordinator
    elif designation == "Coordinator/ Facilitator/ Informatics Officer/ Supervisor/ ERP and Production":
        constraint = '(Designation like "%coor%" or Designation like "%co-or%" or Designation like "%fac%" or Designation like "%info%" or Designation like "%supe%" or ' \
                     'Designation like "%tech%" or Designation like "%sdo%" or Designation like "%sto%" or Designation like "%sdf%" or Designation like "%sse%")'

    # clerk
    elif designation == "Clerk":
        constraint = '(Designation like "%clerk%" or Designation like "%ldc%" or Designation like "%udc%")'

    # CEO
    elif designation == "CEO, Co-founder/ Co- Founder/ Co-ordinator/CO-FOUNDER/ co-owner":
        constraint = '(Designation like "%ceo%" or Designation like "%co%" or Designation like "%foun%" or Designation like "%own%" or Designation like "%amba%" or ' \
                     'Designation like "%led%" or Designation like "%head%")'
    # elif designation.find("-") >= 0 or designation.find("/") >= 0:
    #    constraint = split_multiple_designations_form_query(designation)
    # elif designation.find(" ") >= 0:
    #    constraint = ' Designation like "%' + designation.replace(' ', '%') + '%" '
    else:
        constraint = ' Designation like "%' + designation + '%" '
    return constraint

def get_applicant_ids_query_as_per_skill(skills):
    #print(skills)
    #print(skills_exp)
    skill_set = skills.split("/")
    query = 'select distinct ApplicantID from recruit.candidate_skill_exp where '
    count = 0
    for skill in skill_set:
        if count > 0:
            skill = skill[1:]
        count = count + 1
        query = query + 'Skill like "%'+skill+'%" or '
    query = query[:query.rfind("or")] + ";"
    return query

def filter_applicant_ids_as_per_skill_exp(skills_exp):
    min_exp = skills_exp[:skills_exp.find('-')]
    if skills_exp.find("above") < 0:
        max_exp = skills_exp[skills_exp.find('-') + 1:]
        query = 'select distinct ApplicantID from recruit.candidate_skill_exp where  ' \
                     'Experience >= CAST("' + min_exp + '" AS DECIMAL) and Experience <= CAST("' + max_exp + '" AS DECIMAL);'
    else:
        query = 'select distinct ApplicantID from recruit.candidate_skill_exp where  ' \
                'Experience >= CAST("' + min_exp + '" AS DECIMAL);'
    return query

def get_filter_query(post_name, age, preferences, min_degree, max_degree, specialisation, percentage,
                     designation,  total_experience): #responsibilities,


    query = 'SELECT distinct ApplicantID FROM candidates where '
    if post_name != "select":
        post_name_constraint = ' PostName = "' + post_name + '" '
        query = query + post_name_constraint

    age_constraint = fetch_age_constraint(age)
    if age_constraint != 'select' and age_constraint != '':
        query = query + 'and' + age_constraint

    if preferences != "select":
        if preferences != "Thiruvananthapuram (TVM)":
            preferences_constraint = ' Preferences like "%' + preferences + '%" '
        else:
            preferences_constraint = ' Preferences like "%T%V%M%" '
        query = query + 'and' + preferences_constraint

    if min_degree != "select":
        min_degree_constraint = fetch_degree_constraint(min_degree)
        if min_degree_constraint != '':
            query = query + 'and' + min_degree_constraint

    if max_degree != "select":
        max_degree_constraint = fetch_degree_constraint(max_degree)
        if max_degree_constraint != '':
            query = query + 'and' + max_degree_constraint

    if specialisation[0] != "select":
        specialisation_constraint = combine_multiple_spec_constraints(specialisation)
        if specialisation_constraint != '':
            query = query + ' and ' + specialisation_constraint

    if percentage[0] != "select":
        percentage_constraint = combine_multiple_percent_constraints(percentage)
        if percentage_constraint != '':
            query = query + ' and ' + percentage_constraint

    if designation[0] != "select":  # convert to multiple
        # designation_constraint = fetch_designation_constraint(designation)
        designation_constraint = combine_multiple_designation_constraint(designation)
        if designation_constraint != '':
            query = query + ' and ' + designation_constraint

    #if responsibilities != 'select':
    #    query = query + 'and' + 'Responsibilities ="' + responsibilities + '" '

    if total_experience != 'select':
        exp_constraint = combine_multiple_totl_exp_constraint(total_experience)
        if exp_constraint != '':
            query = query + ' and ' + exp_constraint
    query = query + ';'
    return query


def combine_multiple_totl_exp_constraint(exp_list):
    if len(exp_list) == 1:
        return fetch_exp_constraint(exp_list[0])
    else:
        constraint = '( '
        # print(designation)
        for exp in exp_list:
            # print(design)
            constraint = constraint + fetch_exp_constraint(exp) + ' or '
        constraint = constraint.strip(" or ")
        constraint = constraint + ' ) '
        return constraint


def combine_multiple_designation_constraint(designation):
    if len(designation) == 1:
        return fetch_designation_constraint(designation[0])
    else:
        constraint = '( '
        # print(designation)
        for design in designation:
            # print(design)
            constraint = constraint + fetch_designation_constraint(design) + ' or '
        constraint = constraint.strip(" or ")
        constraint = constraint + ' ) '
        return constraint


def get_skill_exp_patterns(min_exp, max_exp):
    patt_list = []
    end_ind = max_exp * 12 + 1
    if min_exp == 0:
        strt_ind = 1
    else:
        strt_ind = 12 * min_exp
    for i in range(strt_ind, end_ind):
        patt_list.append(i)
    return patt_list


def fetch_skill_exp_constraint(skills_exp): #in-progress
    #Just add for above case
    #0-3
    #year_ind = skills_exp.find('years')
    #skills_exp = skills_exp[:year_ind]
    if skills_exp.find('-') >= 0:
        ind = skills_exp.find('-')
        if skills_exp.find('above') < 0:
            patterns = get_skill_exp_patterns(int(skills_exp[:ind]), int(skills_exp[ind + 1:]))
            constraint = '('
            for patt in patterns:
                constraint = constraint + 'Skills like "%- ' + str(patt) + '%" or '
            constraint = constraint.strip("or ")
            constraint = constraint + ')'
        else:
            print("Only one experience field")

    else:  # no exp
        constraint = 'Skills like "%- 0%"'
    return constraint


def combine_multiple_skill_constraints(skills):
    if len(skills) == 1:
        return fetch_skill_constraint(skills[0])
    else:
        constraint = '( '
        for skill in skills:
            constraint = constraint + fetch_skill_constraint(skill) + ' or '
        constraint = constraint.strip(" or ")
        constraint = constraint + ' ) '
        return constraint


def combine_multiple_spec_constraints(specialisation):
    constraint = ''
    if len(specialisation) == 1:
        # print("here")
        # print(specialisation)
        return fetch_specialisation_constraint(specialisation)
    else:
        constraint = '( '
        for spec in specialisation:
            sub_constraint = fetch_specialisation_constraint(spec)
            if sub_constraint != '':
                constraint = constraint + fetch_specialisation_constraint(spec) + ' or '
            else:
                continue
        constraint = constraint.strip(" or ")
        constraint = constraint + ' ) '
        return constraint


def combine_multiple_percent_constraints(percentage):
    if len(percentage) == 1:
        print("not here")
        return fetch_percent_constraint(percentage[0])
    else:
        const_list = []
        for percent_val in percentage:
            const_list.append(fetch_percent_constraint(percent_val))
            #constraint = constraint + '(' + fetch_percent_constraint(percent_val) + ') or( '
        comb_constraint = '('
        for constraint in const_list:
            comb_constraint = comb_constraint + '(' + constraint + ') or '
        comb_constraint = comb_constraint[:comb_constraint.rfind("or")]
        comb_constraint = comb_constraint + ' ) '
        print("percent constraint"+comb_constraint)
        return comb_constraint


def combine_multiple_skill_exp_constraints(skill_exp):
    if len(skill_exp) == 1:
        return fetch_skill_exp_constraint(skill_exp[0])
    else:
        constraint = '( '
        for exp_val in skill_exp:
            constraint = constraint + fetch_skill_exp_constraint(exp_val) + ' or '
        constraint = constraint.strip(" or ")
        constraint = constraint + ' ) '
        return constraint


def fetch_skill_constraint(skill):
    if skill.find("Java/") >= 0:
        return 'Skills like "%Java %" or Skills like "%oop%" or Skills like "%object oriented programming%"'
    elif skill.find("CSS") >= 0:
        return 'Skills like "%CSS%"'
    elif skill == "C":
        return 'Skills like "%C %"'
    elif skill == "C++":
        return 'Skills like "%C++ %"'
    elif skill.find("HTML") >= 0:
        return 'Skills like "%HTML%"'
    elif skill.find("Hibernate") >= 0:
        return 'Skills like "%Hibernate%"'
    elif skill.find("PHP") >= 0:
        return 'Skills like "%PHP%"'
    elif skill.find("Data Structure") >= 0:
        return 'Skills like "%Data Structure%"'
    elif skill.find("SQL") >= 0:
        return 'Skills like "%SQL%"'
    elif skill.find("Android") >= 0:
        return 'Skills like "%Android%"'
    elif skill.find("IoT") >= 0:
        return 'Skills like "%IoT%" or Skills like "%Internet of Things%"'
    elif skill.find("(ML)") >= 0:
        return 'Skills like "%ML)%" or Skills like "%Machine Learning%")'
    elif skill.find("FPGA") >= 0:
        return 'Skills like "%FPGA%" or Skills like "%Microcontroller%"'
    else:
        if skill.find("/") >=0:
            skill_constraint = ''
            skill_col = skill.split("/")
            for skill in skill_col:
                skill_constraint = skill_constraint + 'Skills like "%' + skill + '%" or'
            skill_constraint = skill_constraint.strip("or")
        return skill_constraint


def get_year_exp_pattern_list(exp):
    patt_list = []
    if exp.find('-') >= 0:
        ind = exp.find('-')
        min_exp = int(exp[:ind])
        max_exp = int(exp[ind + 1:])
    patt_list.append(str(min_exp) + " year(s) 0 month(s) 0 day(s)")
    for i in range(min_exp, max_exp):
        patt_list.append(str(i) + " year(s)%")
    patt_list.append(str(max_exp) + " year(s) 0 month(s) 0 day(s)")
    return patt_list


def fetch_exp_constraint(total_experience):
    total_experience = total_experience.replace("year(s)", "")
    constraint = ''
    if total_experience == 'No Experience':
        constraint = constraint + ' QualifyingExperience = "0 year(s) 0 month(s) 0 day(s)"'
    elif total_experience.find("-") >= 0:
        pattern_list = get_year_exp_pattern_list(total_experience)
        count = 0
        for patt in pattern_list:
            if count == 0:
                count = count + 1
                constraint = constraint + ' QualifyingExperience != "' + patt + '" '
            else:
                if count == 1:
                    count = count + 1
                    constraint = constraint + ' and ((QualifyingExperience like "' + patt + '") or '
                else:
                    constraint = constraint + ' (QualifyingExperience like "' + patt + '") or '
        constraint = constraint.strip("or ")
        constraint = constraint + ')'
    else:  # and above case
        ind = total_experience.find("year")
        exp = total_experience[:ind]
        constraint = constraint + ' QualifyingExperience like "' + exp + ' year(s)%" and QualifyingExperience != "' + exp + 'year(s) 0 month(s) 0 day(s)"'
    return constraint
