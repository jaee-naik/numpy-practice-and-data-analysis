
#                 ---------------------- Numpy Tasks. --------------------------
# 
# 
#  # TASK 1: STUDENT MARKS ANALYSIS
# import numpy as np

marks = np.array([
    [78, 85, 90, 88, 76],
    [67, 72, 70, 75, 69],
    [91, 89, 95, 94, 92],
    [55, 60, 58, 62, 57],
    [80, 82, 84, 86, 88],
    [73, 75, 77, 79, 81],
    [95, 93, 97, 96, 94],
    [64, 68, 66, 70, 72],
    [88, 90, 85, 87, 89],
    [76, 78, 80, 82, 84]
])
#Display the complete marks array

print(f"The marks are :{marks} ")
print("="*64)


#  Calculate total marks obtained by every student
total=[]
for i in marks :
    total.append(int(sum(i)))
sub_count=len(i)    
print(total)    
print("="*64)

#  Calculate the average marks of every student

for i in total:
    avg= i/sub_count
    print(avg)  
print("="*64)

#  Find the student with the highest total marks

highest=np.max(total)
print(f"The highest marks are : {highest}")
print("="*64)

# # #sub wise highest marks  incomplte

sub_highest=np.max(marks,axis=0)
print(f"the subject wise hoghest marks {sub_highest}")
print("="*64)
            
 # average above 75
for i in total:
    avg = i / sub_count
    if avg >= 75:
        print(f"{avg}: Above average")
print("="*64)
#   ------------------------------------------------------------------------------------------------
# #task 2 : sales data analysis

import numpy as np


sales = np.array([
    [25000, 51000, 58000, 50000],
    [33000, 45000, 65000, 48000],
    [61000, 55000, 42000, 71000],
    [32000, 44000, 52000, 54000],
    [51000, 53000, 56000, 70000],
    [42000, 29000, 54000, 63000],
    [20000, 13000, 43000, 75000]
])

# print(sales)
print("="*64)

# #total of weekly sales  

weekly_sales=np.sum(sales,axis=0)
print(f"the total weekly sales are : {weekly_sales}")
print("="*64)                       
 

# #Total sales of each product

sales_product=np.sum(sales,axis=1)
print(f"the toatal sales of each product : {sales_product}")
print("="*64)


# #highest total sales
highest = max(total)
print(f"the highest sales are :{highest}")
print("="*64)

# #lowest toal sales
lowest=min(total)
print(f"The lowest sales are : {lowest}")
print("="*64)

# Find the week with the lowest total sales           
result=[]
for i in sales:
    a = np.sum(i)
    result.append(a)

lowest = np.min(result)
print(lowest)
print("="*64)

# #all sales value greater the 50000
new = []
for i in sales:
    for j in i:
        if j > 50000:
            new.append(int(j))
print(new)
print(""*64)
# ------------------------------------------------------------------------------------------------------
# TASK 3 :EMPLOYEE SALARY ANALYSIS

import numpy as np 

salary = np.array([35000, 42000, 55000, 60000, 48000,
    75000, 51000, 39000, 65000, 58000,
    47000, 52000, 70000, 45000, 53000])
print(salary)
print("="*64)

# #average
total = np.sum(salary)
count=len(salary)

average=total/count
print(average)
print("="*64)

# #find maximum and minimum salary

maximum=max(salary)
print(f"maximum salary: {maximum}")
minimum=min(salary)
print(f"Minimum salary : {minimum}")
print("="*64)

# #emp haing salary greater than 50000

high=[]

for i in salary:
    if i>50000:
        high.append(int(i))
print(f"emp having salary greater than 50000 are : {high}")
print("="*64)

# #count emps having salary below average
count = 0
for i in salary :
    if i<average:
        count+=1
print(f"the count of emp having salary below average are :{count}")
sort_salary=np.sort(salary)
sort_salary=sort_salary[::-1]
print(sort_salary)
print("="*64)
# -----------------------------------------------------------------------------------------------------------------

#task 4 :  TEMPERATURE MONITORING

import numpy as np
temp = np.array([
    25, 28, 27, 31, 35, 32, 36, 38, 34, 29,
    22, 22, 27, 30, 33, 37, 39, 40, 25, 26,
    21, 26, 36, 35, 34, 32, 27, 29, 22, 41
])
# display
print(temp)
print("="*64)

# #highest and lowest temp
highest=max(temp)
print(f"the highest temp is : {highest}")
lowest=min(temp)
print(f"the lowest temp is : {lowest}")
print("="*64)

# #average temp
total=np.sum(temp)
count=len(temp)

avg=total/count
print(f"average:{avg}")
print("="*64)

# #all days having temp above 35 c 
new=[]
for i in temp :
    if i>35:
        new.append(int(i))
print(f"days having temp above 35 : {new}")
print("="*64)

# #count day having temp below 25 c
count=0
for i in temp:
    if i<25:
        count+=1
print(count)
print("="*64)

# #diff between max and min 
diff=highest-lowest
print(f"difference: {diff}")
print("="*64)

# -------------------------------------------------------------------------------------------------------------
# TASK 5 : 5.  STUDENT ATTENDANCE SYSTEM

# import numpy as np 

attendene=np.array([90,80,54,67,70,
              88,65,99,34,67,
              48,87,67,56,44,
              86,67,78,89,92])
#display
print(attendene)
print("="*64)

# #average
total=np.sum(attendene)
count=len(attendene)
average=total/count
print(f"average: {average}")
print("="*64)


# #having attendence below 75
new=[]
for i in attendene:
    if i<75:
        new.append(int(i))
print(f"having attendence below 75 : {new}")
print("="*64)

# #count haivg above 90 
count=0
for i in attendene:
    if i>90:
        count+=1
print(f"count: {count}")     
print("="*64)   

# #highest and lowest attendence
high=max(attendene)
print(f"highest attendence: {high}")
low=min(attendene)
print(f"the lowest attendence : {low}")
print("="*64)

#replace all attend value below 75 to 0           
new=attendene.copy()
for i in new:
    if new[i]<75:
        new[i]=0
print(new)      
print("="*64)  

# #-----------------------------------------------------------------------------------------------------
# TASK6.  E-COMMERCE ORDER ANALYSIS
import numpy as np
orders = np.array([
    1200, 4500, 800, 2500, 6700,
    3200, 1500, 9000, 5200, 4300,
    7800, 1800, 6100, 2900, 7400,
    3600, 1100, 5500, 4800, 8300
])

# #revenue
revenue=np.sum(orders)
print(revenue)
print("="*64)

# #average
total=revenue
count=len(orders)
avg=total/count
print(f"average: {avg}")
print("="*64)

#orders below 2000
new=[]
for i in orders:
    if i>5000:
        new.append(int(i))
print(new)
print("="*64)

# #count below 2000
count=0
for i in orders:
    if i<2000:
        count+=1
print(count)
print("="*64)

# #sort orders in ascending order

sorted_list=np.sort(orders)
print(sorted_list)
print("="*64)

# #top 5 highest orders
sorted_list=sorted_list[::-1]
print(sorted_list[:5])
print("="*64)

# -------------------------------------------------------------------------------------------------------------------
#TASK 7:  BANK TRANSACTION ANALYSIS

import numpy as np

transactions = np.array([
    4000, -1000, 6000, -200, 3300,
    -1300, 7000, -2000, 2500, -300,
    3700, -2200, 1800, -800, 1200,
    -2000, 5500, -900, 1600, -1100,
    2900, -600, 3200, -2500, 1500,
    -500, 2800, -1700, 2100, -1300
])

#total balance 
total_balance=np.sum(transactions)
print(f"the total balance : {total_balance}")
print("="*64)
deposite=[]
for i in transactions:
    if i >0 :
        deposite.append(int(i))
print(f"deposite : {deposite}")
# 
print("="*64)

# find all withdrawal
withdrawal=[]
for i in transactions:
    if i<0:
        withdrawal.append(int(i))
print(f"the withdrawal : {withdrawal}")

print("="*64)

#total diposited amount
total_deposited=np.sum(deposite)
print(f"the total deposited amount is : {total_deposited}")
print("="*64)


#total withdrawal amount
total_withdrawal=np.sum(withdrawal)
print(f"the total withdrawal amount is : {total_withdrawal}")
print("="*64)

#largest withdrawal 
largest=np.max(withdrawal)
print(f"the largest withdrawal is : {largest}")
print("="*64)

#====================================================================================

# TASK 8.  HOSPITAL PATIENT DATA


import numpy as np

age = np.array([32,48,52,86,90,
                 12,10,15,78,65,
                 85,55,78,79,80,
                 45,43,44,40,38,
                 47,58,52,28,30])

#average age
total=np.sum(age)
count=len(age)

average=total/count
print(f"The average is : {average}")
print("="*64)


#youngest and oldest

youngest=np.min(age)
print(f"The youngest age is {youngest}")
oldest=max(age)
print(f"The oldest age is : {oldest}")
print("="*64)


#patients age above 60 years
new=[]
for i in age:
    if i>60:
        new.append(int(i))
print(f"the patients having age above 60 are : {new}")
print("="*64)

#count patient age below 18

count=0
for i in age:
    if i <18:
        count+=1
print(f"the patients having age below 18 are : {count}")   
print("="*64)

#sort patients age
sorted_list=np.sort(age)
print(sorted_list)
print("="*64)
a=np.median(age)
print(a)
print("="*64)

# ---------------------------------------------------------------------------------------------------------------------
# TASK 9.  EXAM RESULT ANALYSIS
import numpy as np

marks = np.array([
    [78, 85, 90, 88, 76, 80],
    [45, 56, 67, 70, 62, 58],
    [91, 92, 95, 89, 94, 90],
    [35, 42, 38, 50, 47, 40],
    [66, 72, 68, 75, 70, 73],
    [88, 84, 91, 86, 90, 89],
    [55, 60, 58, 62, 64, 61],
    [98, 96, 95, 99, 97, 98],
    [40, 45, 50, 42, 38, 41],
    [75, 78, 80, 82, 77, 79],
    [60, 65, 63, 67, 69, 64],
    [82, 85, 87, 90, 84, 86],
    [30, 35, 40, 45, 38, 42],
    [92, 90, 94, 91, 93, 95],
    [68, 70, 72, 74, 69, 71],
    [50, 55, 53, 58, 56, 54],
    [85, 88, 90, 87, 89, 91],
    [44, 48, 46, 50, 52, 49],
    [95, 97, 96, 98, 94, 99],
    [72, 74, 76, 78, 75, 77]
])

#each stud total marks

total_marks=[]
for i in marks:
    total_marks.append(int(sum(i)))
print(f"total marks of each student: {total_marks}")
suj_total=len(i)
print("="*64)


#ppercentage of each stud
percentage=[]
for i in total_marks:
    percentage.append((i/600)*100)
print(f"the percentage of each student is : {percentage} %")    
print("="*64)


#student with highest percentage
highest=np.max(percentage)
print(f"The highest percentage is : {highest}")
print("="*64)

# #subject wise average marks                      
average=np.mean(marks,axis=0)
print(average)
print("="*64)

#have marks below 40 in any subject
print("\nStudents Scoring Below 40 in Any Subject:")
for i in range(len(marks)):
    if np.any(marks[i] < 40):
        print("Student", i + 1, ":", marks[i])
print("="*64)


#count std having percentage above 80
count=0
for i in percentage:
    if i >80:
        count +=1
print(f"count : {count}")  
print("="*64)

      
# -----------------------------------------------------------------------------------------------------------
# Task 10. PRODUCT INVENTORY ANALYSIS

import numpy as np 

stock = np.array([
    [30, 25, 40],
    [15, 20, 18],
    [50, 35, 25],
    [10, 15, 12],
    [45, 30, 35],
    [22, 18, 20],
    [60, 55, 50],
    [12, 25, 18],
    [28, 32, 30],
    [16, 14, 19]
])

#display 
print(stock)
print("="*64)


#Calculate total stock for each product
total=np.sum(stock , axis=0)
print(f"total : {total}")

print("="*64)

#total stock in each warehouse
t=np.sum(stock , axis=1)
print(f"total : {t}")

print("="*64)
# 

# total stock below 100

for i in new:
    if i<100:
        print(f"stock below 100 are : {i}")
print("="*64)

#highest total stock
for i in new:
    high=max(new)
print(f"the highest total stock is : {high}")
print("="*64)

#replace stock below 20 to 0
   
a = stock.copy()
a[a < 20] = 0
print("Updated Stock:")
print(a)
print("="*64)
# -------------------------------------------------------------------------------------------------------------------

#TASK 11  CRICKET PLAYER STATISTICS

import numpy as np

runs = np.array([
    [45, 60, 30, 55, 70],
    [80, 75, 65, 90, 85],
    [25, 40, 35, 50, 45],
    [60, 55, 70, 65, 80],
    [15, 20, 25, 30, 35],
    [90, 95, 85, 80, 75],
    [50, 45, 55, 60, 50],
    [35, 40, 30, 45, 50],
    [70, 75, 80, 65, 60],
    [55, 50, 45, 40, 35]
])

print(runs)
print("="*64)

# #total runs of each player

total=[]
for i in runs:
    total.append(int(sum(i)))
print(f"total runs of each player : {total}")
print("="*64)

#average of each players 
average=[]
for i in total:
    average.append(i/5)
print (f"the average is : {average}")    
print("="*64)


#highest individual score
highest=np.max(runs)
print(f"highest individual score is : {highest}")
print("="*64)

#average above 50
for i in average:
    if i>50:
        print(f"the average above 50 is : {i} ")
print("="*64)

#sort players according to total runs         

result = []

for i in runs:
    a = np.sum(i)
    result.append(a)

print("Total runs of each player:")
print(result)

sorted_runs = np.sort(result)
print("Players' total runs in ascending order:")
print(sorted_runs)
# #-----------------------------------------------------------------------------------------------------------

# #12. ELECTRICITY CONSUMPTION ANALYSIS

import numpy as np

consumption = np.array([220, 450, 300, 480, 320, 250, 550, 490, 330, 490, 300, 340])

#annual comsumption 
total=np.sum(consumption)
print(f"the annual consumption is  : { total}")
print("="*64)

#average monthly comsuption 
average=total/len(consumption)
print(f"monthly average : {average:.2f}")
print("="*64)

#month with max comsuption 
highest=max(consumption)
print(f"the max consumption is : {highest}")
print("="*64)

#minimum consumption
lowest=min(consumption)
print(f"the minimum consumption is : {lowest}")
print("="*64)

# Months where consumption exceeded yearly average

for i in range(len(consumption)):
    if consumption[i] > average:
        print("Month", i + 1, "=", consumption[i])

print("="*64)

#per differemce between max and min 

percentage=((highest-lowest)/lowest)*100
print(f"the percentage difference is : {percentage}")
print("="*64)
# -------------------------------------------------------------------------------------------------------------
# TASK 13. IMAGE PIXEL ANALYSIS

import numpy as np

image = np.array([
    [110, 155, 60, 46, 310],
    [96, 190, 230, 180, 70],
    [20, 260, 155, 99, 230],
    [205, 110, 60, 190, 140],
    [90, 150, 215, 210, 35]
])

print(image)
print("="*64)

#max min 
maxmimum=np.max(image)
minimun=np.min(image)
print(f"the maximum image intensity is : {maxmimum}")
print(f"the minimum intensity is : {minimun}")
print("="*64)

#
 #average                
total=np.sum(image)
count=len(image)
avg=total/count
print(f"the average is : {avg}")
print("="*64)

# 
# #pixel greater than 200                  
a=[]
for i in image:
    for j in i :
        if j>200:
            a.append(int(j))
print(f"pixel having intersity greater than 200 are : {a}")    
print("="*64)


# # convert all pixel below 100 to 0 : 
image[image < 100] = 0
print("Image After Replacing Pixels Below 100:")
print(image)
print("="*64)


# Normalize pixel between 0 and 1
normalized_image = (image - np.min(image)) / (np.max(image) - np.min(image))   # min-max formla
print(normalized_image)    
#                                    or 
normalized_image=np.divide(image,225)
print(normalized_image)
print("="*64)

#================================================================================================================================

# 14. DATA NORMALIZATION

import numpy as np 

array=np.array([25,40,55,70,85,100,120,150,180,200])
print(array)
print("="*64)

#Calculate the minimum value

min_value=np.min(array)
print(f"the minimum value is : {min_value}")
print("="*64)

# Calculate the maximum value.
max_value=np.max(array)
print(f"the maximum value is :{max_value}")
print("="*64)

# Perform Min-Max normalization

normalize_value=(array-min_value)/(max_value-min_value)
print(f"the min max normalization is : \n {normalize_value}")
print("="*64)


#Convert normalized values into percentages

per=normalize_value*100
print(f"the normalized values in percentage are  :\n {per}")
print("="*64)


# Find values greater than the normalized average.
a=[]
avg=np.mean(normalize_value)
print(f"the Average is : {avg:.2f}")
for i in array:
    if i>avg:
        a.append(int(i))
print(f"the values greater then  normalized averge are : {a}")
print("="*64)



# Sort the normalized values.

sorted_value=np.sort(normalize_value)
print(f"the sorted normalizd values are :\n {sorted_value}")
print("="*64)

#====================================================================================================================================

#15. MATRIX ANALYSIS

matrix_A=np.array([[22,12,10],
                   [33,12,21],
                   [45,67,54]])

matrix_B=np.array([[10,2,5],
                   [8,3,1],
                   [6,9,6]])

#Perform matrix addition
addition = matrix_A+matrix_B
print(f"the ADDITION IS :\n {addition}")
print("="*64)


# Perform matrix subtraction
substraction = matrix_A-matrix_B
print(f"THE SUBSTRACTION IS  :\n {substraction}")
print("="*64)

# Perform element-wise multiplication

multiplication = matrix_A*matrix_B
print(f"THE MULTIPLICATION IS  : \n{multiplication}")
print("="*64)


#  Perform matrix multiplication.
m_mul=np.dot(matrix_A,matrix_B)
print(f"THE MATRIX WISE MULTIPLICATION IS: \n{m_mul}")
print("="*64)

# Calculate the transpose of both matrices 
transpose_A=np.transpose(matrix_A)
print(f"THE TRANSPOSE OF MATRIX A IS  : \n{transpose_A}")
print("="*64) 


transpose_B=np.transpose(matrix_B)
print(f"THE TRANSPOSE OF MATRIX B : \n{transpose_B}")
print("="*64)



#Calculate the  determinant of matrix A.

determinant = np.linalg.det(matrix_A)
print(f"Determinant of A: {determinant}")
print("="*64)

#=======================================================================================================

# 16. SALES PERFORMANCE BY REGION

import numpy as np 

sales = np.array([
   [80000, 97000, 100000, 320000, 305000, 135000],
  [93000, 86000, 110000, 330000, 325000,  140000],
    [70000, 80000, 95000, 100000, 90000,  110000],
    [100000, 110000, 120000, 115000, 135000, 150000]])


# Calculate total sales of each region

total=np.sum(sales,axis=1)
print(f"total of each region is : {total}")
print("="*64)

# Calculate total sales of each month.

total_sales=np.sum(sales,axis=0)
print(f"the toal sales of each month is  : {total_sales}")
print("="*64)


# Find the best-performing region
result=[]
for i in sales : 
    a=np.max(i)
    result.append(int(a))
print(result)
best=np.max(result)
print(f"the best performance is : {best} ")
print("="*64)


# Find the  best-performing month


a=[]
max_month=np.max(sales,axis=0)
a.append(max_month)
best_month=np.max(a)
print(f"the performing month is  : {best_month}")
print("="*64)

# Find all sales values above 100000

list=[]
for i in sales :
    for j in i:
        if j>100000:
            list.append(int(j))
print(list)
print("="*64)


# Calculate the average sales for every region.

print("Average sales of each region:")
print(np.mean(sales, axis=1))
print("="*64)
#==============================================================================================================================

# 17. NUMPY BROADCASTING CHALLENGE
# Create the price matrix
prices = np.array([
    [100, 200, 300],
    [150, 250, 350],
    [200, 300, 400],
    [250, 350, 450],
    [300, 400, 500]
])


# Create discount percentages
discount = np.array([10, 20, 30])


#  2. Apply discounts using NumPy broadcasting
discount_amount=prices*discount/100
print("discount amount=",discount_amount)
print("="*64)


# Calculate discounted prices
discounted_prices = prices - discount_amount
print("disconted pricev:",discounted_prices)
print("="*64)


# Total price before discount
total_before = np.sum(prices)
print("Total price before discount:", total_before)
print("="*64)



# Total price after discount
total_after = np.sum(discounted_prices)
print("Total price after discount:", total_after)
print("="*64)



# Total discount amount for each product
total_discount = np.sum(discount_amount, axis=1)
print("Total discount amount for each product:", total_discount)
print("="*64)

#========================================================================================================

# 18. COMPLETE DATA ANALYTICS CHALLENGE

import numpy as np

# Employee_ID Age Experience Salary Performance_Score Projects_Completed
data = np.array([
    [101, 24, 1, 30000, 72, 4],
    [102, 29, 4, 50000, 88, 7],
    [103, 26, 2, 35000, 78, 5],
    [104, 32, 6, 65000, 92, 9],
    [105, 28, 3, 45000, 85, 6],
    [106, 35, 8, 75000, 95, 10],
    [107, 23, 1, 28000, 68, 3],
    [108, 30, 5, 55000, 82, 8],
    [109, 27, 3, 40000, 76, 4],
    [110, 33, 7, 60000, 90, 9]
])

print(data)
print("="*64)


#  Calculate the average salary of all employees

avg=np.mean(data[:3])
print(f"the average salary is : {avg}")
print("="*64)


# Find employees whose performance score is above 80. 

print("Employees with performance score above 80:")
for i in data:
    if i[4] > 80:
        print(f"the emp id {i[0]} has performance above 80")

print("="*64)



#   Find employees having more than 5 completed projects
print("employess havinhg completed more then 5 projects : ")
for i in data:
    if i[5]>5:
        print(f" the emp id {i[0]} has completed project more than 5 = {i[5]}")
print("="*64)



# Find the employee with the highest salary.
highest=np.max(data[:,3])
print(highest)
print("="*64)


# Find the employee with the highest performance score
highest_score=np.max(data[:,4])
print(highest_score)
print("="*64)


# Find employees who satisfy both conditions: - Salary > 50000 - Performance Score > 80

print("Employees satisfying both conditions:")
for i in data:
    if i[3] > 50000 and i[4] > 80:
        print(f"the emp id {i[0]} satisfies both condition")
print("="*64)
