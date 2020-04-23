import os
from Filehandler import File_handler
from User import User
import csv

class Carlot:
    def __init__(self,file_name):
        self.User = User(file_name)
        self.File_handler = File_handler(file_name)

    def update_salary_by_name(self, salary, employeeName):

            employee = {}
            newpath = os.path.join('/Users/macpro/PycharmProjects/mini_python_project/cvs.file/user.csv')
            self.File_handler.load_from_csv(newpath)
            for x in self.File_handler.data:
                if x ['first_name'] == employeeName:
                    employee = x

            if employee:
                role = self.User.user_auth(employee["first_name"], employee["password"])
                if role == True:
                    employee["salary"] = str(salary)
                    removevalue = self.File_handler.remove_from_csv(employee["id"])
                    if removevalue == None:
                       addvalue = self.File_handler.append_to_csv(employee)
                       if addvalue == None:
                           print("The salary has been updated")
                           return True
                       else:
                           return False
                    else:
                        return False
                else:
                    return False
            else:
                return False




    def add_to_fleet(self, external_file):
        try:
            with open(external_file, "r") as csv_external:
                csv_reader = csv.reader(csv_external)
                external_headers = next(csv_reader)

            with open("/Users/macpro/PycharmProjects/mini_python_project/cvs.file/vehicle.csv", "r") as csv_file:
                csv_reader = csv.reader(csv_file)
                internal_headers = next(csv_reader)

            if external_headers != internal_headers:
                return False

            external_data = open(external_file, "r")
            internal_data = open("/Users/macpro/PycharmProjects/mini_python_project/cvs.file/vehicle.csv", "r").readlines()

            if external_data != internal_data:
                with open("/Users/macpro/PycharmProjects/mini_python_project/cvs.file/vehicle.csv", "a") as csv_append:
                    next(external_data)
                    for row in external_data:
                        csv_append.writelines(row)
                return True

        except Exception as error:
            print(error)
            raise

    def get_fleet_size(self):
        try:
            vehicle_path = os.path.join("/Users/macpro/PycharmProjects/mini_python_project/carLot.py")
            self.File_handler.load_from_csv(vehicle_path)
            print("There are " + str(len(self.File_handler.data)) + " cars")
            return len(self.File_handler.data)

        except Exception as error:
            print(error)
            raise


carlot = Carlot("/Users/macpro/PycharmProjects/mini_python_project/cvs.file/vehicle.csv")
# carlot.update_salary_by_name("10", "amira")
# carlot.add_to_fleet('/Users/macpro/PycharmProjects/mini_python_project/external_file.csv')
carlot.get_fleet_size()