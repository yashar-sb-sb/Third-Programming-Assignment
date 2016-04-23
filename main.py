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

    #generate frequent itemsets of size one.
    sets = [set().union(*map(lambda x: [frozenset(i)for i in x if sum(i in j for j in data) >= min_support],data))]

    #generate frequent itemsets with sizes greater than 1
    while True:
        new_sets = {i for i in generate(sets[-1]) if sum(i.issubset(j) for j in data) >= min_support}
        if len(new_sets): sets.append(new_sets)
        else: break

    #returns the resulting itemsets with frequency of at least min_support
    return sets

def main():
    import sys,re
    regx = re.compile(r"[\n\t ]")
    input_file = open(sys.argv[1], 'r')
    lines = iter(input_file.readlines())
    next(lines)
    for i in apriori([{*i.split(';')}for i in list(zip(*[re.sub(regx,'',j).split(',')for j in lines]))[1]],int(sys.argv[2])):
        for j in i:
            print('{',', '.join(j),'}')

if __name__ == '__main__':
    main()
