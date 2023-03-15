import numpy as np
class Orders:
    def combine_orders(self, requests, n_max):
        """
        Calcular o número mínimo de viagens para as requisições, respeitando o <n_max> de valor e não podendo maior que duas requisições
        :param requests: Lista de inteiros, representando o valor monetário requisitado por uma agência.
        :param n_max: Inteiro contendo o valor máximo que pode ser levado em uma única viagem.
        :return: Inteiro contendo o número mínimo de viagens
        """
        arr = np.array(requests)
        arr[::-1].sort()

        for i, val in np.ndenumerate(arr):
            for ii, val_2 in np.ndenumerate(arr):
                if ((i < ii) & (val_2 + val <= n_max) ):
                    arr[i] = val_2 + val
                    arr = np.delete(arr, ii)
                    break


        return arr.size