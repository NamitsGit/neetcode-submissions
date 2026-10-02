class Solution:
    def isValid(self, s: str) -> bool:
        char_arr = s[::1]
        char_stack = []
        for c in char_arr:
            print(f"{c=}")
            if c in ["(", "{", "["]:
                char_stack.append(c)
            else:
                if char_stack:
                    if c == ")" and char_stack[-1] == "(":
                        char_stack.pop()
                    elif c == "}" and char_stack[-1] == "{":
                        char_stack.pop()
                    elif c == "]" and char_stack[-1] == "[":
                        char_stack.pop()
                    else:
                        char_stack.append(c)
                else:
                    char_stack.append(c)
                
            print(f"{char_stack=}")

        if char_stack == []:
            return True
        return False