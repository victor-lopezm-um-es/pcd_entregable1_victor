# Implementación_Universidad
# Víctor López Martínez

from enum import Enum

class Sexo(Enum):
    VARON = 1
    MUJER = 2

class Persona:
    def __init__(self, nombre, dni, direccion, sexo):
        self.nombre = nombre
        self.dni = dni
        self.direccion = direccion
        self.sexo = sexo

class Estudiante(Persona):
    def __init__(self, nombre, dni, direccion, sexo, asignaturas):
        super().__init__(nombre, dni, direccion, sexo)
        self.asignaturas = asignaturas

    def muestra_estudiante(self):
        salida = "Nombre: {} | DNI: {} | Dirección: {} | Sexo: {} \nAsignaturas:".format(
            self.nombre, self.dni, self.direccion, self.sexo
            )
        for asig in self.asignaturas:
            salida += f'\n\t{asig}'
        return  salida
    
class Departamento(Enum):
    DIIC = 1
    DITEC = 2
    DIS = 3

class MiembroDepartamento(Persona):
    def __init__(self, nombre, dni, direccion, sexo, departamento):
        super().__init__(nombre, dni, direccion, sexo)
        self.departamento = departamento

    def cambia_departamento(self, departamento):
        if isinstance(departamento, Departamento):
            self.departamento = departamento
        
        else:
            raise ValueError("El atributo de departamento debe pertenecer a la enumeración Departamento")   

class Investigador(MiembroDepartamento):
    def __init__(self, nombre, dni, direccion, sexo, departamento, area_investigacion):
        MiembroDepartamento.__init__(self, nombre, dni, direccion, sexo, departamento)
        self.area_investigacion = area_investigacion

class ProfesorAsociado(MiembroDepartamento):
    def __init__(self, nombre, dni, direccion, sexo, departamento, asignaturas):
        super().__init__(nombre, dni, direccion, sexo, departamento)
        self.asignaturas = asignaturas

class ProfesorTitular(Investigador, ProfesorAsociado):
    def __init__(self, nombre, dni, direccion, sexo, departamento, area_investigacion, asignaturas):
        Investigador.__init__(self, nombre, dni, direccion, sexo, departamento, area_investigacion)
        ProfesorAsociado.__init__(self, nombre, dni, direccion, sexo, departamento, asignaturas)

e1 = Estudiante(nombre='Víctor', dni='23309573Q', direccion='C/ General Aznar, 61', 
                sexo=Sexo.VARON, asignaturas=['PCD', 'ML', 'AEM', 'SSySS', 'BB.DD.-II'])

m1 = MiembroDepartamento(nombre='Pedro', dni='23434945S', direccion='C/ Rio Ebro, 23', 
                         sexo=Sexo.VARON, departamento=Departamento.DIIC)

m1.cambia_departamento(departamento=Departamento.DITEC)

p1 = ProfesorTitular(nombre='Josefa', dni='12312344E', direccion='C/ Calasparra, 23', 
                     sexo=Sexo.MUJER, departamento=Departamento.DITEC, area_investigacion='Ing. Software',
                     asignaturas=['PCD', 'ED'])

print(e1.muestra_estudiante())