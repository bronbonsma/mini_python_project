import csv


class FileHandler:
    def __init__(self):
      self.user = []

    def load_csv_file(self, *args):
        try:
            with open(args[0]) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')

                for row in csv_reader:

                        user ={
                            "id":row[0],
                            "first name": row[1],
                            "last name": row[2],
                            "position": row[3],
                            "password": row[4],
                            "salary": row[5],
                            "role": row[6],
                        }
                        self.user.append(user)
        except Exception as error:
            print("There is an error :" + str(error))

file = FileHandler()
file.load_csv_file("/Users/macpro/PycharmProjects/mini_python_project/cvs.file/user.csv")
print(file.user)



