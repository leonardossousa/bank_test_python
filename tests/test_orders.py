from src.question2 import Orders


def test_combine_orders_max_100():
    orders = [70, 30, 10]
    n_max = 100

    expected_orders = 2
    how_many = Orders().combine_orders(orders, n_max)
    assert how_many == expected_orders

def test_combine_orders_max_200():
    orders = [70, 30, 10, 95, 100]
    n_max = 200

    expected_orders = 3
    how_many = Orders().combine_orders(orders, n_max)

    assert how_many == expected_orders