# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

def prod(arr):
    return reduce(lambda a, c: a * c, arr, 1)

def first_too_small(a, b):
    p = prod(a)
    ps = pows(a, b)
    for i in xrange(len(ps) - 1, -1, -1):
        if ps[i] % p != 0:
            return i
    return -1

def pows(a, b):
    return map(lambda x: x[0] ** x[1], zip(a, b))

class DivisibleSetDiv2:
    def isPossible(self, b):
        b = list(reversed(sorted(b)))
        n = len(b)
        a = [2] * n
        f = first_too_small(a, b)
        if f == -1:
            return "Possible"
        triggered = False
        i = 0
        history = []
        while f != -1 and not triggered:
            s = """
            *********{iteration}*********
            f:    {f}
            a:    {a}
            b:    {b}
            pows: {pows}
            p:    {p}
            hist: {hist}
            *****************************
            """.format(iteration=i, f=f, a=",".join(map(str,a)), b=",".join(map(str,b)), pows=",".join(map(str, pows(a,b))), p=prod(a), hist=",".join(map(str,history)))
            #print(s)
            i += 1
            history.append(f)
            if len(history) >= 60:
                last_sixty = history[:-59]
                if 0 in last_sixty or len(set(last_sixty)) <= 2:
                    return "Impossible"
            
            pa = prod(a)
            while a[f] ** b[f] % pa != 0:
                a[f] *= 2
            f = first_too_small(a, b)

        return "Possible"

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

def do_test(b, __expected):
    startTime = time.time()
    instance = DivisibleSetDiv2()
    exception = None
    try:
        __result = instance.isPossible(b);
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
    sys.stdout.write("DivisibleSetDiv2 (550 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("DivisibleSetDiv2.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            b = []
            for i in range(0, int(f.readline())):
                b.append(int(f.readline().rstrip()))
            b = tuple(b)
            f.readline()
            __answer = f.readline().rstrip()

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(b, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1534027782
    PT, TT = (T / 60.0, 75.0)
    points = 550 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
