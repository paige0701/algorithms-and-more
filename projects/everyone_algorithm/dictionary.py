class Solution:
    def get_name_by_no(self, num):

        li = {
            39:'Justin',
            14: 'John',
            67: 'Mike',
            105: 'Summer'
        }

        return li[num] if num in li else '?'

    def get_names_appear_more_than_once(self, li):

        name_dict = {}

        for i in li:
            if i not in name_dict:
                name_dict[i] = 1
            else:
                name_dict[i] += 1

        result = set()
        for i in name_dict:
            if name_dict[i] > 1:
                result.add(i)

        return result

if __name__ == '__main__':
    a = Solution()
    print(a.get_name_by_no(393))
    print(a.get_names_appear_more_than_once(
        ['Tom', 'Jerry', 'Mike', 'Tom']
    ))
