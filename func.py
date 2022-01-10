import sqlite3


class DB:
    def __init__(self, path: str):
        self.connection = sqlite3.connect(path)
        self.new_cursor()

    def new_cursor(self):
        self.cursor = self.connection.cursor()

    def order_list(self, par):
        self.cursor.execute(
            '''
            SELECT "id" as 'order_i',
            (SELECT Login FROM accounts WHERE accounts.id = customer_id) as 'name',
            (SELECT date FROM accounts WHERE accounts.id = customer_id) as 'date',
            (SELECT regdate FROM accounts WHERE accounts.id = customer_id) as 'regdate',
            (SELECT city FROM accounts WHERE accounts.id = id_b) as 'city',
            (SELECT street FROM accounts WHERE accounts.id = id_b) as 'street',
            (SELECT house FROM accounts WHERE accounts.id = id_b) as 'house'
             FROM basket WHERE basket.customer_id = :par;
            ''', {'par': par}
        )
        return self.cursor.fetchall()

    def order_info(self, par):
        self.cursor.execute(
            '''
            SELECT (SELECT price FROM orders WHERE product.idp = id_o) as 'price',
            (SELECT name FROM product WHERE product.idp = (SELECT id_o FROM orders WHERE product.idp = id_o)) as 'name'
             FROM product WHERE product.idp = :par;
            ''', {'par': par}
        )
        return self.cursor.fetchall()

    def address_list(self, par):
        self.cursor.execute(
            '''
            SELECT "id_b" as 'address id',
            (SELECT Login FROM accounts WHERE accounts.id = customer_id) as 'name',
            (SELECT date FROM accounts WHERE accounts.id = customer_id) as 'date',
            (SELECT regdate FROM accounts WHERE accounts.id = customer_id) as 'regdate',
            (SELECT city FROM accounts WHERE accounts.id = id_b) as 'city',
            (SELECT street FROM accounts WHERE accounts.id = id_b) as 'street',
            (SELECT house FROM accounts WHERE accounts.id = id_b) as 'house'
             FROM basket WHERE basket.customer_id = :par;
            ''', {'par': par}
        )
        return self.cursor.fetchall()

    def __del__(self):
        self.connection.close() 