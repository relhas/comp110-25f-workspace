"""this program simulates a tea party"""

__author__: str = "730661317"


def main_planner(guests: int) -> None:
    """start of program, calculates and prints tea bags, treats, and total cost"""
    tea_needed = tea_bags(guests)
    treats_needed = treats(guests)
    total_cost = cost(tea_needed, treats_needed)

    # prints formatted output
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("")
    print("Tea Bags: " + str(tea_needed))
    print("")
    print("Treats: " + str(treats_needed))
    print("")
    print("Cost: $" + str(total_cost))


# no return needed (returns none)


def tea_bags(people: int) -> int:
    """calculating the number of tea bags needed for the tea party
    each guest needs 2 tea bags
    args: people
    returns: total tea bags needed"""
    return people * 2


def treats(people: int) -> int:
    """calculate the number of treats needed for the tea party.
    for each tea a guest drinks, 1.5 treats
    arg: people
    return: number of treats needed"""
    tea = tea_bags(people=people)
    return int(tea * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """calculates the total set of tea bags and treats that are needed.
    each tea bag is $0.50 and each treat is $0.75
    arg: numer of tea bags needed and the number of treats needed
    return: total cost of both tea bags and treats"""

    tea_cost = tea_count * 0.50  # 0.50 per tea bag
    treat_cost = treat_count * 0.75  # 0.75 per treat bag
    return tea_cost + treat_cost  # returns float


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
