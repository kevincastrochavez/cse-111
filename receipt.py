import csv 
from datetime import datetime

def main():
    print('Inkom Emporium')
    print('')
    # Calls the read_products function and stores the value
    products_dict = read_products()

    # Calls the process_request function
    process_request(products_dict)

def read_products():
    try:
        # Opens the file
        with open('products.csv') as csvfile:
            # Reads the file
            csv_reader = csv.reader(csvfile)
            # Skips the first line in that file
            next(csv_reader)

            # Creates an empty dictionary
            products = {}
            # Loops through each of te lines in the file read
            for row in csv_reader:
                # Gets the first element on the array and stores it
                key = row.pop(0)
                # Assigns the other two elements in the array to this variable
                value = row
                # Creates the dictionary with the previous values
                products[key] = value
            
        return products
    except FileNotFoundError as file_not_found_err:
        print(f"{file_not_found_err}: Such file was not found")
    except PermissionError as perm_err:
        print(f"{perm_err}: Cannot read such file due to lack of permission")

def process_request(products_dict):
    try:
        # Opens the file
        with open('request.csv') as csvfile:
            # Reads the file
            csv_reader = csv.reader(csvfile)
            # Skips the first line in that file
            next(csv_reader)
            # Initializes counts
            quantity = 0
            price = 0
            current_date_and_time = datetime.now()


            # Loops through each of te lines in the file read
            for row in csv_reader:
                try:
                    # Gets the first element on the array and stores it
                    product_id = row[0]

                    # Gets the second element on the array and stores it
                    product_quantity = int(row[1])

                    # Adds the quantity and price on each iteration
                    quantity = quantity + product_quantity
                    price = float(price) + float(products_dict[product_id][1]) * product_quantity

                    # Prints the name of the product, its quantity and the price
                    print(f"{products_dict[product_id][0]}: {product_quantity} @ {products_dict[product_id][1]}")
                except KeyError as key_err: 
                    print(f"{key_err}: The key you are trying to get in the dictionary does not exist")
            print('')
            print(f"Number of items: {quantity}")
            print(f"Subtotal: ${price}")
            print(f"Sales Tax: ${price * 0.06:.2f}")
            print(f"Total: ${price * 0.06 + price:.2f}")
            print('')
            print('Thank you for shopping at the Inkom Emporium.')
            print(f"{current_date_and_time:%a %b %w %X %Y}")
    except FileNotFoundError as file_not_found_err:
        print(f"{file_not_found_err}: Such file was not found")
    except PermissionError as perm_err:
        print(f"{perm_err}: Cannot read such file due to lack of permission")

main()