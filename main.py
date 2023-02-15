



# login function

from user import *
from  project import  *
from time import time


def start():
    user_id=False
    print("____________hello welcom to the Cowfunding__________________ ")
    while not user_id:
        print("        chose from the following options \n"
              "1-login          2- signUp\n"
              "3- Exit")
        choise=(input(" >>> "))
        match choise :
             case "1" :
                 user_id=login()

             case "2" :
                 signUp()
             case "3":
                 exit()

             case '':
                 continue
#   project steps

    while True:
        print("        chose from the following options \n"
              "1-create project           2- list all projets\n"
              "3- Delete                    4-edit your  project\n"
              "5- search ")
        choise = input("Enter your choise :")

        match choise:
            case "1" :
                create_project(user_id,round(time()))
            case '2' :
                list_projects()
            case "3" :
                delete_project(user_id)
            case '4' :
                edit_project(user_id)
            case "5" :
                search_by_date()



















# print(login("waledf@mail.com","Ahgfhgfhg$#$%#65"))




# start point
start()







