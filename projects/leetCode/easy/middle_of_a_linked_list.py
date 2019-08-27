class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        normal = fast = head

        while fast and fast.next:
            normal = normal.next
            fast = fast.next.next
        return normal



if __name__ == '__main__':
    solution = Solution()
    print(solution.middleNode([1,2,3,4,5]))
