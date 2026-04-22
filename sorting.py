
import random


# generator nahodnych cisel
def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]      #probehne to tolikrat kolikrat reknu,
                                 #volitelne parametry, rozmezi nula az sto                               # to je to podtrzitko




small = random_numbers(5, low=0, high=20)  # 5 čísel v rozsahu 0–20

#selection sort - nestabilni radici algoritmus
def selection_sort(seznam):
    seznam = seznam[:]           # udela mi kopii seznamu, puvodni zustane beze zmeny
    n = len(seznam)
    for it in range(n):
        min_idx = it
        for idx in range(it + 1 , n):
            if seznam[idx] < seznam[min_idx]:
                min_idx = idx
        seznam[it], seznam[min_idx] = seznam[min_idx], seznam[it]
    return seznam

def main():
    seznam = random_numbers(10, low=0, high=100)
    sorted_seznam = selection_sort(seznam)
    print(sorted_seznam)







if __name__ == "__main__":
    print(main())

