def get_html_code_for_skills(html_code, field_value_list):
    # print(field_value_list)
    skills_left = []
    skill_set = get_unique_values_list(field_value_list)
    skill_set.sort()

    css_str = 'CSS'
    java_str = 'Java'
    html_str = 'HTML'
    hibernate_str = 'Hibernate'
    php_str = 'PHP'
    sql_str = 'SQL/ Microsoft SQL Server 2008 /2012/2018'
    android_str = 'Android/ Hybrid Mobile application'
    data_struct = 'Data Structures'
    spring_str = 'Spring'
    net_str = 'ASP.NET/ .NET'
    comnet_str = 'Computer Networks/ Wireless Communication'
    aws_str = 'AWS/ Web services/ Cloud Computing'
    python_str = 'Python Frameworks'
    pro_str = 'Project Management/ Project Tracking/ Project Delivery/ Monthly MIS/ Jenkins'
    csharp_str = 'C#/ C/ C++'
    machlear_str = 'Machine Learning (ML)/ Machine Learning (AI)/ Hardware Accelerators'
    exec_str = 'Excellent verbal and written communication/ Ability to inspire and convince others/ Presentation skills'
    soft_str = 'Software development Methodology/ Software Development Life Cycle (SDLC)/ Automation/ MVC/ DevOps tools-CICD/ Agile Methodology/ ' \
               'Performance Testing/ Quality Assurance (QA)'
    webapp_str = 'Web applications/ RESTFUL API/ NodeJS/ Client Side Technologies/ Frontend Development'
    crypto_str = 'Cryptography/ Cyber Security '
    augment_str = 'Augmented Reality/ virtual reality/ 3D Technology'
    image_str = 'Image Processing/ Matlab/ PCB Design'
    signal_str = 'Signal Integrity/Power Integrity analysis tools'
    admin_str = 'Administration/ Database Administration/ System Administration'
    proddev_str = 'Electronics Product Development Cycle/ VLSI/ Communication circuits/ Hardware Design/ Analog and Digital Circuits/ Embedded Systems/ ' \
                  'Verilog HDL coding and Verification/ Microcontroller Programming 8051 ARM/ Microprocessor Assembling Programming/ FPGA tools Xilinx/ FPGA Verilog Programming/ RTOS'
    robotic_str = 'mechatronic/ robotic components'

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

        elif skill.find("sql") >= 0:
            if skill != "sql":
                sql_str = sql_str + "/ " + i

        elif skill.find("data structure") >= 0:
            if skill != "data structure" and skill != "data structures":
                data_struct = data_struct + "/ " + i

        elif skill.find("android") >= 0 or skill.find("hybrid mobile application") >= 0:
            if skill != "android" and skill != "hybrid mobile application":
                android_str = android_str + "/ " + i

        elif skill.find(".net") >= 0:
            if skill != ".net":
                net_str = net_str + "/ " + i

        elif skill.find("networks") >= 0 or skill.find("communication") >= 0 or skill.find("3g") >= 0 or skill.find("4g") >= 0 or skill.find("5g") >= 0 or skill.find("wire") >= 0:
            if skill != "computer networks" and skill != "wireless communication":
                comnet_str = comnet_str + "/ " + i

        elif skill.find("aws") >= 0 or skill.find("web services") >= 0 or skill.find("cloud computing") >= 0:
            if skill != "aws" and skill != "web services" and skill != "cloud Computing":
                aws_str = aws_str + "/ " + i

        elif skill.find("python") >= 0:
            if skill != "python":
                python_str = python_str + "/ " + i

        elif skill.find("project management") >= 0 or skill.find("project delivery") >= 0 or skill.find("event management") >= 0 or skill.find("jenkins") >= 0:
            if skill != "project management" and skill != "project delivery" and skill != "event management" and skill !="jenkins":
                pro_str = pro_str + "/ " + i

        elif skill == "c#" or skill == "c" or skill == "c++":
            continue

        elif skill.find("machine learning") >= 0 or skill.find("artificial intelligence") >= 0 or skill == "ml" or skill == "ai" or skill.find("hardware") >= 0 or\
              skill.find("accelerators") >= 0:
            if skill != "machine learning (ml)" and skill != "artificial intelligence(ai)" and skill != "hardware accelerators" and skill !="ml" and skill !="ai":
                machlear_str = machlear_str + "/ " + i

        elif skill.find("excellent verbal and written communication") >= 0 or skill.find("ability to inspire and convince others") >= 0:
            if skill != "excellent verbal and written communication" and skill != "ability to inspire and convince others":
                exec_str = exec_str + "/ " + i

        elif skill.find("software") >= 0 or skill.find("development") >= 0 or skill.find("techno") >= 0  or skill.find("nodejs") >= 0 or skill.find("app") >= 0 or \
            skill.find("software development life cycle") >= 0 or skill == ("sdlc") or  skill.find("Automation") >= 0 or skill.find("MVC") >= 0 or skill.find("DevOps") >= 0 or \
                skill.find("angular") >= 0 or skill.find("cicd") >= 0 or skill.find("ci/cd") >= 0  or skill.find("performance testing") >= 0 or skill.find("quality assurance") >= 0  \
                or skill == "qa" or skill.find("restful api") >= 0 or skill.find("eclipse") >=0:
            if skill != "software development methodology" and skill != "Software Development Life Cycle (SDLC)" and skill !="SDLC" and skill != "Automation" and skill != "MVC" and \
                    skill != "DevOps tools-CICD" and skill != "angular" and skill != "performance testing" and skill != "quality assurance (qa)" and skill != "restful api":
                soft_str = soft_str + "/ " + i

       elif skill.find("cryptography") >= 0 or skill.find("cyber security") >= 0:
            if skill != "cryptography" and skill != "cyber security":
                crypto_str = crypto_str + "/ " + i

        elif skill.find("augmented reality") >= 0 or skill.find("virtual reality") >= 0) or skill.find("3d") >= 0:
            if skill != "augmented reality" and skill != "virtual reality":
                augment_str = augment_str + "/ " + i

        elif skill.find("image processing") >= 0 or skill.find("matlab") >= 0 or skill.find("pcb design") >= 0:
            if skill != "image processing" and skill != "matlab" and skill != "pcb design":
                image_str = image_str + "/ " + i

        elif (skill.find("signal integrity") >= 0 or skill.find("power integrity analysis tools") >= 0):
            if skill != "signal integrity" and skill != "power integrity analysis tools":
                signal_str = signal_str + "/ " + i

        elif (skill.find("administration") >= 0 or skill.find("database administration") >= 0 or skill.find("system administration") >= 0):
            if skill != "administration" and skill != "database administration" and skill != "system administration":
                admin_str = admin_str + "/ " + i


        elif (skill.find("electronics") >= 0 or skill.find("vlsi") >= 0 or skill.find("circuits") >= 0 or skill.find("hardware") >= 0 \
              or skill.find("analog") >= 0 or skill.find("embeded") >= 0 or skill.find("verilog") >= 0 or skill.find("microcontroller") >= 0 \
              or skill.find("microprocessor") >= 0 or skill.find("arm") >= 0 or skill.find("rtos") >=0 or skill.find("fpga tools xilinx") >= 0\
              or skill.find("fpga verilog programming") >= 0):
            if skill != "electronics product development cycle" and skill != "vlsi" and skill != "communication circuits" and skill != "hardware design" and skill !="analog" and\
                skill !="embeded" and skill !="verilog" and skill != "microcontroller programming 8051 arm" and skill != 'microprocessor assembling programming' and\
                skill != "fpga tools xilinx" and skill != "fpga verilog programming":
                proddev_str = proddev_str + "/ " + i

        elif (skill.find("mechatronic") >= 0 or skill.find("robotic") >= 0):
            if skill != "mechatronic" and skill != "robotic components":
                robotic_str = robotic_str + "/ " + i
        for i in skill_set:
            skill = i.lower().strip()
        if skill.find("java") >= 0 or skill.find("oop") >= 0 or skill.find("object oriented programming") >= 0:
            if
        skill != 'java' and skill != 'javascript':
        java_str = java_str + "/ " + i
        else:
        skills_left.append(skill)
        html_code = html_code + '<option value="select" selected>Select</option>' \
                        '<option value="' + java_str + '">' + java_str + '</option>' + '<option value="' + css_str + '">' + css_str + \
            '</option>' + '<option value="' + html_str + '">' + html_str + '</option>' + '<option value="' + hibernate_str + '">' + hibernate_str + \
            '</option>' + '<option value="' + php_str + '">' + php_str + '</option>' + '<option value="' + data_struct + '">' + data_struct + \
            '</option>' + '<option value="' + sql_str + '">' + sql_str + '</option>' + '<option value="' + android_str + '">' + android_str + \
            '<option value="' + net_str + '">' + net_str + '</option>' + '<option value="' + comnet_str + '">' + comnet_str + '</option>' + \
            '<option value="' + aws_str + '">' + aws_str + '</option>' + '<option value="' + python_str + '">' + python_str + '</option>' + \
            '<option value="' + pro_str + '">' + pro_str + '</option>' + '<option value="' + csharp_str + '">' + csharp_str + '</option>' + \
            '<option value="' + machlear_str + '">' + machlear_str + '</option>' + '<option value="' + exec_str + '">' + exec_str + '</option>' + \
            '<option value="' + soft_str + '">' + soft_str + '</option>' + '<option value="' + webapp_str + '">' + webapp_str + '</option>' + \
            '<option value="' + crypto_str + '">' + crypto_str + '</option>' + '<option value="' + augment_str + '">' + augment_str + '</option>' + \
            '<option value="' + image_str + '">' + image_str + '</option>' + '<option value="' + signal_str + '">' + signal_str + '</option>' + \
            '<option value="' + admin_str + '">' + admin_str + '</option>' + '<option value="' + robotic_str + '">' + robotic_str + '</option>'