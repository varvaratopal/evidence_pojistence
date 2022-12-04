from Evidence import Evidence


def mainLoop():
    evidence = Evidence()
    while True:
        # Zobrazí menu s volbou akce
        vyber = evidence.menu()
        if vyber == 4:
            print("\nKonec...")
            break
        elif vyber == 1:
            evidence.pridatPojistence()
        elif vyber == 2:
            evidence.vypsat()
        else:
            evidence.vyhledat()


if __name__ == '__main__':
    print("----------------------------")
    print("Evidence pojištěných")
    print("----------------------------")
    mainLoop()




