class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        num1,sep,rest1 = version1.partition(".")
        num2,sep,rest2 = version2.partition(".")
        if num1 == "" and num2 == "" :
            return 0
        num1,num2 = int(0 if num1 == "" else num1),int(0 if num2 == "" else num2)
        if num1 == num2 :
            return self.compareVersion(rest1,rest2)
        if num1 < num2 :
            return -1
        if num1 > num2 :
            return 1
