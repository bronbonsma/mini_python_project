import csv

class User:


    def _init__(self):
        self.first_name = str(input('Please insert your username: '))
        self.password = str(input('Please insert your password: '))



    def user_auth(first_name, password):
        with open('/Users/macpro/PycharmProjects/mini_python_project/cvs.file/user.csv') as csv_file:
            csv_reader = csv.reader(csv_file)
            access = False
            user_role = ' '
            for row in csv_reader:
                if first_name.lower() == row[1] and password.lower() == row[3]:
                    access = True
                    user_role = str(row[6])


            if access:
                print('Access Granted')
                print(f'Your role is {user_role}')
                return access
            else:
                print('Access Denied')
                return access


User._init__(User)
User.user_auth(User.first_name, User.password)


