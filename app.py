""""
CBA
Ficha: 2877795
Aprendiz: Kevin Donato Jimenez Rocha
version: 1.0
fecha: 19/06/2024

"""
from module import clases as cl
from module import excepcion as ex


#instanciamos las clases
tiempoCompleto =cl.TiempoCompleto()
ocacionales =cl.Ocasionales()
horaCatedra = cl.HoraCatedra()
auxiliar = cl.Auxiliar()
tecnico = cl.Tecnico()
profesional = cl.Profesional()
ops= cl.OPS()

#llamamos a los set para ponerles los atributos a las clases  y los metodos
if __name__=="__main__":
    
    print("TIEMPO COMPLETO:")
    tiempoCompleto.set_idPersona(ex.solicitar_dato_int("ingrese su ID: "))
    tiempoCompleto.set_nomPersona(ex.verificacionTexto("ingrese su nombre: "))
    tiempoCompleto.set_apePersona(ex.verificacionTexto("ingrese su apellidos: "))
    tiempoCompleto.set_fechaNacimiento(input("ingrese su fecha de nacimiento: "))
    tiempoCompleto.set_cuidadNacimiento(ex.verificacionTexto("ingrese su ciudad de nacimientos: "))
    tiempoCompleto.set_genero(ex.verificacionTexto("ingrese su genero (Masculino/Femenino): "))
    tiempoCompleto.set_estrato(ex.solicitar_dato_int("ingrese su estrato: "))
    tiempoCompleto.set_areaFormacion(ex.verificacionTexto("ingrese de ambito de formacion: "))
    tiempoCompleto.set_tituloProfesional(ex.verificacionTexto("ingrese su titulo profesional: "))
    tiempoCompleto.set_unidadAcademica(ex.verificacionTexto("ingrese su unidad academica: "))
    tiempoCompleto.set_categoria("ingrese su categoria: ")
    tiempoCompleto.set_puntos(ex.solicitar_dato_int("ingrese sus puntos: "))
    tiempoCompleto.set_salario(ex.solicitar_dato_int("ingrese el salario: "))
    tiempoCompleto.calculaSuelto()
    tiempoCompleto.liquidarTC()
    tiempoCompleto.mostrarLiqTC()
    tiempoCompleto.mostrarDG()
    tiempoCompleto.calcularEPS()
    tiempoCompleto.calculaPension()
    tiempoCompleto.calculaARL()
    tiempoCompleto.calculaSENA()
    tiempoCompleto.calculaCajas()
    tiempoCompleto.calculaICBF()
    tiempoCompleto.calculaAuxilio()
    tiempoCompleto.mostrarDatosDocentes()
    print("-"*30)
    #Ocacionales
    print("OCASIONALES")
    ocacionales.set_idPersona(ex.solicitar_dato_int("ingrese su ID: "))
    ocacionales.set_nomPersona(ex.verificacionTexto("ingrese su nombre: "))
    ocacionales.set_apePersona(ex.verificacionTexto("ingrese su apellidos: "))
    ocacionales.set_fechaNacimiento(input("ingrese su fecha de nacimiento: "))
    ocacionales.set_cuidadNacimiento(ex.verificacionTexto("ingrese su ciudad de nacimientos: "))
    ocacionales.set_genero(ex.verificacionTexto("ingrese su genero (Masculino/Femenino): "))
    ocacionales.set_estrato(ex.solicitar_dato_int("ingrese su estrato: "))
    ocacionales.set_areaFormacion(ex.verificacionTexto("ingrese de ambito de formacion: "))
    ocacionales.set_tituloProfesional(ex.verificacionTexto("ingrese su titulo profesional: "))
    ocacionales.set_unidadAcademica(ex.verificacionTexto("ingrese su unidad academica: "))
    ocacionales.mostrarDG()
    ocacionales.calcularEPS()
    ocacionales.calculaPension()
    ocacionales.calculaARL()
    ocacionales.calculaSENA()
    ocacionales.calculaCajas()
    ocacionales.calculaICBF()
    ocacionales.calculaAuxilio()
    ocacionales.mostrarDatosDocentes()
    ocacionales.calcularSueldo()
    ocacionales.liquidarOC()
    ocacionales.mostrarLiqOC()
    print("-"*30)

    #Hora Catedra
    print("HORA CATEDRA: ")
    horaCatedra.set_idPersona(ex.solicitar_dato_int("ingrese su ID: "))
    horaCatedra.set_nomPersona(ex.verificacionTexto("ingrese su nombre: "))
    horaCatedra.set_apePersona(ex.verificacionTexto("ingrese su apellidos: "))
    horaCatedra.set_fechaNacimiento(input("ingrese su fecha de nacimiento: "))
    horaCatedra.set_cuidadNacimiento(ex.verificacionTexto("ingrese su ciudad de nacimientos: "))
    horaCatedra.set_genero(ex.verificacionTexto("ingrese su genero (Masculino/Femenino): "))
    horaCatedra.set_estrato(ex.solicitar_dato_int("ingrese su estrato: "))
    horaCatedra.set_areaFormacion(ex.verificacionTexto("ingrese de ambito de formacion: "))
    horaCatedra.set_tituloProfesional(ex.verificacionTexto("ingrese su titulo profesional: "))
    horaCatedra.set_unidadAcademica(ex.verificacionTexto("ingrese su unidad academica: "))
    horaCatedra.mostrarDG()
    horaCatedra.calcularEPS()
    horaCatedra.calculaPension()
    horaCatedra.calculaARL()
    horaCatedra.calculaSENA()
    horaCatedra.calculaCajas()
    horaCatedra.calculaICBF()
    horaCatedra.calculaAuxilio()
    horaCatedra.calcularSueldo()
    horaCatedra.liquidarHC()
    horaCatedra.mostrarLiqHC()
    horaCatedra.mostrarDatosDocentes()
    print("-"*30)

    #Auxiliar
    print("AUXILIAR: ")
    auxiliar.set_idPersona(ex.solicitar_dato_int("ingrese su ID: "))
    auxiliar.set_nomPersona(ex.verificacionTexto("ingrese su nombre: "))
    auxiliar.set_apePersona(ex.verificacionTexto("ingrese su apellidos: "))
    auxiliar.set_fechaNacimiento(input("ingrese su fecha de nacimiento: "))
    auxiliar.set_cuidadNacimiento(ex.verificacionTexto("ingrese su ciudad de nacimientos: "))
    auxiliar.set_genero(ex.verificacionTexto("ingrese su genero (Masculino/Femenino): "))
    auxiliar.set_estrato(ex.solicitar_dato_int("ingrese su estrato: "))
    auxiliar.set_dependencia(ex.verificacionTexto("ingrese su dependencia: "))
    auxiliar.set_titulo(ex.verificacionTexto("ingrese su titulo: "))
    auxiliar.set_fechaVinculacion(ex.solicitar_dato_int("ingrese su año(0000): "), ex.solicitar_dato_int("ingrese su mes(00): "), ex.solicitar_dato_int("ingrese su dia (00): "))
    auxiliar.set_nivel(ex.solicitar_dato_int("ingrese su nivel: "))
    auxiliar.set_salario(ex.solicitar_dato_int("ingrese su salario: "))
    auxiliar.mostrarDG()
    auxiliar.calcularEPS()
    auxiliar.calculaPension()
    auxiliar.calculaARL()
    auxiliar.calculaSENA()
    auxiliar.calculaCajas()
    auxiliar.calculaICBF()
    auxiliar.calculaAuxilio()
    auxiliar.mostrarDatosAdmin()
    auxiliar.mostrarDatosAdminPlanta()
    auxiliar.calcularSueldo()
    auxiliar.liquidarAux()
    auxiliar.mostrarLiqAux()

    #Tecnico
    print("TECNICO: ")
    tecnico.set_idPersona(ex.solicitar_dato_int("ingrese su ID: "))
    tecnico.set_nomPersona(ex.verificacionTexto("ingrese su nombre: "))
    tecnico.set_apePersona(ex.verificacionTexto("ingrese su apellidos: "))
    tecnico.set_fechaNacimiento(input("ingrese su fecha de nacimiento: "))
    tecnico.set_cuidadNacimiento(ex.verificacionTexto("ingrese su ciudad de nacimientos: "))
    tecnico.set_genero(ex.verificacionTexto("ingrese su genero (Masculino/Femenino): "))
    tecnico.set_estrato(ex.solicitar_dato_int("ingrese su estrato: "))
    tecnico.set_dependencia(ex.verificacionTexto("ingrese su dependencia: "))
    tecnico.set_titulo(ex.verificacionTexto("ingrese su titulo: "))
    tecnico.set_fechaVinculacion(ex.solicitar_dato_int("ingrese su año(0000): "), ex.solicitar_dato_int("ingrese su mes(00): "), ex.solicitar_dato_int("ingrese su dia (00): "))
    tecnico.set_nivel(ex.solicitar_dato_int("ingrese su nivel: "))
    tecnico.set_salario(ex.solicitar_dato_int("ingrese su salario: "))
    tecnico.mostrarDG()
    tecnico.calcularEPS()
    tecnico.calculaPension()
    tecnico.calculaARL()
    tecnico.calculaSENA()
    tecnico.calculaCajas()
    tecnico.calculaICBF()
    tecnico.calculaAuxilio()
    tecnico.mostrarDatosAdmin()
    tecnico.mostrarDatosAdminPlanta()
    tecnico.calcularSueldo()
    tecnico.liquidarTec()
    tecnico.mostrarLiqTec()

    #Profesional 
    print("PROFESIONAL: ")
    profesional.set_idPersona(ex.solicitar_dato_int("ingrese su ID: "))
    profesional.set_nomPersona(ex.verificacionTexto("ingrese su nombre: "))
    profesional.set_apePersona(ex.verificacionTexto("ingrese su apellidos: "))
    profesional.set_fechaNacimiento(input("ingrese su fecha de nacimiento: "))
    profesional.set_cuidadNacimiento(ex.verificacionTexto("ingrese su ciudad de nacimientos: "))
    profesional.set_genero(ex.verificacionTexto("ingrese su genero (Masculino/Femenino): "))
    profesional.set_estrato(ex.solicitar_dato_int("ingrese su estrato: "))
    profesional.set_dependencia(ex.verificacionTexto("ingrese su dependencia: "))
    profesional.set_titulo(ex.verificacionTexto("ingrese su titulo: "))
    profesional.set_fechaVinculacion(ex.solicitar_dato_int("ingrese su año(0000): "), ex.solicitar_dato_int("ingrese su mes(00): "), ex.solicitar_dato_int("ingrese su dia (00): "))
    profesional.set_nivel(ex.solicitar_dato_int("ingrese su nivel:"))
    profesional.set_salario(ex.solicitar_dato_int("ingrese su salario: "))
    profesional.mostrarDG()
    profesional.calcularEPS()
    profesional.calculaPension()
    profesional.calculaARL()
    profesional.calculaSENA()
    profesional.calculaCajas()
    profesional.calculaICBF()
    profesional.calculaAuxilio()
    profesional.mostrarDatosAdmin()
    profesional.mostrarDatosAdminPlanta()
    profesional.calcularSueldo()
    profesional.liquidarProf()
    profesional.mostrarLiqProf()

    #OPS 
    print("OPS:")
    ops.set_idPersona(ex.solicitar_dato_int("ingrese su ID: "))
    ops.set_nomPersona(ex.verificacionTexto("ingrese su nombre: "))
    ops.set_apePersona(ex.verificacionTexto("ingrese su apellidos: "))
    ops.set_fechaNacimiento(input("ingrese su fecha de nacimiento: "))
    ops.set_cuidadNacimiento(ex.verificacionTexto("ingrese su ciudad de nacimientos: "))
    ops.set_genero(ex.verificacionTexto("ingrese su genero (Masculino/Femenino): "))
    ops.set_estrato(ex.solicitar_dato_int("ingrese su estrato: "))
    ops.set_dependencia(ex.verificacionTexto("ingrese su dependencia: "))
    ops.set_titulo(ex.verificacionTexto("ingrese su titulo: "))
    ops.set_fechaVinculacion(ex.solicitar_dato_int("ingrese su año(0000): "), ex.solicitar_dato_int("ingrese su mes(00): "), ex.solicitar_dato_int("ingrese su dia (00): "))
    ops.set_numMeses(ex.solicitar_dato_int("ingrese los meses: "))
    ops.set_valorContrato(ex.solicitar_dato_int("ingrese el valor de su contrato: "))
    ops.set_salario(ex.solicitar_dato_int("ingrese su salario: "))
    ops.mostrarDG()
    ops.calcularEPS()
    ops.calculaPension()
    ops.calculaARL()
    ops.calculaSENA()
    ops.calculaCajas()
    ops.calculaICBF()
    ops.calculaAuxilio()
    ops.mostrarDatosAdmin()
    ops.liquidarValorContrato()
    ops.mostrarLiqOPS()
