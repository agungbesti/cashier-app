"""
Author: Agung Besti
Date: 20/2/2023
This is the transaction.py module.
Usage:
- Class Transaction
"""
from prettytable import PrettyTable


class Transaction:
    """
    A class to represent a Transaction.
    ...
    Attributes
    ----------
    items : dict
        items of the transaction

    Methods
    -------
    add_item( name, quantity, price):
        Prints the item's name, quantity and price.
    remove_item(name_item):
        Prints the name of the deleted item.
    update_item_name(old_name, new_name):
        Prints the updated item name in the transaction.
    update_item_qty(name_item, new_quantity):
        Prints the updated quantity in the transaction.
    update_item_price(name_item, new_price):
        Prints the updated item name in the transaction.
    reset_transaction():
        Show and delete all transactions to be blank.
    list_item():
        Displays a list of items.
    total_price_calculate(qty, price):
        Calculate the total price/item.
    check_order():
        Print the order is correct or there is an error in the input data.
    total_price():
        Print the total price of all customer order transactions.
    """

    # default constructor
    def __init__(self):
        self.items = {}

    def add_item(self):
        """
        Prints the item's name, quantity and price.

        Parameters
        ----------
        Returns
        -------
        None
        """
        name = input("Masukkan nama item: ")
        while True:
            try:
                quantity = int(input("Masukkan jumlah item: "))
                break
            except ValueError:
                print("Please input a number for quantity.")
        while True:
            try:
                price = int(input("Masukkan harga item: "))
                break
            except ValueError:
                print("Please input a number for price.")
        item = {"name": name, "quantity": quantity, "price": price}
        self.items[name] = item
        print(
            f"Item {name} dengan jumlah {quantity} & harga {price} telah ditambahkan.")

    def remove_item(self):
        """
        Prints the name of the deleted item.

        Parameters
        ----------

        Returns
        -------
        None
        """
        self.list_item()
        name_item = input("Masukkan nama item yang ingin dihapus: ")
        if name_item in self.items:
            self.items.pop(name_item)
            print(f"Item {name_item} telah dihapus.")
        else:
            print(f"Item {name_item} tidak ditemukan.")

    def update_item_name(self):
        """
        Prints the updated item name in the transaction.

        Parameters
        ----------
        Returns
        -------
        None
        """
        self.list_item()
        old_name = input("Masukkan nama item yang ingin diubah: ")
        new_name = input("Masukkan nama item yang baru: ")
        if old_name in self.items:
            item = self.items[old_name]
            item["name"] = new_name
            print(f"Nama item {old_name} telah diupdate menjadi {new_name}.")
        else:
            print(f"Item {old_name} tidak ditemukan.")

    def update_item_qty(self):
        """
        Prints the updated quantity in the transaction.

        Parameters
        ----------
        Returns
        -------
        None
        """
        self.list_item()
        name_item = input("Masukkan nama item yang ingin diubah: ")
        new_quantity = int(input("Masukkan jumlah item yang baru: "))
        if name_item in self.items:
            item = self.items[name_item]
            item["quantity"] = new_quantity
            print(
                f"Jumlah item {name_item} telah diupdate menjadi {new_quantity}.")
        else:
            print(f"Item {name_item} tidak ditemukan.")

    def update_item_price(self):
        """
        Prints the updated item name in the transaction.

        Parameters
        ----------
        Returns
        -------
        None
        """
        self.list_item()
        name_item = input("Masukkan nama item yang ingin diubah: ")
        new_price = int(input("Masukkan harga item yang baru: "))
        if name_item in self.items:
            item = self.items[name_item]
            item["price"] = new_price
            print(
                f"Harga item {name_item} telah diupdate menjadi {new_price}.")
        else:
            print(f"Item {name_item} tidak ditemukan.")

    def reset_transaction(self):
        """
        Show and delete all transactions to be blank

        Parameters
        ----------

        Returns
        -------
        None
        """
        self.items.clear()
        print("Transaksi telah direset.")

    def list_item(self):
        """
        Displays a list of items

        Parameters
        ----------

        Returns
        -------
        None
        """
        print("=" * 15, "[Daftar Item]", "=" * 15)
        table = PrettyTable()
        table.field_names = [
            "No",
            "Nama Item",
            "Jumlah Item",
            "Harga/Item",
            "Total Harga"]
        index = 1
        for item in self.items.values():
            total = self.total_price_calculate(item["quantity"], item["price"])
            table.add_row(
                [index, item["name"], item["quantity"], item["price"], total])
            index += 1
        print(table)

    def total_price_calculate(self, qty, price):
        """
        Calculate the total price/item.

        Parameters
        ----------
        qty : int
            quantity of the item
        price : int
            price of the item

        Returns
        -------
        qty * price (int): the total price of the qty multiplied by price
        """
        return qty * price

    def check_order(self):
        """
        Print the order is correct or there is an error in the input data

        Parameters
        ----------

        Returns
        -------
        None
        """
        if self.items:
            is_valid = True
            for item in self.items.values():
                if len(item["name"]) == 0 or item["quantity"] < 0 or item["price"] < 0:
                    is_valid = False
                    break
            if not is_valid:
                print("Terdapat kesalahan input data")
            else:
                print("Pemesanan sudah benar")
                print("=" * 15, "[Daftar Pesanan]", "=" * 15)

            table = PrettyTable()
            table.field_names = [
                "No",
                "Nama Item",
                "Jumlah Item",
                "Harga/Item",
                "Total Harga"]
            index = 1
            for item in self.items.values():
                total = self.total_price_calculate(item["quantity"], item["price"])
                table.add_row(
                    [index, item["name"], item["quantity"], item["price"], total])
                index += 1
            print(table)
        else:
            print("Tidak ada pesanan.")

    def total_price(self):
        """
        Print the total price of all customer order transactions.
        if total purchase over 200000 disc 5%
        if total purchase over 300000 disc 8%
        if total purchase over 500000 disc 10%

        Parameters
        ----------

        Returns
        -------
        None
        """

        if self.items:
            total_purchase = sum(item["quantity"] * item["price"]
                                 for item in self.items.values())

        table = PrettyTable()
        table.field_names = [
            "No",
            "Nama Item",
            "Jumlah Item",
            "Harga/Item",
            "Total Harga"]
        index = 1
        for item in self.items.values():
            total = self.total_price_calculate(item["quantity"], item["price"])
            table.add_row(
                [index, item["name"], item["quantity"], item["price"], total])
            index += 1
        print("Daftar Pesanan")
        print(table)

        if total_purchase > 500000:
            disc = total_purchase * 0.1
            after_disc = total_purchase - disc
            print(f"Total harga transaksi: {total_purchase}")
            print(f"Selamat! Anda Mendapatkan diskon 10% sebesar {disc}")
            print(f"Total harga yang harus dibayar {after_disc}")
        elif total_purchase > 300000:
            disc = total_purchase * 0.08
            after_disc = total_purchase - disc
            print(f"Total harga transaksi: {total_purchase}")
            print(f"Selamat! Anda Mendapatkan diskon 8% sebesar {disc}")
            print(f"Total harga yang harus dibayar {after_disc}")
        elif total_purchase > 200000:
            disc = total_purchase * 0.05
            after_disc = total_purchase - disc
            print(f"Total harga transaksi: {total_purchase}")
            print(f"Selamat! Anda Mendapatkan diskon 5% sebesar {disc}")
            print(f"Total harga yang harus dibayar {after_disc}")
        else:
            print(f"Total harga semua transaksi: {total_purchase}")
