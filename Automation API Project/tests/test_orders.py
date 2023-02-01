from requests_api.api_clients import *
from requests_api.orders import *


class TestOrders:

    def setup_method(self):
        self.token = get_token()

    def test_add_order_book_out_of_stock(self):
        response = add_order(self.token, 2, 'CiprianTest')
        assert response.status_code == 404, 'Status code is not correct'
        assert response.json()['error'] == 'This book is not in stock. Try again later.'

    def test_add_valid_order(self):
        response = add_order(self.token, 1, 'CiprianTest')
        assert response.status_code == 201, 'Status code is not correct'
        assert response.json()['created'] is True, 'Order not created.'
        # cleanup
        delete_order(self.token, response.json()['orderId'])

    def test_get_orders(self):
        add1 = add_order(self.token, 1, 'CiprianTest')
        add2 = add_order(self.token, 1, 'CiprianTest')
        response = get_orders(self.token)
        assert response.status_code == 200, 'Status code is not correct'
        assert len(response.json()) == 2, 'Total of orders returned is not correct'
        # cleanup dupa test
        delete_order(self.token, add1.json()['orderId'])
        delete_order(self.token, add2.json()['orderId'])


    def test_delete_order(self):
        add = add_order(self.token,1,'CiprianTest')
        response = delete_order(self.token, add.json()['orderId'])
        assert response.status_code == 204, 'Status code is not correct'
        get_all = get_orders(self.token)
        assert len(get_all.json()) == 0, 'Order was not deleted'

    def test_delete_invalid_order_id(self):
        response = delete_order(self.token, 'UAI64yJ7bJAKxVFB2LYRB')
        assert response.status_code == 404,'Status code is not correct'
        assert response.json()['error'] == 'No order with id UAI64yJ7bJAKxVFB2LYRB.'

    def test_patch_invalid_order_id(self):
        response = edit_order(self.token, 'UAI64yJ7bJAKxVFB2LYRB','Superman')
        assert response.status_code == 404, 'Status code is not correct'
        assert response.json()['error'] == 'No order with id UAI64yJ7bJAKxVFB2LYRB.'

    def test_patch_valid_order(self):
        order_id =add_order(self.token, 1, 'CiprianTest').json()['orderId']
        response = edit_order(self.token, order_id, 'CiprianTest2')
        assert response.status_code == 204, 'Status code is not correct'
        get = get_order(self.token, order_id)
        assert get.json()['customerName'] == 'CiprianTest2', 'Customer name was not updated'
        # cleanup test update comanda
        delete_order(self.token, order_id)

    def test_get_order(self):
        order_id = add_order(self.token, 1,'CiprianTest').json()['orderId']
        response = get_order(self.token, order_id)
        assert response.status_code == 200, 'Status code is not correct'
        assert response.json()['id'] == order_id, 'order id is not corect'
        assert response.json()['bookId'] == 1, 'Book id is not correct'
        assert response.json()['customerName'] == 'CiprianTest', 'Customer name is not correct'
        assert response.json()['quantity'] == 1, ' quantity is not correct'
        # # cleanup
        delete_order(self.token, order_id)


