# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class MinProduct:
    def findMin(self, amount, blank1, blank2):
        d = {i:amount[i] for i in xrange(len(amount))}
        (blank1, blank2) = (blank2, blank1) if blank2 < blank1 else (blank1, blank2)        
        small_n = min(blank1, blank2)
        if d[0] >= small_n:
            return 0
        a = [None] * blank1
        len_a = 0
        b = [None] * blank2
        len_b = 0
        is_a = True
        while not (len_a == blank1 and len_b == blank2):
            for i in xrange(10):
                if d[i]:
                    if i == 0:
                        how_many = d[0]
                        actually_used = min(how_many, len(a))
                        d[0] -= actually_used
                        did_set = False
                        for x in xrange(actually_used):
                            did_set = True
                            a[x] = 0
                            len_a += 1
                        if did_set:
                            break
                    else:
                        d[i] -= 1
                    if is_a and len_a < blank1:
                        a[len_a] = i
                        len_a += 1
                    else:
                        b[len_b] = i
                        len_b += 1
                    is_a ^= True
                    break

        mn = int("".join(map(str, a))) * int("".join(map(str, b)))

        small_n = min(len_a, len_b)

        for i in xrange(small_n):
            for j in xrange(i, small_n):
                copy_a = a[:]
                copy_b = b[:]
                (copy_a[j], copy_b[j]) = (copy_b[j], copy_a[j])
                copy_a = int("".join(map(str, copy_a)))
                copy_b = int("".join(map(str, copy_b)))
                if copy_a * copy_b < mn:
                    mn = copy_a * copy_b

        return mn

# CUT begin
# TEST CODE FOR PYTHON {{{
import sys, time, math

def tc_equal(expected, received):
    try:
        _t = type(expected)
        received = _t(received)
        if _t == list or _t == tuple:
            if len(expected) != len(received): return False
            return all(tc_equal(e, r) for (e, r) in zip(expected, received))
        elif _t == float:
            eps = 1e-9
            d = abs(received - expected)
            return not math.isnan(received) and not math.isnan(expected) and d <= eps * max(1.0, abs(expected))
        else:
            return expected == received
    except:
        return False

def pretty_str(x):
    if type(x) == str:
        return '"%s"' % x
    elif type(x) == tuple:
        return '(%s)' % (','.join( (pretty_str(y) for y in x) ) )
    else:
        return str(x)

def do_test(amount, blank1, blank2, __expected):
    startTime = time.time()
    instance = MinProduct()
    exception = None
    try:
        __result = instance.findMin(amount, blank1, blank2);
    except:
        import traceback
        exception = traceback.format_exc()
    elapsed = time.time() - startTime   # in sec

    if exception is not None:
        sys.stdout.write("RUNTIME ERROR: \n")
        sys.stdout.write(exception + "\n")
        return 0

    if tc_equal(__expected, __result):
        sys.stdout.write("PASSED! " + ("(%.3f seconds)" % elapsed) + "\n")
        return 1
    else:
        sys.stdout.write("FAILED! " + ("(%.3f seconds)" % elapsed) + "\n")
        sys.stdout.write("           Expected: " + pretty_str(__expected) + "\n")
        sys.stdout.write("           Received: " + pretty_str(__result) + "\n")
        return 0

def run_tests():
    sys.stdout.write("MinProduct (500 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("MinProduct.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            amount = []
            for i in range(0, int(f.readline())):
                amount.append(int(f.readline().rstrip()))
            amount = tuple(amount)
            blank1 = int(f.readline().rstrip())
            blank2 = int(f.readline().rstrip())
            f.readline()
            __answer = int(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(amount, blank1, blank2, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1534054730
    PT, TT = (T / 60.0, 75.0)
    points = 500 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
