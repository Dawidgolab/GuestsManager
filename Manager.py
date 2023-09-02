def Remove(name, guest_list):
    if name in guest_list:
        guest_list.remove(name)
        print(name,"has been removed correctly!")
        save_guest_list(guest_list)
    else:
        print("You gave the wrong data!")

def Search(name,guest_list):
    if name in guest_list:
        print(name,"is on the list!")
    else:
        print(name," is not on the list!!!")

# Funkcja do zapisywania listy gości do pliku
def save_guest_list(guest_list):
    with open('guests.txt', "w") as file:
        for guest in guest_list:
            file.write(f"{guest}\n")
    print("Guest list saved to", 'guests.txt')

# Funkcja do wczytywania listy gości z pliku (jeśli istnieje)
def load_guest_list():
    try:
        with open('guests.txt', "r") as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        return []