from models.order import *
import datetime

date1 = datetime.datetime(2022, 11, 2, 12, 40)
date2 = datetime.datetime(2022, 6, 29, 15, 00)
date3 = datetime.datetime(2021, 12, 12, 9, 30)




order1 = Order("Tom",date1,2, "peperoni , pineapple", "small")
order2 = Order("Jerry",date2,1, "burrata, parma ham, mozzarella ", "large")
order3 = Order("Sam",date3,10, "mozzarella nduja and spicy pork sausage", "mega - extra - large")
order_list = [order1, order2, order3]
