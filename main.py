def apriori(data,min_support):
    """Return frequent itemset of data
    data should be an iterable containing sets of items.
    (item can be any hashable type.)
    """

    def generate(sets):
        """sets should contain sets of same length.
        This iterator generator function yields union of every two sets included in sets. provided that the two sets have exactly one uncommon item.
        """
        for i in sets:
            for j in sets:
                if i != j:
                    new_set = i.union(j)
                    if len(new_set) == len(i)+1:
                        yield frozenset(new_set)

    #generate itemsets of size one.
    sets = [set().union(*map(lambda x: [frozenset(i)for i in x if sum(i in j for j in data) >= min_support],data))]

    #generate itemsets with sizes greater than 1
    while True:
        new_sets = {i for i in generate(sets[-1]) if sum(i.issubset(j) for j in data) >= min_support}
        if len(new_sets): sets.append(new_sets)
        else: break

    #returns the resulting itemsets with frequency of at least min_support
    return sets
