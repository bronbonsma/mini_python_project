import csv
from csv import writer
import os


class File_handler:

    def __init__(self,):
        self.data = []

    def load_from_csv(self, file_name):
        try:
            with open(file_name, 'r') as csv_file:
                csv_reader = csv.DictReader(csv_file)

                for line in csv_reader:
                    self.data.append(line)

        except Exception as error:
            print("There is an error :" + str(error))

    def append_to_csv(self, file_name, data):
        try:

            self.load_from_csv(file_name)
            for row in self.data:
                if row.get("id") == data[0]:
                    raise Exception("This ID already exists")

            with open(file_name, 'a+', newline='') as write_obj:
                csv_writer = writer(write_obj)
                csv_writer.writerow(data)

        except Exception as error:
            print("There is an error :" + str(error))


    def remove_from_csv(self, file_name, id):
        try:

            f = open(file_name, 'r+')
            file_content = list(csv.reader(f))
            # print(file_content[1][0])
            found = False

            for row in file_content:
                if row[0] == id:
                    file_content.remove(row)
                    found = True

            with open(file_name, 'w') as f:
                writer = csv.writer(f)
                writer.writerows(file_content)

            if not found:
                raise Exception("That id does not exist")

        except Exception as error:
            print("There is an error :" + str(error))





# data_input = ['24', 'Tom', 'Knecht', 'password', 'student', 100, 'teacher']
#
file = File_handler()
# file.append_to_csv("/Users/macpro/PycharmProjects/mini_python_project/cvs.file/user.csv", data_input)
# file.load_from_csv("/Users/macpro/PycharmProjects/mini_python_project/cvs.file/user.csv")
file.remove_from_csv("/Users/macpro/PycharmProjects/mini_python_project/cvs.file/user.csv", "8")





















