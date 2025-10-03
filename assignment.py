def __optimal_subset_value(value: list[int], weight: list[int], Cmax: int) -> list[list[int]]:
    """
    Build the DP table for the 0/1 Knapsack problem.
    value[i] = value of item i
    weight[i] = weight of item i
    Cmax = capacity of the knapsack
    Returns the DP table S.
    """
    n = len(value)
    # Initialize DP table with zeros
    S = [[0] * (Cmax + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for r in range(1, Cmax + 1):
            if weight[i - 1] > r:
                S[i][r] = S[i - 1][r]
            else:
                S[i][r] = max(S[i - 1][r], S[i - 1][r - weight[i - 1]] + value[i - 1])
    return S


def __build_subset(value: list[int], weight: list[int], Cmax: int, S: list[list[int]]) -> list[int]:
    """
    Backtrack through the DP table S to find which items are included in the optimal subset.
    Returns a list of indices (0-based) of items chosen.
    """
    n = len(value)
    subset = []
    r = Cmax

    for i in range(n, 0, -1):
        if S[i][r] != S[i - 1][r]:  # Item i-1 was included
            subset.append(i - 1)
            r -= weight[i - 1]
    subset.reverse()
    return subset


def optimal_subset(value: list[int], weight: list[int], Cmax: int):
    """
    Wrapper: returns both the optimal value and the chosen subset.
    """
    S = __optimal_subset_value(value, weight, Cmax)
    subset = __build_subset(value, weight, Cmax, S)
    return S[len(value)][Cmax], subset
