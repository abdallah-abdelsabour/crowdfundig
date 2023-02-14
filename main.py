



# login function

from user import *



def start():

    print("____________hello welcom to the Cowfunding__________________ ")
    while True:
        print("        chose from the following options \n"
              "1-login          2- signUp\n"
              "3- Exit")
        choise=(int(input(" >>> ")))
        match choise :
             case 1 :
                 login()

             case 2 :
                 signUp()
             case 3:
                 exit()

             case '':
                 continue













# print(login("waledf@mail.com","Ahgfhgfhg$#$%#65"))




# start point
start()







