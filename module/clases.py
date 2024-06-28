"""aqui creamos las clases

CBA
Ficha: 2877795
Aprendiz: Kevin Donato Jimenez Rocha
version: 1.0
fecha: 19/06/2024

"""

import datetime

class Persona():
    #definimos el metodo constructor

    
    def __init__ (self, idPersona= 0, nomPersona='',apePersona='',fechaNacimiento='',cuidadNacimiento='',genero='',estrato=''):
        self.__idPersona = idPersona #identificacion INT
        self.__nomPersona = nomPersona # nombres STR
        self.__apePersona = apePersona # apellidos STR
        self.__fechaNacimiento = fechaNacimiento #fechas (0000-00-00) 
        self.__cuidadNacimiento = cuidadNacimiento #cuidad donde nacio SRT
        self.__genero = genero #genero con que se identifica SRT
        self.__estrato = estrato # estrato social INT
        
    #Getter para obtener los valores 
    #Setter para asignar nuevos valores
    def get_idPersona (self):
        return self.__idPersona
    
    
    def set_idPersona (self, value):
        self.__idPersona = value
        
        
    def get_nomPersona (self):
        return self.__nomPersona
    
    
    def set_nomPersona (self, value):
        self.__nomPersona = value
        
        
    def get_apePersona(self):
        return self.__apePersona
    
    
    def set_apePersona (self, value):
        self.__apePersona = value
        
        
    def get_fechaNacimiento(self):
        return self.__fechaNacimiento
    
    
    def set_fechaNacimiento (self, value):
        self.__fechaNacimiento = value
        
        
    def get_ciudadNacimiento(self):
        return self.__cuidadNacimiento
    
    
    def set_cuidadNacimiento (self, value):
        self.__cuidadNacimiento = value
        
        
    def get_genero(self):
        return self.__genero
    
    
    def set_genero (self, value):
        self.__genero = value
        
        
    def get_estrato(self):
        return self.__estrato
    
    
    def set_estrato (self, value):
        self.__estrato = value
        
    #informacion basica    
    def mostrarDG(self):
        print("ID: {0}, Nombre: {1}, Apellido: {2}, Fecha Nacimiento: {3}, Ciudad de Nacimiento: {4}, Genero: {5}, Estrato: {6}".format(self.get_idPersona(), self.get_nomPersona(), self.get_apePersona(), self.get_fechaNacimiento(), self.get_ciudadNacimiento(), self.get_genero(), self.get_estrato()))
        
    
    #se calcula la eps
    def calcularEPS(self):
      """  aporte_empleado= 130000*(8.5/100)
        aporte_Trabajador= 1300000*(4/100)
        total = aporte_empleado + aporte_Trabajador
        print('\n EPS \n Aporte empleador : {1: 2f}\n Aporte Trabajador: {1: 2f}\n Total: {2: 2f}'.format(aporte_empleado, aporte_empleado, total))
        return total"""
    print("Calculando EPS:")
       
        
    #se calcula la pension
    def calculaPension(self):
        print("Calculando Pension:")
        
    
    # se calcula la ARL
    def calculaARL(self):
        print("Calculando ARL:")
       
        
    #SENA
    def calculaSENA(self):
        print("Calculando SENA:")
        
    
    #calculando las Cajas
    def calculaCajas(self):
        print("Calculando Cajas:")
        
    
    # calculando ICBF
    def calculaICBF(self):
        print("Calculando ICBF:")
        
    
    #calculando Auxilio
    def calculaAuxilio(self):
        print("Calculando Auxilio:")
        
    
    
class Docentes(Persona):
    #definimos el metodo constructor
    def __init__(self,idPersona= 0, nomPersona='',apePersona='',fechaNacimiento='',cuidadNacimiento='',genero='',estrato='', areaFormacion='', tituloProfesional='', unidadAcademica='',):
        super().__init__(idPersona, nomPersona,apePersona,fechaNacimiento,cuidadNacimiento,genero,estrato)  
        self.__areaFormacion = areaFormacion # Area de formacion STR
        self.__tituloProfesional = tituloProfesional # Titulo del profesional STR
        self.__unidadAcademica = unidadAcademica # la unidad academica STR
        
    #Getter para obtener los valores 
    #Setter para asignar nuevos valores
    def get_areaFormacion(self):
        return self.__areaFormacion
    
    
    def set_areaFormacion(self, value):
        self.__areaFormacion = value    
        
    
    def get_tituloProfesional(self):
        return self.__tituloProfesional
    
    
    def set_tituloProfesional(self, value):
        self.__tituloProfesional = value   
     
        
    def get_unidadAcademica(self):
        return self.__unidadAcademica
    
    
    def set_unidadAcademica(self, value):
        self.__unidadAcademica = value 
        
    #informacion basica
    def mostrarDatosDocentes(self):
        print("ID: {0}\n Nombre: {1}\n Apellido: {2}\n Fecha Nacimiento: {3}\n Ciudad de Nacimiento: {4}\n Genero: {5}\n Estrato: {6}\n Area de formacion: {7}\n Titulo Profesional: {8} \n Unidad academica {9}\n".format(self.get_idPersona(), self.get_nomPersona(), self.get_apePersona(), self.get_fechaNacimiento(), self.get_ciudadNacimiento(), self.get_genero(), self.get_estrato(), self.get_areaFormacion(),self.get_tituloProfesional(), self.get_unidadAcademica()))
        
        
class TiempoCompleto(Docentes):
    #definimos el metodo constructor
    def __init__(self,idPersona= 0, nomPersona='',apePersona='',fechaNacimiento='',cuidadNacimiento='',genero='',estrato='', areaFormacion='', tituloProfesional='', unidadAcademica='', categoria='',puntos=0, salario=0):
        super().__init__(idPersona, nomPersona,apePersona,fechaNacimiento,cuidadNacimiento,genero,estrato, areaFormacion, tituloProfesional, unidadAcademica)  
        self.__categoria= categoria
        self.__puntos= puntos
        self.__salario= salario
        
    #Getter para obtener los valores 
    #Setter para asignar nuevos valores
    def get_categoria(self):
        return self.__categoria
    
    
    def set_categoria(self, value):
        self.__categoria = value    
        
    
    def get_puntos(self):
        return self.__puntos
    
    
    def set_puntos(self, value):
        self.__puntos = value
        
    
    def get_salario(self):
        return self.__salario
    
    
    def set_salario(self,value):
        self.__salario = value
        
    # calcula el sueldo 
    def calculaSuelto(self):
        print("Calculando Sueldo: ")
        
    # realiza la liquidacion TC
    def liquidarTC(self):
        print("liquitando la TC")
        
    # muestra la liquidacion TC
    def mostrarLiqTC(self):
        print("mostrando la liquidacion de TC")
        
        

class Ocasionales(Docentes):
    #definimos el metodo constructor
    def __init__(self,idPersona= 0, nomPersona='',apePersona='',fechaNacimiento='',cuidadNacimiento='',genero='',estrato='', areaFormacion='', tituloProfesional='', unidadAcademica='',   ultimoTitulo='', numMeses=0,salario=0):
        super().__init__(idPersona,nomPersona,apePersona,fechaNacimiento,cuidadNacimiento,genero,estrato,areaFormacion,tituloProfesional,unidadAcademica)
        self.__ultimoTitulo = ultimoTitulo #ultimo titulo obtenido STR
        self.__numMeses = numMeses #numero de meses que estuvo  STR
        self.__salario = salario # salario INT
        
        
    #Getter para obtener los valores
    #Setter para asignar nuevos valores
    def get_ultimoTitulo(self):
        return self.__ultimoTitulo
    
    
    def set_ultimoTitulo(self,value):
        self.__ultimoTitulo = value
       
        
    def get_numMeses(self):
        return self.__numMeses
    
    
    def set_numMeses(self,value):
        self.__numMeses = value
       
        
    def get_salario(self):
        return self.__salario
    
    
    def set_salario(self,value):
        self.__salario = value
        
    
    #calcula el sueldo 
    def calcularSueldo(self):
        print("Calculando Sueldo: ")
        
    # realiza la liquidacion   
    def liquidarOC(self):
        print("liquitando la OC")
        
    # muestra la liquidacion OC    
    def mostrarLiqOC(self):
        print("mostrando la liquidacion de OC")
    

class HoraCatedra(Docentes):
    #definimos el metodo constructor
    def __init__(self,idPersona= 0, nomPersona='',apePersona='',fechaNacimiento='',cuidadNacimiento='',genero='',estrato='', areaFormacion='', tituloProfesional='', unidadAcademica='',   ultimoTitulo='', numHoras=0,salario=0 , valorContrato=0):
        super().__init__(idPersona,nomPersona,apePersona,fechaNacimiento,cuidadNacimiento,genero,estrato,areaFormacion,tituloProfesional,unidadAcademica)
        self.__ultimoTitulo = ultimoTitulo #ultimo titulo obtenido STR
        self.__numHoras = numHoras #numero de meses que estuvo  STR
        self.__salario = salario # salario INT
        self.valorContrato= valorContrato # el valor del contrato INT
        
        
    #Getter para obtener los valores
    #Setter para asignar nuevos valores
    def get_ultimoTitulo(self):
        return self.__ultimoTitulo
    
    
    def set_ultimoTitulo(self,value):
        self.__ultimoTitulo = value
        
        
    def get_numHoras(self):
        return self.__numHoras
    
    
    def set_numHoras(self,value):
        self.__numHoras = value
     
        
    def get_salario(self):
        return self.__salario
    
    
    def set_salario(self,value):
        self.__salario = value
       
        
    def get_valorContrato(self):
        return self.__valorContrato
    
    
    def set_valorContrato(self,value):
        self.__valorContrato = value
        

    # se calcula el sueldo
    def calcularSueldo(self):
        print("Calculando Sueldo: ")
        

    # se realizaq la liquidacion HC  
    def liquidarHC(self):
        print("Liquidando HC: ")


    # se muestra la liquidacion HC   
    def mostrarLiqHC(self):
        print("mostrando la liquidacion HC")    
        
"""------------------------------------------------------------------------------------------------------------------"""   

class Administrativos(Persona):
    #definimos el metodo constructor
    def __init__(self,idPersona= 0, nomPersona='',apePersona='',fechaNacimiento='',cuidadNacimiento='',genero='',estrato='', dependencia='',titulo=''):
        super().__init__(idPersona, nomPersona,apePersona,fechaNacimiento,cuidadNacimiento,genero,estrato)  
        self.__dependencia = dependencia # la dependencia que pertenece STR
        self.__titulo = titulo # el titulo STR
        
    #Getter para obtener los valores 
    #Setter para asignar nuevos valores
    def get_dependencia(self):
        return self.__dependencia
    
    
    def set_dependencia(self, value):
        self.__dependencia = value
        
    
    def get_titulo(self):
        return self.__titulo
    
    def set_titulo(self,value):
        self.__titulo = value
        
    # muestra los datos basicos
    def mostrarDatosAdmin(self):
        print("ID: {0}, Nombre: {1}, Apellido: {2}, Fecha Nacimiento: {3}, Ciudad de Nacimiento: {4}, Genero: {5}, Estrato: {6}, Dependencia: {7}, Titulo: {8}".format(self.get_idPersona(), self.get_nomPersona(), self.get_apePersona(), self.get_fechaNacimiento(), self.get_ciudadNacimiento(), self.get_genero(), self.get_estrato(), self.get_dependencia(),self.get_titulo()))
        
    
class Planta(Administrativos):
    #definimos el metodo constructor
    def __init__(self,idPersona= 0, nomPersona='',apePersona='',fechaNacimiento='',cuidadNacimiento='',genero='',estrato='', dependencia='',titulo='', ano=1, mes=1, dia=1):
        super().__init__(idPersona, nomPersona,apePersona,fechaNacimiento,cuidadNacimiento,genero,estrato,dependencia,titulo)
        self.__fechaVinculacion = datetime.datetime(ano, mes, dia) # la fecha cuando se vinculo DATETIME
        
        
    #Getter para obtener los valores
    #Setter para asignar nuevos valores
    def get_fechaVinculacion(self):
        return self.__fechaVinculacion
    
    
    def set_fechaVinculacion(self,ano, mes ,dia):
        self.__fechaVinculacion = datetime.datetime(ano,mes,dia)
        

     #muestra los datos basicos   
    def mostrarDatosAdminPlanta(self):
        print("ID: {0}, Nombre: {1}, Apellido: {2}, Fecha Nacimiento: {3}, Ciudad de Nacimiento: {4}, Genero: {5}, Estrato: {6}, Dependencia: {7}, Titulo: {8}, Fecha de vinculacion: {9}".format(self.get_idPersona(), self.get_nomPersona(), self.get_apePersona(), self.get_fechaNacimiento(), self.get_ciudadNacimiento(), self.get_genero(), self.get_estrato(), self.get_dependencia(),self.get_titulo(), self.get_fechaVinculacion()))
        

class Auxiliar(Planta):
    #definimos el metodo constructor
    def __init__(self,idPersona= 0, nomPersona='',apePersona='',fechaNacimiento='',cuidadNacimiento='',genero='',estrato='', dependencia='',titulo='', ano=1, mes=1, dia=1, nivel=0, salario=0,):
        super().__init__(idPersona, nomPersona,apePersona,fechaNacimiento,cuidadNacimiento,genero,estrato,dependencia,titulo,ano, mes, dia)
        self.__nivel = nivel # int
        self.__salario = salario #int
        
        
    #Getter para obtener los valores
    #Setter para asignar nuevos valores
    def get_nivel(self):
        return self.__nivel
    
    
    def set_nivel(self,value):
        self.__nivel = value
        
    
    def get_salario(self):
        return self.__salario
    
    
    def set_salario(self,value):
        self.__salario = value
        

    # caculando el sueldo
    def calcularSueldo(self):
        print("calculando sueldo: ")
        
    
    # se realiza la liquidacion
    def liquidarAux(self):
        print("liquidando el auxilio: ")


    # se muestra la liquidacion    
    def  mostrarLiqAux(self):
        print("mostrando la liquidacion del auxilio: ")
        
    

class Tecnico(Planta):
    #definimos el metodo constructor
    def __init__(self,idPersona= 0, nomPersona='',apePersona='',fechaNacimiento='',cuidadNacimiento='',genero='',estrato='', dependencia='',titulo='', ano=1, mes=1, dia=1, nivel=0, salario=0):
        super().__init__(idPersona, nomPersona,apePersona,fechaNacimiento,cuidadNacimiento,genero,estrato,dependencia,titulo,ano, mes, dia)
        self.__nivel = nivel #INT
        self.__salario = salario #INT
        
        
    #Getter para obtener los valores
    #Setter para asignar nuevos valores
    def get_nivel(self):
        return self.__nivel
    
    
    def set_nivel(self,value):
        self.__nivel = value
        
    
    def get_salario(self):
        return self.__salario
    
    
    def set_salario(self,value):
        self.__salario = value
       

    # se calcula el sueldo   
    def calcularSueldo(self):
        print("calculando sueldo: ")
        
    
    # se realiza la liquidacion TEC
    def liquidarTec(self):
        print("liquidando Tec: ")
        
    
    #se muestra la liquidacion 
    def mostrarLiqTec(self):
        print("mostrando la liquidacion de Tec: ")



class Profesional(Planta):
    #definimos el metodo constructor
    def __init__(self,idPersona= 0, nomPersona='',apePersona='',fechaNacimiento='',cuidadNacimiento='',genero='',estrato='', dependencia='',titulo='', ano=1, mes=1, dia=1, nivel=0, salario=0):
        super().__init__(idPersona, nomPersona,apePersona,fechaNacimiento,cuidadNacimiento,genero,estrato,dependencia,titulo,ano, mes, dia)
        self.__nivel = nivel #INT
        self.__salario = salario #INT
        
        
    #Getter para obtener los valores
    #Setter para asignar nuevos valores
    def get_nivel(self):
        return self.__nivel
    
    
    def set_nivel(self,value):
        self.__nivel = value
        
    
    def get_salario(self):
        return self.__salario
    
    
    def set_salario(self,value):
        self.__salario = value


    #calculando el sueldo 
    def calcularSueldo(self):
        print("calculando sueldo: ")
        
    
    # se realiza la liquidacion del Profesional
    def liquidarProf(self):
        print("liquidando Prof: ")
        
    
    # se muestra la liquidacion 
    def mostrarLiqProf(self):
        print("mostrando la liquidacion de Prof: ")
        


class OPS(Administrativos):
    #definimos el metodo constructor
    def __init__(self,idPersona= 0, nomPersona='',apePersona='',fechaNacimiento='',cuidadNacimiento='',genero='',estrato='', dependencia='',titulo='', ano=1, mes=1, dia=1,numMeses=0, valorContrato=0, salario=0,):
        super().__init__(idPersona, nomPersona,apePersona,fechaNacimiento,cuidadNacimiento,genero,estrato,dependencia,titulo)
        self.__fechaVinculacion = datetime.datetime(ano, mes, dia) #fecha cuando se vinculo DATETIME
        self.__numMeses= numMeses # numero de meses INT
        self.__valorContrato = valorContrato# valor por contrato INT
        self.__salario = salario # salario INT
        
        
    #Getter para obtener los valores
    #Setter para asignar nuevos valores
    def get_fechaVinculacion(self):
        return self.__fechaVinculacion
    
    
    def set_fechaVinculacion(self,ano, mes ,dia):
        self.__fechaVinculacion = datetime.datetime(ano,mes,dia)
        
    
    def get_numMeses(self): 
        return self.__numMeses
    
    
    def set_numMeses(self,value):
        self.__numMeses = value
        
    
    def get_valorContrato(self):
        return self.__valorContrato
    
    def set_valorContrato(self,value):
        self.__valorContrato = value


    def get_salario(self):
        return self.__salario
    

    def set_salario(self, value):
        self.__salario= value
        
    
    # se realiza la liquidacion del valor de contrato
    def liquidarValorContrato(self):
        print("liquidando el valor del contrato: ")


    # se muestra la liquidacion OPS 
    def mostrarLiqOPS(self):
        print("mostrando la liquidacion OPS: ")
        
    
    

    
        

    
    
        
    
    
        
        
        