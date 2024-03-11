import random

word_list = {
    "male":
        {
            "Simon",
            "Joseph",
            "Lazarus",
            "Judah",
            "John",
            "Jesus",
            "Ananias",
            "Jonathan",
            "Matthew",
            "Manaen",
            "James",
            "Michael"
        },
        "female":
        {
            "Mary",
            "Salome",
            "Shelamzion",
            "Martha",
            "Joanna",
            "Sapphira",
            "Berenice",
            "Imma",
            "Mara",
            "Cyprus",
            "Sarah",
            "Alexandra"
        }
}

def random_name():
    # Randomly select one of the values of either set male or female
    x = random.choice(list(word_list.values()))
    # Randomly select one of the names from the selected set
    y = random.choice(list(x))
    return y


def main():
    for x in word_list:
        print(x)
        for y in word_list[x]:
            print(y)


if __name__ == "__main__":
    #main()
    print(random_name())