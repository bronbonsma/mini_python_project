import csv

class FileHandler:

    def load_from_function(self, file_name):
        try:
            with open(file_name, 'r') as csv_file:
                csv_reader = csv.reader(csv_file)

                for line in csv_reader:
                    print(line)


        except Exception as error:
            print("There is an error :" + str(error))






file = FileHandler()
file.load_from_function("/Users/macpro/PycharmProjects/mini_python_project/cvs.file/user.csv")






