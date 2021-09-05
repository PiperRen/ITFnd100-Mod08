# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# LTurner, 8.26.2021, Started reviewing the starter code and plan out what needs to be done
#                     Started on the product class.
# LTurner, 8.27.2021, Continued to work on updated the code and adding script to
#                     the product class.
# LTurner, 8.30.2021, Started working on the file processing class
# LTurner, 8.31.2021, Worked on processing class and presentation class
# LTurner, 9.1.2021, Worked on error handling to continue running instead of stopping
# LTurner, 9.4.2021, Worked on fixing issues with the save file option
# LTurner, 9.5.2021, Worked on improving the error handling to clean it up with better error mesaages
# LTurner,
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
str_file_name = 'products.txt'
product_objects = []
message = ""


class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products name
        product_price: (float) with the products standard price
    methods:
        print product_name and product_price
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        LTurner,8.26.2021, Started working on filling in the code for constructor
                           attributes, properties, and methods
        LTurner, 8.27.21, Continued working on the product class fixing getter and setter
        LTurner, 8.30.21, Updated the data types for the inputs
        LTurner, 9.1.21, Update the data class to run through errors instead of stopping program
        LTurner, 9.5.21, Updated the error handling messages
    """

    # Constructor
    def __init__(self, product_name: str, product_price: float):
        # Attribute
        self.__product_name = ""
        self.__product_price = ""
        try:
            self.product_name = str(product_name)
            self.product_price = float(product_price)
        except ValueError():
            print('A float was asked for. Please enter a numerical input not string. ')
        except Exception as e:
            e = "Error initializing values."
            print(e)

    # Properties
    # property of product name
    @property
    def product_name(self):  # (getter or accessor)
        return str(self.__product_name).title()  # Title case

    @product_name.setter
    def product_name(self, value):  # setter)
        try:
            self.__product_name = str(value)
        except Exception as e:
            e = 'Product name can not be numerical'
            print(e)

    # property of the product price
    @property
    def product_price(self): # getter
        return float(self.__product_price)

    @product_price.setter
    def product_price(self,value: float):  # setter
        try:
            self.__product_price = float(value)
        except ValueError as e:
            e = "Error"
            print(e + 'Product price needs to be a string.')

    def to_string(self):
        return self.__str__()

    def __str__(self):
        return self.product_name + ',' + str(self.product_price)

# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #


class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        LTurner, 8.30.2021, Started working on the save data to file method
        LTurner, 8.31.2021, Continues working on save data and read methods
        LTurner, 9.4.2021, Working on the save function
        LTurner, 9.5.2021, Worked on improving the error handling
    """
    @staticmethod
    def save_data_to_file(file_name: str, list_of_products: list):
        """ Write the data to a file from a list of products

        :param: file_name: string for the file name
        :param: list_of_products: list of products to be saved
        :return: success_status (boolean), message - return to user
        """
        success_status = False
        try:
            file = open(file_name, 'w')
            for products in list_of_products:
                file.write(products.__str__() + "\n")
            file.close()
            success_status = True
        except Exception as e:
            print('There was an error saving the data to the file.')
            print(e)
        return success_status

    @staticmethod
    def read_data_from_file(file_name: str):
        """ Reads the data from a file and saves it to a list

        :param: file_name: string used for the file name
        :return: list of product rows from the file
        """
        list_of_rows = []
        message_error = ""
        try:
            file = open(file_name, "r")
            for line in file:
                data = line.split(',')
                row = Product(data[0], data[1])
                list_of_rows.append(row)
            file.close()
            message_error = 'File found and read.'
        except FileNotFoundError:
            message_error = 'File not found, please save a file if you want to read from it.'
            print()
        except ValueError:
            message_error = 'Issue with converting the data from the file.' \
                            'Potential that not all the data from the file was read.'
        except Exception as e:
            print('There was an error.')
            print('Error: ', e)
            print()
            message_error = 'There was an issue reading the file. ' \
                            'Not all the data was loaded from file. ' \
                            'Check file data for issues.'
        return list_of_rows, message_error

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #


class IO:
    """Input and output tasks:

    methods:
        print_menu_items(): -> prints menu, nothing returned

        input_menu_choice():-> returns users input choice

        print_current_list_of_products(list_of_rows): -> prints list of products

        input_product_info(): -> returns list of product objects
        input_press_to_continue: -> prints message to user and asks them to enter to continue

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        LTurner, 8.31.2021, Started working on the input and output tasks
    """

    # function used to print the menu to the user
    @staticmethod
    def print_menu_items():
        """ Print a menu of choices to the user """
        print('''
        Menu of Options:
        1) Show current data
        2) Add a new line
        3) Save data to a file
        4) Exit Program
        ''')
        print()

    @staticmethod
    def input_menu_choice():
        """ Gets the menu option from the user

        return: user input as a string (user_choice)
        """
        # Asks for users input and strips any extra characters(spaces) from the input
        user_choice = str(input('Which option would you like to perform? [1 - 4] - ')).strip()
        print()
        return user_choice

    @staticmethod
    def print_current_list_of_products(list_of_rows: list):
        """ Print what is currently in the list of products.

        :param: list_of_rows: list of rows to be displayed
        """
        print('############## The Current List of Products: ################')
        for row in list_of_rows:  # goes through rows of data in the table and then prints data
            print(row.product_name + ' (' + str(row.product_price) + ')')
        print('#############################################################')
        print()

    @staticmethod
    def input_product_info():
        """ Gets product information from the user as an object
            and adds the object to the list of rows

         return: row_add - product object with data input from user
        """
        try:
            name = str(input('What is the product name?: ').strip())
            price = float(input('What is the product price?: ').strip())
            print()
            row_add = Product(product_name=name, product_price=price)
            product_objects.append(row_add)
        except ValueError:
            print('A string was entered instead of a numerical input.')
            print('Please select menu option 2, to try entering product to the list')
        except Exception as e:
            print(e)
            print('Please select menu option 2, to try entering product to the list')
        return product_objects

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')
        print()

    @staticmethod
    def input_yes_no_choice(input_message):
        """ Gets a yes or no choice from the user

        :return: string
        """
        return str(input(input_message)).strip().lower()

# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #


# Load data from file into a list of product objects when script starts
# Press enter to continue
product_objects, message = FileProcessor.read_data_from_file(str_file_name)
IO.input_press_to_continue(message)

while True:

    IO.print_current_list_of_products(product_objects)  # Show current data in the list/table
    IO.print_menu_items()  # Shows menu
    choice = IO.input_menu_choice()  # Get menu option from user

    # If 1 is chosen, the user wants to see the current list
    if choice == '1':
        IO.print_current_list_of_products(product_objects)
        continue

    # If 2 is chosen, Add a new line to the list of product objects
    if choice == '2':
        product_objects = IO.input_product_info()
        continue

    # Save product object list to file
    if choice == '3':
        choice_y_n = IO.input_yes_no_choice("Save this data to file? (y/n) - ")  # User input if they want to save
        if choice_y_n.lower() == "y":
            success = FileProcessor.save_data_to_file(str_file_name, product_objects)
            if success:
                IO.input_press_to_continue("Save Completed!")
            else:
                IO.input_press_to_continue("Save not complete. Issues saving!")
            continue
        else:
            IO.input_press_to_continue("Save Cancelled!")
            continue

    if choice == '4':
        # User input if they want to save
        choice_y_n = IO.input_yes_no_choice("Do you want to exit this program? (y/n) - ")
        if choice_y_n.lower() == "y":
            IO.input_press_to_continue("Thanks for using this program.")
            break
        else:
            IO.input_press_to_continue("Program will continue.")
            continue

    else:
        IO.input_press_to_continue("Enter a menu option [1-4]")
        continue

# # Main Body of Script  ---------------------------------------------------- #
#
#

# DEMO and Testing Code
# objP1 = Product('Apple', 10.34)
# print(objP1)
#
# objP2 = Product('Apple', "Apple")
# print(objP2)
#
# objP3 = Product(1.23, 5.25)
# print(objP3)


