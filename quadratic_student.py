import cmath


def make_int(ans):
    if ans[1] % 1 == 0:
        for i in range(2):
            ans[i] = int(ans[i])
    return ans


def solve(a, b, c):
    if not ((isinstance(a, int) or (isinstance(a, float))) and (isinstance(b, int) or (isinstance(b, float))) and (
            isinstance(c, int) or (isinstance(c, float)))):
        raise TypeError("Inputs must be numbers")
    ans = []
    if a == 0:
        if b * c < 0:
            ans = [-((-c / b) ** 0.5), +((-c / b) ** 0.5)]
            ans = make_int(ans)
        else:
            ans = [-(cmath.sqrt(-c / b)), +(cmath.sqrt(-c / b))]
    else:
        discriminant = b ** 2 - 4 * a * c
        if discriminant < 0:
            ans = [(-b + cmath.sqrt(b ** 2 - 4 * a * c)) / (2 * a), (-b - cmath.sqrt(b ** 2 - 4 * a * c)) / (2 * a)]
        else:
            ans = [(-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a), (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)]
            ans = make_int(ans)
    return tuple(ans)


if __name__ == "__main__":
    solution = solve(1, 4, 8)
    print(solution, type(solution[1]))
