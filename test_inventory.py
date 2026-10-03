import inventory
import pytest
from datetime import datetime

def test_sale_reduces_stock():
    inventory.products.clear()
    inventory.movements.clear()

    cola=inventory.add_product("cola", "л", 10)
    inventory.add_receipt(cola, 10, "tom")
    inventory.add_sale(cola, 3, "ted")
    assert inventory.get_stock(cola) == 7





def test_receipt():
    inventory.products.clear()
    inventory.movements.clear()

    cake=inventory.add_product("cake", "кг", 3)
    inventory.add_receipt(cake, 5, "ted")
    assert inventory.get_stock(cake)==5




def test_stock_without_movements_is_zero():
    inventory.products.clear()
    inventory.movements.clear()

    apple=inventory.add_product("apple", "кг", 2)
    assert inventory.get_stock(apple)==0




def test_products_stock_is_independent():
    inventory.products.clear()
    inventory.movements.clear()

    fanta=inventory.add_product("fanta", "л", 10)
    candy=inventory.add_product("candy", "кг", 3)
    inventory.add_receipt(fanta, 10, "tom")
    inventory.add_receipt(candy, 5, "ted")
    assert inventory.get_stock(fanta)==10
    assert inventory.get_stock(candy)==5

def test_withdraw_too_much():
    inventory.products.clear()
    inventory.movements.clear()

    fanta=inventory.add_product("fanta", "л", 10)
    inventory.add_receipt(fanta, 10, "tom")

    with pytest.raises(ValueError):
        inventory.add_sale(fanta, 15, "tom")

    assert inventory.get_stock(fanta)==10

    

def test_stock_before_movement_date_is_zero():
    inventory.products.clear()
    inventory.movements.clear()
    
    fanta=inventory.add_product("fanta", "л", 10)
    inventory.add_receipt(fanta, 10, "tom", datetime(2026, 10, 3))

    assert inventory.get_stock(fanta, datetime(2026, 9, 5))==0

def test_stock_on_date_counts_earlier_movements():
    inventory.products.clear()
    inventory.movements.clear()
        
    fanta=inventory.add_product("fanta", "л", 10)
    inventory.add_receipt(fanta, 10, "tom", datetime(2026, 9, 14))

    assert inventory.get_stock(fanta, datetime(2026, 9, 15))==10
    assert inventory.get_stock(fanta, datetime(2026, 8, 5))==0


def test_stock_on_date_ignores_movement_order():
    inventory.products.clear()
    inventory.movements.clear()
            
    fanta=inventory.add_product("fanta", "л", 10)
    inventory.add_receipt(fanta, 10, "tom", datetime(2026, 10, 2))
    inventory.add_receipt(fanta, 7, "tom", datetime(2026, 9, 11))

    assert inventory.get_stock(fanta, datetime(2026, 9, 15))==7
    assert inventory.get_stock(fanta, datetime(2026, 10, 3))==17


