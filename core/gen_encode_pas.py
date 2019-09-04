import getpass
import base64

def gen_pas():
    pas_byte = getpass.getpass("Enter your password: ").encode('utf-8')
    with open('[5].txt', 'wb') as file:
        file.write(base64.b64encode(pas_byte))