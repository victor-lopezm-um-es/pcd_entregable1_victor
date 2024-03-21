from universidad import *

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