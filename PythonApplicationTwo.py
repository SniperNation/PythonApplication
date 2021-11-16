answer = input("What is the tallest mountain on earth from the base? Options: A) Mt. Everest, Nepal B) Mauna Kea, "
               "Hawaii C) K2, Pakistan D) Kilimanjaro, Africa\n>>> ")
if answer == "B":
    print("Good")

while answer not in ("B",):
    answer = input("WRONG ANSWER! or you didn't type A, B, C, or D.\n>>> ")

answertwo = input("What is the biggest sea in the world? Options: A) Caspian Sea B) Baltic Sea C) Black Sea D) "
                  "Mediterranean Sea\n>>> ")
if answertwo == "D":
    print("Good")

while answertwo not in ("D",):
    answertwo = input("WRONG ANSWER! or you didn't type A, B, C, or D.\n>>> ")

answerthree = input(
    "What's the deepest part of the ocean? A) Challenger Deep, Mariana Trench (Pacific) B) Puerto Rico Trench ("
    "Caribbean Sea) C) Philippine Trench (Pacific) D) Tonga Trench (Pacific)\n>>> ")
if answerthree == "A":
    print("Good")

while answerthree not in ("A",):
    answerthree = input("WRONG ANSWER! or you didn't type A, B, C or D.\n>>> ")
