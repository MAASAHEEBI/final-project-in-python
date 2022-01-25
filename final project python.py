class Restaurant:
    
    def __init__(self, name):
        self.restro_name=name
        self.food={}
        self.food_ID=len(self.food)+1
        self.user_details={}
        self.ordered_item=[]
        self.menu=[]
        self.final_price=[]

        
        
    # admin functionalities
               
        
    def add_food_item(self):
        try:
            name=input("Enter the food name : ")
            qty=int(input("Enter the quanty: "))
            qty_type=input("qty type(For eg,ml,gm,pieces etc): ")
            price=int(input("Enter price,only numeric value: "))
            discount=int(input("Enter rate of dis only numeric value: "))
            final_price=price-(price*(discount/100))
            stock=int(input("Enter the available stock: "))
            
            food_item={"Name":name.title(),"Quantity":str(qty)+qty_type,"Price":str(price)+"rs"+'/'+qty_type,
                       "Discount":str(discount)+"%","Final price":final_price,"Stock":str(stock)+qty_type}
            self.food_ID=len(self.food)+1
            self.food[self.food_ID]=food_item
            
            
           
            print("\nFood Items added successfully \nNewly Added items :", self.food  )
           
        except:
            print("\n!! Something went wrong please try again !!")
        
    def edit_food_item(self):
        try:
            x=int(input("\nEnter the Food ID you want to update : \n"))
            if x in self.food.keys():
                print("1. Update Food Name\n2. Update Quantity\n3. Update Price\n4. Update Discount\n5. Update Stock \n")
                y= input("\nEnter the number only : ")
                if y=="1":
                    self.food[x]["Name"]=input("Updated Food name : ")
                    print("\n!! Successfully Updated !!")
                elif y=="2":
                    self.food[x]["Quantity"]=int(input("Updated Quantity in values only : "))
                    print("\n!! Successfully Updated !!")
                elif y=="3":
                    self.food[x]["Price"]=int(input("Updated Price in Rs only : "))
                    print("\n!! Successfully Updated !!")
                elif y=="4":
                    self.food[x]["Discount"]=int(input("Updated Discount in Rs only : "))
                    print("!! successfully Updated !!")
                elif y=="5":
                    self.food[x]["Stock"]=int(input("Updated Stock in values only : "))
                    print("\n!! Successfully Updated !!")
                else:
                    print("\n!! Sorry Invalid Number !!")
            else:
                print("\n!! Incorrect Food ID !!")
        except:
            print("\n!! Something went wrong please try again !!\n")  
            
    def view_food_item(self):
        print("List of Food Items : ")
        if len(self.food)!=0:    
            for i in self.food:
                print(f"Food Id : {i}")
                for j in self.food[i]:
                    print(j, ":", self.food[i][j])
                print()
        else:
            print("\n!! Sorry No Food Items is Added !!\n")

    def delete_food_item(self):
        try:
            print("\n!! Warning !!\nFood Item will Delete Permanently\n")
            print("Enter the Food ID ")
            x=int(input())
            if x in self.food.keys():
                del self.food[x]
                print("\n!! Food item deleted successfully !!")
                print("\nUpdated Food List\n",self.food)
            else:
                print("\n!! Incorrect Food ID !!")
        except:
            print("\n!! Something went wrong please try again !!\n")
                
                
    # user functionalities
                   
        
    def user_register(self):
        try:
            while True:
                user_name=input("Enter your full name : ")
                phone_no=int(input("Enter your 10 digit phone number : "))
                email=input("Enter your email id : ")
                password=input("Enter your password : ")
                address=input("Enter your address with area PIN code ")
                self.user_details={"User Name":user_name,"Phone No.":phone_no,"Email_ID":email,"Password":password,"Address":address}
                print("!! Your Account is Created Successfully !!")
                print(f"\nWelcome TO {self.restro_name} Restaurant")
                print("User Details : ")
                for i in self.user_details:
                    print(i, ":", self.user_details[i])
                break
            
        except:
            print("\n!! Something went wrong please try again !! ")      
               
    def user_login(self):
        try:
            while True:
                print(f"\nWelcome TO {self.restro_name} Restaurant\n\n")
                email=input("\nEnter Your Email ID : ")
                pas=input("Enter Your Password : ")
                if len(self.user_details)!=0:
                    if email==self.user_details["Email_ID"] and pas==self.user_details["Password"]:
                        print("\n!! Login successfully !!")
                        while True:
                            print("\nEnter the Below Options\n")
                            print("1. Place New Order\n2. Check Order History\n3. Edit item quantity\n4. Update Your Profile Details\n5. Exit")
                            z=input()
                            if z=="1":
                                self.place_order()
                            elif z=="2":
                                self.ordered_history()
                            elif z=="3":
                                self.edit_food_qty()
                            elif z=="4":
                                self.update_details()
                            elif z=="5":
                                break
                            else:
                                print("invalid Number")
                    else:
                        print("\n!! Incorrect Email or Password!!\n")
                else:
                    print("\n! There is no Account with this Email ID !\n\n!! Please Creat Your Account First!!\n")
                    break
                break
        except:
            print("\n!! Something went wrong please try again !!")  
            
            
    def place_order(self):
        try:
            if len(self.food)!=0:
             menu=[]
            for items in self.food:
                menu.append([self.food[items]["Name"],self.food[items]["Quantity"],self.food[items]["Price"]])
            for i in menu:
                print(i)
            while True:
                 print("\nEnter 1 to Place the Order\nEnter 2 to Exit ")
                 x=input()
                 if x=="1":
                    print("Enter the Food number You want to ordered separated by comma,")
                    y=input().split(",")
                    for i in y:
                        z=int(i)
                        if z<=len(menu):
                            self.ordered_item.append(menu[z-1])
                        else:
                            print("We Don't have this Food Item : ",z)
                    print("List of food item you selected : \n")
                    for j in self.ordered_item:
                        print(j)
                 elif x=="2":
                        break
                 else:
                        print("!! Invalid Number !!\n")
            else:
                print("\n!! Sorry! No Food Items are available Now !!\n")
                        
        except:
            print("\n!! Something went wrong try again !!")
            

    def ordered_history(self):
        print("\nList of Previous ordered : ")
        for i in self.ordered_item:
            print(i)



    def edit_food_qty(self):
            
            y={i:self.ordered_item[i]for i in range(len(self.ordered_item))}

            print("your selected items are !!")
            print(y)
            x=int(input("\nEnter the Food ID you want to update the quantity : \n"))
            if x in y.keys():
             qty=input("\nEnter quantity with qty_type: ")
             y[x][1]=qty
             print("\n!! Successfully Updated !!\nyour updated ordered items...\n")
             print(y)

            
    
        
       
            
            
    def update_details(self):
        try:
            while True:
                print("\nSelect Below Options to Update Your Profile Details\n")
                print("1. Name\n2. Phone number\n3. Email ID\n4. Password\n5. Address\n6. Exit\n")
                x=input()
                if x=="1":
                    self.user_details["User Name"]=input("Enter your updated full name : ")
                    print("\n!! Detail Updated Successfully !!\n")
                elif x=="2":
                    self.user_details["Phone No."]=int(input("Enter your updated 10 digit phone number : "))
                    print("\n!! Detail Updated Successfully !!\n")      
                elif x=="3":
                    self.user_details["Email_ID"]=input("Enter your updated email id : ")
                    print("\n!! Detail Updated Successfully !!")
                    
                elif x=="4":
                    self.user_details["Password"]=input("Enter your updated password : ")
                    print("\n!! Detail Updated Successfully !!\n")
                    
                elif x=="5":
                    self.user_details["Address"]=input("Enter your updated address with area PIN code ")
                    print("\n!! Detail Updated Successfully !!\n")
                    
                elif x=="6":
                    break
                else:
                    print("\n!! Invalid Number Entered !!\n")
                    
                if x in ["1","2","3",'4',"5"]:
                    for i in self.user_details:
                        print(i, ":",self.user_details[i])
                    else:
                        print("\nPlease Enter correct Input\n")      
        except:
            print("\n!! Something went wrong please try again !!\n ")



    
        
            
            
       # defining the Main function to run the code in one shot     

try:
    def main():
        obj=Restaurant(" 'Shahi and Cuisine' ")
        print(f"!!  Welcome To {obj.restro_name} Restaurant  !!")
        print("------------------------------------------------")
        print("           How can we help you?  ")
        print("------------------------------------------------")
        print("\nplease select from the below options...")
        
        while True:
            print("1. Admin\n2. User\n3. Exit\n")
            x=input()
            if x=="1":
                while True:
                    print("\nHello Admin...!!! \nPlease Enter the below options...")
                    print("\n1. Add New Food Items\n2. Edit Food Items\n3. View Food Items \n4. Delete Food Items\n5. Exit")
                    y=input()
                    if y=="1":
                        obj.add_food_item()
                    elif y=="2":
                        obj.edit_food_item()
                    elif y=="3":
                        obj.view_food_item()
                    elif y=="4":
                        obj.delete_food_item()
                    elif y=="5":
                        break
                    else:
                        print("Invalid Number")
            elif x=="2":
                while True:
                    print("\nWe are HAPPY to SERVE you")
                    print("\nPlease Enter the Below Options...")
                    print("\n1. Register\n2. Login\n3. Exit\n")
                    y=input()
                    if y=="1":
                        obj.user_register()
                    elif y=="2":
                        obj.user_login()           
                    elif y=="3":
                        break
                    else:
                        print("\nInvalid Number ")        
            elif x=="3":
                break
            else:
                print("Invalid Number")
except:
    print("something went wrong please give input carefully")
            
        # calling the main function 
        
if __name__=='__main__':
    main()

print("!! ...THANK YOU...VISITE AGAIN... !!")
