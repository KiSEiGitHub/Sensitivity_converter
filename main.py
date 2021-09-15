class sensi:
    def __init__(self, c_old_sensi, c_old_dpi, c_new_sensi):
        self.old_sensi = c_old_sensi
        self.old_dpi = c_old_dpi
        self.new_sensi = c_new_sensi

    def calcul_new_sens(self):
        return self.old_sensi * self.old_dpi / self.new_sensi

    @staticmethod
    def affich_new_sensi(x):
        print(f'New sens = {round(x, 2)}')
        print('-' * 30)


def main():
    while True:
        try:
            a = int(input('current dpi: '))
            b = float(input('current sens: '))
            c = int(input('New dpi: '))
            old_sensitivity = sensi(b, a, c)
            new_sensitivity = old_sensitivity.calcul_new_sens()
            old_sensitivity.affich_new_sensi(new_sensitivity)
        except ValueError:
            print('un nombre!')


if __name__ == '__main__':
    main()