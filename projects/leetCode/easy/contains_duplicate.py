def main(nums):
    if len(nums) == 0:
        return False
    else:
        map1 = {}

        count = 0
        result = False
        while count < len(nums):
            key = str(nums[count])
            if map1.get(key) is None:
                map1[key] = key
                count = count + 1
            else:
                result = True
                break
        return result


if __name__ == '__main__':
    print(main([1,2,3,4,1]))