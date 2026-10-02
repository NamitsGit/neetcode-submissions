class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += str(len(s))+"%"+s+"#"
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        _len = ""
        i = 0
        while i < len(s):
            c = s[i]
            if c != "%" and c.isdigit():
                _len += c
            elif c == "%":
                _len = int(_len)
                decoded_strs.append(s[i + 1 : i + _len + 1])
                i += _len
                _len = ""
            i += 1
        return decoded_strs