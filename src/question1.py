from collections import defaultdict
from functools import total_ordering

@total_ordering
class Contract():
    def __init__(self, id, debt):
        self.id = id
        self.debt = debt

    def __str__(self):
        return 'id={}, debt={}'.format(self.id, self.debt)

    def __lt__(self, other):
        return self.debt < other.debt

class Contracts:
    def get_top_N_open_contracts(self, open_contracts, renegotiated_contracts, top_n):
        """
        Gera um lista de contratos abertos desconsiderando os contratos já negociados.
        :param open_contracts: Uma lista em que cada elemento é uma instância de Contract,
        :param renegotiated_contracts: Uma lista de numeros inteiros (int) representando os identificadores dos associados que já renegociaram seus débitos
        :param top_n: Um inteiro com a quantidade de devedores que devem ser retornados pelo método.
        :return: Retornar uma lista contendo top_n inteiros referentes aos identificadores dos devedores, ordenada do maior devedor para o menor.
        """

        not_renegotiated_contracts = defaultdict(Contract)
        not_renegotiated_contracts = [obj for obj in open_contracts if obj.id not in renegotiated_contracts]
        not_renegotiated_contracts = sorted(not_renegotiated_contracts, reverse=True)

        top = list([obj.id for obj in not_renegotiated_contracts[:top_n]])

        return top
