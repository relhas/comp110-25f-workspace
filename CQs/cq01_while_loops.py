__author__: str = "730661317"


def num_instances(phrase, search_char) -> int:
    count = 0
    index = 0
    while index < len(phrase):
        if phrase[index] == search_char:
            count += 1
            index += 1

    return count
