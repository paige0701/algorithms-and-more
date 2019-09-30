# https://leetcode.com/problems/lemonade-change/

def solution(li):
    result = True
    changes = {5: 0, 10: 0, 20: 0}
    for i in li:
        changes[i] += 1
        if i == 10:
            if changes[5] == 0:
                result = False
                break
            else:
                changes[5] -= 1
        elif i == 20:
            if changes[10] > 0 and changes[5] > 0:
                changes[10] -= 1
                changes[5] -= 1
            elif changes[5] > 3:
                changes[5] = changes[5] - 3
            else:
                result = False
                break
    return result




if __name__ == '__main__':
    print(solution([5,5,5,10,5,20,5,10,5,20]))