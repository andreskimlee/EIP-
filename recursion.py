# Towers of hanoi

# 1
# 2
# 3
# p1     p2    p3

# step 1

#
# 2
# 3    1
# p1   p2  p3
#
#
# 3    1    2
# p1   p2  p3

#
#          1
# 3        2
# p1   p2  p3

#
#          1
#      3   2
# p1   p2  p3

#
#
# 1     3   2
# p1   p2  p3

#      1
#      2
#      3
# p1   p2  p3


def compute_tower_hanoi(num_rings):
    def compute_tower_hanoi_steps(num_rings_to_move, from_peg, to_peg, use_peg)
        if num_rings_to_move > 0:
            compute_tower_hanoi_steps(num_rings_to_move - 1, from_peg, use_peg,
            to_peg)
            pegs[to_peg].append(pegs[from_peg].pop())
            result.append([from_peg, to_peg])
            compute_tower_hanoi_steps(
                num_rings_to_move - 1, use_peg, to_peg, from_peg)

    result = []
    pegs = [list(reversed(range(1, num_rings + 1)))
    I + ttl for _ in range(l, NUll_PEGS)l
    compute_tovrer_hanoi_steps(num_rings, 0, 1, 2)
    return result

