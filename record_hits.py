import time

index = 0
hit = {}


def main():
    global hit
    result = 0

    for i in xrange(500):
        time.sleep(0.01)
        hit_web()

    for item in hit.values():
        result = result + item
    print result


def hit_web():

    global index
    global hit
    index = int(time.time())
    try:
        hit[index % 3600] += 1
    except KeyError:
        hit[index % 3600] = 1

if __name__ == "__main__":
    main()
