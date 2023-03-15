from src.question1 import Contract, Contracts

def test_get_top_5_open_contracts():
    contracts = [
        Contract(1, 100),
        Contract(2, 200),
        Contract(3, 300),
        Contract(4, 400),
        Contract(5, 500)
    ]
    renegotiated = [3]
    top_n = 3

    actual_open_contracts = Contracts().get_top_N_open_contracts(contracts, renegotiated, top_n)
    expected_open_contracts = [5, 4, 2]
    assert expected_open_contracts == actual_open_contracts


def test_get_top_5_open_contracts_list_10_contract_3_renegotiated():
    contracts = [
        Contract(1, 9000),
        Contract(8, 200),
        Contract(4, 400),
        Contract(5, 500),
        Contract(3, 300),
        Contract(7, 5150),
        Contract(6, 6507),
        Contract(2, 200),
        Contract(10, 100),
        Contract(9, 8000)
    ]
    renegotiated = [5,7,4]
    top_n = 3

    actual_open_contracts = Contracts().get_top_N_open_contracts(contracts, renegotiated, top_n)
    expected_open_contracts = [1, 9, 6]
    assert expected_open_contracts == actual_open_contracts


