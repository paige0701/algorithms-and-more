"""

You are given a string representing an attendance record for a student. The record only contains the following three characters:
'A' : Absent.
'L' : Late.
'P' : Present.
A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

You need to return whether the student could be rewarded according to his attendance record.
"""

def solution(n):
    if n.count('A') > 1:
        return False
    if n.find('LLL') > -1:
        return False
    return True

if __name__ == '__main__':
    print(solution('ALLPP'))

