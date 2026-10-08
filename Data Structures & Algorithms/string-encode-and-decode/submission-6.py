class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ''
        for s in strs:
            len_s = len(s)
            encoded_str += str(len_s) + "#" + s 
        return encoded_str

    def decode(self, s: str) -> List[str]:
        strs = []
        str_len_of_word = ''
        word_len = 0
        word = ''
        i = 0
        while i < len(s):
            j = i
            # print(f"{i=} {j=} {s[i]=} {s[j]=}")
            while j < len(s) and s[j] != "#":
                str_len_of_word += s[j]
                j += 1
            word_len = int(str_len_of_word)
            # print(f"{i=} {j=} {s[i]=} {s[j]=} {word_len=}")
            word = s[j + 1 : j + 1 + word_len]
            strs.append(word)
            i = j + 1 + word_len
            # print(f"i updated to {i=} {j+1=} {word_len=}")
            str_len_of_word = ''
            word_len = 0
        return strs


