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

def capital_city(data):
    for key, value in capital_cities.items():
        if value == data:
            for key2, value2 in states.items():
                if value2 == key:
                    print(key2)
                    return
    print("Unknown capital city")

if __name__ == '__main__':

    if (len(sys.argv) == 2):
        capital = sys.argv[1]
        capital_city(capital)