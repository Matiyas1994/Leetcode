class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        set1 = set()
        for i in range(10):
            if i < 6:
                set1.add(chr(ord('a')+i))
                set1.add(chr(ord('A')+i))
            set1.add(str(i))
    
        k = queryIP.replace('.',':').split(':')
        if len(k) == 4:
            for i in k:
                if not i.isdigit():
                    return "Neither"
                temp = [x for x in i]
                if ((temp[0] == '0') and (len(temp) > 1)):
                    return "Neither"
                if not (255 >= int(i) >= 0):
                    return "Neither"
            return "IPv4"

        if len(k) == 8:
            for i in k:
                temp = [x for x in i]
                for let in temp:
                    if let not in set1:
                        return "Neither"
                if not (4 >= len(i) >= 1):
                    return "Neither"
            return "IPv6"
        return "Neither"
        