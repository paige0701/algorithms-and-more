"""
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


def solution(li, target):

    h = {}
    for i, v in enumerate(li):

        n = target-v
        if n not in h:
            h[v] = i
        else:
            return [h[n], i]


if __name__ == '__main__':
    print(solution([2, 7, 11, 15], 9))
