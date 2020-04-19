import csv
from csv import writer

class FileHandler:

    def load_from_cvs(self, file_name):
        try:
            with open(file_name, 'r') as csv_file:
                csv_reader = csv.DictReader(csv_file)

                for line in csv_reader:
                    print(line)


        except Exception as error:
            print("There is an error :" + str(error))

    def append_to_csv(self, file_name, data_input):
        try:
            with open(file_name, 'a+', newline='') as write_obj:
                csv_writer = writer(write_obj)
                csv_writer.writerow(data_input)

                for row in csv_writer:
                    print(row[0])

        except Exception as error:
            print("There is an error:" + str(error))


data_input = [14, 'Tom', 'Jerry', 'password', 'student', 100, 'teacher']

file = FileHandler()
file.append_to_csv("/Users/macpro/PycharmProjects/mini_python_project/cvs.file/user.csv",data_input)
file.load_from_cvs("/Users/macpro/PycharmProjects/mini_python_project/cvs.file/user.csv")










