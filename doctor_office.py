class Patient():
    '''patient record'''
    def __init__(self, social_security_num, date_of_birth, health_ins_num, first_name, last_name, address):
        '''initialize patient record information'''
        self.__social_security_num = social_security_num
        self.__date_of_birth = date_of_birth
        self.__health_ins_num = health_ins_num
        self.__first_name = first_name
        self.__last_name = last_name
# dunderscore is used because you want to keep these properties private. However, you will be able to pass in arguments.
# keep parameters in order to pass in the information needed
    '''define getter for social security number, d.o.b. and health insurance account number.(readonly)'''
    @property
    def social_security_num(self):
        try:
            return f"{self.__social_security_num}"
        except AttributeError:
            return "Patient does not have a full social security number"
    @property
    def date_of_birth(self):
        try:
            return f"{self.__date_of_birth}"
        except AttributeError:
            return "Patient does not have a full date of birth"
    @property
    def health_ins_num(self):
        try:
            return f"{self.__health_ins_num}"
        except AttributeError:
            return "Patient does not have a full health insurance account number"


    '''define getter and setter for address'''
    @property
    def address(self):
        try:
            return(f"{self.address}")
        except AttributeError:
            return ("Please enter a full address")

    @address.setter
    def address(self,address):
        if type (address) is str:
            self.__address = address
        else:
            raise TypeError("Please provide a string value for the address")
# you only need a getter which creates the calculated full name by combining first name and last name
    '''define getter and setter for full name'''
    @property
    def full_name(self):
        try:
            return f"{self.__first_name} {self.__last_name}"
        except AttributeError:
            return "Student does not have a full name"

cashew = Patient("097-23-1003", "08/13/92", "7001294103","Daniela", "Agnoletti", "500 Infinity Way")
print(cashew.full_name)
print(cashew.social_security_num)
print(cashew.health_ins_num)
print(cashew.date_of_birth)


