# -> Problem Statement 007

# Supply Chain Management System:
# You have a dictionary representing the supply chain for a manufacturing company. The keys are product IDs, and the values are nested dictionaries containing 'name', 'components' (a list of dictionaries with 'component ID', 'supplier', and 'quantity'), and 'production' (another dictionary with 'units produced' and 'cost per unit'). Write a program to calculate the total cost for producing a given number of units of each product, considering the component quantities and production costs.

supply_chain = {
    101: {
        'name': 'ProductA',
        'components': [
            {'component_id': 'C1', 'supplier': 'Supplier1', 'quantity': 2},
            {'component_id': 'C2', 'supplier': 'Supplier2', 'quantity': 1}
        ],
        'production': {'units_produced': 1000, 'cost_per_unit': 50}
    },
    102: {
        'name': 'ProductB',
        'components': [
            {'component_id': 'C3', 'supplier': 'Supplier3', 'quantity': 3},
            {'component_id': 'C4', 'supplier': 'Supplier4', 'quantity': 2}
        ],
        'production': {'units_produced': 2000, 'cost_per_unit': 75}
    },
    103: {
        'name': 'ProductC',
        'components': [
            {'component_id': 'C5', 'supplier': 'Supplier5', 'quantity': 4},
            {'component_id': 'C6', 'supplier': 'Supplier6', 'quantity': 1}
        ],
        'production': {'units_produced': 1500, 'cost_per_unit': 60}
    }
}

product_id = int(input("Enter the product_id: "))
units_needed = int(input("Enter the units you want to manufacture: "))

product = supply_chain.get(product_id)

if not product:
    print("Product Not Found!")
else:
    total_cost = product['production']['cost_per_unit'] * units_needed
    print(f"Total Manufacturing Cost needed to manufacture {units_needed} of {product.get('name')} is {total_cost}")