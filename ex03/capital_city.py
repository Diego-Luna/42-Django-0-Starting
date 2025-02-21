import sys

states = {
    "Oregon" : "OR",
    "Alabama" : "AL",
    "New Jersey": "NJ",
    "Colorado" : "CO"
}
capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
}

def capital_city(capital):
    if capital in states:
        print(capital_cities[states[capital]])
    else:
        print("Unknown state")

if __name__ == '__main__':

    if (len(sys.argv) == 2):
        capital = sys.argv[1]
        capital_city(capital)