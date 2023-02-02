class Solution:
    def singleDigit(self, num):
        dic = { 0:" ", 1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine"
               }
        return dic[num]
    
    def twoDigit (self, num):
        if num < 10:
            return self.singleDigit(num)
        elif num == 10:
            return "Ten"
        elif num == 11:
            return "Eleven"
        elif num == 12:
            return "Twelve"
        elif num == 13:
            return "Thirteen"
        elif num == 14:
            return "Fourteen"
        elif num == 15:
            return "Fifteen"
        elif num == 16:
            return "Sixteen"
        elif num == 17:
            return "Seventeen"
        elif num == 18:
            return "Eighteen"
        elif num == 19:
            return "Nineteen"
        elif num == 20:
            return "Twenty"
        elif num == 30:
            return "Thirty"
        elif num == 40:
            return "Forty"
        elif num == 50:
            return "Fifty"
        elif num == 60:
            return "Sixty"
        elif num == 70:
            return "Seventy"
        elif num == 80:
            return "Eighty"
        elif num == 90:
            return "Ninety"
        elif num>20 and num < 30:
            return "Twenty " + self.singleDigit(num%10)
        elif num > 30 and num < 40:
            return "Thirty " + self.singleDigit(num%10)
        elif num > 40 and num < 50:
            return "Forty " + self.singleDigit (num%10)
        elif num > 50 and num < 60:
            return "Fifty " + self.singleDigit (num%10)
        elif num > 60 and num < 70:
            return "Sixty " + self.singleDigit (num%10)
        elif num > 70 and num < 80:
            return "Seventy " + self.singleDigit (num%10)
        elif num > 80 and num <90:
            return "Eighty " + self.singleDigit (num%10)
        elif num > 90 and num < 100:
            return "Ninety " + self.singleDigit (num%10)
    
    def threeDigit (self, num):
        if num<100:
            return self.twoDigit (num)
        elif num %100 == 0:
            return self.singleDigit(num//100) + " Hundred"
        elif num>100 and num<1000 and num%100 !=0:
            return self.singleDigit (num//100) + " Hundred " + self.twoDigit (num%100)
    
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        billion = (num// 1000000000)
        million =  (num - billion*1000000000)//1000000
        thousand =  (num - billion*1000000000 - 1000000*million)//1000
        rest = num - billion*1000000000 - 1000000*million - 1000*thousand
        s = ""
        if billion > 0 and num%1000000000 == 0:
            s = s + self.threeDigit (billion) + " Billion"
            return s
        
        elif billion > 0:
            # print(billion)
            s = s + self.threeDigit(billion) + " Billion "
        if million > 0 and num%1000000 == 0:
            s = s + self.threeDigit (million) + " Million"
            return s
        
        elif million > 0:
            s = s + self.threeDigit (million) + " Million "
        if  thousand > 0 and num%1000 ==0:
            s = s + self.threeDigit (thousand) + " Thousand"
            return s
        
        elif thousand > 0:
            s = s + self.threeDigit (thousand) + " Thousand "
        if  rest > 0:
            s = s + self.threeDigit(rest)
        
        return s
 