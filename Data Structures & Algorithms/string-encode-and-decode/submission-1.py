class Solution:

    def encode(self, strs: List[str]) -> str:

        if strs == []:
            return "emp"

        encoded_str = "/*/".join(st[::-1] for st in strs)
        
        return encoded_str

    def decode(self, s: str) -> List[str]:

        if s == "emp":
            return []

        decoded_strs = s.split("/*/")

        for st in range(len(decoded_strs)):
            decoded_strs[st] = decoded_strs[st][::-1]

        return decoded_strs
