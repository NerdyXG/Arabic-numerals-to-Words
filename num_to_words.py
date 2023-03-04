import sys
num = input("Enter num: ")
length = len(num)
ans = ""
if num == "0":
    print ("zero")
    sys.exit()
place_value = len(num) // 3
degree = len(num) % 3
place_value_dict = {"0": "", "1": "Thousand ", "2": "Million ", "3": "Billion "}
num_dict = {
    "0": "",
	"1": "One",
	"2": "Two",
	"3": "Three",
	"4": "Four",
	"5": "Five",
	"6": "Six",
	"7": "Seven",
	"8": "Eight",
	"9": "Nine"
}
tens_dict = {
    "10": "Ten",
	"11": "Eleven",
	"12": "Twelve",
	"13": "Thirteen",
	"14": "Fourteen",
	"15": "Fifteen",
	"16": "Sixteen",
	"17": "Seventeen",
	"18": "Eighteen",
	"19": "Nineteen",
	"20": "Twenty",
	"30": "Thirty",
	"40": "Forty",
	"50": "Fifty",
	"60": "Sixty",
	"70": "Seventy",
	"80": "Eighty",
	"90": "Ninety"
}

i = 0
while i < length:
	if degree == 0:
		if num[i] == "0":
		    ans = ans
		else:
		    ans = ans + num_dict.get(num[i]) + " Hundred "
		degree = 3
		place_value -= 1
		
	elif degree == 1:
		if num[i] == "0":
		    ans = ans
		else:
		    ans = ans + num_dict.get(num[i]) + " " + place_value_dict.get(str(place_value))
		
	elif degree == 2:
		if num[i] == 1:
			special_num = str(num[i]) + str(num[i + 1])
			ans = ans + " " + tens_dict.get(special_num)
		elif num[i] == "0":
		    ans = ans  
		else:
			ans = ans + " " + tens_dict.get(str(num[i]) + "0") + "-"
			
	degree -= 1
	i += 1

print(ans)