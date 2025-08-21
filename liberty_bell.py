import random

def payout():
    global nickel_konto_spieler
    global nickel_konto_machine
    if player_combination_1.count('Hufeisen') >= 2:
        print("juhu, du hast gewonnen! :D")
        nickel_konto_spieler['nickel'] += 1
        nickel_konto_machine['nickel'] -= 1
    elif player_combination_1.count('Glocke') == 3:
        print("juhu, du hast gewonnen! :D")
        nickel_konto_spieler['nickel'] += 10
        nickel_konto_machine['nickel'] -= 10
    elif player_combination_1.count('Herz') == 3:
        print("juhu, du hast gewonnen! :D")
        nickel_konto_spieler['nickel'] += 8
        nickel_konto_machine['nickel'] -= 8
    elif player_combination_1.count('Karo') == 3:
        print("juhu, du hast gewonnen! :D")
        nickel_konto_spieler['nickel'] += 6
        nickel_konto_machine['nickel'] -= 6
    elif player_combination_1.count('Pik') == 3:
        print("juhu, du hast gewonnen! :D")
        nickel_konto_spieler['nickel'] += 4
        nickel_konto_machine['nickel'] -= 4
    elif ['Hufeisen', 'Hufeisen', 'Herz'] in all_combinations:
        print("juhu, du hast gewonnen! :D")
        nickel_konto_spieler['nickel'] += 2
        nickel_konto_machine['nickel'] -= 2
    elif ['Hufeisen', 'Hufeisen', 'Herz'] in all_combinations:
        print("juhu, du hast gewonnen! :D")
        nickel_konto_spieler['nickel'] += 2
        nickel_konto_machine['nickel'] -= 2
    else:
        print("Leider kein Gewinn :(")
        nickel_konto_spieler['nickel'] -= 1
        nickel_konto_machine['nickel'] += 1


def drehrad():
    global all_combinations
    global player_combination_1
    symbole_1 = ['Glocke', 'Karo', 'Herz', 'Pik', 'Hufeisen'] 
    symbole_2 = ['Glocke', 'Karo', 'Herz', 'Pik', 'Hufeisen']
    symbole_3 = ['Glocke', 'Karo', 'Herz', 'Pik', 'Hufeisen']

    rad_1 = random.choice(symbole_1)
    rad_2 = random.choice(symbole_2)
    rad_3 = random.choice(symbole_3)
    print(rad_1)
    print(rad_2)
    print(rad_3)
    # Alle möglichen Kombinationen
    player_combination_1 = []
    player_combination_2 = []
    player_combination_3 = []
    player_combination_4 = []
    player_combination_5 = []
    player_combination_6 = []
    
    player_combination_1.append(rad_1)
    player_combination_1.append(rad_2)
    player_combination_1.append(rad_3)

    player_combination_2.append(rad_1)
    player_combination_2.append(rad_3)
    player_combination_2.append(rad_2)

    player_combination_3.append(rad_2)
    player_combination_3.append(rad_1)
    player_combination_3.append(rad_3)

    player_combination_4.append(rad_2)
    player_combination_4.append(rad_3)
    player_combination_4.append(rad_1)

    player_combination_5.append(rad_3)
    player_combination_5.append(rad_1)
    player_combination_5.append(rad_2)

    player_combination_6.append(rad_3)
    player_combination_6.append(rad_2)
    player_combination_6.append(rad_1)
    
    all_combinations = [
    player_combination_1,
    player_combination_2,
    player_combination_3,
    player_combination_4,
    player_combination_5,
    player_combination_6]



player_money = int(input("Mit wie vielen Nickel möchtest du spielen? "))
nickel_konto_spieler = {"nickel":player_money}
nickel_konto_machine = {"nickel" : 20}

while True:
    if nickel_konto_spieler['nickel'] <= 0:
        print("Du bist Pleite :(")
        break
    if nickel_konto_machine['nickel'] <= 0:
        print("Die Machine ist Pleite :(")
        break
    spielen = input("Bist du bereit zu spielen? j/n ")
    if spielen == "j":
        drehrad()
        payout()
        print(f"Dein Kontostand ist: {nickel_konto_spieler['nickel']}\n")
    if spielen == "n":
        print("Goodbye")
        break

