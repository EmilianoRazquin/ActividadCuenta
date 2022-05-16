
class Cuenta:
  
  def __init__(self, titular, cantidad):
    self.titular = titular
    self.cantidad = cantidad

    
  
  def ingresar(self, ingreso):
    
    if ingreso >= 0:
      print(f"La cantidad ahora es: {self.cantidad + ingreso}")
    else:
      print("No es posible el ingreso")
  
  def retirar(self, retiro):
    
    if retiro > self.cantidad:
      print(f"Su cuenta está en rojo: {self.cantidad - retiro}")
    else:
      print(f"Su monto ahora es: {self.cantidad - retiro}")

cuenta1= Cuenta("Emiliano Razquin", 10000)
print(f"El titular de la cuenta es: {cuenta1.titular}\nCantidad disponible: {cuenta1.cantidad}")
cuenta1.ingresar(-5)
cuenta1.retirar(200000.50)