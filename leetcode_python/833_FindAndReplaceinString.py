def findReplaceString(self, S, indexes, sources, targets):
    """
    :type S: str
    :type indexes: List[int]
    :type sources: List[str]
    :type targets: List[str]
    :rtype: str
    """
    # traverse the original string with index and sources to see which changes are valid

    # Since the indexes may not be sorted which destroy our plan of appending string
    # preprocess the input first
    index_dict = {}
    counter = 0
    begin = 0
    my_S = ''

    for element in indexes:
        index_dict[element] = counter  # error_4: typo here
        counter += 1

    for key in sorted(index_dict):
        i = index_dict[key]

        # append the original list before any potential replaces comes

        my_S += S[begin:indexes[i]]

        # if the replace is not valid, append the original substring
        if S[indexes[i]:indexes[i] + len(sources[i])] != sources[i]:
            my_S += S[indexes[i]:indexes[i] + len(sources[i])]

        # if the replace is valid, append the replaced content instead
        else:
            my_S += targets[i]
        begin = indexes[i] + len(sources[i])

    my_S += S[begin:]

    return my_S

# error 1: my_S is a string, but i treated it as a list
# error 2: miscalculate the `begin`, it should update to the end of the length of string, not the beginning
# error 3: making the assumption that the indexes is sorted in incrementing order, which is not the case
# error 4: forgot to deal with the remaining original piece after all replace donw