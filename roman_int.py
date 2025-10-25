def roman_to_int(a):
    roman={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    int_form=0
    for i in range(len(a)):
        if i+1<len(a) and roman[a[i]]<roman[a[i+1]]:
            int_form=roman[a[i]]
        else:
            roman[a[i]]

        return int_form

a=int(input("Enter the roman numeral:"))
print("The roman numeral of",a,"is:",roman_to_int(a))