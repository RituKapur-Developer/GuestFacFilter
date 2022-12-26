import dao

def remove_extra_last_hyphen_space(skill_val):
    flag = 0
    if skill_val.rfind('-') >= 0:
        ind = skill_val.rfind('-')
        skill_last_comp = skill_val[ind+1:]
        if len(skill_last_comp.strip()) == 0:
            flag = 1
    if flag == 1:
        skill_val = skill_val[:ind].strip()
    return skill_val

def clean_cmpl_skills_str(skills_str):
    if skills_str.find(", AVR, ARM") >= 0:
        skills_str = skills_str.replace(", AVR, ARM", " - AVR - ARM")
    if skills_str.find("`") >= 0:
        skills_str = skills_str.replace("`", "")
    if skills_str.find("Cellular (3G, 4G)") >= 0:
        skills_str = skills_str.replace("Cellular (3G, 4G)","Cellular (3G and 4G)")
    if skills_str.find("Cellular (3G ") >= 0:
        skills_str = skills_str.replace("Cellular (3G ","Cellular 3G ")
    if skills_str.find("Cellular 4G) ") >= 0:
        skills_str = skills_str.replace("Cellular 4G) ","Cellular 4G ")
    if skills_str.find("0.") >= 0:
        skills_str = skills_str.replace("0.", "")
    if skills_str.find("+") >= 0:
        skills_str = skills_str.replace("+", "")
    return skills_str

def clean_skill_exp(exp):
    if exp.find('ne') >= 0:
        exp = '1'
    if exp.find('ah') >= 0:
        exp = exp.replace('ah', '')
    if exp.find('x') >= 0:
        exp = exp.replace('x', '')
    if exp.find('th') >= 0:
        exp = exp[:exp.find('th')]
    if exp.find('1/2') >= 0:
        exp = '6'
    if exp.find('m') >= 0:
        if exp.find('mo') >= 0:
            exp = exp.replace('mo', 'm')
        if exp.find('mn') >= 0:
            exp = exp.replace('mn', 'm')
        if exp.find('+') >= 0:
            exp = exp.replace('+', 'm')
        exp = exp.replace('m', '')
        exp = exp.strip()
    elif exp.find('y') >= 0:
        if exp.find('yr') >= 0:
            exp = exp.replace('yr', 'y')
        exp = exp.replace('y', '')
        exp = str(int(exp.strip()) * 12)
    elif exp.find('.') >= 0:
        if exp.find('.') == 0:
            exp = exp[1:]
        else:
            yr_months = exp.split('.')
            try:
                if yr_months[0] == ' ':
                    yr_months[0] = 0
                exp = str(int(yr_months[0]) * 12 + int(yr_months[1]))
            except:
                print('. case')
                print(yr_months)

    else:
        exp = exp.strip().lstrip()
    # checking finally
    exp = exp.strip().lstrip()
    if exp.strip().find(' ') >= 0:
        yr_months = exp.split(" ")
        if yr_months[0] == ' ' or yr_months[0] == '':
            yr_months[0] = 0
        try:
            exp = str(int(yr_months[0]) * 12 + int(yr_months[1]))
        except:
            print(exp)
    # converting finally to int
    try:
        exp = int(exp)
    except:
        print(exp)
        exp = 0
    return exp

def get_skill_nd_exp_from_str(skills_str):
    skill_exp_map = {}
    clean_skills_str = clean_cmpl_skills_str(skills_str)
    skills = clean_skills_str.split(",")
    for skill in skills:
        if len(skill) > 1:
            # valid skill with experience
            ind = skill.rfind('-')
            skill_val = skill[:ind - 1].strip().lstrip()
            skill_val = remove_extra_last_hyphen_space(skill_val)
            exp = clean_skill_exp(skill[ind + 1:].strip(',').lower().lstrip())
            if exp > 0:
                skill_exp_map[skill_val] = exp
    return skill_exp_map


def normalize_skill():
    cand_skill_map = {}
    print("fetching data")
    skill_map = dao.get_applicant_skill_map()
    print("normalizing")
    for app_id in skill_map.keys():
        skills = skill_map[app_id]
        skill_exp_map = get_skill_nd_exp_from_str(skills)
        cand_skill_map[app_id] = skill_exp_map
    print("storing normalized data")
    dao.insert_norm_cand_skill_exp(cand_skill_map)
    return

