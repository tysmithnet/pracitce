# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class TwoDiagonals:
    def maxPoints(self, x, y):
        coord = zip(x, y)
        coord = sorted(coord, lambda x, y: x[0] - y[0] if x[0] != y[0] else x[1] - y[1])
        back_slash = set([])
        forward_slash = set([])
        
        remain = coord[:]
        while len(remain) > 0:
            left = remain[0]
            remain = remain[1:]
            s = set([left])
            for c in coord:
                if c in s or c in back_slash:
                    continue
                dx = c[0] - left[0]
                dy = c[1] - left[1]
                if dx == -dy:
                    s.add(c)
                if len(s) > len(back_slash):
                    back_slash = set(s)

        remain = coord[:]
        while len(remain) > 0:
            right = remain[-1]
            remain = remain[:-1]
            s = set([right])
            for c in coord:
                if c in s or c in forward_slash:
                    continue
                dx = c[0] - right[0]
                dy = c[1] - right[1]
                if dx == dy:
                    s.add(c)
                if len(s) > len(forward_slash):
                    forward_slash = set(s)

        return len(back_slash.union(forward_slash))

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

def do_test(x, y, __expected):
    startTime = time.time()
    instance = TwoDiagonals()
    exception = None
    try:
        __result = instance.maxPoints(x, y);
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
    sys.stdout.write("TwoDiagonals (500 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("TwoDiagonals.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            x = []
            for i in range(0, int(f.readline())):
                x.append(int(f.readline().rstrip()))
            x = tuple(x)
            y = []
            for i in range(0, int(f.readline())):
                y.append(int(f.readline().rstrip()))
            y = tuple(y)
            f.readline()
            __answer = int(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(x, y, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1534060282
    PT, TT = (T / 60.0, 75.0)
    points = 500 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
