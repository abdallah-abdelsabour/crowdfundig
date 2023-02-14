import re
MAILRE=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
USERNAMERE="^[a-zA-Z0-9_.-]+$"
PASSRE="^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"
PHONERE="^(?:\+20|0)?1[0125]\d{8}$"

# validator fun
def validator(type,value):
    if type=="name":
        if re.fullmatch(USERNAMERE , value):
            return True
    elif type =="email":
        if re.fullmatch(MAILRE , value):
            return True
    elif type =="password":
        if re.fullmatch(PASSRE , value):
            return True
    elif type == "phone":
        if re.fullmatch(PHONERE , value):
            return True


    return False




def auth_user(email,password):
    valid_email=''
    valid_password=''

    userdata = open("users.txt" , "r")
    all_users ="".join(userdata.readlines()).split("\n")
    for user in all_users:
        if len(user ) < 2  :
            return False
        # print(user.split(":")[2],end="\n")
        # print(user.split(":")[3])
        elif email == user.split(":")[2] and password == user.split(":")[3]:
            return True

    return False



def save_user(f_name,l_name , email ,passwrd , phone):
    user_data  = open("users.txt" , "a")
    user_data.write(f"{f_name}:{l_name}:{email}:{phone}:{passwrd}\n")
    user_data.close()




# login
def login():
    print("________________________LOGIN______________________________")
    while True:
        email = input("Enter your Email :")
        if email =="exit":
            break

        password = input("Enter your password :")
        if auth_user(email ,password):
            print("login succefully ")
            break



        else:
            print("Errror: uncorrect Email or Password try again [press exit to Exit]")




# authin






def signUp():
    valid_first_name= ''
    valid_last_name=''
    valid_password=''
    valid_password2=''

    valid_email=''
    valid_phone=''


    # get inputs from user
    while True:

        print("welcome")
        # valid name
        while len(valid_first_name ) < 1:
            name =input("please Enter your name :")
            if validator("name" , name):
                valid_first_name=name
                break
            else:
                print("wrong name formate try again ")
                continue
         # validate last name
        while len(valid_last_name) < 1 :
            l_name =input("Enter your last Name :")
            if validator("name" , l_name):
                valid_last_name = l_name
            else:
                 print("wronge last name formate plase try again ")

        # validate Email
        while len(valid_email) < 1 :
            email = input("please enter valid email :")
            if validator("email", email):
                valid_email = email
            else:
                print("sorry wrong email fprmate please try again ")
        while len(valid_password) < 1 :
            password = input("please Enter valid password :")
            if validator("password" , password):
                valid_password = password
            else:
                print("wrong password formate please try again ")


        while len(valid_password2) < 1:
            password = input("confirm password :")
            if password == valid_password :
                valid_password2 = password
            else:
                print("please Enter the Same password you Enter pefore ")





        while len(valid_phone ) < 1:
            phone = input("please Enter phone number")
            if validator("phone", phone):
                valid_phone=phone
            else:
                print("wrong phone formate ")

        save_user(valid_first_name, valid_last_name,valid_email,valid_password ,valid_phone)
        print("signup succefully you can login now  ")
        break







