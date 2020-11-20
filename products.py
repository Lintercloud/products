# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 10:30:41 2020

@author: Linter
"""

products = []

while True:
    name = input("輸入商品名字: ")
    if name == "q":
        break
    price = input("輸入商品價格: ")
    p = [name, price]
    products.append(p)
print(products)

for p in products:
    print(p[0],"的價格是", p[1])
    
with open("products.csv", "w") as f :
    f.write("商品,價格\n")
    for p in products:
        f.write(p[0] + ","+ p[1]+ "\n")
        