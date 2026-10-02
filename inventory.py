from datetime import datetime

products={}

movements=[]

def add_product(name, unit, min_stock):
    if not products:
        product_id=1
    else:
        last_key=list(products)[-1]
        product_id=last_key+1

    products[product_id]={"name": name, "unit": unit, "min_stock": min_stock}
    return product_id


def add_receipt(product_id, quantity, who, when=None):
    if quantity <= 0:
        raise ValueError("Error: quantity must be greater than 0.")
    if product_id not in products:
        raise ValueError("This product is not available.")
    if when is None:
        created_at=datetime.now()
    else:
        created_at=when
    movements.append({"product_id": product_id, "quantity": quantity, 
                      "operation": "receipt", "created_at":created_at, "who": who})
    
def get_stock(product_id):
    result_quantity=0
    for move in movements:
        if move["product_id"]==product_id:
            number=move["quantity"]
            result_quantity+=number

    return result_quantity

        

