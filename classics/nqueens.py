count = 0

# back tracking helper
def help(avail, col, n):
    global count
    if col == n:
        count += 1
        return
    first_avail = filter(lambda q: q[1] == col, avail)
    for i in first_avail:
        new_avail = filter(lambda q: q[0] != i[0] and q[1] != i[1] and abs(q[0] - i[0]) != abs(q[1] - i[1]), avail)
        help(new_avail, col + 1, n)

def num_ways(n):
    global count
    count = 0
    avail = set([])
    for i in xrange(n):
        for j in xrange(n):
            avail.add((i, j))

    help(avail, 0, n)
    return count

if __name__ == "__main__":
    assert(num_ways(1) == 1)
    assert(num_ways(2) == 0)
    assert(num_ways(3) == 0)
    assert(num_ways(4) == 2)
    assert(num_ways(5) == 10)
    assert(num_ways(6) == 4)
    assert(num_ways(7) == 40)
    assert(num_ways(8) == 92)
    assert(num_ways(9) == 352)
    assert(num_ways(10) == 724)
    print "SUCCESS!"