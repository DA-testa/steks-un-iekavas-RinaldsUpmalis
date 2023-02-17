# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next,i))

        if next in ")]}":
            if opening_brackets_stack:
                right = next
                left = opening_brackets_stack[-1].char
                if are_matching(left, right):
                    opening_brackets_stack.pop()
                else:
                    return i+1
            else:
                return i+1
    if opening_brackets_stack:
        return opening_brackets_stack[-1].position


def main():
    text = input()
    if text[0]=="I":
        text=input()
    mismatch = find_mismatch(text)

    if not mismatch:
        print("Success")
    else:
        print(mismatch)

if __name__ == "__main__":
    main()
