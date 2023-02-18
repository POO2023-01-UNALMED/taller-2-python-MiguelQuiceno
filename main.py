class Asiento:
    def __init__(self, color, precio, registro):
        self. color = color
        self.registro = registro
        self.precio = precio
    
    def cambiarColor(self, color):
        if color == "rojo" or color == "verde" or color == "amarillo" or color == "negro" or color == "blanco":
            self.color = color
class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro
        
    def cambiarRegistro(self, registro):
        self.registro = registro
    
    def asignarTipo(self, tipo):
        if tipo == "electrico" or tipo == "gasolina":
            self.tipo = tipo
    
class Auto:
    cantidadCreados = 0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self. modelo = modelo
        self.registro = registro
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
    
    def cantidadAsientos(self):
        a = 0
        for i in self.asientos:
            if i != None:
                a += 1
        return a
    
    def verificarIntegridad(self):
        b = False
        if self.registro == self.motor.registro:
            for i in self.asientos:
                if i != None:
                    if i.registro == self.registro:
                        b = True
                    else:
                        return "Las piezas no son originales"
        if b:
            return "Auto original"