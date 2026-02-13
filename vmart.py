
print("################ WELCOME TO V-MART Shopping Mall ####################")#\n new line
CART=input("Choose your category=[Men's/Women's/Children's]")
if CART=="Men's":
    print("***********WELCOME TO MEN'S CATEGORY*************")
    Product=input("choose your category=[Shirts/Pants/Trousers]")
    Size=input("choose your size=[S/M/L/XL]")
    Payment=input("Choose your payment type=[Card/UPI/Cash]")
    Amount=int(input("enter amount="))
    print("Thank you for shopping")
if CART=="Women's":
    print("***********WELCOME TO WOMEN'S CATEGORY*************")
    Product=input("choose your category=[Shirts/Pants/Trousers]")
    Size=input("choose your size=[S/M/L/XL]")
    Payment=input("Choose your payment type=[Card/UPI/Cash]")
    Amount=int(input("enter amount="))
    print("Thank you for shopping")
if CART=="Children's":
    print("***********WELCOME TO MEN'S CATEGORY*************")
    Product=input("choose your category=[Skin Care/Food/Toys/Clothes]")
    if Product=="Clothes":      
        Size=input("Choose your size=[S/M/L/XL]")    
    Payment=input("Choose your payment type=[Card/UPI/Cash]")
    Amount=int(input("enter amount="))
    print("Thank you for shopping")
print("your bill is ready:\n Category=",CART,"\n Product=",Product,"\n Size=",Size,"\n Paymentmode="
      ,Payment,"\nAmount=",Amount)



    


   

    
