
text: str
encrypted_text = ""
num = 0
asci_size = 128
file_name = "accounts.txt"
logins: dict = {}
login: str
password: str

def get_login():
    global text
    global num
    global login
    global password
    login = input()
    password = input()
    #text = input()
    #num = input()

def encrypt_text(tekst, num):
    global encrypted_text
    for i in text:
        new_char_int = (ord(i ) +int(num))
        if new_char_int > 127:
            new_char_int -= asci_size
        encrypted_text =(chr(new_char_int))
    return encrypted_text

def read_file (file):
    with open(file_name, 'r') as f:
        for line in f:
            line = line.strip()
            (key, val) = line.split(':')
            logins[(key)] = val

    f.close()

if __name__ == '__main__':

    # encrypt_text(text, num)
    # print(encrypted_text)

    read_file(file_name)
    get_login()

    #print(logins)
    #print(login,password)

    account_found = False
    for x, y in logins.items():
        if x == login and y == password:
            account_found = True
    if account_found is True:
        print("konto znaleziono")
    else: print("konto nieznaleziono")

g = lambda x: x*2
print(g(3))