units = ["", "One", "Two", "Three", "Four",
			"Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve",
			"Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen",
			"Eighteen", "Nineteen"]

tens= [
    "", 	
	"",	
	"Twenty", 
	"Thirty", 
	"Forty", 
	"Fifty", 
	"Sixty", 
	"Seventy",
	"Eighty", 
	"Ninety" 
]

def convert(n):
    print(n)
    n = int(n)
    if (n < 20):
        return units[n]

    if (n < 100):
        return tens[int(n / 10)] + (" " if(n % 10 != 0) else "") + units[n % 10]

    if (n < 1000):
        return units[int(n / 100)] + " Hundred" + (" " if(n % 100 != 0) else "") + convert(n % 100)

    if (n < 100000):
        return convert(int(n / 1000)) + " Thousand" + (" " if(n % 10000 != 0) else "") + convert(n % 1000);
    

    if (n < 10000000):
        return convert(int(n / 100000)) + " Lakh" + (" " if(n % 100000 != 0) else "") + convert(n % 100000);
    

    return convert(int(n / 10000000)) + " Crore" + (" " if(n % 10000000 != 0) else "") + convert(n % 10000000)
