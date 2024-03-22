# Implementación_Universidad
# Víctor López Martínez

from enum import Enum
from abc import ABCMeta, ABC, abstractmethod

class NoDepartamentoError(Exception):
    pass

class NoAsignaturaStrError(Exception):
    pass

class NoAsignaturasListError(Exception):
    pass

class NoEstudianteStrError(Exception):
    pass

class NoMiembroDepartamentoStrError(Exception):
    pass

class NoSexoError(Exception):
    pass

class NoAreaInvestigacionStrError(Exception):
    pass

class NoEstudianteError(Exception):
    pass

class NoMiembroDepartamentoError(Exception):
    pass

class NotFoundEstudianteStrError(Exception):
    pass

class Sexo(Enum):
    VARON = 1
    MUJER = 2

class Persona(metaclass=ABCMeta):
    def __init__(self, nombre, dni, direccion, sexo):
        if not isinstance(nombre, str):
            raise TypeError("Debes pasar el parámetro nombre como un string")
        
        if not isinstance(dni, str):
            raise TypeError("Debes pasar el parámetro dni como un string")
        
        if not isinstance(direccion, str):
            raise TypeError("Debes pasar el parámetro direccion como un string")
        
        if not isinstance(sexo, Sexo):
            raise NoSexoError("Debes pasar el parámetro sexo como un objeto Sexo")

        self.nombre = nombre
        self.dni = dni
        self.direccion = direccion
        self.sexo = sexo

class Estudiante(Persona):
    def __init__(self, nombre, dni, direccion, sexo, asignaturas):
        if not isinstance(asignaturas, list):
            raise NoAsignaturasListError("Debes pasar el parámetro asignaturas como una lista")
        
        super().__init__(nombre, dni, direccion, sexo) # Hereda atributos de Persona
        self._asignaturas = asignaturas

    def matricularse_de_asignatura(self, asignatura):
        if not isinstance(asignatura, str):
            raise NoAsignaturaStrError("Debes pasar el parámetro asignatura como un string")

        if asignatura in self._asignaturas:
            print(f"{self.nombre} ya estaba matriculado de la asignatura {asignatura}")
        
        else:
            self._asignaturas.append(asignatura)
            print(f"{self.nombre} se matricula de {asignatura}")

    def finalizar_asignatura(self, asignatura):
        if not isinstance(asignatura, str):
            raise NoAsignaturaStrError("Debes pasar el parámetro asignatura como un string")
        
        if asignatura in self._asignaturas:
            self._asignaturas.remove(asignatura)
            print(f"Asignatura {asignatura} finalizada para {self.nombre}")
        
        else:
            print(f"{self.nombre} no estaba matriculado de {asignatura}")

    def muestra_estudiante(self):   # Muestra todos los datos del estudiante
        salida = "Nombre: {} | DNI: {} | Dirección: {} | Sexo: {} \nAsignaturas:".format(
            self.nombre, self.dni, self.direccion, self.sexo
            )
        for asig in self._asignaturas:
            salida += f"| {asig} |"
        return  salida
    
class Departamento(Enum): # Enumeración
    DIIC = 1
    DITEC = 2
    DIS = 3

class MiembroDepartamento(Persona): # Clase abstracta
    def __init__(self, nombre, dni, direccion, sexo, departamento):
        if not isinstance(departamento, Departamento):  # Nos aseguramos de que departamento sea un elemento de la enumeración
            raise NoDepartamentoError("ERROR: Debes pasar el parámetro departamento como un objeto Departamento")
        
        super().__init__(nombre, dni, direccion, sexo) # Hereda de persona
        self.departamento = departamento

    def muestra_datos(self):
        salida = "Nombre: {} | DNI: {} | Dirección: {} | Sexo: {} | Departamento: {}".format(
            self.nombre, self.dni, self.direccion, self.sexo, self.departamento
            )
        return  salida

    def cambia_departamento(self, departamento):
        if not isinstance(departamento, Departamento):
            raise NoDepartamentoError("ERROR: Debes pasar el parámetro departamento como un objeto Departamento")
        self.departamento = departamento      

class Investigador(MiembroDepartamento): # Hereda de MiembroDepartamento
    def __init__(self, nombre, dni, direccion, sexo, departamento, area_investigacion):
        if not isinstance(area_investigacion, str): 
            raise NoAreaInvestigacionStrError("Debes pasar el parámetro area_investigacion como un string")

        MiembroDepartamento.__init__(self, nombre, dni, direccion, sexo, departamento)
        self.area_investigacion = area_investigacion

    def muestra_datos(self): # Sobrecarga el método muestra_datos
        salida = MiembroDepartamento.muestra_datos(self)
        salida += '\nÁrea investigación: {}'.format(self.area_investigacion)
        return salida

class Profesor(MiembroDepartamento, metaclass=ABCMeta): # Hereda de MiembroDepartamento
    def __init__(self, nombre, dni, direccion, sexo, departamento, asignaturas):
        if not isinstance(asignaturas, list):
            raise NoAsignaturasListError("Debes pasar el parámetro asignaturas como una lista")
        
        super().__init__(nombre, dni, direccion, sexo, departamento)
        self.asignaturas = asignaturas

    @abstractmethod
    def muestra_datos(self): # Sobrecarga el método muestra_datos
        pass
    
class ProfesorTitular(Investigador, Profesor):
    def __init__(self, nombre, dni, direccion, sexo, departamento, area_investigacion, asignaturas):
        Investigador.__init__(self, nombre, dni, direccion, sexo, departamento, area_investigacion)
        Profesor.__init__(self, nombre, dni, direccion, sexo, departamento, asignaturas)

    def muestra_datos(self):
        salida = Investigador.muestra_datos(self)
        salida += '\nAsignaturas: '

        for asig in self.asignaturas:
            salida += f"| {asig} |"

        return salida
    
class ProfesorAsociado(Profesor):
    def __init__(self, nombre, dni, direccion, sexo, departamento, asignaturas):
        super().__init__(nombre, dni, direccion, sexo, departamento, asignaturas)

    def muestra_datos(self): # Sobrecarga el método muestra_datos
        salida = MiembroDepartamento.muestra_datos(self)
        salida += '\nAsignaturas: '

        for asig in self.asignaturas:
            salida += f"| {asig} |"

        return salida
    
class Universidad: # Clase desde la que se gestionan las operaciones
    def __init__(self, estudiantes, miembros_departamento): # Almacena todas las personas de la universidad
        self._estudiantes = estudiantes
        self._miembros_departamento = miembros_departamento

    # TODAS LAS OPERACIONES QUE SE DESEAN HACER

    def añadir_estudiante(self, estudiante):
        try:
            self._estudiantes.append(estudiante)
        
        except NoEstudianteError:
            print("ERROR: Debes pasar el parámetro estudiante como un objeto del tipo Estudiante")
        
    def eliminar_estudiante(self, estudiante): 
        try:
            estudiante_obj = self._obtener_estudiante(estudiante) # obtengo la instancia a través del nombre del estudiante
            self._estudiantes.remove(estudiante_obj)

        except NoEstudianteStrError:
            print("Debes pasar el parámetro estudiante como un string")

    def añadir_miembro_departamento(self, miembro_departamento):
        if isinstance(miembro_departamento, MiembroDepartamento):
            self._miembros_departamento.append(miembro_departamento)

        else:
            raise NoMiembroDepartamentoError("Debes pasar como parámetro un objeto del tipo MiembroDepartamento")
        
    def eliminar_miembro_departamento(self, miembro_departamento): 
        try:
            mD_obj = self._obtener_miembroDepartamento(miembro_departamento) # obtengo la instancia a través del nombre del MD
            self._miembros_departamento.remove(mD_obj)

        except NoMiembroDepartamentoStrError:
            print("ERROR: Debes pasar el parámetro miembro_departamento como un string")

    def cambia_departamento(self, miembro_departamento, departamento):
        try:
            mD_obj = self._obtener_miembroDepartamento(miembro_departamento) # obtengo la instancia a través del nombre del MD
            mD_obj.cambia_departamento(departamento)

        except NoMiembroDepartamentoStrError:
            print("ERROR: Debes pasar el parámetro miembro_departamento como un string")

        except NoDepartamentoError:
            print("ERROR: Debes pasar el parámetro departamento como un objeto Departamento")

    def matricular_estudiante_asignatura(self, estudiante, asignatura):
        try:
            estudiante_obj = self._obtener_estudiante(estudiante) # obtengo la instancia a través del nombre del estudiante
            estudiante_obj.matricularse_de_asignatura(asignatura)

        except NoEstudianteStrError:
            print("ERROR: Debes pasar el parámetro estudiante como un string")

        except NoAsignaturaStrError:
            print("ERROR: Debes pasar el parámetro asignatura como un string")

    def finalizar_estudiante_asignatura(self, estudiante, asignatura):
        try:
            estudiante_obj = self._obtener_estudiante(estudiante) # obtengo la instancia a través del nombre del estudiante
            estudiante_obj.finalizar_asignatura(asignatura)

        except NoEstudianteStrError:
            print("ERROR: Debes pasar el parámetro estudiante como un string")

        except NoAsignaturaStrError:
            print("ERROR: Debes pasar el parámetro asignatura como un string")

    def muestraEstudiantes(self):
        print("\tESTUDIANTES: ")
        for est in self._estudiantes:
            print(f"{est.muestra_estudiante()}\n")

    def muestraMiembrosDepartamento(self):
        print("\tMIEMBROS DE DEPARTAMENTO: ")

        for miem in self._miembros_departamento:
            print(f"{miem.muestra_datos()}\n")

    def _obtener_estudiante(self, estudiante_str):
        if not isinstance(estudiante_str, str):
            raise NoEstudianteStrError("ERROR: Debes pasar el parámetro estudiante_str como un string")

        for estudiante_obj in self._estudiantes:
            if estudiante_obj.nombre == estudiante_str:
                return estudiante_obj
        
        # Si no se encuentra el estudiante, se lanza una excepción
        raise NotFoundEstudianteStrError(f"ERROR: No se encontró el estudiante con el nombre '{estudiante_str}'")
    
    def _obtener_miembroDepartamento(self, mD_str):
        if not isinstance(mD_str, str):
            raise NoMiembroDepartamentoStrError("ERROR: Debes pasar el parámetro mD_str como un string")
        
        for mD_obj in self._miembros_departamento:
            if mD_obj.nombre == mD_str:
                return mD_obj
    
    def _obtener_departamento_de_miembro(self, mD_str):
        try:
            mD_obj = self._obtener_miembroDepartamento(mD_str)
            dep = mD_obj.departamento
        except NoMiembroDepartamentoStrError:
            print("ERROR: Debes pasar el parámetro mD_str como un string")
            dep = Departamento.DIIC # Establecemos un departamento por defecto
        finally:
            return dep



# Pruebas exploratorias
if __name__=='__main__':
    e1 = Estudiante(nombre='Víctor', dni='23309573Q', direccion='C/ General Aznar, 61', 
                    sexo=Sexo.VARON, asignaturas=['PCD', 'ML', 'AEM', 'SSySS', 'BB.DD.-II'])

    i1 = Investigador(nombre='Pedro', dni='23434945S', direccion='C/ Rio Ebro, 23', 
                    sexo=Sexo.VARON, departamento=Departamento.DIIC, area_investigacion='Biologia Molecular')

    i1.cambia_departamento(departamento=Departamento.DITEC)

    p1 = ProfesorTitular(nombre='Josefa', dni='12312344E', direccion='C/ Calasparra, 23', 
                        sexo=Sexo.MUJER, departamento=Departamento.DIIC, area_investigacion='Ing. Software',
                        asignaturas=['PCD', 'ED'])


    p1.cambia_departamento(departamento=Departamento.DIIC)

    uni = Universidad(estudiantes=[], miembros_departamento=[])
    uni.añadir_estudiante(estudiante=e1)
    uni.añadir_miembro_departamento(miembro_departamento=p1) 
    uni.añadir_miembro_departamento(miembro_departamento=i1) 

    uni.cambia_departamento(miembro_departamento='Josefa', departamento="Departamento.DIS")

    uni.muestraEstudiantes()
    uni.muestraMiembrosDepartamento()