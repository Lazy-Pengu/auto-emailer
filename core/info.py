import datetime
import platform
import sys
import os

curr_date = datetime.datetime.now()
due_dates = {'[8]': [9]}
# EXAMPLE
# rent_due_date = datetime.datetime(int(curr_date.strftime('%Y')), (int(curr_date.strftime('%m')) + 1), 1)
# due_dates = {"Rent":rent_due_date}

msg_body_template = "[10]"
msg_ender = "[11]
email_list = {'[12]'}

file_id = '[13]'

def due_date_info():  
    msg_builder = ""
    for typ in due_dates:
        date = str(due_dates[typ].strftime('%x'))
        remaining_day = int(due_dates[typ].strftime('%j')) - int(curr_date.strftime('%j'))
        
        if remaining_day == [14]:
            msg_builder = "[15]"

    msg_builder = msg_builder + msg_ender
    return msg_builder

def print_email_list():
    print("Current Email List\n" +
          "------------------")
    for email in email_list:
        print("{} : {}".format(email, email_list[email]))
    print("all : ALL")
    
    sender_names = input("Enter name(s) separated by space: ").lower().split(' ')
    return sender_names;
    
def trigger(pause):
    if curr_date.strftime('%d') != '[16]':
        print("Not correct Date: ", curr_date.strftime('%x'))
        pause(1.5)
        sys.exit(1)
        
        
def file_path_builder(name, dir_name=None):
    return_list = []
    dir_div = '/'
    if platform.system() == 'Windows':
        dir_div = '\\'
    
    core_path = os.path.dirname(os.path.realpath("__file__"))
    if dir_name == None:
        file_temp = "{}{}{}".format(core_path, dir_div, name)
        return_list.append(file_temp)
        
        return return_list
    else:
        dir_temp = "{}{}{}{}".format(core_path, dir_div, dir_name, dir_div)
        file_temp = "{}{}".format(dir_temp, name)
        
        return_list.append(file_temp)
        return_list.append(dir_temp)
        return return_list