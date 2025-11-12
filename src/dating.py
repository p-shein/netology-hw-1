def get_pairs(boys, girls):
    boys.sort()
    girls.sort()
    if len(boys) != len(girls):
        print("Внимание, кто-то может остаться без пары.")
        return

    print("Идеальные пары:")

    for boy, girl in zip(boys, girls):
        print(f"{boy} и {girl}")

get_pairs(['Peter', 'Alex', 'John', 'Arthur', 'Richard', 'Michael'], ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha'])
