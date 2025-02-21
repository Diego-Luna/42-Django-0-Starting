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

def get_state_by_capital(capital):
    capital = capital.strip().title()

    for state_code, city in capital_cities.items():
        if city == capital:
            for state, code in states.items():
                if code == state_code:
                    return state
    return None

def get_capital_by_state(state):
    state = state.strip().title()

    if state in states:
        return capital_cities[states[state]]
    return None

def all_in(data):
    if not data :
        return

    data = data.split(",")
    info = [item.strip() for item in data]

    
    for item in info:
        if not item:
            continue
            
        capital = get_capital_by_state(item)
        state = get_state_by_capital(item)
        
        if capital:
            print(f"{capital} is the capital of {item.title()}")
        elif state:
            print(f"{item.title()} is the capital of {state}")
        elif len(item) > 0:
            print(f"{item} is neither a capital city nor a state")

if __name__ == '__main__':
    if len(sys.argv) == 2:
        all_in(sys.argv[1])