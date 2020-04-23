
from Filehandler import File_handler


class User:
    def __init__(self, file_name):
        self.handler = File_handler(file_name)


    def user_auth(self, username, password):

        res = {}
        self.handler.load_from_csv('/Users/macpro/PycharmProjects/mini_python_project/cvs.file/user.csv')

        access = False
        user_role = ' '

        for row in self.handler.data:
            res.update(row)
            if username == row["first_name"] and password == row["password"]:
                access = True
                user_role = str(row["role"])

                if access:
                    print('Access Granted')
                    print(f'Your role is {user_role}')
                    return access

                else:
                    print('Access Denied')
                    return access

# User.__init__(User, '/Users/macpro/PycharmProjects/mini_python_project/cvs.file/user.csv')
# User.user_auth(User, "Tom", 'password')


