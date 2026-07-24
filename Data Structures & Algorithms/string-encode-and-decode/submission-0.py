class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for i, v in enumerate(strs):
            each_str = ""
            for j in v:
                each_str += f"{ord(j)}||"
            encoded_str += f"{each_str} "
        print(encoded_str)
        return encoded_str
                
    def decode(self, s: str) -> List[str]:
        list_result = []
        for i in s.split(" ")[:-1]:
            build_up_string = ""
            for j in i.split("||")[:-1]:
                build_up_string += chr(int(j))
            list_result.append(build_up_string)
        return list_result

