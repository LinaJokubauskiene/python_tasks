#
# Sukurkite klasę "Movie", kuri gebės sukurti objektus 3 savybėm ir 1 metodu.
# Naudojant šią klasę sukurkite bent du skirtingus objektus.

# Savybės:
# title: string
# director: string
# budget: number

# Metodas: 
# was_expensive() - jeigu filmo "budget" yra daugiau nei 100 000 000 mln USD, tada grąžins True, kitu atveju False.


class Movie:
    def __init__(self, title, director, budget):
        self.title = title
        self.director = director
        self.budget = budget

def __str__(self):
    print (f"{self.budget}")

Movie1 = Movie("Eternal Sunshine of the Spotless Mind", "Michale Goundry", 20000000)
Movie2 = Movie("Memento", "Christopher Nolan", 9000000)

def was_expensive(self):
    if self.budget >= 100000000:
     print("True")
    else:
     print ("False")

