# Here we import mysql conector for database usage.
import mysql.connector as my_database

# Here we import cloting_store_mange_validation for Validation.
import cloting_store_mange_validation as my_validation

# Here we import datatime,tabulate,sys and linecache modules.
import datetime
import tabulate
import sys
import linecache

# Here we create Admin_manage class.

class Admin_manage:

    # Here we crete constructor for Admin_manage class.
    
    def __init__(self):

        # Here we get the current time.
        
        cur_time = datetime.datetime.now() 
        self.cur_date = cur_time.replace(microsecond=0)

        # Here we connect to the database by connent() function.

        self.mysql = my_database.connect(
            host = "localhost",
            user = "root",
            password = "dnagaraj@2207")

        # Here we create cursor object for the connection.

        self.cursor=self.mysql.cursor()

        # Here we create cloting_store database.
        
        self.cursor.execute("create database if not exists cloting_store")
        self.cursor.execute("use cloting_store")

        # Here we create clothing_item table.

        self.cursor.execute("create table if not exists clothing_item\
        (Item_id int primary key auto_increment,\
         Title varchar(30) not null,\
         Brand varchar(30) not null,\
         Price float(10,2) not null,\
         Category varchar(30) not null,\
         Size varchar(3) not null,\
         Stock_Quantity bigint(10) not null)auto_increment = 101")

        self.admin_username = "naga2207"
        self.__admin_password = "dnagaraj@2207"

    # Here we create get_admin_password() function for get the password in the private variable.
        
    def get_admin_password(self):
        return self.__admin_password

    # Here we create_error_log_file() to store the Errors.

    def create_error_log_file(self,cur_date,exception_traceback,exception_object,exception_type):
        e = open("error_log_clothing_store.txt","a+")
        line_number = exception_traceback.tb_lineno
        line_of_code = linecache.getline(__file__, line_number).strip()
        e.write('\n\n{} - error occured in - "{}" - line No:{} - {} - {} '.format(exception_type,line_of_code,line_number,exception_object,cur_date))
        e.close()

    # Here we create add_clothing_item() for add cloths.

    def add_clothing_item(self):
        print("\n"+("="*35))
        print("\n*** Enter Your Clothing Item Details Below ***")
        print("\n"+("="*35))
        item = 1
        while item:
            try:
                self.item_name = input("\nEnter the Title of the Item:").capitalize()
                my_validation.cloth_name_validation(self.item_name)
                item = 0
            except Exception as er:
                print(er)
        brand = 1
        while brand:
            try:
                self.brand_name = input("\nEnter the Brand of the Item:").upper()
                self.brand_name = self.brand_name.replace(" ","")
                my_validation.name_validation(self.brand_name)
                brand = 0
            except Exception as er:
                print(er)
        price = 1
        while price:
            try:
                self.item_price = float(input("\nEnter the Item Price:"))
                price = 0
            except ValueError:
                exception_type, exception_object, exception_traceback = sys.exc_info()
                self.create_error_log_file(self.cur_date,exception_traceback,exception_object,exception_type)
                print("\nItem Price must be in Numbers")

        categ = 1
        while categ:
            try:
                self.category_name = input("\nEnter the Category of the Item:").capitalize()
                self.category_name = self.category_name.replace(" ","")
                my_validation.name_validation(self.category_name)
                categ = 0
            except Exception as er:
                print(er)

        size = 1
        item_size_list = ["S","M","L","XL","XXL"]
        while size:
            try:
                self.item_size = input("\nEnter the Size of the Item (S,M,L,XL,XXL):").upper()
                self.item_size = self.item_size.replace(" ","")
                if len(self.item_size) == 0:
                    print("\nSize should not be Empty!!!")
                elif self.item_size not in item_size_list:
                    print("\nPlease Enter the Valid Size!!")
                else:
                    size = 0
            except Exception as er:
                print(er)
        quan = 1
        while quan:
            count = 0
            try:
                self.stock_quantity = int(input("\nEnter the Stack Quantity:"))
                data = self.cursor.execute("select Title,Brand,Size from clothing_item")
                my_data = self.cursor.fetchall() 
                if my_data != []:
                    for x in my_data:
                        print(x)
                        if self.item_name not in x or self.brand_name not in x or self.item_size not in x:
                            count = 1
                        else:
                            count = 0
                            break

                    if count > 0:
                        quan = 0
                    else:
                        print("\nYou Already Added this Item!!!")
                        quan = 0
                else:
                    quan = 0
            except ValueError:
                exception_type, exception_object, exception_traceback = sys.exc_info()
                self.create_error_log_file(self.cur_date,exception_traceback,exception_object,exception_type)
                print("\nStock Quantity must be in Numbers!!!")

    # Here we create get_product_id() to get the id.

    def get_product_id(self):
        print("\n"+("="*35))
        print("\n*** Enter Your Cloth ID Below ***")
        print("\n"+("="*35))
        ad_id = 1
        my_product_list = []
        while ad_id:
            try:
                self.product_id = int(input("\nEnter the Item Id:"))
                self.cursor.execute("select Item_id from clothing_item")
                my_data = self.cursor.fetchall()
                for x in my_data:
                    for y in x:
                        my_product_list.append(y)
                if self.product_id in my_product_list:
                    ad_id = 0
                else:
                    print("\nProduct Id Not Exists")
            except ValueError:
                exception_type, exception_object, exception_traceback = sys.exc_info()
                self.create_error_log_file(self.cur_date,exception_traceback,exception_object,exception_type)
                print("\nProduct ID must be in Numbers!!!")

    # Here we fetch_all_clothing_items() for view all items.

    def fetch_all_clothing_items(self):
        self.cursor.execute("select * from clothing_item")
        my_data = self.cursor.fetchall()
        print(tabulate.tabulate(my_data,headers = ["Item Id","Title","Brand","Price","Category","Size","Stock Quantity"],tablefmt = "grid"))

    # Here we Retrieve_clothing_item() for view the clothing items.

    def Retrieve_clothing_item(self):
        rt_choose = 1
        while rt_choose:
            try:
                print("\n"+("o~"*21))
                print("\n{:>28}*** Welcome to Retrieve Clothing Items Page***".format(" "))
                print("\n{:<27}".format(" "),("~o"*62))
                print("\n{:>28}1.Retrieve All Item".format(" "))
                print("\n{:>28}2.Retrieve Single Item".format(" "))
                print("\n{:>28}3.Exit".format(" "))
                ad_choice = int(input("\nEnter Your Choice:"))
                if ad_choice == 1:
                    self.fetch_all_clothing_items()

                elif ad_choice == 2:
                    self.get_product_id()
                    self.cursor.execute("select * from clothing_item where Item_id ={}".format(self.product_id))
                    my_data1 = self.cursor.fetchall()
                    print(tabulate.tabulate(my_data1,headers = ["Item Id","Title","Brand","Price","Category","Size","Stock Quantity"],tablefmt = "grid"))

                elif ad_choice == 3:
                    rt_choose = 0
                else:
                    print("\nPlease Enter the Correct Choice!!!")
            except ValueError:
                exception_type, exception_object, exception_traceback = sys.exc_info()
                self.create_error_log_file(self.cur_date,exception_traceback,exception_object,exception_type)
                print("\nChoice must be in Numbers.")

    # Here we create update_clothing_item() for update the clothing Items.
                
    def update_clothing_item(self):
        up_choice = 1
        self.get_product_id()
        while up_choice:
            self.cursor.execute("select * from clothing_item where Item_id ={}".format(self.product_id))
            my_data1 = self.cursor.fetchall()
            print(tabulate.tabulate(my_data1,headers = ["Item Id","Title","Brand","Price","Category","Size","Stock Quantity"],tablefmt = "grid"))
            try:
                ad_choice = int(input("\nPress 1 to Update or 0 to Exit:"))
                if ad_choice == 1:
                    self.add_clothing_item()
                    query = "replace into clothing_item (Item_id,Title,Brand,Price,Category,Size,Stock_Quantity) values (%s,%s,%s,%s,%s,%s,%s)"
                    values = (self.product_id,self.item_name,self.brand_name,self.item_price,self.category_name,self.item_size,self.stock_quantity)
                    self.cursor.execute(query,values)
                    self.mysql.commit()
                    print("\nClothing Item Updated Sucessfully!!!")
                    
                elif ad_choice == 0:
                    up_choice = 0
                else:
                    print("\nPlease Enter the correct choice (0/1)!!!")
            except ValueError:
                exception_type, exception_object, exception_traceback = sys.exc_info()
                self.create_error_log_file(self.cur_date,exception_traceback,exception_object,exception_type)
                print("\nChoice must be in Numbers!!!")

    # Here we create delete_clothing_item() for delete the clothing Items.

    def delete_clothing_item(self):
        self.get_product_id()
        self.cursor.execute("delete from clothing_item where Item_id ={}".format(self.product_id))
        self.mysql.commit()
        print("\nClothing Item Deleted Sucessfully!!!")

    # Here we create current_cus_orders() to the current customer orders.

    def current_cus_orders(self):
        cus_name = ""
        cus_ph_no = ""
        cus_email = ""
        self.cursor.execute("select distinct Customer_Name,Customer_Phone_Number,Customer_email from clothing_cart")
        my_data1 = self.cursor.fetchall()
        for x in my_data1:
            cus_name = x[0]
            cus_ph_no = x[1]
            cus_email = x[2]
            query = "select Item_id,Title,Brand,Price,Quantity,Category,Size,Status from clothing_cart where Customer_Name = %s  and Customer_Phone_Number = %s and Customer_email = %s"
            values = (cus_name,cus_ph_no,cus_email)
            self.cursor.execute(query,values)
            my_data = self.cursor.fetchall()
            print("\nCustomer Name:",cus_name)
            print("Customer Phone Number:",cus_ph_no)
            print("Customer Email Id:",cus_email)
            print(tabulate.tabulate(my_data,headers = ["Item Id","Title","Brand","Price","Quantity","Category","Size","Status"],tablefmt="grid"))

    # Here we create history_cus_orders() for view the history of the Orders.

    def history_cus_orders(self):
        cus_name = ""
        cus_ph_no = ""
        cus_email = ""
        self.cursor.execute("select distinct Customer_Name,Customer_Phone_Number,Customer_email from customer_cart_history")
        my_data1 = self.cursor.fetchall()
        for x in my_data1:
            cus_name = x[0]
            cus_ph_no = x[1]
            cus_email = x[2]
            query = "select Item_id,Title,Brand,Price,Quantity,Category,Size,Status from customer_cart_history where Customer_Name = %s  and Customer_Phone_Number = %s and Customer_email = %s"
            values = (cus_name,cus_ph_no,cus_email)
            self.cursor.execute(query,values)
            my_data = self.cursor.fetchall()
            print("\nCustomer Name:",cus_name)
            print("Customer Phone Number:",cus_ph_no)
            print("Customer Email Id:",cus_email)
            print(tabulate.tabulate(my_data,headers = ["Item Id","Title","Brand","Price","Quantity","Category","Size","Status"],tablefmt="grid"))

    # Here we create view_cus_orders() for view customers orders.

    def view_cus_orders(self):
        vi_choose = 1
        while vi_choose:
            try:
                print("\n"+("o~"*21))
                print("\n{:>28}*** Welcome to View Customer Orders Page ***".format(" "))
                print("\n{:<27}".format(" "),("~o"*62))
                print("\n{:>28}1.View Current Customer Orders".format(" "))
                print("\n{:>28}2.View Customer Order's History".format(" "))
                print("\n{:>28}3.Exit".format(" "))
                vi_choice = int(input("\nEnter your Choice:"))
                if vi_choice == 1:
                    self.cursor.execute("select * from clothing_cart")
                    my_data = self.cursor.fetchall()
                    if my_data != []: 
                        self.current_cus_orders()
                    else:
                        print("\nCurrently No Orders Placed!!!")
                elif vi_choice == 2:
                    self.cursor.execute("select * from customer_cart_history")
                    my_data1 = self.cursor.fetchall()
                    if my_data1 != []: 
                        self.history_cus_orders()
                    else:
                        print("\nThere is No Order History's Found!!!")
                elif vi_choice == 3:
                    vi_choose = 0
                else:
                    print("\nPlease Enter the Correct Choice!!!")
            except ValueError:
                exception_type, exception_object, exception_traceback = sys.exc_info()
                self.create_error_log_file(self.cur_date,exception_traceback,exception_object,exception_type)
                print("\nChoice must be in Numbers!!!")

    # Here we create admin_login() for admin login to the portal.
        

    def admin_login(self):
        l = open("login_logout_clothing_store.txt","a+")
        l.write("\nAdminLogin - {}".format(self.cur_date))
        l.close()
        print("\n"+("="*35))
        print("\n*** Enter Your Admin Details Below ***")
        print("\n"+("="*35))
        ad_us = 1
        while ad_us:
            try:
                admin_user_name = input("\nEnter the Admin User Name:").lower()
                admin_user_name = admin_user_name.replace(" ","")
                my_validation.user_name_validation(admin_user_name)
                if admin_user_name == self.admin_username:
                    ad_us = 0
                else:
                    print("\nPlease Enter the correct User Name")
            except Exception as er:
                print(er)
            
        ad_ps = 1
        while ad_ps:
            admin_password = input("\nEnter the Admin User Password:").lower()
            admin_password = admin_password.replace(" ","")
            if admin_password == self.get_admin_password():
                ad_ps= 0
            else:
                print("\nPlease Enter the correct Admin Password!!!")

        ad_choose = 1
        while ad_choose:
            try:
                print("\n"+("o~"*21))
                print("\n{:>28}*** Welcome to Admin Page ***".format(" "))
                print("\n{:<27}".format(" "),("~o"*62))
                print("\n{:>28}1.Add clothing item".format(" "))
                print("\n{:>28}2.Retrieve clothing item".format(" "))
                print("\n{:>28}3.Update clothing item".format(" "))
                print("\n{:>28}4.Remove clothing item".format(" "))
                print("\n{:>28}5.View Customer orders".format(" "))
                print("\n{:>28}6.Exit".format(" "))
                admin_choice = int(input("\nEnter Your Choice:"))
                self.cursor.execute("select * from clothing_item")
                my_data = self.cursor.fetchall()
                if admin_choice == 1:
                    self.add_clothing_item()
                    query = "insert into clothing_item (Title,Brand,Price,Category,Size,Stock_Quantity) values (%s,%s,%s,%s,%s,%s)"
                    values = (self.item_name,self.brand_name,self.item_price,self.category_name,self.item_size,self.stock_quantity)
                    self.cursor.execute(query,values)
                    self.mysql.commit()
                elif admin_choice == 2:
                    if my_data != []:
                        self.Retrieve_clothing_item()
                    else:
                        print("\nThere is no Clothing Items to Retrieve.Please first add the clothing Items")
                elif admin_choice == 3:
                    if my_data != []:
                        self.update_clothing_item()
                    else:
                        print("\nThere is no Clothing Items to Update.Please first add the clothing Items")
                elif admin_choice == 4:
                    if my_data != []:
                        self.delete_clothing_item()
                    else:
                        print("\nThere is no Clothing Items to Delete.Please first add the clothing Items")
                elif admin_choice == 5:
                    self.view_cus_orders()
                elif admin_choice == 6:
                    l = open("login_logout_clothing_store.txt","a+")
                    l.write("\nAdminLogin - {}".format(self.cur_date))
                    l.close()
                    ad_choose = 0
                else:
                    print("\nPlease Enter the correct choice!!!")
            except ValueError as er:
                exception_type, exception_object, exception_traceback = sys.exc_info()
                self.create_error_log_file(self.cur_date,exception_traceback,exception_object,exception_type)
                print("\nChoice Must be in Numbers!!!")

# Here we create Customer_manage class.

class Customer_manage(Admin_manage):# Here we inherit Admin_manage class to Customer_manage.

    # Here we create constructor for Customer_manage class.

    def __init__(self):

        # Here we use super() for use the Admin_manage class instance attributes.
        
        super().__init__()

        # Here we create customer_details table.
        
        self.cursor.execute("create table if not exists customer_details\
                            (Name varchar(30) not null,\
                             Phone_number bigint(10) not null primary key,\
                             Email_id varchar(40) not null unique,\
                             Password varchar(20) not null)")

        # Here we create clothing_cart table.

        self.cursor.execute("create table if not exists clothing_cart\
                            (Customer_Name varchar(20) not null,\
                             Customer_Phone_Number bigint(20) not null,\
                             Customer_email varchar(40) not null,\
                             Item_id int not null,\
                             Title varchar(30) not null,\
                             Brand varchar(30) not null,\
                             Price float(10,2) not null,\
                             Quantity bigint(10) not null,\
                             Category varchar(30) not null,\
                             Size varchar(1) not null,\
                             Status varchar(20) not null default 'Not Paid')")

        # Here we create customer_cart_history table.
        
        self.cursor.execute("create table if not exists customer_cart_history\
                            (Customer_Name varchar(20) not null,\
                             Customer_Phone_Number bigint(20) not null,\
                             Customer_email varchar(40) not null,\
                             Item_id int not null,\
                             Title varchar(30) not null,\
                             Brand varchar(30) not null,\
                             Price float(10,2) not null,\
                             Quantity bigint(10) not null,\
                             Category varchar(30) not null,\
                             Size varchar(1) not null,\
                             Status varchar(20) not null default 'Paid')")

    # Here we create customer_register() for Customer Register.

    def customer_register(self):
        print("\n"+("o~"*21))
        print("\n{:>28}*** Welcome to Customer Register Page ***".format(" "))
        print("\n{:<27}".format(" "),("~o"*62))
        print("\n"+("="*35))
        print("\n*** Enter Your Details Below ***")
        print("\n"+("="*35))
        name = 1
        while name:
            try:
                cus_name = input("\nEnter Your Name:").capitalize()
                cus_name = cus_name.replace(" ","")
                my_validation.name_validation(cus_name)
                name = 0
            except Exception as er:
                print(er)
        ph_num = 1
        while ph_num:
            try:
                cus_phone_number = input("\nEnter your Phone Number:")
                cus_phone_number = cus_phone_number.replace(" ","")
                my_validation.customer_phone_number_validation(cus_phone_number)
                ph_num = 0
            except Exception as er:
                print(er)
        email = 1
        while email:
            try:
                cus_email_id = input("\nEnter Your Email Id:")
                cus_email_id = cus_email_id.replace(" ","")
                my_validation.customer_email_id_validation(cus_email_id)
                email = 0
            except Exception as er:
                print(er)
        cus_pass = 1
        while cus_pass:
            try:
                cus_password = input("\nEnter Your Password:")
                cus_password = cus_password.replace(" ","")
                my_validation.customer_password_validation(cus_password)
                query = "insert into customer_details (Name,Phone_number,Email_id,Password) values (%s,%s,%s,%s)"
                values = (cus_name,cus_phone_number,cus_email_id,cus_password)
                self.cursor.execute(query,values)
                self.mysql.commit()
                cus_pass = 0
            except my_database.IntegrityError as e:
                if e.errno == 1062:
                    print("\nError:The phone number or email address already exists!!!")
            except Exception as er:
                print(er)

    # Here we create fetch_all__items() for to view alll items.

    def fetch_all__items(self):
        self.cursor.execute("select Item_id,Title,Brand,Price,Category,Size from clothing_item")
        my_data = self.cursor.fetchall()
        print(tabulate.tabulate(my_data,headers = ["Item Id","Title","Brand","Price","Category","Size"],tablefmt = "grid"))

    # Here view_single_item() for to view single item.

    def view_single_item(self,field_name):
        query = "select Item_id,Title,Brand,Price,Category,Size from clothing_item where Category = %s or Brand = %s or Size = %s"
        values = (field_name,field_name,field_name)
        self.cursor.execute(query,values)
        my_data1 = self.cursor.fetchall()
        print(tabulate.tabulate(my_data1,headers = ["Item Id","Title","Brand","Price","Category","Size","Stock Quantity"],tablefmt = "grid"))

    # Here we create view_by_category() for view item by entering the Category.

    def view_by_category(self):
        category_list = []
        self.cursor.execute("select Category from clothing_item")
        my_data = self.cursor.fetchall()
        for x in my_data:
            for y in x:
                category_list.append(y)
        print(category_list)
        categ = 1
        while categ:
            try:
                category_name = input("\nEnter the Category of the Item:").capitalize()
                category_name = category_name.replace(" ","")
                my_validation.name_validation(category_name)
                if category_name in category_list:
                    categ = 0
                else:
                    print("\nCategory Name Not Available!!!")
            except Exception as er:
                print(er)
        self.view_single_item(category_name)

    # Here we create view_by_brand() for view item by entering the brand.
    
    def view_by_brand(self):
        brand_list = []
        self.cursor.execute("select Brand from clothing_item")
        my_data = self.cursor.fetchall()
        for x in my_data:
            for y in x:
                brand_list.append(y)
        print(brand_list)
        brand = 1
        while brand:
            try:
                brand_name = input("\nEnter the Brand of the Item:").upper()
                brand_name = brand_name.replace(" ","")
                my_validation.name_validation(brand_name)
                if brand_name in brand_list:
                    brand = 0
                else:
                    print("\nBrand Name Not Available")
            except Exception as er:
                print(er)
        self.view_single_item(brand_name)

    # Here we create view_by_price_range() for view item by Price Range.

    def view_by_price_range(self):
        pri_range = 1
        while pri_range:
            try:
                print("\n"+("o~"*21))
                print("\n{:>28}*** Welcome to View Clothing Items by Price Range Page ***".format(" "))
                print("\n{:<27}".format(" "),("~o"*62))
                print("\n{:>28}1.Small to Big Price Range".format(" "))
                print("\n{:>28}2.Large to Small Price Range".format(" "))
                print("\n{:>28}3.Exit".format(" "))
                pri_choice = int(input("\nEnter Your Choice:"))
                if pri_choice == 1:
                    self.cursor.execute("select Item_id,Title,Brand,Price,Category,Size from clothing_item order by Price")
                    my_data = self.cursor.fetchall()
                    print(tabulate.tabulate(my_data,headers = ["Item Id","Title","Brand","Price","Category","Size"],tablefmt = "grid"))
                elif pri_choice == 2:
                    self.cursor.execute("select Item_id,Title,Brand,Price,Category,Size from clothing_item order by Price desc")
                    my_data = self.cursor.fetchall()
                    print(tabulate.tabulate(my_data,headers = ["Item Id","Title","Brand","Price","Category","Size"],tablefmt = "grid"))
                elif pri_choice == 3:
                    pri_range = 0
                else:
                    print("\nPlease Enter the Correct Choice!!!")
            except ValueError:
                exception_type, exception_object, exception_traceback = sys.exc_info()
                self.create_error_log_file(self.cur_date,exception_traceback,exception_object,exception_type)
                print("\nChoice must be in Numbers!!!")

    # Here we create view_by_size() for view item by entering the size.

    def view_by_size(self):
        size_list = []
        self.cursor.execute("select Size from clothing_item")
        my_data = self.cursor.fetchall()
        for x in my_data:
            for y in x:
                size_list.append(y)
        print(size_list)
        size = 1
        while size:
            try:
                item_size = input("\nEnter the Size of the Item (S,M,L,XL,XXL):").upper()
                item_size = item_size.replace(" ","")
                if len(item_size) == 0:
                    print("\nSize should not be Empty!!!")
                elif item_size in size_list:
                    size = 0
                else:
                    print("\nSize is Not Available!!!")
            except Exception as er:
                print(er)
        self.view_single_item(item_size)

    # Here we create browse_clothing_items() for view Items.

    def browse_clothing_items(self):
        cus_choose = 1
        while cus_choose:
            try:
                print("\n"+("o~"*21))
                print("\n{:>28}*** Welcome to Browse Clothing Items Page ***".format(" "))
                print("\n{:<27}".format(" "),("~o"*62))
                print("\n{:>28}1.View All Clothing Items".format(" "))
                print("\n{:>28}2.View Filtered Clothing Items by their Fields".format(" "))
                print("\n{:>28}3.Exit".format(" "))
                cus_choice = int(input("\nEnter your choice:"))
                if cus_choice == 1:
                    self.fetch_all__items()
                elif cus_choice == 2:
                    fill_choose = 1
                    while fill_choose:
                        try:
                            print("\n"+("o~"*21))
                            print("\n{:>28}*** Welcome to Browse Clothing Items Page ***".format(" "))
                            print("\n{:<27}".format(" "),("~o"*62))
                            print("\n{:>28}1.Category".format(" "))
                            print("\n{:>28}2.Brand".format(" "))
                            print("\n{:>28}3.Price Range".format(" "))
                            print("\n{:>28}4.Size".format(" "))
                            print("\n{:>28}5.Exit".format(" "))
                            fill_choice = int(input("\nEnter your choice:"))
                            if fill_choice == 1:
                                self.view_by_category()
                            elif fill_choice == 2:
                                self.view_by_brand()
                            elif fill_choice == 3:
                                self.view_by_price_range()
                            elif fill_choice == 4:
                                self.view_by_size()
                            elif fill_choice == 5:
                                fill_choose = 0
                            else:
                                print("Please Enter the correct choice!!!")
                        except ValueError:
                            exception_type, exception_object, exception_traceback = sys.exc_info()
                            self.create_error_log_file(self.cur_date,exception_traceback,exception_object,exception_type)
                            print("\nChoice must be in Numbers!!!")

                elif cus_choice == 3:
                    cus_choose = 0
                else:
                    print("\nPlease Enter the Correct Choice!!!")
            except ValueError:
                exception_type, exception_object, exception_traceback = sys.exc_info()
                self.create_error_log_file(self.cur_date,exception_traceback,exception_object,exception_type)
                print("\nChoice must be in Numbers!!!")

    # Here we create add_item_cart() to add the Items to the cart.

    def add_item_cart(self):
        print("\n"+("o~"*21))
        print("\n{:>28}*** Welcome to Purchase Clothing Items Page ***".format(" "))
        print("\n{:<27}".format(" "),("~o"*62))
        print("\n"+("$"*35))
        print("\n*** The Clothing Store's Offers are Given Below ***")
        print("\n"+("$"*35))
        discount_list = [["1.","Purchase Above Rs.10,000","5%"],["2.","Purchase Above Rs.30,000","20%"],["3.","Purchase Above Rs.50,000","40%"]]
        print(tabulate.tabulate(discount_list,headers = ["S.No","Offers","Discount"],tablefmt="grid"))
        my_num = 0
        self.cursor.execute("select count(Item_id) as count from clothing_item")
        my_data = self.cursor.fetchall()
        for x in my_data:
            for y in x:
                my_num = y
        num_list1 = [x for x in range(1,my_num+1)]
        self.cursor.execute("select Item_id,Title,Brand,Price,Category,Size from clothing_item")
        my_data1 = self.cursor.fetchall()
        table = [[num_list1[i]] + list(my_data1[i]) for i in range(len(num_list1))]
        cus_choose = 1
        my_cart_data = []
        temp_id = 0
        temp_price = 0
        temp_stock = 0
        count = 2
        count2 = 0
        count3 = 0
        my_cart = ()
        while cus_choose:
            try:
                print("\n"+("="*35))
                print("\n*** Select Items to Purchase ***")
                print("\n"+("="*35))
                print(tabulate.tabulate(table,headers = ["SI.No","Item Id","Title","Brand","Price","Category","Size"],tablefmt = "grid"))
                cus_choice = input("\nEnter Your Choice to Add to the Cart or Press Q to Exit:").upper()
                count1 = 0
                for x in range(1,my_num+1):
                    if cus_choice == str(x):
                        quan = 1
                        while quan:
                            try:
                                cus_quan = int(input("\nEnter the Quantity of the Item:"))
                                temp_id = my_data1[x-1][0]
                                my_cart = (self.current_customer_name,self.current_customer_ph_no,self.current_customer_email,my_data1[x-1][0],my_data1[x-1][1],my_data1[x-1][2],my_data1[x-1][3],cus_quan,my_data1[x-1][4],my_data1[x-1][5])
                                query4 = "select Item_id,Quantity,Customer_Phone_Number from clothing_cart where Item_id = %s and Customer_Phone_Number = %s"
                                values4 = (temp_id,self.current_customer_ph_no)
                                self.cursor.execute(query4,values4)
                                my_cart_data = self.cursor.fetchall()
                                query3 = "select * from clothing_item where Item_id = %s"
                                values3 = (temp_id,)
                                self.cursor.execute(query3,values3)
                                my_stock_data = self.cursor.fetchall()
                                quan = 0
                                count = 1
                                for y in my_stock_data:
                                    if y[6] == 0:
                                        print("\nStock is Empty Please Choose Different Product!!!")
                                        count1 = 1
                                        break
                                    elif cus_quan > y[6]:
                                        print("\nStock Out of Range!!!")
                                        print("\nThe Number Of Stocks Available is:",y[6])
                                        count1 = 1
                                        break
                                    
                    
                            except ValueError:
                                print("\nQuantity Must be in Numbers!!!")
                        break
                                
                    elif cus_choice == "Q":
                        cus_choose = 0
                        count = 2
                    else:
                        count = 0
                if my_cart_data != []:
                    for x in my_cart_data:
                        temp_price = x[1]+cus_quan
                        if temp_id != x[0] or self.current_customer_ph_no != x[2]:
                            count2 = 2
                            break
                        else:
                            count3 = 3
                if count1 == 1:
                    cus_choose = 1
                elif count == 2:
                    cus_choose = 0
                elif count > 0:
                    if my_cart_data != []:
                        if count1 != 1:
                            if count2 == 2:
                                query = "insert into clothing_cart (Customer_Name,Customer_Phone_Number,Customer_email,Item_id,Title,Brand,Price,Quantity,Category,Size) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                values = my_cart
                                self.cursor.execute(query,values)
                                self.mysql.commit()
                                cus_choose = 1
                            elif count3 == 3:
                                query1 = "update clothing_cart set Quantity = %s where Item_id = %s and Customer_Phone_Number = %s"
                                values1 = (temp_price,temp_id,self.current_customer_ph_no)
                                self.cursor.execute(query1,values1)
                                self.mysql.commit()
                    else:
                        if count1 != 1:
                            query = "insert into clothing_cart (Customer_Name,Customer_Phone_Number,Customer_email,Item_id,Title,Brand,Price,Quantity,Category,Size) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                            values = my_cart
                            self.cursor.execute(query,values)
                            self.mysql.commit()
                            cus_choose = 1
                else:
                    print("\nPlease Enter the Correct Choice to Add!!!")
                    cus_choose = 1
            except Exception as er:
                print(er)

    # Here we create discount_cart() for discount the total amount.

    def discount_cart(self,total_value):
        self.total_discount_value = 0
        if total_value > 50000:
            self.total_discount_value = total_value - (total_value*(40/100))
        elif total_value > 30000:
            self.total_discount_value = total_value - (total_value*(20/100))
        elif total_value > 10000:
            self.total_discount_value = total_value - (total_value*(5/100))
        else:
            self.total_discount_value = total_value

    # Here we create view_cart() function for view the cart.

    def view_cart(self):
        query = "select Item_id,Title,Brand,Price,Quantity,Category,Size,(price*Quantity) as Total_price from clothing_cart where Customer_Phone_Number = %s"
        values = (self.current_customer_ph_no,)
        self.cursor.execute(query,values)
        my_data = self.cursor.fetchall()
        query1 = "select sum(price*Quantity) from clothing_cart where Customer_Phone_Number = %s"
        values1 = (self.current_customer_ph_no,)
        self.cursor.execute(query1,values1)
        my_data1 = self.cursor.fetchall()
        total_sum=my_data1[0][0]
        self.discount_cart(total_sum)
        print(tabulate.tabulate(my_data,headers = ["Item Id","Title","Brand","Price","Quantity","Category","Size","Total Price"],tablefmt = "grid"))
        print("\n"+("$"*35))
        print("\n*** The Total Sum of the Price is:",total_sum)
        print("\n"+("$"*35))


    # Here we create pay_Card() for paying through Credit or debit card

    def pay_Card(self):
        print("\n"+("="*35))
        print("\n*** Enter Your Card Details Below ***")
        print("\n"+("="*35))
        card_name = 1
        while card_name:
            try:
                user_card_name = input("\nEnter Cardholder's Name:")
                user_card_name = user_card_name.replace(" ","")
                my_validation.name_validation(user_card_name)
                card_name = 0
            except Exception as er:
                print(er)

        card_num = 1
        while card_num:
            try:
                user_card_num = input("\nEnter the Card Number:")
                user_card_num = user_card_num.replace(" ","")
                my_validation.card_number_validation(user_card_num)
                card_num = 0
            except Exception as er:
                print(er)

        ex_date = 1
        while ex_date:
            try:
                expire_date = input("\nEnter the Expiration Date:")
                expire_date = expire_date.replace(" ","")
                my_validation.card_expire_date_validation(expire_date)
                current_date = datetime.date.today()
                expiration_date_pattern = datetime.datetime.strptime(expire_date,"%m/%Y")
                expiration_month = expiration_date_pattern.month
                expiration_year = expiration_date_pattern.year
                expiration_start_date = datetime.datetime(expiration_year, expiration_month, 1).date()
                valid_years = range(2023, 2031)
                if expiration_start_date < current_date:
                    raise Exception ("\nCard has expired,please update to current year {}.".format(current_date.year))
                elif expiration_year not in valid_years:
                    raise Exception ("\nInvalid expiration year. Please enter a date between 2023 and 2030.")
                else:
                    ex_date = 0
            except Exception as er:
                print(er)

        cvv = 1
        while cvv:
            try:
                user_cvv = int(input("\nEnter the CVV Number:"))
                if user_cvv not in range(100,999):
                    print("CVV Number Should be in 3 digits!!!")
                else:
                    cvv = 0
            except ValueError:
                exception_type, exception_object, exception_traceback = sys.exc_info()
                self.create_error_log_file(self.cur_date,exception_traceback,exception_object,exception_type)
                print("\nCVV Number must be in Numbers!!!")

    # Here we create pay_net_banking() for paying through Net Banking.

    def pay_net_banking(self):
        print("\n"+("="*35))
        print("\n*** Enter Your Net Banking Details Below ***")
        print("\n"+("="*35))
        net_id = 1
        while net_id:
            try:
                user_net_id = input("\nEnter the NetBanking User Id:")
                user_net_id = user_net_id.replace(" ","")
                my_validation.net_id_validation(user_net_id)
                net_id = 0
            except Exception as er:
                print(er)
                
        net_pass = 1        
        while net_pass:
            try:
                user_net_password = input("\nEnter the NetBanking Password:")
                user_net_password = user_net_password.replace(" ","")
                my_validation.user_password_validation(user_net_password)
                net_pass = 0
            except Exception as er:
                print(er)

    # Here we create pay_mobile_ubi() for paying through UBI.

    def pay_mobile_ubi(self):
        print("\n"+("="*35))
        print("\n*** Enter Your Mobile UBI Details Below ***")
        print("\n"+("="*35))
        ubi = 1
        while ubi:
            try:
                user_ubi_id = input("\nEnter the UBI ID:")
                user_ubi_id = user_ubi_id.replace(" ","")
                my_validation.ubi_id_validation(user_ubi_id)
                ubi = 0
            except Exception as er:
                print(er)

        ubi_num = 1
        while ubi_num:
            try:
                ubi_mobile_number = input("\nEnter Your UBI Mobile Number:")
                ubi_mobile_number = ubi_mobile_number.replace(" ","")
                my_validation.customer_phone_number_validation(ubi_mobile_number)
                ubi_num = 0
            except Exception as er:
                print(er)

        pin = 1
        while pin:
            try:
                ubi_pin = int(input("\nEnter Your UBI PIN:"))
                if ubi_pin not in range(1000,9999):
                    print("UPI PIN should be 4 digits")
                else:
                    pin = 0
            except ValueError:
                print("\nUPI PIN should be in Numbers!!!")
                exception_type, exception_object, exception_traceback = sys.exc_info()
                self.create_error_log_file(self.cur_date,exception_traceback,exception_object,exception_type)

    # Here we create deliver_cart() for get thier delivery location.

    def deliver_cart(self,total_amount):
        print("\n"+("="*35))
        print("\nThe Available Delivery Locations are:")
        print("\n"+("="*35))
        self.total_delivery_value = 0
        dl_loc = 1
        while dl_loc:
            try:
                print("\n1.Anna Nagar")
                print("\n2.Adyar")
                print("\n3.Guindy")
                print("\n4.K.K.Nagar")
                print("\n5.Others")
                del_choice = int(input("\nEnter Your Choice:"))
                if del_choice == 1 or del_choice == 2 or del_choice == 3 or del_choice == 4:
                    print("\n"+("$"*35))
                    print("\nThe Total Price is to pay Rs."+str(total_amount))
                    print("\n"+("$"*35))
                    dl_loc = 0
                elif del_choice == 5:
                    print("\n"+("*"*35))
                    print("\nDelivery Charges will be Applied!!")
                    print("\n"+("*"*35))
                    del_loc = 1
                    while del_loc:
                        try:
                            dele_loca = input("\nEnter Your Location to Deliver:")
                            dele_loca = dele_loca.replace(" ","")
                            my_validation.name_validation(dele_loca)
                            print("\n"+("*"*35))
                            print("\nThe Delivery Charge is Rs.40")
                            print("\n"+("*"*35))
                            self.total_delivery_value = total_amount + 40
                            print("\n"+("$"*35))
                            print("\nAfter Applying Delivery Charges the Total Prise is Rs."+str(self.total_delivery_value))
                            print("\n"+("$"*35))
                            del_loc = 0
                            dl_loc = 0
                        except Exception as er:
                            print(er)
                else:
                    print("\nPlease Enter the Correct Choice!!!")
            except ValueError:
                exception_type, exception_object, exception_traceback = sys.exc_info()
                self.create_error_log_file(self.cur_date,exception_traceback,exception_object,exception_type)
                print("\nChoice must be in Numbers!!!")

    # Here we create delete_cart_items() for delete the cart items.

    def delete_cart_items(self):
        query = "insert into customer_cart_history(Customer_Name,Customer_Phone_Number,Customer_email,Item_id,Title,Brand,Price,Quantity,Category,Size)\
                 select Customer_Name,Customer_Phone_Number,Customer_email,Item_id,Title,Brand,Price,Quantity,Category,Size \
                 from clothing_cart where Customer_Phone_Number = %s"
        values = (self.current_customer_ph_no,)
        self.cursor.execute(query,values)
        query1 = "delete from clothing_cart where Customer_Phone_Number = %s"
        values1 = (self.current_customer_ph_no,)
        self.cursor.execute(query1,values1)
        self.mysql.commit()
                

    def update_stock_quantity(self):
        query = "select Item_id,Quantity from clothing_cart where Customer_Phone_Number = %s"
        value = (self.current_customer_ph_no,)
        self.cursor.execute(query,value)
        my_cart_quantity_data = self.cursor.fetchall()
        print(my_cart_quantity_data)
        for x in range(len(my_cart_quantity_data)):
            query1 = "select Stock_Quantity from clothing_item where Item_id = %s"
            value1 = (my_cart_quantity_data[x][0],)
            self.cursor.execute(query1,value1)
            my_old_stock = self.cursor.fetchall()
            print(my_old_stock)
            my_stock =my_old_stock[0][0]- my_cart_quantity_data[x][1]
            print(my_stock)
            query2 = "update clothing_item set Stock_Quantity = %s where Item_id = %s"
            values2 = (my_stock,my_cart_quantity_data[x][0])
            self.cursor.execute(query2,values2)
            self.mysql.commit()

    # Here we create check_out() for check out the cart Items.
                        
    def check_out(self):
        self.view_cart()
        if self.total_discount_value > 1000:
            print("\n"+("="*35))
            print("\nAfter Applying Discount the Total Price is:"+str(self.total_discount_value))
            print("\n"+("="*35))
        self.deliver_cart(self.total_discount_value)
        py_choose = 1
        while py_choose:
            try:
                pay_choose = int(input("\nPress 1 to Pay the Amount:"))
                if pay_choose == 1: 
                    pay_choice1 = 1
                    while pay_choice1:
                        try:
                            print("\n"+("o~"*21))
                            print("\n{:>28}*** Welcome to Payments Page ***".format(" "))
                            print("\n{:<27}".format(" "),("~o"*62))
                            print("\n{:>28}1.Credit/Debit Card".format(" "))
                            print("\n{:>28}2.Internet Banking".format(" "))
                            print("\n{:>28}3.Mobile Payments/UBI's".format(" "))
                            print("\n{:>28}4.Cash on Delivery".format(" "))
                            pay_choice = int(input("\nEnter Your choice:"))
                            if pay_choice == 1:
                                self.pay_Card()
                                self.update_stock_quantity()
                                self.delete_cart_items()
                                print("\nThank Your Order Will be Delivered in Your Location!!!")
                                pay_choice1 = 0
                                py_choose = 0
                            elif pay_choice == 2:
                                self.pay_net_banking()
                                self.update_stock_quantity()
                                self.delete_cart_items()
                                print("\nThank Your Order Will be Delivered in Your Location!!!")
                                pay_choice1 = 0
                                py_choose = 0
                            elif pay_choice == 3:
                                self.pay_mobile_ubi()
                                self.update_stock_quantity()
                                self.delete_cart_items()
                                print("\nThank Your Order Will be Delivered in Your Location!!!")
                                pay_choice1 = 0
                                py_choose = 0
                            elif pay_choice == 4:
                                self.update_stock_quantity()
                                self.delete_cart_items()
                                print("\nThank Your Order Will be Delivered in Your Location!!!")
                                pay_choice1 = 0
                                py_choose = 0
                            else:
                                print("\nPlease Enter the Correct Choice!!!!")
                                
                        except ValueError:
                            exception_type, exception_object, exception_traceback = sys.exc_info()
                            self.create_error_log_file(self.cur_date,exception_traceback,exception_object,exception_type)
                            print("\nChoice must be in Numbers!!!")
                else:
                    print("\nPlease Enter the correct Choice!!!")
            except ValueError:
                exception_type, exception_object, exception_traceback = sys.exc_info()
                self.create_error_log_file(self.cur_date,exception_traceback,exception_object,exception_type)
                print("\nChoice must be in Numbers!!!")

    # Here we create customer_login() for customer login to the portal.

    def customer_login(self):
        print("\n"+("="*35))
        print("\n*** Enter Your Registered Customer Details Below ***")
        print("\n"+("="*35))
        cus_log = 1
        log_list = []
        self.current_customer_name = ""
        self.current_customer_ph_no = 0
        self.current_customer_email = ""
        while cus_log:
            user_log = input("\nEnter your Registered Phone Number or Email Id:")
            query = "select * from customer_details where Phone_number = %s or Email_id = %s"
            values = (user_log,user_log)
            self.cursor.execute(query,values)
            my_data = self.cursor.fetchall()
            for x in my_data:
                self.current_customer_name = x[0]
                self.current_customer_ph_no = x[1]
                self.current_customer_email = x[2]
                for y in x:
                    log_list.append(str(y))

            l = open("login_logout_clothing_store.txt","a+")
            l.write("\nCustomerLogin - {} - {}".format(self.current_customer_name,self.cur_date))
            l.close()
                    
            if user_log in log_list:
                cus_log = 0
            else:
                print("\nPlease Enter the Correct Phone Number or Email ID")

        log_pass = 1
        while log_pass:
            user_password = input("\nEnter your Registered Password:")
            if user_password in log_list:
                log_pass = 0
            else:
                print("\nPlease Enter the Correct Password!!!")

        cus_choose = 1
        while cus_choose:
            try:
                print("\n"+("o~"*21))
                print("\n{:>28}*** Welcome to Customer Login Page ***".format(" "))
                print("\n{:<27}".format(" "),("~o"*62))
                print("\n{:>28}1.Browse clothing items".format(" "))
                print("\n{:>28}2.Add item to cart".format(" "))
                print("\n{:>28}3.View cart".format(" "))
                print("\n{:>28}4.Checkout".format(" "))
                print("\n{:>28}5.Exit".format(" "))
                log_choice = int(input("\nEnter Your Choice:"))
                query = "select * from clothing_cart where Customer_Phone_Number = %s"
                value = (self.current_customer_ph_no,)
                self.cursor.execute(query,value)
                my_data = self.cursor.fetchall()
                if log_choice == 1:
                    self.browse_clothing_items()
                elif log_choice == 2:
                    self.add_item_cart()
                elif log_choice == 3:
                    if my_data != []: 
                        self.view_cart()
                    else:
                        print("\nThe Cart is Empty!!!Please Add Item to the Cart to View the Purchase Items.")
                elif log_choice == 4:
                    count = 0
                    if my_data != []:
                        query = "select Item_id,Quantity from clothing_cart where Customer_Phone_Number = %s"
                        value = (self.current_customer_ph_no,)
                        self.cursor.execute(query,value)
                        my_cart_quantity_data = self.cursor.fetchall()
                        print(my_cart_quantity_data)
                        for x in range(len(my_cart_quantity_data)):
                            query1 = "select Stock_Quantity from clothing_item where Item_id = %s"
                            value1 = (my_cart_quantity_data[x][0],)
                            self.cursor.execute(query1,value1)
                            my_old_stock = self.cursor.fetchall()
                            print(my_old_stock)
                            if my_cart_quantity_data[x][1] > my_old_stock[0][0]:
                                count = 0
                                break
                            else:
                                count = 1
                        if count > 0:
                            self.check_out()
                        else:
                            print("\nSorry Stock Quantity out of Stock!!!")
                    else:
                        print("\nThe Cart is Empty!!!Please Add Item to the Cart to Checkout the Products!!!")
                elif log_choice == 5:
                    l = open("login_logout_clothing_store.txt","a+")
                    l.write("\nCustomerLogout - {} - {}".format(self.current_customer_name,self.cur_date))
                    l.close()
                    lo_choice = 0
                    cus_choose = 0
                else:
                    print("\nPlease Enter the Correct Choice!!!")
            except ValueError:
                exception_type, exception_object, exception_traceback = sys.exc_info()
                self.create_error_log_file(self.cur_date,exception_traceback,exception_object,exception_type)
                print("\nChoice must be in Numbers!!!")

    # Here we create main_menu() function to call all functions.

    def main_menu(self):
        choose = 1
        while choose:
            try:
                print("\n"+("o~"*21))
                print("\n{:>28}*** Welcome to Clothing Store Inventory Management System ***".format(" "))
                print("\n{:<27}".format(" "),("~o"*62))
                print("\n{:>28}1.Admin Login".format(" "))
                print("\n{:>28}2.Customer Register".format(" "))
                print("\n{:>28}3.Customer Login".format(" "))
                print("\n{:>28}4.Exit".format(" "))
                choice = int(input("\nEnter Your Choice:"))
                if choice == 1:
                    self.admin_login()
                elif choice == 2:
                    self.customer_register()
                elif choice == 3:
                    self.cursor.execute("select * from customer_details")
                    my_data = self.cursor.fetchall()
                    self.cursor.execute("select * from clothing_item")
                    my_data1 = self.cursor.fetchall()
                    if my_data1 != []:
                        if my_data != []:
                            self.customer_login()
                        else:
                            print("\nThere is no user to Login.Please First Register to Portal")
                    else:
                        print("\nThere is no Clothing Item for purchase.Please Visit Some Other Time Thank You!!!")
                elif choice == 4:
                    print("\n"+("o~"*21))
                    print("\n{:>28}*** Thank You For Using Clothing Store Inventory Management System ***".format(" "))
                    print("\n{:<27}".format(" "),("~o"*62))
                    choose = 0
                else:
                    print("\nPlease Enter the correct choice!!!")
            except ValueError as er:
                exception_type, exception_object, exception_traceback = sys.exc_info()
                self.create_error_log_file(self.cur_date,exception_traceback,exception_object,exception_type)
                print("\nChoice must be in Numbers.")

# Here we create object for Customer_manage class.

cloting_store = Customer_manage()

# Here we call the main_menu() by object.

cloting_store.main_menu()

        
    
