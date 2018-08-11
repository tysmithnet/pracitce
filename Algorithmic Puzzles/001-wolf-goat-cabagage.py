from pprint import pprint as pp

def calc():
    def help(left, is_left, right, so_far):
        if len(left) == 0:
            new_so_far = so_far[:]
            new_so_far.append((left, is_left, right))
            pp(new_so_far)
            return
        if is_left: #if we are on the left, then we came from the right so we must make sure that is ok
            if set("WG").issubset(right) or set("GC").issubset(right) or (left, True, right) in so_far:
                return
            new_so_far = so_far[:]
            new_so_far.append((left, is_left, right))
            # try to take each thing out of left and send to the right
            for i in left.union(set([None])):
                new_left = left.difference(set(i)) if i is not None else left
                new_right = right.union(set(i)) if i is not None else right
                help(new_left, False, new_right, new_so_far)
        else:
            if set("WG").issubset(left) or set("GC").issubset(left) or (left, False, right) in so_far:
                return
            new_so_far = so_far[:]
            new_so_far.append((left, is_left, right))
            # try to take each thing out of left and send to the right
            for i in left.union(set([None])):
                new_left = left.difference(set(i)) if i is not None else left
                new_right = right.union(set(i)) if i is not None else right
                help(new_left, False, new_right, new_so_far)
    
    help(set("CGW"), True, set([]), [])

if __name__ == "__main__":
    calc()
