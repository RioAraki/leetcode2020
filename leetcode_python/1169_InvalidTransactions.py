import collections

def invalidTransactions(transactions):
    people = collections.defaultdict(list)
    ret = []
    for i in transactions:
        name, time, price, place = i.split(",")
        time = int(time)
        price = int(price)
        people[name].append((time, price, place))


    for j in people.keys():
        invalidSet = set()
        people[j].sort()
        tmp = people[j]
        n = len(people[j])
        print(tmp)
        for k in range(n):
            if tmp[k][1] > 1000:
                invalidSet.add(tmp[k])
            i = 1
            while k + i < n:
                if tmp[k + i][0] - tmp[k][0] <= 60:
                    if tmp[k + i][2] != tmp[k][2]:
                        invalidSet.add(tmp[k])
                        invalidSet.add(tmp[k + i])
                else:
                    break
                i += 1

        for inv in invalidSet:
            ret.append(j + "," + str(inv[0]) + "," + str(inv[1]) + "," + inv[2])

    return ret

if __name__ == "__main__":
    transactions = ["bob,689,1910,barcelona","alex,696,122,bangkok","bob,832,1726,barcelona","bob,820,596,bangkok","chalicefy,217,669,barcelona","bob,175,221,amsterdam"]
    print(invalidTransactions(transactions))