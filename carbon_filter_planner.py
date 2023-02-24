import itertools


def filter_plan(input_str):
    n = len(input_str)
    result = list(input_str)
    for i in range(n):
        if result[i] == "?":
            # try to fit "a"
            if i < 2 or result[i-2] != "a" and result[i-1] != "a":
                result[i] = "a"
            # try to fit "b" if "a" doesn't work
            elif i < 2 or result[i-2] != "b" and result[i-1] != "b":
                result[i] = "b"

    # generate all possible combinations of "a" and "b"
    options = [''.join(combo) for combo in itertools.product(['a', 'b'], repeat=n)]

    # remove invalid options (containing "aaa" or "bbb")
    options = [opt for opt in options if "aaa" not in opt and "bbb" not in opt]

    # find the best option
    best_option = min(options, key=lambda opt: sum([1 for i in range(n) if opt[i] != result[i]]))

    return best_option
