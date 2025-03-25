def find_element(list, predicate):
    return next((x for x in list if predicate(x)), None)