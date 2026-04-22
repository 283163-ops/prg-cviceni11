import matplotlib.pyplot as plt
import random


# generator nahodnych cisel
def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]      #probehne to tolikrat kolikrat reknu,
                                 #volitelne parametry, rozmezi nula az sto                               # to je to podtrzitko


#selection sort - nestabilni radici algoritmus
def selection_sort(seznam):
    seznam = seznam[:]           # udela mi kopii seznamu, puvodni zustane beze zmeny
    n = len(seznam)

    for it in range(n):
        min_idx = it
        for idx in range(it + 1 , n):
            if seznam[idx] < seznam[min_idx]:
                min_idx = idx
        seznam[it], seznam[min_idx] = seznam[min_idx], seznam[it] # tohle musi byt venku z cyklu
    return seznam


# bubble sort: - serazene je nejvetsi cislo

def bubble_sort(seznam):
    seznam = seznam[:]
    n = len(seznam)
    plt.ion()
    plt.show()
    for it in range(n-1,): # for cyklus pres iterace
        for idx in range(n-1 - it):# rozmezi n-1 a potom je to mene o jednu iteraci
            if seznam[idx] > seznam[idx+1]:
                seznam[idx], seznam[idx+1] = seznam[idx+1], seznam[idx] # tenhle radek musi
                                        # byt na tomhle miste, a az potom ty dalsi RADKY
                index_highlight1 = idx
                index_highlight2 = idx + 1
                colors = ["steelblue"] * len(seznam)
                colors[index_highlight1] = "tomato"
                colors[index_highlight2] = "tomato"
                plt.clf()
                plt.bar(range(len(seznam)), seznam, color=colors)
                plt.title("Bubble Sort")
                plt.pause(0.1)
    plt.ioff()
    plt.show()          # do terminalu k nainstalovani matplotlibu uv pip install matplotlib

    return seznam    # slozitost = O n*(2) O n na druhou




def main():
    seznam = random_numbers(20, low=0, high=100)
    sorted_seznam = selection_sort(seznam)
    bubble_sorted = bubble_sort(seznam)
    print(bubble_sorted)



if __name__ == "__main__":
    print(main())

