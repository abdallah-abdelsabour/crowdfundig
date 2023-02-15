
from  user import  validator
from datetime import datetime
from time import time


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'






def get_user_projects(user_Id):
    projects  = open("projects.txt" , "r")
    all_projects  = "".join(projects.readlines()).split("\n")
    projects.close()
    user_projects = [pro.split("|")   for pro in all_projects if pro.split("|")[0]==user_Id ]
    return user_projects


def get_all_project():
    projects = open("projects.txt", "r")
    all_projects = "".join(projects.readlines()).split("\n")
    projects.close()
    projects = [pro.split("|") for pro in all_projects if len(pro ) > 1  ]
    return projects


def list_projects():
    projects  = get_all_project()
    print("ALL-_____________________________projects _____________________________")
    for indx , pro in enumerate(projects):
        print(f" {indx+1 }-{pro[2]}")


# sort project function
def sort_projs(pro):
    return int(pro[1])


def update(projects):
    projects.sort(key=sort_projs)
    projects_file = open("projects.txt", "w")
    for pro in projects :
        projects_file.write(f"{pro[0]}|{pro[1]}|{pro[2]}|{pro[3]}|{pro[4]}|{pro[5]}|{pro[6]}\n")

    projects_file.close()



def delete_project_by_id(id):
    all_projects = get_all_project()
    # return new projects to update
    updated_opjs = [pro for  pro in all_projects if  pro[1] != id]
    update(updated_opjs)



def save_project(user_id,project_id,valid_title,valid_details,valid_total_target,valid_start,valid_end):
    # projects = open("projects.txt", "a")
    # projects.write(f"\n{user_id}|{project_id}|{valid_title}|{valid_details}|{valid_total_target}|{valid_start}|{valid_end}")
    # projects.close()
    all_project = get_all_project()
    new_project =[user_id, project_id, valid_title  , valid_details , valid_total_target , valid_start  , valid_end]
    all_project.append(new_project)
    update(all_project)




def delete_project(user_id):
   user_projects =  get_user_projects(user_id)
   while True:
       if len(user_projects) < 1 :
           print("you dont have projects please add one first")
           return None

       # print project to user
       for i in range( len(user_projects)):
           print(f"{i+1} -{user_projects[i][2]}")

       number =  input("Enter project number you want to delete:")
       try:
          num=int(number) - 1
       except Exception as e:
          print(f"{e}")
          continue

       if num not in range(len(user_projects)):
           print("not valid project number please enter valid number ")
           continue
       else:

           delete_project_by_id(user_projects[num][1])
           print(" project deleted succefully ")
           break


def get_project_by_id(id):
    all_projs = get_all_project()
    for pro in all_projs :
        if pro[1] ==id:
            return pro
    return None


def create_project(user_id,project_id):
    """ take data from users"""
    valid_title=''
    valid_details=''
    valid_total_target=''
    valid_start=''
    valid_end=''


    while True:

        while len(valid_title) < 1:
            title = input("project title :")
            if validator("name",title):
                valid_title = title
            else:
                print("Error title not valid try again :")

        while len(valid_details) < 1 :
            details = input("Enter Details :")
            if validator("description" , details):
                valid_details = details
            else:
                print("ERROR not valid descriptiom must be at least 25 charcter")

        while len(valid_total_target) < 1 :
            total_target = input("Enter amount you target :")
            if validator("amount"  , total_target):
                valid_total_target = total_target
            else:
                print("Error invalid amount mony ")

        while not valid_start  :
            start_data = input("Enter start data for your project:in formate 'YYYY-M-D' : ")
            if validator("date" , start_data):
                if datetime.now() > datetime.strptime(start_data ,'%Y-%m-%d'):
                    print("you have to pick incomoing data not past")
                    continue
                else:
                    valid_start = datetime.strptime(start_data ,'%Y-%m-%d')
            else:
                print("Error formate must be 'YYYY-M-D :")

        while not valid_end  :
            end_data = input("Enter End data for your project:in formate 'YYYY-M-D' :")
            if validator("date" , end_data):
                end_data = datetime.strptime(end_data, '%Y-%m-%d')
                if end_data < valid_start :

                    print("Erorr : End Data must be after Start data")
                    continue
                else :
                    valid_end = end_data
            else:
                print("wrong data formate ")




        print("project created succefully  ")

        save_project(user_id,project_id, valid_title,valid_details,valid_total_target,valid_start,valid_end)
        break





def select_project(projs):
    for indx , pro in enumerate(projs):
        print(f"{indx +1 }-{pro[2]}")
    try:
        num = input("Enter Project Number :")
        num  = int(num) - 1
    except Exception as e :
        print("uvalid number please select from above ")
        return None
    else:
        if num not in range(len(projs) ) :
            print("out range number ")
            return None
        else:
            return num















def edit_project(user_id):
    while True:
        user_prjects = get_user_projects(user_id)
        pro_num = select_project(user_prjects)
        if pro_num ==0  or pro_num :
            project_id = user_prjects[pro_num][1]
            delete_project_by_id(project_id)
            create_project(user_id,project_id)

        else:
            print("not valid project number please try again")
            continue






def get_project_in_range(start, end):


    all_projects = get_all_project()
    return [ pro for pro in all_projects if ( datetime.strptime(pro[5],'%Y-%m-%d %H:%M:%S')  >= start and datetime.strptime(pro[6],'%Y-%m-%d %H:%M:%S') <= end)]






def search_by_date():
    valid_start_date=''
    valid_end_date=''


    while True:

        while not valid_start_date :
            start_date=input("Enter start Date you want to search in in formate 'YYYY-M-D':")
            if validator("date", start_date):
                valid_start_date = datetime.strptime(start_date, '%Y-%m-%d')



            else:
                print("invalid date formate it must be like 'YYYY-M-D'")
                continue

        while not valid_end_date :
            end_date = input("Enter End Date you want to search in in formate 'YYYY-M-D':")
            if validator("date" , end_date):
                valid_end_date = datetime.strptime(end_date ,'%Y-%m-%d' )

            else:
                print(  "invalid date formate it must be like 'YYYY-M-D'")
                continue


        all_projects = get_project_in_range(valid_start_date , valid_end_date)

        if not all_projects :
            print("no projects in selected range try another range ")
            break
        else:
            for pro in all_projects:

                print(f"{pro[2]}-----------------start date:{pro[5]}|end:{pro[6]}")
        break