import csv
from csv import DictWriter



class File_handler:
    data = None

    def __init__(self, file_name):
        if self.data is None:
            self.data = []
        self.load_from_csv(file_name)
        self.file_name = file_name


    def load_from_csv(self,file_name):
        try:
            self.data = []
            with open(file_name, 'r') as csv_file:
                csv_reader = csv.DictReader(csv_file, delimiter = ',')
                for line in csv_reader:
                    self.data.append(line)

        except Exception as error:
            print("There is an error :" + str(error))



    def append_to_csv(self, data):
        try:
            for row in self.data:
                if row.get("id") == data.get('id'):
                    raise Exception("This ID already exists")

            with open(self.file_name, 'a+', newline='') as write_obj:
                dict_writer = DictWriter(write_obj, fieldnames=data)
                dict_writer.writerow(data)

        except Exception as error:
            print("There is an error :" + str(error))


    def remove_from_csv(self, id):

        try:
            found = False
            for item in self.data:
                if item["id"] == id:
                    print("Found & Deleted")
                    self.data.remove(item)
                    found = True

            if found:
                keys = self.data[0].keys()
                with open(self.file_name, 'w') as f:
                    dict_writer = csv.DictWriter(f,keys)
                    dict_writer.writeheader()
                    dict_writer.writerows(self.data)
            else:
                raise Exception("That id does not exist")

        except Exception as error:
            print("There is an error :" + str(error))

    def update_csv(self, id, row):
        try:
            found = False
            for item in self.data:
                if item["id"] == id:
                    print("Found & Changed")
                    self.data.remove(item)
                    found = True
            if found:
                keys = self.data[0].keys()  # grabbing the keys from teh data
                with open(self.file_name, 'w') as f:
                    dict_writer = csv.DictWriter(f, keys)  # setting the first row
                    dict_writer.writeheader()  # writing the first row
                    dict_writer.writerows(self.data)  # writing the rows
                self.append_to_csv(row)
            else:
                raise Exception("That id does not exist")

        except Exception as e:
            print(e)


# data_input = {'id': '16', 'first_name': 'kim', 'last_name': 'Berg', 'password': 'password', 'position': 'teacher',
#               'salary': '100', 'role': 'admin'}


# file = File_handler("/Users/macpro/PycharmProjects/mini_python_project/cvs.file/vehicle.csv")
# file.append_to_csv(data_input)
# file.load_from_csv('/Users/macpro/PycharmProjects/mini_python_project/cvs.file/vehicle.csv')
# file.remove_from_csv("2")
# file.update_cvs("7", data_input)



























