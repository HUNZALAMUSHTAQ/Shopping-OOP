from os import name
from datetime import datetime as d
from abc import ABC,abstractmethod
from EmailSender import Email_sender_s
import sqlite3

#USER CLASS(PARENT CLASS)
class user:
    def __init__(self):
        print('------------------------------------------------------------')
        self.choice = input("DO YOU WANT TO LOGIN AS ADMINISTRATOR[YES/NO]:")
        print('----------------------------------------------------')
        if self.choice=='YES':
            A=administrator()
        elif self.choice=='NO':
            B=customer()
        else:
            print('INVALID INPUT!!!')

    def info_(self):
        self.email=input('Enter email address:')
        self.password=input('Enter password:')


    def sign_up(self):
        database=sqlite3.connect('user.db')                 #build a connection
        cor=database.cursor()                               #creating a cursor
        cor.execute('''CREATE TABLE IF NOT EXISTS users(
            first_name text,
            last_name text,
            user_name text,
            password text,
            email text)''')                                      #creating table

        lst=[self.first_name,self.last_name,self.user_name,self.password,self.email]
        cor.execute("INSERT INTO users VALUES(?,?,?,?,?)",lst)

        #commit our command
        database.commit()
        #close our connection
        cor.close()

    def user_info(self):
        print("you can only enter your username ")
        #check user name
        self.choice=[input('enter username:')]

        database=sqlite3.connect('user.db')
        cor=database.cursor()

        cor.execute('SELECT * FROM users WHERE user_name = (?)',self.choice)
        #print the user info.
        items= cor.fetchall()
        print("FIRST NAME"+"\t\t\t\t\tLAST NAME" + "\t\t\t\t\tUSER NAME" + "\t\t\t\t\tPASSWORD"+"\t\t\t\t\tEMAIL ADDRESS")
        print("----------------"+"\t\t\t\t----------------"+"\t\t\t\t-----------------"+"\t\t\t\t------------------"+'\t\t\t\t-------------------')
        for item in items:
            print(item[0]+'\t\t\t\t'+item[1]+'\t\t\t\t'+item[2]+'\t\t\t\t'+item[3]+'\t\t\t\t\t'+item[4])

        #COMMIT OUR COMMAND
        database.commit()
        #CLOSE OUR CONNECTION
        cor.close()


class Product:
    #CREATIE TABLE OF PRODUCTS
    def create_table(self):
        database1=sqlite3.connect('product.db')
        cor1=database1.cursor()                                              #creating a cursor
        cor1.execute('''CREATE TABLE IF NOT EXISTS products(
            cake_flavor text,
            quantity text,
            unit_price text,
            stock text)''')

        cake_lst=[                                                            #cake list
                ('Kitkat Cake','2.5 Pound','1400.00','20'),
                ('Chocalate Heaven Cake','2.5 Pound','1400.00','20'),
                ('Galaxy Cake','2.5 Pound','1400.00','20'),
                ('Coffee Cake','2.5 Pound','1200.00','20'),
                ('Nutella Cake','2.5 Pound','1500.00','20'),
                ('Red Velvet Cake','2.5 Pound','1200.00','20'),
                ('Black Forest Cake','2.5 Pound','1100.00','20'),
                ('Belgian Chocolate','2.5 Pound','1400.00','20'),
                ('Caramel Crunch Cake','2.5 Pound','1000.00','20'),
                ('Bombay Bakery Coffee Cake','2.5 Pound','1000.00','20')
                ]
        cor1.executemany("INSERT INTO products VALUES(?,?,?,?)",cake_lst)
        #commit our command
        database1.commit()
        #close our connection
        cor1.close()

#DISPLAY PRODUCTS IN  TABLE FORM
    def display(self):
        database1=sqlite3.connect('product.db')
        cor1=database1.cursor()
        #EXECUTE OUR COMMAND
        cor1.execute('SELECT rowid,* FROM products')
        #FETCHING VALUES
        items= cor1.fetchall()
        print("PRODUCT_ID"+"\t\tCAKE_FLAVOUR" + "\t\t\tQUANTITY" + "\t\t\tPRICE"+"\t\t\tSTOCK")
        print("-------------"+"\t\t-------------"+"\t\t\t---------------"+"\t\t\t-------------"+'\t\t------------')
        for item in items:
            if item[0]==1 or item[0]==3 or item[0]==4 or item[0]==5 or item[0]==6 :
                print(str(item[0])+'\t\t\t'+item[1]+'\t\t\t'+item[2]+'\t\t\t'+(item[3])+'\t\t\t'+(item[4]))
            elif item[0]==10:
                print(str(item[0])+'\t\t\t'+item[1]+'\t'+item[2]+'\t\t\t'+(item[3])+'\t\t\t'+(item[4]))
            else:
                print(str(item[0])+'\t\t\t'+item[1]+'\t\t'+item[2]+'\t\t\t'+(item[3])+'\t\t\t'+(item[4]))
        #COMMIT OUR COMMAND
        database1.commit()
        #CLOSE OUR CONNECTION
        cor1.close()

#METHOD HAVING MORE INFORMATION ABOUT THE PRODUCTS
    @staticmethod
    def info(select):
        if select==1:
            return "Imported Chocolate with soft sponge layered to perfection ,topped with KitKat"
        if select==2:
            return 'A decadent chocolate cake with smooth chocolate'
        if select==3:
            return 'Covered with creamy galaxy chocolate butter cream with moist chocolate sponge'
        if select==4:
            return 'A moist ,tender sponge cake with two layers separated by coffee and butter icing'
        if select==5:
            return 'Richly flavored chocolate cake lathered in a delicious Nutella icing'
        if select==6:
            return 'Classic red velvet cake with cream cheese icing'
        if select==7:
            return 'Creamy, chocolate-cherry dream!Made with Moist chocolate cake,cocktail filling,and vanilla whipped cream'
        if select==8:
            return 'Coated with ganache made from chocolate and cream ,topped with bittersweet chocolatae curls and surrounded by crunchy hazelnuts'
        if select==9:
            return 'Soft melt in mouth vanilla sponge topped butter cream frosting along with caramel sauce'
        if select==10:
            return 'Our take on famous Bombay coffe cake,coffee based spomge with coffee frosting'
#DISPLAY PRODUCTS INFORMATION
    def product_info(self):
        while True:
            print('See further info. of CAKE :','\n'+'\n'+'select product_id :',end='')
            select=int(input())
            print('------------------------------------------------------------------------------------------------------------------------')
            choice=self.info(select)
            print(choice)
            print('------------------------------------------------------------------------------------------------------------------------')
            print()
            print('do you want to see more info',end='')
            e=input('ENTER HERE[Y/N]:')
            if e=='Y':
                continue
            else:
                break

#CUSTOMER CLASS(CHILD USER)
class customer(user):
    email__=None
    def input(self):
        print('''CREATING  ACCOUNT
        PLEASE FILL OUT GIVEN INFO..''')                                         #taking user's information
        self.first_name=input('Enter your first name:')
        self.last_name=input('Enter last name:')
        self.user_name=input('Enter user name for your account:')
        self.info_()
        self.sign_up()
        print('\t\tACCOUNT HAS BEEN CREATED..!!!')

    def login(self):
        print('==================================')
        print('LOGIN TO YOUR ACCOUNT')
        print('-----------------------------------')
        self.email__=input("Enter email:")
        self.passw=input('Enter password:')
        lst1=[self.email__,self.passw]
        customer.email__=self.email__

        # connection to database
        database=sqlite3.connect('user.db')
        cor=database.cursor()
        cor.execute('SELECT * FROM users WHERE email = (?) AND password = (?)',lst1)
        d=cor.fetchall()
        if d == []:
            print('''email or password is incorrect...
            1.TRY AGAIN
            2.FORGOT PASSWORD
            ''')
            q=int(input('PLEASE ENTER [1/2]:'))
            if q == 1:
                self.login()
            else:                       #WHEN USER ENTERS WRONG PASSWORD
                A=Email_sender_s()
                A.send_code(self.email__)
                print('YOU HAVE TO VERIFY YOUR CODE....')
                w=A.verify_me()
                if w=='Verified':
                    print('****************************** VERIFIED ******************************************')
                    self.call()
                else:
                    print('INCORRECT')
                    print('RESENDING THE CODE AGAIN')
                    A.resend_code()
                    A.verify_me()
                    self.call()
        else:
            print('=========================================== SUCCESSFULLY LOGIN....================================================')
            print()
            self.call()


    def call(self):
        #MAIN FLOW OF OUR PROGRAM
        C= Product()
        C.create_table()            #this should be comment out after 1st run
        C.display()
        print()
        C.product_info()
        #instantiate shopping_cart class
        q=shopping_cart()
        q.add_item()
        q.remove_item()
        print('-------------------------------------------------------------------')
        ask_=input('''DO YOU WANT TO SEE YOUR CART[Y]
            OR
DO YOU WANT TO CHECK OUT[C]:''')
        print('--------------------------------------------------------------------')
        if ask_=='Y':
            q.view_cart()
            print("=======================================================================")
        else:
            q.check_out()
        print('-------------------------------------------------------------------')
        ask1=input('DO YOU WANT TO SEE YOUR PREVIOUS ORDERS:[Y/N]')
        if ask1=='Y':
            r=record_of_customers()
            r.history()
            V=main()
            V.print()
        else:
            V=main()
            V.print()

# CUSTOMERS' INFO
    def __init__(self):
        self.account=input('DO YOU HAVE AN ACCOUNT[Y/N]:')
        if self.account=='Y':
            self.login()
        elif self.account=='N':
            self.input()
            self.login()
        else:
            print("YOU HAVE ENTERD WRONG OPTION")




#(CHILD CLASS OF USER)
class administrator(user):
    #PRINT ALL USERS' INFORMATION
    def users_info(self):
        database=sqlite3.connect('user.db')
        cor=database.cursor()
        cor.execute('SELECT * FROM users')
        #print the users info.
        items= cor.fetchall()
        print("FIRST NAME"+"\t\tLAST NAME" + "\t\tUSER NAME" + "\t\t\t\tPASSWORD"+"\t\t\t\tEMAIL ADDRESS")
        print("--------------"+"\t\t--------------"+"\t\t------------------"+"\t\t-------------------------"+'\t\t------------------------------')
        for item in items:
            print(item[0]+'\t\t\t'+item[1]+'\t\t\t'+item[2]+'\t\t\t\t'+item[3]+'\t\t\t\t'+item[4])

        #CCOMMIT OUR COMMAND
        database.commit()
        #CLOSE OUR CONNECTION
        cor.close()

    def update_table(self):
        database1=sqlite3.connect('product.db')
        cor1=database1.cursor()
        sql_statement=("UPDATE products SET stock = 20 WHERE stock = 0")        #UPDATE THE PRODUCTS' DATA BASE
        cor1.execute(sql_statement)
        database1.commit()                                                  #COMMIT OUR DATABASE
        cor1.close()                                                        #CLOSE OUR CONNECTION
        #DISPLAY OUR PRODUCTS' TABLE
        D=Product()
        D.display()

    # LOGIN INFORMATION OF ADMINISTRATOR
    def __init__(self):
        self.info_()
        if self.email == "computerprogram812@gmail.com" and self.password == "computer812":
            print('''YOU HAVE FOLLOWING OPTIONS
            1.YOU CAN SEE THE USERS INFORMATION
            2.YOU CAN UDPATE THE PRODUCTS STOCK''')
            self.check_=int(input('Please enter the number:'))
            if self.check_ == 1:
                self.users_info()
            elif self.check_ == 2:
                self.update_table()
        else:
            print("INVALID EMAIL OR PASSWORD..")


class shopping_cart():
    datetime=None
    value=0
    shop_dict={}
    def __init__(self):
        #connection to the data base
        database1=sqlite3.connect('product.db')
        cor1=database1.cursor()
        cor1.execute('SELECT * FROM products')                       #fetch all values
        fet=cor1.fetchall()
        #creating dictionary
        self.dict={1:list(fet[0]),2:list(fet[1]),3:list(fet[2]),4:list(fet[3]),5:list(fet[4]),6:list(fet[5]),7:list(fet[6]),8:list(fet[7]),9:list(fet[8]),10:list(fet[9])}
        database1.commit()                              #COMMIT OUR DATABASE
        cor1.close()                                    #CLOSE OUR CONNECTION

    def add_item(self):
        print('=============================================================================')
        while True:
            self.check1=input("ADD TO CART[Y/N]:")
            print('----------------------------------------------------------')
            if self.check1=='Y':
                #taking input(cake name) from user(key)
                print("Enter CAKE ID:",end='')
                self.key=int(input())                                       #row id
                self.quan=int(input("Enter QUANTITY:"))                     #taking the quantity
                print('--------------------------------------------------------')
                self.get1=self.dict.get(self.key)                              #fetch the required list with the key
                self.a=int(self.get1[3])
                if self.a == 0:
                    print("OUT OF STOCK..!!!")
                if self.a < self.quan:
                    print(self.a,'IS AVAILABLE...')
                    print('TRY AGAIN....BY PLACING YOUR ORDER...')
                    self.add_item()
                else:
                    self.a-=self.quan                                    #subtracting the quantity
                    self.get1[3]=self.a
                    # print(self.get1)                                   #updated list of product
                    self.dict[self.key]=self.get1
                    #connection to the data base
                    database1=sqlite3.connect('product.db')
                    cor1=database1.cursor()
                    #UPDATING THE PRODUCT'S DATA BASE
                    sql_statement="UPDATE products SET stock = (?) WHERE rowid = (?)"
                    temp=(self.get1[3],self.key)
                    cor1.execute(sql_statement,temp)
                    database1.commit()                              #COMMIT OUR DATABASE
                    cor1.close()                                    #CLOSE OUR CONNECTION
                    #apppending into the cart
                    shopping_cart.shop_dict.update({self.get1[0]:[self.get1[2],self.quan,self.quan*float(self.get1[2])]})
            else:
                break

    def remove_item(self):
        print('==================================================================')
        print(shopping_cart.shop_dict)                                  #PRINTS THE CURRENT SHOPPING CART
        while True:
            self.check2=input("REMOVE FROM CART[Y/N]:")
            print('---------------------------------------------------------------')
            if self.check2 == 'Y':
                self.cake=input('Enter the CAKE NAME:')                 #entering cake name
                self.lst2=shopping_cart.shop_dict.get(self.cake)        #value(list) of the key(self.cake)
                self.quan1=int(input("Number of CAKES:"))               #number of cakes
                print('---------------------------------------------------------------')
                if self.lst2[1]>self.quan1:
                    self.lst2[1]-=self.quan1                            #removing the quantity of cake from cart
                    self.get1[3]+=self.quan1                            #returning the quantity to the dictionary(shop_dict)
                    self.lst2[2]=self.lst2[1]*float(self.lst2[0])       #calculating the total price of cake

                    self.dict[self.key]=self.get1

                    #connection to the data base
                    database1=sqlite3.connect('product.db')
                    cor1=database1.cursor()
                    #UPDATING THE PRODUCT'S DATA BASE
                    sql_statement="UPDATE products SET stock = (?) WHERE rowid = (?)"
                    temp=(self.get1[3],self.key)
                    cor1.execute(sql_statement,temp)
                    database1.commit()                              #COMMIT OUR DATABASE
                    cor1.close()                                    #CLOSE OUR CONNECTION
                elif self.lst2[1]==self.quan1:
                    print('this cake has been removed from your cart!!')
                    # print(shopping_cart.shop_dict.pop(self.cake))
                else:
                    print("your cart does not contain enough quantity..!!")
            else:
                break

    def view_cart(self):
        tu=shopping_cart.shop_dict.items()                                      #taking out the key value pair
        print('===========================================================================')
        print('CAKE NAME'+'\t\t\t\t'+'UNIT PRICE'+'\t\t\t\t'+'QUANTITY'+'\t\t\t\t'+'TOTAL PRICE')
        print('--------------------'+'\t\t--------------------'+'\t\t\t-----------------------'+'\t\t\t-------------------')
        for item in tu:
            a=item[0].split()
            if len(a)==2:
                 print(item[0]+'\t\t\t\t'+str(item[1][0])+'\t\t\t\t\t'+str(item[1][1])+'\t\t\t\t\t'+str(item[1][2]))
            if len(a)==3:
                print(item[0]+'\t\t\t'+str(item[1][0])+'\t\t\t\t\t'+str(item[1][1])+'\t\t\t\t\t'+str(item[1][2]))
            if len(a)==4:
                print(item[0]+'\t\t'+str(item[1][0])+'\t\t\t\t\t'+str(item[1][1])+'\t\t\t\t\t'+str(item[1][2]))
            a=0
            self.lst3=[]
            for i in tu:
                self.lst3.append(i)
            for j in range (len(self.lst3)):
                a+=self.lst3[j][1][2]
            shopping_cart.value=a
        print('----------------------------------------------------------------------------------------------------------------------------')
        print('TOTAL BILL IS',a,'RS')
        print()
        #add/remove the item
        self.check1=input('''WANT TO ADD OR REMOVE[Y]
            OR
ELSE YOU CAN CHECK OUT[C]:''')
        if self.check1=='Y':
            self.add_item()
            self.remove_item()
            self.view_cart()
        else:
            self.check_out()

    def check_out(self):
        print('---------------------------------------------------------------------')
        self.remove_item()
        print('***************************************************************')
        credit_no=int(input("Enter CREDIT CARD Number:"))
        print('=============================================================')
        print("\t\t\tCHECKING OUT!!!")
        print('-------------------------------------------------------------------')
        shopping_cart.datetime=d.now()
        print('TOTAL BILL IS',shopping_cart.value,'RS')
        print('--------------------------------------------------------------------')
        print('YOUR CHECKING OUT DATE AND TIME IS:'+'\t\t'+str(shopping_cart.datetime))
        print()
        # else:
        #     print('AN INVALID OPTION ENTERED..!!')

class record_of_customers:
    def __init__(self):
        self.ask1=input("Enter your EMAIL:")
        print('-----------------------------------------------------------')
        self.history()                                                #want to see your record or not

    def history(self):
        item=shopping_cart.shop_dict
        #history database
        database2=sqlite3.connect('shopping history.db')
        cor2=database2.cursor()

        cor2.execute('''CREATE TABLE IF NOT EXISTS history(
            email text,
            shopping_list text,
            total_bill text,
            datetime text
        )''')                                  #creating table

        lst=[customer.email__,str(item),shopping_cart.value,shopping_cart.datetime]
        cor2.execute("INSERT INTO history VALUES(?,?,?,?)",lst)

        cor2.execute('SELECT * FROM history WHERE email = (?)',[self.ask1])
        d=cor2.fetchall()
        print('CUSTOMER NAME'+'\t\t\t'+'DATE AND TIME')
        print('================================================================')
        for items in d:
            a=list(eval(items[1]))
            print(items[0]+'\t\t\t'+items[3])
            print('''===============================================================
                    CAKE ORDERED''')
            for i in range(len(a)):
                print('\t\t'+a[i])
            print('---------------------------------------------------------')
            print('\t\t\t\t\t\t'+'TOTAL BILL')
            print('\t\t\t\t\t\t'+items[2]+'RUPEES')
            print('===================================================================')
        #COMMIT OUR COMMAND
        database2.commit()
        #CLOSE OUR CONNECTION
        cor2.close()




class abstractclass(ABC):
    @abstractmethod
    def print(self):
        pass

class main(abstractclass):
    def print(self):                                #OVERRIDING PRINT FUCNTION
        print('''\t\t\t ============= THANKYOU FOR VISITING OUR BAKERY ===========
\t\t\t =================== DO VISIT AGAIN =======================
\t\t\t ================= HAVE A GOOD DAY.... :)))===============''')



X=user()






