class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores) #zjistuje pocet studentu

    def get_grade(self, index): # dam si novou definici metody
        score = self.get_by_index(index)
        if score < 50:
            return "F"
        elif 50 <= score < 60:
            return "E"
        elif 60 <= score < 70:
            return "D"
        elif 70 <= score < 80:
            return "C"
        elif 80 <= score < 90:
            return "B"
        elif 90 <= score <= 100:
            return "A"

    def find(self, score):
        idx = 0
        count = 0
        positions = []
        searched_data = self.scores
        while idx < len(searched_data):
            if searched_data == score:
                positions.append(idx)
            idx += 1
        return positions
    def get_sorted(self):
        seznam = self.scores[:]
        n = len(seznam)
        for it in range(n - 1, ):  # for cyklus pres iterace
            for idx in range(n - 1 - it):  # rozmezi n-1 a potom je to mene o jednu iteraci
                if seznam[idx] > seznam[idx + 1]:

                    seznam[idx], seznam[idx + 1] = seznam[idx + 1], seznam[idx]
        return seznam

def main():
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
    print(results.count())
    for student_id in range(len(results.count())):
        print(f"Student {student_id}: {results.get_by_index(student_id)} points - {results.get_grade(student_id)}")
    print(f"plny poset bodu meli studenti: {results.find(student_id)}")
    print(f"Serazene vysledky: {}")
    random_results = StudentGrades(random_numbers())

if __name__ == "__main__":
    main()