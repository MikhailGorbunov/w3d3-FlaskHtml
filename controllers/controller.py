from flask import render_template
from app import app
from models.order_list import order_list

@app.route('/orders')
def index():
    return render_template('index.html', title='home', orders=order_list )


@app.route('/orders/<number>')
def single_order(number):
    selected_order = order_list[int(number)]
    return render_template('order.html', title='order', order=selected_order)


# @app.route('/orders/2')
# def order1():
#     return render_template('order.html', title='order', orders=order_list[1])

# @app.route('/orders/3')
# def order2():
#     return render_template('order.html', title='order', orders=order_list[2])