def main(str):

    mapped = dict(('()', '[]', '{}'))
    stack = []

    for i in str:
        if len(stack) > 0 and stack.pop() == i:
            return True
        elif i in mapped.keys():
            stack.append(mapped[i])

    return stack






if __name__ == '__main__':
    print(main('(5+2)+((4+1)/(20+1))'))