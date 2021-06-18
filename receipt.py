import csv 

def main():
    products_dict = read_products()
    print(products_dict)

    process_request(products_dict)

def read_products():
    with open('products.csv') as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)

        products = {}
        for row in csv_reader:
            key = row.pop(0)
            value = row
            products[key] = value
        
        return products

def process_request(products_dict):
    with open('request.csv') as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)

        for row in csv_reader:
            product_id = row[0]
            product_quantity = row[1]

            print(f"{products_dict[product_id][0]}: {product_quantity} @ {products_dict[product_id][1]}")
            
main()