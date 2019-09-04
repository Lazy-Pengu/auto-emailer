import getpass
import os
import time

from info import print_email_list, trigger, email_list
from email_server import Emailer

clear = lambda: os.system('cls')
pause = lambda x: time.sleep(x)

def main():
    trigger(pause)
    
    emailer = Emailer()
    emailer.login(pause)

    sender_names = print_email_list()

    if 'all' in sender_names:
        sender_names = list(email_list.keys())

    accessed = False
    emails_sent = 0
    for name in sender_names:
        try:
            email_list[name]
        except:
            print("[{}] is not a valid name --- SKIPPING".format(name))
            pause(.5)
            continue
        
        msg = Emailer.msg_builder(name, accessed)
        
        print(msg)
        send = input("Send Email? [Y/n]: ")
        if(send == 'Y'):
            emailer.send(msg)
            print("---MSG SENT---\n")
            emails_sent += 1
            pause(.5)
        else:
            print("---SKIPPING---\n")
            pause(.5)
        
        accessed = True
        clear()

    print("{} emails were sent".format(emails_sent))
    print('---Program Ended---')
    print('---CLOSING---')
    emailer.logoff()

    pause(2)

if __name__ == "__main__":
   main()