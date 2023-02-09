class Solution:
    def reformatDate(self, date: str) -> str:
        month_to_number = {"Jan" : '01', "Feb":'02', "Mar":'03', "Apr":'04', "May":'05', "Jun":'06', "Jul":'07', "Aug":'08', "Sep":'09', "Oct":'10', "Nov":'11', "Dec":'12'}
        temp = date.split()
        temp[0] = temp[0][:2] if temp[0][1].isdigit() else '0'+temp[0][:1]
        return temp[2]+'-'+month_to_number[temp[1]]+'-'+temp[0]
        