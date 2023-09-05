"""
Author: Agung Besti
Date: 20/2/2023
This is the kasir.py module.
Usage:
- Class Kasir
"""
from prettytable import PrettyTable
from transaction import Transaction


class Kasir(Transaction):
    """
    A class to represent a Kasir.
    ...
    Attributes
    ----------

    Methods
    -------
    None
    """
    def __init__(self):
        super().__init__()
        self.trnsct_123 = Transaction()

    def exit_order(self):
        """
        Exit the apps.

        Parameters
        ----------
        Returns
        -------
        None
        """
        print("Terima kasih sudah berkunjung.")

    def table_menu(self):
        """
        print table menu.

        Parameters
        ----------
        Returns
        -------
        None
        """
        print("\n")
        print('=' * 10, '[MAIN MENU Point of Sales]', '=' * 10)
        print('' * 5, '[Selamat Datang di Toko Abesti]', )
        tabel_menu = PrettyTable(["No Menu", "Jenis Pesanan"])
        tabel_menu.add_row(["1", "Tambah Pesanan"])
        tabel_menu.add_row(["2", "Update nama Pesanan"])
        tabel_menu.add_row(["3", "Update Jumlah Pesanan"])
        tabel_menu.add_row(["4", "Update Harga Pesanan"])
        tabel_menu.add_row(["5", "Hapus Pesanan"])
        tabel_menu.add_row(["6", "Periksa Pesanan"])
        tabel_menu.add_row(["7", "Reset Pesanan"])
        tabel_menu.add_row(["8", "Total harga Pesanan"])
        tabel_menu.add_row(["9", "Keluar Aplikasi"])
        # Cetak Tabel Menu
        print(tabel_menu)

    def default_menu(self):
        """
        print options if not in the list.

        Parameters
        ----------
        Returns
        -------
        None
        """
        return "Pilihan tidak valid. Silakan masukkan angka 1-9."

    def menu(self, pilihan):
        """
        Select the menu.

        Parameters
        ----------
        pilihan : str
            pilihan of the menu
        Returns
        -------
        dict_pilihan.get(pilihan, default_menu) (str) : select the menu
        """
        dict_pilihan = {
            "1": self.trnsct_123.add_item,
            "2": self.trnsct_123.update_item_name,
            "3": self.trnsct_123.update_item_qty,
            "4": self.trnsct_123.update_item_price,
            "5": self.trnsct_123.remove_item,
            "6": self.trnsct_123.check_order,
            "7": self.trnsct_123.reset_transaction,
            "8": self.trnsct_123.total_price,
            "9": self.exit_order

        }
        return dict_pilihan.get(pilihan, self.default_menu)

    def main_menu(self):
        """
        Prints the main menu Point of Sales (POS).

        Parameters
        ----------
        Returns
        -------
        None
        """
        lanjut_beli = "y"
        while lanjut_beli.lower() == "y":
            self.table_menu()
            # input pilihan
            pilihan = input('Pilih menu: ')
            if pilihan != "9":
                self.menu(pilihan)()
            else:
                self.menu(pilihan)()
                lanjut_beli = "n"
                break
