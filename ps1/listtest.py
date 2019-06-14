"""
This is where I start to mess around with lists
"""

lst = list(range(1, 100))

def FindBest(lst):
    lstlen = len(lst)
    save_pct = lst[lstlen - 50]
    print(save_pct)


FindBest(lst)