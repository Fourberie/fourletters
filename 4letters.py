def four_letters(names):
    res = 0
    for s in names.split(" "):
        print (s)
        if len(s) == 4:
            res += 1
    return res

four_letters("Tror Gvigris Deriana Nori")