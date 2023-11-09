# Here we import re,datetime modules

import re
import datetime

# Here we create multiple functions for validation.

def cloth_name_validation(string_name):
    name_pattern = re.match(r"^[A-Za-z]{1}[A-Za-z\s-]*(?:T-[A-Za-z\s-]*)?$",string_name)
    if len(string_name) == 0 or string_name.isspace():
        raise Exception ("\nCloth Name should not be empty.")
    elif len(string_name)<=4:
        raise Exception ("\nPlease Enter the proper Cloth Name.")
    elif not name_pattern:
        raise Exception ("\nCloth Name must be a Alphabets.")
    
def user_name_validation(string_name):
    
    if len(string_name) == 0 or string_name.isspace():
        raise Exception("\nUser Name should not be empty.")
    elif not string_name.isalnum():
        raise Exception("\nUser Name must be a Alphabets and Numbers.")
    
    
def name_validation(string_name):
    if len(string_name) == 0 or string_name.isspace():
        raise Exception ("\nName should not be empty.")
    elif not string_name.isalpha():
        raise Exception ("\nName must be a Alphabets.")
    elif len(string_name)<=2:
        raise Exception ("\nPlease Enter the proper Name.")


def customer_phone_number_validation(string_name):
    ph_num_pattern = re.match("^[6-9]{1}[0-9]{9}$",string_name)
    if string_name.isalpha():
        raise ValueError ("\nCustomer Phone Number must be in digits (or) numbers.")
    elif len(string_name) != 10:
        raise Exception ("\nCustomer Phone Number must be 10 digits")
    elif not ph_num_pattern:
        raise Exception ("\nCustomer Phone Number must be starts with 6-9 and 10 digits(Eg:6379276534)")
    count = 0
    for x in string_name:
        if int(x)==0:
            count +=1
    if count >= 8:
        raise Exception ("\nPhone Number must not be contain more than or equal to 8 0's")

def customer_email_id_validation(user_string):
    
    email_pattern = re.search(r"^[a-z0-9]+([\._]?[a-z0-9]+)*@[a-z]{5}+\.[a-z]{2,3}$",user_string)
    if len(user_string.split("@")[0]) < 6 or len(user_string.split("@")[0]) > 15:
        raise Exception ("\nEmail should be in the length of 6 to 15")
    elif not email_pattern:
        raise Exception ("\nEmail should be in the correct pattern (Eg:dnagaraj3828@gamil.com)")

def customer_password_validation(user_string):
    password_pattern = re.search(r"^[A-Z]{1}[a-z0-9]+[a-z0-9\W_]", user_string)
    if len(user_string) < 3 or len(user_string) > 20:
        raise Exception ("\nPassword should be in the length of 3 to 20")
    elif user_string.endswith(" "):
        raise Exception ("\npassword should not endswith space")
    elif not password_pattern:
        raise Exception ("\npassword should be starts with Capital Letter Eg:Nagaraj@007.")

def card_number_validation(string_name):
    card_pattern = re.search(r"^\d{4}-\d{4}-\d{4}-\d{4}$",string_name)
    if len(string_name) == 0 or string_name.isspace():
        raise Exception ("\nCard Number should not be empty.")
    elif not card_pattern:
        raise Exception ("\nCard Number should 16 digits and in the correct Format (Eg:1234-5678-9012-3456)")

def is_valid_date(date_string):
    try:
        datetime.datetime.strptime(date_string,"%m/%Y")
        return True
    except ValueError:
        return False

def card_expire_date_validation(string_name):
    if not is_valid_date(string_name):
        raise Exception ("\nExpire Date should be in this format (Eg:12/2023)")
    

def net_id_validation(string_name):
    net_id_pattern = re.search(r"^[a-z]{3,10}+[0-9]{2,6}$",string_name)
    if len(string_name) < 5 or len(string_name) > 20:
        raise Exception ("\nUser Id should be in the length of 5 to 20 charcters.")
    elif not net_id_pattern:
        raise Exception ("\nUser Id should be 3 small character and atleast 2 numbers and in this Format (Eg:john123)")

def ubi_id_validation(string_name):
    ubi_id_pattern = re.search(r"^[a-z0-9]{10,15}+@[a-z]{3,5}",string_name)
    if not ubi_id_pattern:
        raise Exception ("\nUBI ID must be in the length of 10 to 15 and in this format (Eg:ramkumar1234@ybl)")



def user_password_validation(user_string):
    password_pattern = re.search(r"^[A-Z]{1}[a-z0-9]+[a-z0-9\W_]", user_string)
    if len(user_string) < 3 or len(user_string) > 20:
        raise Exception ("\nPassword should be in the length of 3 to 20")
    elif user_string.endswith(" "):
        raise Exception ("\npassword should not endswith space")
    elif not password_pattern:
        raise Exception ("\npassword should be starts with Capital Letter Eg:Nagaraj@007.")
