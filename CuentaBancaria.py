class CuentaBancaria:
    
    #Atributos de clase
    list_cuentas = []

    def __init__(self, balance = 0, tasa_interés = 0.01): 
        self.tasa_interés = tasa_interés
        self.balance = balance
        CuentaBancaria.list_cuentas.append(self)

    def depósito(self, amount):
        self.balance += amount
        return self
        
    def retiro(self, amount):
        if(CuentaBancaria.validar_retiro(self.balance,amount)):
            self.balance -= amount
        else:
            self.balance -= 5
        return self

    @staticmethod
    def validar_retiro(balance,amount):
        if(balance - amount < 0):
            print("Fondos insuficientes: cobrando una tarifa de $5")
            return False;
        else:
            return True;
    
    @staticmethod
    def validar_balance(balance):
        if(balance <= 0):
            return False;
        else:
            return True;

    def mostrar_info_cuenta(self):
        print(f"Balance: $ {self.balance}")

    def generar_interés(self):
        if(CuentaBancaria.validar_balance(self.balance)):
            self.balance += self.balance * self.tasa_interés
        return self

    @classmethod
    def print_cuentas(cls):
        for cuenta in cls.list_cuentas:
            CuentaBancaria.mostrar_info_cuenta(cuenta)