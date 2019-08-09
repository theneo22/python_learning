
text: str
encrypted_text = ""
num = 0
asci_size = 128
file_name = "accounts.txt"
logins: dict = {}
login: str
password: str

def get_login():
    # global text
    # global num
    global login
    global password
    login = input()
    password = input()


def encrypt_text(tekst, num):
    global encrypted_text
    for i in tekst:
        new_char_int = (ord(i) + int(num))
        if new_char_int > 127:
            new_char_int -= asci_size
        encrypted_text += (chr(new_char_int))

        # print(encrypted_text)
    return encrypted_text

def read_file (file):
    with open(file_name, 'r') as f:
        for line in f:
            line = line.strip()
            (key, val) = line.split(':')
            logins[(key)] = val
    f.close()

def write_user_into_file(file_name, user, password):
    account_found = False
    for x, y in logins.items():
        if x == login:
            account_found = True
    if account_found is True:
        print("user already exists")
    else:
        with open(file_name,'a+') as f:
            f.write("\n{}:{}".format(user,password))
            print("user added")

def switch_choise(arg):
    switch = {
        'A': write_user_into_file(file_name, login, encrypt_text(password, 2)),
        'L': "",
        'Q': "",
    }
    return switch.get(arg, "wrong chooise")

if __name__ == '__main__':

    # encrypt_text(text, num)
    # print(encrypted_text)
    wybor = ""
    read_file(file_name)
    while True:
        print("Choose answer")
        wybor = input()
        if wybor != "Q":
            get_login()
            switch_choise(wybor)
        else:
            break



    # get_login()

    #print(logins)
    #print(login,password)






    # print(encrypt_text("abcdefghj", 1))
g = lambda x: x*2
print(g(3))