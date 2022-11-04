def phoneCalls(start, duration, volume):
    intervals = []
    for (s, d, v) in zip(start, duration, volume):
        intervals.append([s, d, v])

    intervals = sorted(intervals, key=lambda x: x[2])
    intervals = sorted(intervals, key=lambda x: x[0])

    start, duration, end, volume = 0, 1, 1, 2
    for interval in intervals:
        interval[end] = interval[start] + interval[duration]

    # Get the 1st interval, assuming it's not overlapping
    res = []
    start, duration = 0, 1
    for idx, interval in enumerate(intervals):
        if idx == 0:
            res.append(interval)
            continue

        prev = res[-1]
        cur = interval

        if cur[start] <= prev[end]:  # Overlapping
            res[-1][end] = min(prev[end], cur[end])  # Serve the call with Min duration(Or MaxProfit???)
        else:  # Non-overlapping, serve
            res.append(cur)



    totalVolume = 0
    for r in res:
        totalVolume += r[volume]


    print(res, totalVolume)
    return totalVolume


start = [1, 2, 4]
duration = [2, 2, 1]
volume = [1, 2, 3]
phoneCalls(start, duration, volume)
