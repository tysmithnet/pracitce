# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

def partition(board):
    good = []
    bad = []
    for i in xrange(len(board)):
        for j in xrange(len(board[0])):
            if board[i][j] == ".":
                good.append((i, j))
            else:
                bad.append((i,j))
    return good, bad

class TurtleGame:
    def getwinner(self, board):
        #board = ["....", ".#..", "...#", ".#.."]
        l = len(board[0])
        h = len(board)
        all_nodes = [(i, j) for i in xrange(h) for j in xrange(l)]
        path_length = l + h - 1
        not_holes, holes = partition(board)
        start = (0, 0)
        end = (h - 1, l - 1)
        paths = []
        node_count = {}
        def help(loc, history):
            if loc == end:
                if history not in paths:
                    clone = history[:]
                    clone.append(end)
                    paths.append(clone)
                    for s in history:
                        if s not in node_count:
                            node_count[s] = 0
                        node_count[s] += 1
                return
            row = loc[0]
            col = loc[1]
            copy = history[:]
            copy.append(loc)
            if row < h and col + 1 < l and board[row][col + 1] == ".":
                help((row, col + 1), copy)
            if col < l and row + 1 < h and board[row + 1][col] == ".":
                help((row + 1, col), copy)               
        
        help(start, [])
        not_in_paths = set(not_holes) - set(node_count.keys()) - set(holes) - set([start, end])
        n = len(paths)

        is_player_1 = True
        game_over = False
        while not game_over:
            if not_in_paths:
                victim = not_in_paths.pop()
                holes.append(victim)
            else:
                victim = sorted(filter(lambda (k,v): v != 0 and (v,k) not in holes, node_count.iteritems()), key=lambda (k,v): (v,k))[0][0]
                counts = {}
                for i in paths:
                    for j in i:
                        if j not in counts:
                            counts[j] = 0
                        counts[j] += 1
                victim = None
                mn = float("inf")
                for count in counts:
                    if counts[count] < mn:
                        mn = counts[count]
                        victim = count
                
                holes.append(victim)
                dead_paths = filter(lambda p: victim in p, paths)
                live_paths = filter(lambda p: p not in dead_paths, paths)
                paths = live_paths
                still_in_paths = set([])
                for i in live_paths:
                    for j in i:
                        still_in_paths.add(j)
                if not live_paths:
                    game_over = True
                    break
                
                all_in_dead_paths = set([])
                for i in dead_paths:
                    for j in i:
                        all_in_dead_paths.add(j)

                to_be_added = all_in_dead_paths.difference(still_in_paths).difference(set(holes))
                not_in_paths = not_in_paths.union(to_be_added)

            if not game_over:
                is_player_1 ^= True

        return "Win" if not is_player_1 else "Lose"

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

def do_test(board, __expected):
    startTime = time.time()
    instance = TurtleGame()
    exception = None
    try:
        __result = instance.getwinner(board);
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
    sys.stdout.write("TurtleGame (500 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("TurtleGame.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            board = []
            for i in range(0, int(f.readline())):
                board.append(f.readline().rstrip())
            board = tuple(board)
            f.readline()
            __answer = f.readline().rstrip()

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(board, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1534064294
    PT, TT = (T / 60.0, 75.0)
    points = 500 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
