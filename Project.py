import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data_set="Sales_Dataset.csv"
df=pd.read_csv(data_set)

#Data Cleaning Start

df=df.drop_duplicates().reset_index(drop=True)
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")
df.loc[df['Price'] < 0, 'Price'] = np.nan
df["Price"] = df["Price"].fillna(int(df["Price"].median()))
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
df.loc[df['Quantity'] < 0, 'Quantity'] = np.nan
df["Quantity"] = df["Quantity"].fillna(int(df["Quantity"].median()))
df["City"] = df["City"].fillna(df["City"].mode()[0])
df["Total_Sales"] = pd.to_numeric(df["Total_Sales"], errors="coerce")
df.loc[df['Total_Sales'] < 0, 'Total_Sales'] = np.nan
df["Total_Sales"] = df["Total_Sales"].fillna(int(df["Total_Sales"].median()))
df["Customer_Age"] = pd.to_numeric(df["Customer_Age"], errors="coerce")
df.loc[df['Customer_Age'] < 14, 'Customer_Age'] = np.nan
df["Customer_Age"] = df["Customer_Age"].fillna(int(df["Customer_Age"].median()))
df["Total_Cost"] = pd.to_numeric(df["Total_Cost"], errors="coerce")
df.loc[df['Total_Cost'] < 0, 'Total_Cost'] = np.nan
df["Total_Cost"] = df["Total_Cost"].fillna(int(df["Total_Cost"].median()))
df["Total_Cost"] = (df["Price"] * df["Quantity"] * 0.7).round(2)

#Data Cleaning End

#Checking Cleaned Dataset
# print(df.isnull().sum())   
# print(df.shape)            
# print(df.dtypes)

def menu():
    print("******Data Analysis Dashboard******")
    print("Operations That can be Performed:-")
    print("1.Maximum Sales")
    print("2.Minimum Sales")
    print("3.Average Sales")
    print("4.Median Sales")
    print("5.Sales By Products")
    print("6.Max Sales Per City")
    print("7.Min Sales Per City")
    print("8.Total Sales")
    print("9.Sales Over The Years(Line Chart)")
    print("10.Most Sold Product")
    print("11.Least Sold Product")
    print("12.Frequency Of Products Sold")
    print("13.Total Profit")
    print("14.Profit Over The Years(Line Chart)")

def operations():
    op=input("Enter Your Operation No. (M for Menu):")
    if op.isdigit():
        op=int(op)
    match op:
        case 1:
            yr = input("Enter the year(2021-2025) or type 'all': ")
            if yr in ['2021','2022','2023','2024','2025','all']:
                df["Date"] = pd.to_datetime(df["Date"])
                df["Year"] = df["Date"].dt.year
                if yr.lower() == "all":
                    print("Max sales overall:", df["Total_Sales"].max())
                else:
                    yr = int(yr)
                    max_sales = df.loc[df["Year"] == yr, "Total_Sales"].max()
                    if pd.isnull(max_sales):
                        print("No result,Enter Valid Value")
                    else:    
                        print("Maximum Sales:",max_sales)
            else:
                print("Year Not in Dataset")
                
        case 2:
            yr = input("Enter the year(2021-2025) or type 'all': ")
            if yr in ['2021','2022','2023','2024','2025','all']:
                df["Date"] = pd.to_datetime(df["Date"])
                df["Year"] = df["Date"].dt.year
                if yr.lower() == "all":
                    print("Min sales overall:", df["Total_Sales"].min())
                else:
                    yr = int(yr)
                    min_sales = df.loc[df["Year"] == yr, "Total_Sales"].min()
                    if pd.isnull(min_sales):
                        print("No result,Enter Valid Value")
                    else:    
                        print("Mininum Sales:",min_sales)
            else:
                print("Year Not in Dataset")
        
        case 3:
            mean_sales = df["Total_Sales"].mean()
            print("Average Sales:", int(mean_sales))

        case 4:
            median_sales = df["Total_Sales"].median()
            print("Median Sales:", int(median_sales))
            
        case 5:
            sales_by_product=df.groupby("Product")["Total_Sales"].sum()
            print("Sales By Product:")
            print(sales_by_product)
        
        case 6:
            max_sales_by_city=df.groupby("City")["Total_Sales"].max().idxmax()
            print("Max Sales By City:",max_sales_by_city)

        case 7:
            min_sales_by_city=df.groupby("City")["Total_Sales"].min().idxmin()
            print("Min Sales By City:",min_sales_by_city)
            
        case 8:
            yr = input("Enter the year(2021-2025) or type 'all': ")
            if yr in ['2021','2022','2023','2024','2025','all']:
                df["Date"] = pd.to_datetime(df["Date"])
                df["Year"] = df["Date"].dt.year
                if yr.lower() == "all":
                    print("Sum sales overall:", df["Total_Sales"].sum())
                else:
                    yr = int(yr)
                    total_sales = df.loc[df["Year"] == yr, "Total_Sales"].sum()
                    if total_sales==0:
                        print("No result,Enter Valid Value")
                    else:    
                        print("Total_Sales:",total_sales)
            else:
                print("Year Not in Dataset")
        
        case 9:
            df['Date'] = pd.to_datetime(df['Date'])
            df['Year'] = df['Date'].dt.year
            yearly_sales = df.groupby('Year')['Total_Sales'].sum()
            yearly_sales.plot()
            plt.title('Sales Over the Years')
            plt.xlabel('Year')
            plt.ylabel('Total Sales (₹)')
            plt.grid()
            plt.xticks(yearly_sales.index)
            plt.tight_layout()
            plt.show()
    
        case 10:
            most_sold_product=df.groupby("Product")["Quantity"].sum().idxmax()
            print("Most Sold Product:",most_sold_product)

        case 11:
            least_sold_product=df.groupby("Product")["Quantity"].sum().idxmin()
            print("Least Sold Product",least_sold_product)

        case 12:
            all_sold_product=df.groupby("Product")["Quantity"].sum()
            print("Sold Products Frequency:")
            all_sold_product=all_sold_product.astype(int)
            print(all_sold_product)
        
        case 13:
            df["Profit"]=df["Total_Sales"]-df["Total_Cost"]
            yr = input("Enter the year(2021-2025) or type 'all': ")
            if yr in ['2021','2022','2023','2024','2025','all']:
                df["Date"] = pd.to_datetime(df["Date"])
                df["Year"] = df["Date"].dt.year
                if yr.lower() == "all":
                    print("Total Profit Overall:", int(df["Profit"].sum()))
                else:
                    yr = int(yr)
                    max_sales = df.loc[df["Year"] == yr, "Profit"].sum()
                    if pd.isnull(max_sales):
                        print("No result,Enter Valid Value")
                    else:    
                        print("Total Profit:",int(max_sales))
            else:
                print("Year Not in Dataset")
        
        
        case 14:
            df["Profit"]=df["Total_Sales"]-df["Total_Cost"]
            df['Date'] = pd.to_datetime(df['Date'])
            df['Year'] = df['Date'].dt.year
            yearly_profit = df.groupby('Year')['Profit'].sum()
            yearly_profit.plot()
            plt.title('Profit Over the Years')
            plt.xlabel('Year')
            plt.ylabel('Total Profit (₹)')
            plt.grid()
            plt.xticks(yearly_profit.index)
            plt.tight_layout()
            plt.show()
        
        case 'M':
            menu()
            operations()
            
        case _:
            print("Choose From Above Options Only")
            operations()

menu()
operations()
while(True):
    con=input("Do You Want to Continue(y/n):")
    if con=='y':
        operations()
    elif con=='n':
        print("Program Has Ended")
        exit(0)
    else:
        print("Please Only Choose From Above Options")