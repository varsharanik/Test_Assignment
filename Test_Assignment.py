import pandas as pd
import numpy as np

def coustomers_info():          # Function for checking the Subscription is Active or not
    cust_id = input("Enter your coustomer id to check all information about your Subscription: ")
    with open('C:/Users/ASUS/Desktop/Python3.8/cust_perf.txt', 'r') as fh:
        data = fh.read()
        if cust_id in (data):
            subs_id = input ("enter your subscription id: ")
            
            with open('C:/Users/ASUS/Desktop/Python3.8/subs_perf.txt', 'r') as fh1:
                data1 = fh1.read()
                if subs_id in (data1):
                    print ("your Coustomer id is 'Active' for ", cust_id, "and Subscription id ", subs_id )
                    #print((data) + (data1))
                else:
                    print ("Invalid Subscription id: ", subs_id)
        else:
            print ("Invalid Coustomer id ", cust_id)
            #break
        
def coustomers_performance():       # To calcualate the performance for given subscription
    Ans = input("Do you want to check your performance? ")
    if Ans in ('yes','y'):
        cust_id = input ("enter coustomer id to check performance: ")

        df = pd.read_txt("C:/Users/ASUS/Desktop/Python3.8/cust_perf.txt")   #Dataframe df
        if cust_id in df:
            print ( df )
            performance = df.sum(axis = 0, skipna = True)
            print ( performance )
            print ( performance['rtrn'].aggregate(np.sum))

#We can also calculate performance(sum of rtrn column) by importing Numpy library with pandas library

def daywise_performance():
    print ("you can check last 30 or last 60 days performance")
    Ans = input(" for how many days do you want to check performance??? 30 days or 60 days ??? : " )
    df = pd.read_txt("C:/Users/ASUS/Desktop/Python3.8/cust_perf.txt")    # dataframe df

    if Ans in ('30','30 days','30 Days','30 DAYS'):
        # Select the top 30 rows of the Dataframe
        dfObj1 = empDfObj.head(30)
        print("Last 30 days datewise performance: ")
        print(dfObj1)
        performance_30 = dfObj1.sum(axis = 0, skipna = True)
        print ( performance_30 )
        print ( performance_30['rtrn'].aggregate(np.sum))
    elif Ans in ('60','60 days','60 Days','60 DAYS'):
        # Select the top 60 rows of the Dataframe
        dfObj2 = empDfObj.head(60)
        print("Last 60 days datewise performance: ")
        print(dfObj2)
        performance_60 = dfObj2.sum(axis = 0, skipna = True)
        print ( performance_60 )
        print ( performance_60['rtrn'].aggregate(np.sum) )
    else:
        print ("Invalid entry")
        print ("please enter either 30 or 60")



    

coustomers_info()
print ("Coustomer information")
coustomers_performance()
print ("Coustomers overall performance")
daywise_performance()
print ("Coustomers datewise performance")
