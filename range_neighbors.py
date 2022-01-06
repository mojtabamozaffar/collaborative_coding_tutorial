from typing import List


def range_neighbors(A: List, B: List, d1: int, d2: int, d3: int, d4: int, d5: int) -> List:

    results = []

    d1 = d1 ** 2
    d2 = d2 ** 2
    d3 = d3 ** 2
    d4 = d4 ** 2
    d5 = d5 ** 2

    for point in A:
        count1, count2, count3, count4 = 0, 0, 0, 0

        for t_point in B:
            dis = (point[0] - t_point[0]) ** 2 + (point[1] -
                                                  t_point[1]) ** 2 + (point[2] - t_point[2]) ** 2

            if d1 <= dis < d2:
                count1 += 1
            elif d2 <= dis < d3:
                count2 += 1
            elif d3 <= dis < d4:
                count3 += 1
            elif d4 <= dis < d5:
                count4 += 1

        results.append([count1, count2, count3, count4])

    return results


if __name__ == "__main__":
    range_neighbors([], [], 0, 0, 0, 0, 0)
    print('success!')
