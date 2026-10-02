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

add_product("cola")
add_product("cake")
add_product("telephone")

print(products)