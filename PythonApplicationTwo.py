answer = input("What is the tallest mountain on earth from the base? Options: A) Mt. Everest, Nepal B) Mauna Kea, "
               "Hawaii C) K2, Pakistan D) Kilimanjaro, Africa\n>>> ")
if answer == "B":
    print("Good")

else:
    while answer not in ("B",):
        answer = input("WRONG ANSWER! or you didn't type A, B, C, or D.\n>>> ")
    print("Good")

answertwo = input("What is the biggest sea in the world? Options: A) Caspian Sea B) Baltic Sea C) Black Sea D) "
                  "Mediterranean Sea\n>>> ")
if answertwo == "D":
    print("Good")
else:
    while answertwo not in ("D",):
        answertwo = input("WRONG ANSWER! or you didn't type A, B, C, or D.\n>>> ")
    print("Good")
answerthree = input(
    "What's the deepest part of the ocean? A) Challenger Deep, Mariana Trench (Pacific) B) Puerto Rico Trench ("
    "Caribbean Sea) C) Philippine Trench (Pacific) D) Tonga Trench (Pacific)\n>>> ")
if answerthree == "A":
    print("Good")

else:
    while answerthree not in ("A",):
        answerthree = input("WRONG ANSWER! or you didn't type A, B, C or D.\n>>> ")
    print("Good")
answerfour = input("What percent of the world's population resides in Asia? A) 56% B) 70% C) 98% D) 60%")

if answerfour == "D":
    print("Good")

else:
    while answerfour not in ("D",):
        answerfour = input("WRONG ANSWER! Or you didn't type A, B, C, or D.\n>>>")


