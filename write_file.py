with open("compound_interest.txt", "wt") as out:
    for i in range(10):
        out.write(f"=======================\n")
        print(i, file=out)
        out.write(f"=======================\n")
