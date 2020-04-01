class Solution:

    def print_all_friends(self, g, name):

        qu = []
        result = set()

        qu.append(name)
        result.add(name)

        while qu:

            p = qu.pop(0)
            print(p)
            for x in g[p]:
                if x not in result:
                    qu.append(x)
                    result.add(x)
        return result


    def print_friends_with_intimacy(self, g, start):
        qu = []
        result = set()

        qu.append((start, 0))
        result.add(start)

        while qu:
            (p,d) = qu.pop(0)
            print(p,d)
            for x in g[p]:
                if x not in result:
                    qu.append((x,d+1))
                    result.add(x)



if __name__ == '__main__':
    g = {
        'Summer': ['John', 'Justin', 'Mike'],
        'John': ['Summer', 'Justin'],
        'Justin': ['John', 'Summer', 'Mike', 'May'],
        'Mike': ['Summer', 'Justin'],
        'May': ['Justin', 'Kim'],
        'Kim': ['May'],
        'Tom': ['Jerry'],
        'Jerry': ['Tom']
    }
    s = Solution()
    s.print_all_friends(g, 'Tom')
    print()
    s.print_friends_with_intimacy(g, 'Tom')


