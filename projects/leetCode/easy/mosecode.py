class Solution:
    def morse_code(self, words):
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        result = set()
        for i in words:
            st = ''
            for j in i:
                st+= morse[ord(j) - 97]
            result.add(st)
        # return len(result)


        # 위에거랑 같은말인데 러닝타임은 이게 더 빠르다. for 문 작성 하는 방법은 조금 더 공부해보갈~
        return len({''.join(j[ord(j)-97] for j in i) for i in words})


if __name__ == "__main__":
    s = Solution()
    print(s.morse_code(["gin", "zen", "gig", "msg"]))


