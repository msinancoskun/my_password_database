import sqlite3


ADMIN_PASSWORD = '123456'


def login(password):
    welcome_message = "Welcome to my password database!"

    if password == ADMIN_PASSWORD:
        print("You have successfully logged in!")
        print(welcome_message)
        print(40 * '-')
        
    else:
        print("Wrong username or password, try again...")
        login(input('Provide username...\n'), input('Provide password...\n'))


login(input('Provide password...\n'))
are_you_ready = input("Ready to add to database?\n").upper()

if are_you_ready == 'Y':
    platform_name = input('Provide the information for which the username-password will be stored...\n')
    user = input('Provide the username to store on the database...\n')
    key = input('Provide the password to store on the database...\n')
    
else:
    print("Program terminated...")


db = sqlite3.connect("passwords.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS passwords (platform_name TEXT, user TEXT, key INTEGER)")
db.execute("INSERT INTO passwords(platform_name, user, key) VALUES(?, ?, ?)", (platform_name, user, key))


cursor = db.cursor()
cursor.execute("SELECT * FROM passwords")

print(cursor.fetchall())


cursor.close()
db.commit()
db.close()
