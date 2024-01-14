# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 09:35:58 2023

@author: hilala-ug
"""

"""
Write a program Lab5_Q3.py, to track all customers and accounts of a customer (by
her/his customer number). Your program should store the list of customers and accounts in a
dictionary, where the key is the customer number and the value is a list of tuples (account id,
branch and balance). Your program should define the following functions:
1. addCustomer(): takes a dictionary of customers, a customer id number and
tuple containing the account id, branch, and balance as parameters and creates
a dictionary entry for the customer and adds the first account (tuple) to the list of
accounts. Display error message if customer already exists and success
message if customer is successfully added to the dictionary.
2. addAccount(): takes a dictionary, customer id number and account tuple
(account_id, account_branch, account_balance), and adds the account tuple to
the list of accounts. If the customer is not in the dictionary, display an error
message.
3. findCustomer(): takes a customer id number as a parameter and returns the
list of accounts of the given customer. Return None if the customer is not in the
list.
Your program should create a dictionary and implement the menu shown below.
1)Add Customer
2)Search Customer
3)Add Account
4)Quit
Enter Choice: 1
Enter customer number: 123
Enter account id: 11
Enter branch name: Bilkent
Enter balance: 100
Customer Added
1)Add Customer
2)Search Customer
3)Add Account
4)Quit
Enter Choice: 2
Enter customer number: 123
List of accounts: [(11, 'Bilkent', 100.0)]
1)Add Customer
2)Search Customer
3)Add Account
4)Quit
Enter Choice: 1
Enter customer number: 123
Enter account id: 234
Enter branch name: Bilkent
Enter balance: 200
Customer already exists
1)Add Customer
2)Search Customer
3)Add Account
4)Quit
Enter Choice: 2
Enter customer number: 123
List of accounts: [(11, 'Bilkent', 100.0)]
1)Add Customer
2)Search Customer
3)Add Account
4)Quit
Enter Choice: 1
Enter customer number: 5
Enter account id: 22
Enter branch name: Ulus
Enter balance: 200
Customer Added
1)Add Customer
2)Search Customer
3)Add Account
4)Quit
Enter Choice: 3
Enter customer number: 123
Enter account id: 55
Enter branch name: Ulus
Enter balance: 500
"""

all_customers={}

def add_customers(dicto ,no ,tupl):
    if no in dicto:
        print("Customer already exists")
    else:
        dicto[no]=[tupl]
        print("Customer Added")
    
def add_account(dicto ,no ,tupl):
    if no in dicto:
        dicto[no].append(tupl)
    else:
        print("Customer does not exists")
        
def search_customer(no):
    if no in all_customers:
        print("list of accounts:", all_customers[no])
    else:
        print("Customer does not exists")
        
    

choice= 1
while(choice==1 or choice==2 or choice==3 and choice==4):
    print("1)Add Customer")
    print("2)Search Customer")
    print("3)Add Account")
    print("4)Quit)")
    choice= int(input("Enter Choice: "))
    print("---------------------")
    if choice==1:
        no = int(input("Enter customer number: "))
        acc= int(input("Enter account id:"))
        branch=input("Enter branch name: ")
        balance= float(input("Enter balance:"))
        
        add_customers(all_customers, no, (acc,branch,balance))
        
    if choice==2:
        no = int(input("Enter customer number: "))
        
        search_customer(no)
        
        
    if choice==3:
        no = int(input("Enter customer number: "))
        acc= int(input("Enter account id:"))
        branch=input("Enter branch name: ")
        balance= float(input("Enter balance:"))
        
        add_account(all_customers, no, (acc,branch,balance))
    
    if choice==4:
        print("Program ended...")
    
    
    