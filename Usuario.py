from CuentaBancaria import CuentaBancaria

class Usuario:

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.cuenta = []
    
    # agregando el método de depósito
    def hacer_depósito(self, amount, index):
        self.cuenta[index].depósito(amount)
        return self

    # agregando el método de retiro
    def hacer_retiro(self, amount, index):
        self.cuenta[index].retiro(amount)
        return self

    def mostrar_balance_usuario(self, index):
        print(f"User: {self.name}, Balance de cuenta {index}: {self.cuenta[index].balance}")
        return self

    def crear_cuenta(self,monto,tasa_interés):
        self.cuenta.append(CuentaBancaria(monto,tasa_interés))
        print("Se creo una cuenta")
        return self
