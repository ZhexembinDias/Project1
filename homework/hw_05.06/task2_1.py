def superset(set1: set,set2: set):
    if set1 == set2:
        print("Множества равны")
    elif set1.issuperset(set2):
        print("Set1 является супермножеством для set2")
    elif set2.issuperset(set1):
        print("Set2 является супермножеством для set1")
    else:
        print("Супермножество не обнаружено")

set1 = {1, 2, 3, 4}
set2 = {2, 3}

superset(set1, set2)