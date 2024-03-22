from universidad import *
import pytest

def test_añadir_estudiante():
    uni = Universidad(estudiantes=[], miembros_departamento=[])
    estudiante = Estudiante("Roberto", "12345678A", "Calle Echegaray, 27", Sexo.VARON, ["PCD", "IE"])
    uni.añadir_estudiante(estudiante)
    assert len(uni._estudiantes) == 1


def test_añadir_miembroDepartamento():
    uni = Universidad(estudiantes=[], miembros_departamento=[])
    miembro = ProfesorAsociado("Marisa", "87654321B", "Calle San Antonio", Sexo.MUJER, Departamento.DIIC, ["AMD"])
    uni.añadir_miembro_departamento(miembro)
    assert len(uni._miembros_departamento) == 1

def test_eliminar_estudiante():
    uni = Universidad(estudiantes=[], miembros_departamento=[])
    estudiante = Estudiante("Roberto", "12345678A", "Calle Echegaray, 27", Sexo.VARON, ["PCD", "IE"])
    uni.añadir_estudiante(estudiante)
    assert len(uni._estudiantes) == 1
    uni.eliminar_estudiante("Roberto")
    assert len(uni._estudiantes) == 0

def test_eliminar_miembroDepartamento():
    uni = Universidad(estudiantes=[], miembros_departamento=[])
    miembro = ProfesorAsociado("Marisa", "87654321B", "Calle San Antonio", Sexo.MUJER, Departamento.DIIC, ["AMD"])
    uni.añadir_miembro_departamento(miembro)
    assert len(uni._miembros_departamento) == 1
    uni.eliminar_miembro_departamento("Marisa")
    assert len(uni._miembros_departamento) == 0

def test_cambiar_Departamento():
    uni = Universidad(estudiantes=[], miembros_departamento=[])
    p1 = ProfesorTitular(nombre='Josefa', dni='12312344E', direccion='C/ Calasparra, 23', 
                        sexo=Sexo.MUJER, departamento=Departamento.DITEC, area_investigacion='Ing. Software',
                        asignaturas=['PCD', 'ED']) 
    uni.añadir_miembro_departamento(p1)
    new_dep = Departamento.DIS
    mD_str = 'Josefa'
    uni.cambia_departamento(miembro_departamento=mD_str, departamento=new_dep)
    assert p1.departamento == uni._obtener_departamento_de_miembro(mD_str)

def test_cambiar_Departamento_tipo_invalido(capsys):
    """"
    Como hemos capturado las excepciones y hemos impreso el correspondiente
    error por pantalla debemos usar capsys para capturar la salida
    """

    uni = Universidad(estudiantes=[], miembros_departamento=[])
    p1 = ProfesorTitular(nombre='Josefa', dni='12312344E', direccion='C/ Calasparra, 23', 
                        sexo=Sexo.MUJER, departamento=Departamento.DITEC, area_investigacion='Ing. Software',
                        asignaturas=['PCD', 'ED']) 
    uni.añadir_miembro_departamento(p1)
    mD_str = 'Josefa'
    invalid_dep = 'Departamento.DIIC'  # Departamento como un string en lugar de un objeto Departamento

    
    uni.cambia_departamento(miembro_departamento=mD_str, departamento=invalid_dep)
    captured = capsys.readouterr()
    assert "ERROR: Debes pasar el parámetro departamento como un objeto Departamento" in captured.out

# Para matricularse desde la instancia Estudiante
def test_matricularse_de_asignatura():
    estudiante = Estudiante("Ismael", "23435494F", "Calle Echegaray, 42", Sexo.VARON, ["PCD", "IE"])
    estudiante.matricularse_de_asignatura("ED")
    assert "ED" in estudiante._asignaturas

def test_matricularse_de_asignatura_existente():
    estudiante = Estudiante("Ismael", "23435494F", "Calle Echegaray, 42", Sexo.VARON, ["PCD", "IE"])
    estudiante.matricularse_de_asignatura("PCD")
    assert "PCD" in estudiante._asignaturas

def test_finalizar_asignatura_existente():
    estudiante = Estudiante("Ismael", "23435494F", "Calle Echegaray, 42", Sexo.VARON, ["PCD", "IE"])
    estudiante.finalizar_asignatura("PCD")
    assert "PCD" not in estudiante._asignaturas

def test_finalizar_asignatura_inexistente():
    estudiante = Estudiante("Ismael", "23435494F", "Calle Echegaray, 42", Sexo.VARON, ["PCD", "IE"])
    estudiante.finalizar_asignatura("ED")
    assert "ED" not in estudiante._asignaturas

# Para matricularse desde la instancia universidad
def test_matricular_estudiante_asignatura():   
    uni = Universidad(estudiantes=[], miembros_departamento=[])
    estudiante = Estudiante("Roberto", "12345678A", "Calle Echegaray, 27", Sexo.VARON, ["PCD", "IE"])
    uni.añadir_estudiante(estudiante)

    uni.matricular_estudiante_asignatura("Roberto", "ED")
    assert "ED" in estudiante._asignaturas

def test_matricular_estudiante_asignatura_invalid_estudiante(capsys):
    """"
    Como hemos capturado las excepciones y hemos impreso el correspondiente
    error por pantalla debemos usar capsys para capturar la salida
    """

    uni = Universidad(estudiantes=[], miembros_departamento=[])
    uni.matricular_estudiante_asignatura(123, "ED")
    captured = capsys.readouterr()
    assert "ERROR: Debes pasar el parámetro estudiante como un string" in captured.out

def test_matricular_estudiante_asignatura_invalid_asignatura(capsys):
    """"
    Como hemos capturado las excepciones y hemos impreso el correspondiente
    error por pantalla debemos usar capsys para capturar la salida
    """

    uni = Universidad(estudiantes=[], miembros_departamento=[])
    estudiante = Estudiante("Roberto", "12345678A", "Calle Echegaray, 27", Sexo.VARON, ["PCD", "IE"])
    uni.añadir_estudiante(estudiante) # Hay que añadir un estudiante para que no salte antes
                                      # el error de estudiante no encontrado
    uni.matricular_estudiante_asignatura("Roberto", 123)
    captured = capsys.readouterr()
    assert "ERROR: Debes pasar el parámetro asignatura como un string" in captured.out

def test_finalizar_estudiante_asignatura():
    uni = Universidad(estudiantes=[], miembros_departamento=[])
    estudiante = Estudiante("Roberto", "12345678A", "Calle Echegaray, 27", Sexo.VARON, ["PCD", "IE"])
    uni.añadir_estudiante(estudiante)

    uni.finalizar_estudiante_asignatura("Roberto", "PCD")
    assert "PCD" not in estudiante._asignaturas

def test_finalizar_estudiante_asignatura_invalid_estudiante(capsys):
    """"
    Como hemos capturado las excepciones y hemos impreso el correspondiente
    error por pantalla debemos usar capsys para capturar la salida
    """

    uni = Universidad(estudiantes=[], miembros_departamento=[])
    uni.finalizar_estudiante_asignatura(123, "ED")
    captured = capsys.readouterr()
    assert "ERROR: Debes pasar el parámetro estudiante como un string" in captured.out

def test_finalizar_estudiante_asignatura_invalid_asignatura(capsys):
    """"
    Como hemos capturado las excepciones y hemos impreso el correspondiente
    error por pantalla debemos usar capsys para capturar la salida
    """

    uni = Universidad(estudiantes=[], miembros_departamento=[])
    estudiante = Estudiante("Roberto", "12345678A", "Calle Echegaray, 27", Sexo.VARON, ["PCD", "IE"])
    uni.añadir_estudiante(estudiante)

    uni.finalizar_estudiante_asignatura("Roberto", 123)

    captured = capsys.readouterr()
    assert "ERROR: Debes pasar el parámetro asignatura como un string" in captured.out
