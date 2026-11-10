import csv
import os
from datetime import date
from exercises import EXERCISES
from trainings import TRAININGS
DIARY_PATH = "dziennik.csv"

class Trening:
    def __init__(self, name_trening, date): 
        self.name_trening = name_trening
        self.date = date
        self.serie = []
    class Seria:
        def __init__(self, exercise, weight, reps, rir):
            self.exercise = exercise
            self.weight = weight
            self.reps = reps
            self.rir = rir
        def __str__(self):
            return f"{self.exercise}: {self.weight}kg x {self.reps} - {self.rir}rir"



    def add_seria(self, exercise, weight, reps, rir):
        new_seria = self.Seria(exercise, weight, reps, rir)
        self.serie.append(new_seria)

    def list_seria(self):
        return self.serie

    def save_trening(self, path):
        file_exists = os.path.exists(path)

        with open(path, "a", newline="") as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["date", "trening", "exercise", "weight", "reps", "rir"])
            for s in self.serie:
                writer.writerow([self.date, self.name_trening, s.exercise, s.weight, s.reps, s.rir])

    def total_volume(self):
        return sum(s.weight * s.reps for s in self.serie)
        

    def count_serie(self):
        return len(self.serie)
            



def get_float(prompt):
    while True:
        try:
            return float(input(prompt).replace(",", "."))
        except ValueError:
            print("Enter a number")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Enter a number")

def choose_exercise(exercises):
    for i, exercise in enumerate(exercises, start=1):
        print(f"{i}. {exercise}")
    print("0. finish")

    while True:
        number = get_int("Choose exercise: ")
        if number == 0:
            return None
        elif 1 <= number <= len(exercises):
            return exercises[number - 1]
        else:
            print("Enter right number")

def choose_training(trainings):
    for i, training in enumerate(trainings, start=1):
        print(f"{i}. {training} ")
    print("0. finish")

    while True:
        number = get_int("Choose training: ")
        if number == 0:
            return None
        elif 1 <= number <= len(trainings):
            return trainings[number - 1]
        else:
            print("Enter right number")

def get_last_seria(path, exercise):
    file_exists = os.path.exists(path)
    last = None
    if not file_exists:
        return None

    with open(path, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["exercise"] == exercise:
                last = row
        return last

def get_int_in_range(prompt, min_value, max_value):
    while True:
        try:
            value = int(input(prompt))
            if min_value <= value <= max_value:
                return value
            else:
                print(f"number must be between ({min_value}-{max_value})")

        except ValueError:
            print("Use number")






def main():
    today = date.today()
    name_trening = choose_training(TRAININGS)
    trening = Trening(name_trening, today)
    if trening is None:
        print("Thank you")

    while True:

        exercise = choose_exercise(EXERCISES)
        if exercise is None:
                print("Thank you")
                break
        
        last = get_last_seria(DIARY_PATH, exercise)
        if last is None:
            print("No previous data")
        else:
            print(f"{last['date']}: {last['weight']} x {last['reps']} - {last['rir']} rir")

        weight = get_float("Weight: ")
        reps = get_int_in_range("Reps: ", 1, 50)
        rir  = get_int_in_range("RIR: ", 0, 10)

        trening.add_seria(exercise, weight, reps, rir)

    print(trening.name_trening)
    print(trening.date)
    print("----------------")

    for seria in trening.list_seria():
        print(seria)
    trening.save_trening(DIARY_PATH)
    print(f"total volume = {trening.total_volume()} kg")
    print(f"total series = {trening.count_serie()}")

if __name__ == "__main__":
    main()