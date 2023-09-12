resteraunts = ("Mcdonalds", "Chick-fil-a", "Taco Bell", "In n out")

new_res = input("What resteraunt would you like to rank into your list")

def rank_resteraunt(new_res, resteraunts):

    for i in range(len(resteraunts)):

        rank = input("do you like A)" + new_res + "more or B)" + resteraunts(i) + "more? A/B")

        if rank == "A":
            resteraunts.insert(i, new_res)
            break
        elif rank == "B":
            continue

    