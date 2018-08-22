k = 3
mydict = {}


def insert(str):
    global k
    global mydict

    try:
        mydict[len(str)] = mydict[len(str)].append(str)
    except KeyError:
        mydict[len(str)] = [str]

    sortedKeys = sorted(mydict.iterkeys())
    # mydict = sorted(mydict, key=lambda item: item[0], reverse=True)

    inserted = 0

    for key in sortedKeys:
        if inserted > k:
            del mydict[key]
        else:
            inserted += 1
            continue


def lookup(k):
    global mydict
    for key, val in mydict.items():
        print val


insert("That is")
insert("nothing")
insert("Compare to")
insert("What I have gone through")
insert("This")
lookup(3)
