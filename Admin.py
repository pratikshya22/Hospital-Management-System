from Doctor import Doctor
from Patient import Patient


class Admin:
    """A class that deals with the Admin operations"""
    def __init__(self, username, password, address = ''):
        """
        Args:
            username (string): Username
            password (string): Password
            address (string, optional): Address Defaults to ''
        """
        self.__username = username
        self.__password = password
        self.__address =  address

    def view(self,a_list):
        """
        print a list
        Args:
            a_list (list): a list of printables
        """
        for index, item in enumerate(a_list):
            print(f'{index+1:3}|{item}')

    def login(self) :
        """
        A method that deals with the login
        Raises:
            Exception: returned when the username and the password ...
                    ... don`t match the data registered
        Returns:
            string: the username
        """
    
        print("-----Login-----")
        #Get the details of the admin

        username = input('Enter the username: ')
        password = input('Enter the password: ')

        # check if the username and password match the registered ones
        if(self.__username == username) & (self.__password == password):
            return True
        else:
            print("Invalid username and password.")
            
            

    def find_index(self,index,doctors):
        
            # check that the doctor id exists          
        if index in range(0,len(doctors)):
            
            return True

        # if the id is not in the list of doctors
        else:
            return False
            
    def get_doctor_details(self) :
        """
        Get the details needed to add a doctor
        Returns:
            first name, surname and ...
                            ... the speciality of the doctor in that order.
        """
        
        d_fname = input("Enter the first name of the doctor: ")
        d_sname = input("Enter the surname of the doctor: ")
        d_spec = input("Enter the speciality of the doctor: ")

        return d_fname,d_sname,d_spec

    def doctor_management(self, doctors):
        """
        A method that deals with registering, viewing, updating, deleting doctors
        Args:
            doctors (list<Doctor>): the list of all the doctors names
        """

        print("-----Doctor Management-----")

        # menu
        print('Choose the operation:')
        print(' 1 - Register')
        print(' 2 - View')
        print(' 3 - Update')
        print(' 4 - Delete')

       
        op = input("Please choose the number: ")


        # register
        if op == '1':
            print("-----Register-----")

            # get the doctor details
            print('Enter the doctor\'s details:')
            # doc = self.get_doctor_details()
            d_fname, d_sname, d_spec = self.get_doctor_details()
            # check if the name is already registered
            name_exists = False
            for a in doctors:
                if(d_fname==a.get_first_name() and d_sname==a.get_surname()):
                     print("Name already exists.")
                     break
            else:
                
                doctors.append(Doctor(d_fname,d_sname,d_spec))
                print('Doctor registered.')
                self.view(doctors)
                   

        # View
        elif op == '2':
            print("-----List of Doctors-----")
            print('ID |          Full name           |  Speciality')
            self.view(doctors)

        # Update
        elif op == '3':
            while True:
                print("-----Update Doctor`s Details-----")
                print('ID |          Full name           |  Speciality')
                self.view(doctors)
                try:
                    index = int(input('Enter the ID of the doctor: ')) - 1
                    doctor_index=self.find_index(index,doctors)
                    if doctor_index!=False:
                        
                        break
                        
                    else:

                        print("Doctor not found")

                    
                        # doctor_index is the ID mines one (-1)
                        

                except ValueError: # the entered id could not be changed into an int
                    print('The ID entered is incorrect')

            # menu
            print('Choose the field to be updated:')
            print(' 1 First name')
            print(' 2 Surname')
            print(' 3 Speciality')
            op = int(input('Input: ')) # make the user input lowercase
            if(op == 1):
                new_firstname = input("Enter the new first name : ")
                doctors[index].set_first_name(new_firstname)
                print("Your first name is updated.")
                self.view(doctors)
            elif(op == 2):
                new_surname = input("Enter the new surname : ")
                doctors[index].set_surname(new_surname)
                print("Your surname is updated.")
                self.view(doctors)
            elif(op == 3):
                new_spec = input("Enter the new speciality : ")
                doctors[index].set_speciality(new_spec)
                print("Your speciality is updated.")
                self.view(doctors)

            


        # Delete
        elif op == '4':
            print("-----Delete Doctor-----")
            print('ID |          Full Name           |  Speciality')
            self.view(doctors)

            index = int(input('Enter the ID of the doctor to be deleted: '))-1
            doctor_index=self.find_index(index,doctors)
            if(doctor_index!=False):
                doctors.pop(index)
                print("Doctor deleted")
                self.view(doctors)

            else:
               print("Invalid operation choosen. Check your spelling!")

    def view_patient(self, patients):
        """
        print a list of patients
        Args:
            patients (list<Patients>): list of all the active patients
        """
        print("-----View Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(patients)

    def assign_doctor_to_patient(self, patients, doctors):
        """
        Allow the admin to assign a doctor to a patient
        Args:
            patients (list<Patients>): the list of all the active patients
            doctors (list<Doctor>): the list of all the doctors
        """
        print("-----Assign-----")

        print("-----Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(patients)

        patient_index = input('Please enter the patient ID: ')

        try:
            # patient_index is the patient ID mines one (-1)
            patient_index = int(patient_index) -1

            # check if the id is not in the list of patients
            if patient_index not in range(len(patients)):
                print('The id entered was not found.')
                return # stop the procedures

        except ValueError: # the entered id could not be changed into an int
            print('The id entered is incorrect')
            return # stop the procedures

        print("-----Doctors Select-----")
        print('Select the doctor that fits these symptoms:')
        patients[patient_index].print_symptoms() # print the patient symptoms

        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors)
        doctor_index = input('Please enter the doctor ID: ')

        try:
            # doctor_index is the patient ID mines one (-1)
            doctor_index = int(doctor_index) -1

            # check if the id is in the list of doctors
            if self.find_index(doctor_index,doctors)!=False:
                    
                # link the patients to the doctor and vice versa
                patients[patient_index].link(doctors[doctor_index].full_name()) 
                print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
                self.view(patients)
                doctors[doctor_index].add_patient(patients[patient_index].full_name())
                print('The patient is now assign to the doctor.')

            # if the id is not in the list of doctors
            else:
                print('The id entered was not found.')

        except ValueError: # the entered id could not be changed into an in
            print('The id entered is incorrect')

    def discharge(self, patients, discharge_patients):
        """
        Allow the admin to discharge a patient when treatment is done
        Args:
            patients (list<Patients>): the list of all the active patients
            discharge_patients (list<Patients>): the list of all the non-active patients
        """
       
        # print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        print("-----Discharge Patient-----")
        patient_index = int(input("Please Enter the patient ID: "))-1
        if patient_index in range(len(patients)):
                discharge_patients.append(patients.pop(patient_index))
                # self.view_discharge(discharged_patients)
                self.view_patient(patients)
        else:
            print("Invalid patient ID.")

    def view_discharge(self, discharged_patients):
        """
        Prints the list of all discharged patients
        Args:
            discharge_patients (list<Patients>): the list of all the non-active patients
        """

        print("-----Discharged Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(discharged_patients)

    def admin_details(self):
        print(f"Username : {self.__username}")
        print(f"Password : {self.__password}")
        print(f"Address : {self.__address}")

    def update_details(self):
        """
        Allows the user to update and change username, password and address
        """

        print('Choose the field to be updated:')
        print(' 1 Username')
        print(' 2 Password')
        print(' 3 Address')
        op = int(input('Input: '))

        if op == 1:
            self.admin_details()
            username1 = input('Enter the new username: ')
            # validate the username
            username2 = input('Enter the new username again: ')
            if(username1 == username2):
                print("Username matched.")
                self.__username = username2
                print("------------------------------")
                self.admin_details()
                print("-----------Username updated--------------")
            else:
                print("Username not matched")   


        elif op == 2:
            self.admin_details()
            password = input('Enter the new password: ')
            # validate the password
            if password == input('Enter the new password again: '):
                self.__password = password
                self.admin_details()
                print("----------------Password updated---------------")

        elif op == 3:
            self.admin_details()
            address = input('Enter the new address: ')
            # validate the address
            if address == input('Enter the new address again: '):
                self.__address = address
                self.admin_details()
                print("address updated.")

        else:
            print("Invalid Choice.")

admin = Admin('admin','123','B1 1AB') # username is 'admin', password is '123'
doctors = [Doctor('John','Smith','Internal Med.'), Doctor('Jone','Smith','Pediatrics'), Doctor('Jone','Carlos','Cardiology')]
patients = [Patient('Sara','Smith', 20, '07012345678','B1 234'), Patient('Mike','Jones', 37,'07555551234','L2 2AB'), Patient('Daivd','Smith', 15, '07123456789','C1 ABC')]
discharged_patients = []


# admin.get_doctor_details()
# admin.view(doctors)
# admin.doctor_management(doctors)
# admin.view_patient(patients)
# admin.assign_doctor_to_patient(patients,doctors)
# admin.discharge(patients, discharged_patients)
# admin.update_details()