import csv

# ITEMS = [


#     {'id' : 1200, 'name': "Coffee", 'BarcodeID' : 'B60khaB12#' , 'Price' : '$100'},
#     {'id' : 1201, 'name': "Chips", 'BarcodeID' : 'B60khaB13#' , 'Price' : '$200'},
#     {'id' : 1202, 'name': "Choclate", 'BarcodeID' : 'B60khaB15#' , 'Price' : '$300'},
#     {'id' : 1203, 'name': "Iphone", 'BarcodeID' : 'B60khaB14#' , 'Price' : '$1000'},

# ]

# for items in ITEMS:

#     for k,v in items.items():

#         print(f"{v}",end=",")
    
#     print("\n")

ITEMS = []

with open('data/csv_data/items.csv','r') as file:

    data = csv.DictReader(file)

    for row in data:
        
        ITEMS.append(dict(row))



   
        