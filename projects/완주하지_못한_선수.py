
import copy
def un_completed_participant(participant, completion):

    if len(participant) > 100000 or len(participant) < 1:
        return '마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.'

    if len(completion) != len(participant)-1:
        return 'completion의 길이는 participant의 길이보다 1 작아야합니다'

    # cloned_copy = copy.deepcopy(completion)
    #
    # for i in range(len(participant)):
    #     if len(participant[i]) < 2 or len(participant[i]) > 20:
    #         print('Student name must between 2 and 20')
    #
    #     if participant[i].isalpha() and participant[i].islower():
    #         try:
    #             idx = cloned_copy.index(participant[i])
    #             cloned_copy.pop(idx)
    #         except ValueError:
    #             return participant[i]
    #     else:
    #         print('Student name must be alphabet and lower case')

        # remove 의 time complexity 는 O(N) 이다. 여기에 for loop 까지 더해저서 O(N^2) time complexity 가 나오는데...
        # is there are faster and more efficient way of doing it?
        # if participant[i] in completion:
        #     completion.remove(participant[i])
        # else:
        #     return participant[i]

    # completion.sort()
    # participant.sort()
    # result = ''
    # for i in range(len(participant)):
    #     if participant[i] != completion[i]:
    #         result = participant[i]
    #         break
    # return result


    # collection 함수를 사용하면 쉽게 풀 수 있음.
    import collections

    c = collections.Counter(completion)
    p = collections.Counter(participant)

    f = p-c
    return list(f.keys())[0]

def main():
    print(un_completed_participant(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))

if __name__ == '__main__':
    main()