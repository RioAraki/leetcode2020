def fullJustify(words, maxWidth):
    """
    :type words: List[str]
    :type maxWidth: int
    :rtype: List[str]
    """

    ret = []
    w_count, ch_count = 0, 0
    tmp = []
    idx = 0

    while idx < len(words):
        print(words[idx])

        if w_count + ch_count + len(words[idx]) <= maxWidth:
            tmp.append(words[idx])
            w_count += 1
            ch_count += len(words[idx])
            idx += 1

        else:
            line = ""
            space = maxWidth - ch_count
            if w_count == 1:
                line += words[idx - 1] + " " * (maxWidth - len(words[idx - 1]))
            else:
                space_list = [space // (w_count - 1) for i in range(w_count - 1)]
                for x in range(space % (w_count - 1)):
                    space_list[x] += 1
                    # print(space_list, space, w_count-1, tmp)
                for j in range(len(space_list)):
                    line += tmp[j] + " " * space_list[j]
                line += tmp[-1]
            ret.append(line)
            tmp, w_count, ch_count = [], 0, 0

    lastline = ""
    for i in tmp:
        lastline += i + " "
    ret.append(lastline[:-1] + (maxWidth - len(lastline[:-1])) * " ")
    return ret