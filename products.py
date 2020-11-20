# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 10:30:41 2020
@author: Linter
"""
#讀取之前檔案
def read_file(filename):
    products = []
    with open(filename, "r", encoding = "utf-8") as f:
            for line in f:
                if "商品,價格" in line:
                    continue
                name, price = line.strip().split(",")
                products.append([name,price]) 
    return products
         
#輸入新的商品
def user_input(products):
    while True:
        name = input("輸入商品名字: ")
        if name == "q":
            break
        price = input("輸入商品價格: ")
        p = [name, price]
        products.append(p)
    print(products)
    return products

#列出所有購買商品
def print_list(products):
    for p in products:
        print(p[0],"的價格是", p[1])

#寫入商品資料
def writen_data(filename, products):    
    with open(filename, "w", encoding= "utf-8") as f :
        f.write("商品,價格\n")
        for p in products:
            f.write(p[0] + ","+ p[1]+ "\n")

# 主程式
def main():
    import os
    if os.path.isfile("products.csv"):
        products = read_file("products.csv")
        print("找到檔案了")
    else:
        print("沒有找到檔案")
    
    products = user_input(products)
    print_list(products)
    writen_data("products.csv", products)

main()
