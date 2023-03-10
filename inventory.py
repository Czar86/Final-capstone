# =====importing libraries===========

# Some text formatting codes
GREEN = '\033[92m'
RED = '\033[91m'
BLUE = '\033[94m'
BOLD = '\033[1m'
WHITE = '\033[0m'
CYAN = '\033[96m'
YELLOW = '\033[93m'
PINK = '\033[95m'

# ========The beginning of the class==========


class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        '''
        In this function, you must initialise the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        '''
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        '''
        Add the code to return the cost of the shoe in this method.
        '''
        shoe_cost = f"{self.cost}"
        return shoe_cost

    def get_quantity(self):
        '''
        Add the code to return the quantity of the shoes.
        '''
        shoe_quantity = f"{self.quantity}"
        return shoe_quantity

    def __str__(self):
        '''
        Add a code to returns a string representation of a class.
        '''
        shoe_details = f'''
        Country: {self.country}
        Code: {self.code}
        Product: {self.product}
        Cost: {self.cost}
        Quantity: {self.quantity}
        '''
        return shoe_details


# =============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []
# ==========Functions outside the class==============


def read_shoes_data():
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. It skips the first line in the file.
    Try-except in this function is for error handling. 
    '''
    try:
        with open("inventory.txt", "r") as file:
            # This stores all lines into a list excluding the first line[0]
            lines = file.readlines()[1:]
            for line in lines:
                line.strip()  # removes any preceeding and trailing spaces(\n)
                line_list = line.split(",")  # splits line into list items.
                # Creates shoe object.
                shoe = Shoe(line_list[0], line_list[1],
                            line_list[2], line_list[3], line_list[4])
                shoe_list.append(shoe)  # Adds shoe object to shoe_list.
    except IndexError:
        print(
            f"\n{RED}There were some issues building the inventory. Check source file and try again.{WHITE}")

    return print(f"\n{GREEN}Shoe database succesfully read from file.{WHITE}")


def capture_shoes():
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''
    country = input("\nCountry: ")
    code = input("Code: ")
    product = input("Product: ")
    cost = input("Cost: ")
    quantity = input("Quantity: ")

    shoe = Shoe(country, code, product, cost, quantity)  # Creates shoe object.
    shoe_list.append(shoe)  # Adds shoe object to shoe_list.
    print(
        f"\n{GREEN}The live inventory database has been succesfully updated.{WHITE}")

    # The following updates the inventory.txt file with the new shoe.
    update_text = f"{country},{code},{product},{cost},{quantity}"
    with open("inventory.txt", "a+") as file:
        file.write(f"\n{update_text}")
    print(f"\n{GREEN}The inventory.txt file has been succesfully updated.{WHITE}")


def view_all():
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. 
    '''
    for shoe in shoe_list:
        print(shoe.__str__())


def re_stock():
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. The user is asked if they
    want to add x quantity of shoes and then update it.
    This quantity is updated on the text file for this shoe.
    '''
    stock_list = []  # Stores shoe quantity for all shoes.
    for shoe in shoe_list:
        # Removes "\n" from object quantity and converts the variable to an integer.
        shoe_quantity = int(shoe.quantity.strip())
        # Adds each integer build a list of shoe quantities.
        stock_list.append(shoe_quantity)

    lowest_stock = min(stock_list)  # This finds lowest stock value in list.
    for number, shoe in enumerate(shoe_list):
        # This indentifies the appopriate shoe object.
        if int(shoe.quantity) == lowest_stock:
            lowest_stock_shoe = shoe_list[number]

            # This stores the index number of the shoe object as it would be on the inventory.txt file if all
            # lines are stored into a list with readlines(). This will be used later to edit the txt file.
            shoe_index = number + 1

    print("\nThe lowest stocked item is:")
    print(lowest_stock_shoe.__str__())

    choice = input("Do you want to update stock quantity? Y or N: ").lower()
    if choice == "y":
        update = int(input("Enter the quantity you want to add: "))
        updated_quantity = int(f"{lowest_stock_shoe.quantity}") + update
        # Updates/changes quantity of shoe object
        lowest_stock_shoe.quantity = str(updated_quantity)
        print(
            f"\n{GREEN}Shoe item {YELLOW}{lowest_stock_shoe.code}{GREEN} has been successfuly updated to {lowest_stock_shoe.quantity}.{WHITE}")

        # The following reads the inventory.txt file and edits the created list with updated quantity.
        with open("inventory.txt", "r") as file:
            # This stores all lines into a list.
            lines = file.readlines()
            # This uses the previously stored index to locate an edit the correct shoe/item.
            lines[shoe_index] = "{},{},{},{},{}\n".format(
                lowest_stock_shoe.country,
                lowest_stock_shoe.code,
                lowest_stock_shoe.product,
                lowest_stock_shoe.cost,
                lowest_stock_shoe.quantity
            )
        # The following rewrites the inventory.txt file with the updated list.
        with open("inventory.txt", "w+") as file:
            for line in lines:
                file.write(line)

        print(f"{GREEN}The inventory.txt file has been succesfully updated.{WHITE}")

    elif choice == "n":
        print("No changes have been made to stock quantity.")


def seach_shoe():
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''
    choice = input("Enter the product code of the shoe: ").upper()
    for number, item in enumerate(shoe_list):
        if choice == f"{item.code}":
            found_shoe = shoe_list[number]

    return found_shoe


def value_per_item():
    '''
    This function will calculate the total value for each item.
    and prints this information on the console for all the shoes.
    '''
    total_all = 0  # This stores initial value of all combined stock prices.

    # This outputs each shoe details with a total value for the shoe.
    for shoe in shoe_list:
        total_value = int(shoe.quantity) * int(shoe.cost)
        print(f'''\n
        Product: {shoe.product}
        Product code: {shoe.code}
        Total value: {total_value}
        ''')

    # This calculates total value of all combined inventory stock.
        total_all += total_value
    print(f"Total value of all stock is: {total_all} ")


def highest_qty():
    '''
    This determines the product with the highest quantity and
    prints this shoe as being for sale.
    '''
    stock_list = []  # Stores shoe quantity for all shoes.
    for shoe in shoe_list:
        # Adds each shoe object quantity to list.
        stock_list.append(int(f"{shoe.quantity}"))

    highest_stock = max(stock_list)  # This finds highest value in list.
    for number, shoe in enumerate(shoe_list):
        # This indentifies the appopriate shoe object.
        if int(shoe.quantity) == highest_stock:
            highest_stock_shoe = shoe_list[number]

    print(f"\n{highest_stock_shoe.product} is on SALE!!!!")


# ==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
main_menu = f'''
{CYAN}INVENTORY MANAGER ver 1.0{WHITE}

Type the highlighted {YELLOW}letter{WHITE} to perform the following functions.

{CYAN}∘{YELLOW} V{CYAN}iew inventory{WHITE}.
This displays all items in the inventory.

{CYAN}∘{YELLOW} S{CYAN}earch for a product{WHITE}.
This allows the user to search and find a product using the product code.

{CYAN}∘{YELLOW} A{CYAN}dd a product{WHITE}. 
This allows the user to add a product to the inventory.

{CYAN}∘{YELLOW} R{CYAN}estock a product{WHITE}.
This allows the user to identify the lowest stocked item and provides the option to restock.

{CYAN}∘{YELLOW} F{CYAN}ind sale item{WHITE}.
This allows the user to identify the highest stocked item and puts the item on sale.

{CYAN}∘{YELLOW} C{CYAN}alculate the total value of inventory items{WHITE}.
This displays the total value of each item in the inventory.

{CYAN}∘{YELLOW} E{CYAN}xit.
This exits the program. 

'''
while True:
    print(main_menu)
    user_choice = input(f"{YELLOW}Enter option:{WHITE}").lower()

    # This reads the inventory.txt file and builds the most current shoe list.
    read_shoes_data()

    # This uses the view_all function to output all shoes in the inventory.
    if user_choice == "v":
        view_all()

    # This uses the search_shoe function to find a shoe using the product code and prints it.
    elif user_choice == "s":
        print(f"{seach_shoe()}")

    # This uses the capture_shoes function to add a new product to the inventory.
    elif user_choice == "a":
        capture_shoes()

    # This uses the re_stock function to find the lowest stocked item.
    # It then allows the user to update the stock quantity.
    elif user_choice == "r":
        re_stock()

    # This uses the re_stock function to find the highest stocked item.
    # The item is then listed for sale.
    elif user_choice == "f":
        highest_qty()

    # This uses the user_choice function to calculate and display total stock value of each item.
    # Total value of all stock is also displayed.
    elif user_choice == "c":
        value_per_item()

    # This exits the program.
    elif user_choice == "e":
        exit()
