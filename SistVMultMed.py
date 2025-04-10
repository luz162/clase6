class Medicamento:
    def __init__(self):
        self.__nombre = "" 
        self.__dosis = 0 
    
    def verNombre(self):
        return self.__nombre 
    
    def verDosis(self):
        return self.__dosis 
    
    def asignarNombre(self,med):
        self.__nombre = med 
        
    def asignarDosis(self,med):
        self.__dosis = med 
        
class Mascota:
    
    def __init__(self):
        self.__nombre= " "
        self.__historia=0
        self.__tipo=" "
        self.__peso=" "
        self.__fecha_ingreso=" "
        self.__lista_medicamentos=[]
    
        
    def verNombre(self):
        return self.__nombre
    def verHistoria(self):
        return self.__historia
    def verTipo(self):
        return self.__tipo
    def verPeso(self):
        return self.__peso
    def verFecha(self):
        return self.__fecha_ingreso
    def verLista_Medicamentos(self):
        return self.__lista_medicamentos 
        
            
    def asignarNombre(self,n):
        self.__nombre=n
    def asignarHistoria(self,nh):
        self.__historia=nh
    def asignarTipo(self,t):
        self.__tipo=t
    def asignarPeso(self,p):
        self.__peso=p
    def asignarFecha(self,f):
        self.__fecha_ingreso=f
    def asignarLista_Medicamentos(self,n):
        self.__lista_medicamentos = n

    # eliminar medicamento
    def eliminar_medicamento(self,nombre_medicamento):
        inicial=len(self.__lista_medicamentos)
        self.__lista_medicamentos=[med for  med in self.__lista_medicamentos
            if med.verNombre() !=nombre_medicamento]   
        return len(self.__lista_medicamentos) < inicial
    
class sistemaV:
    def __init__(self):
        self.__lista_mascotas = []
        self.__caninos = {}  # Diccionario de caninos
        self.__felinos = {}  # Diccionario de felinos
        
    def registrarMascota(self, mascota):
        historia = mascota.verHistoria()
        especie = mascota.verTipo().lower()

        if especie == "canino":
            if historia not in self.__caninos:
                self.__caninos[historia] = mascota
                print("Canino registrado con éxito.")
            else:
                print("Canino ya registrado.")
        elif especie == "felino":
            if historia not in self.__felinos:
                self.__felinos[historia] = mascota
                print("Felino registrado con éxito.")
            else:
                print("Felino ya registrado.")
        else:
            print("Especie no reconocida. Solo se aceptan 'canino' o 'felino'.")
   
    def verificarExiste(self,historia):
        for m in self.__lista_mascotas:
            if historia == m.verHistoria():
                return True
        #solo luego de haber recorrido todo el ciclo se retorna False
        return False
        
    def verNumeroMascotas(self):
        return len(self.__lista_mascotas) 
    
    def ingresarMascota(self,mascota):
        self.__lista_mascotas.append(mascota) 
   

    def verFechaIngreso(self,historia):
        #busco la mascota y devuelvo el atributo solicitado
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                return masc.verFecha() 
        return None

    def verMedicamento(self,historia):
        #busco la mascota y devuelvo el atributo solicitado
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                return masc.verLista_Medicamentos() 
        return None
    
    def eliminarMascota(self, historia):
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                self.__lista_mascotas.remove(masc)  #opcion con el pop
                return True  #eliminado con exito
        return False 
    
    #Elimina medicamento de la lista
    def eliminarMedicamento(self,historia,nombre_medicamento):
        for mascota in self.__lista_mascotas:
            if mascota.verHistoria() == historia:
                return mascota.eliminar_medicamento(nombre_medicamento)
        return False 

    def verMascotasPorTipo(self):
        print("\n--- Caninos Registrados ---")
        if self.__caninos:
            for historia, mascota in self.__caninos.items():
                print(f"Historia: {historia} | Nombre: {mascota.verNombre()}")
        else:
            print("No hay caninos registrados.")

        print("\n--- Felinos Registrados ---")
        if self.__felinos:
            for historia, mascota in self.__felinos.items():
                print(f"Historia: {historia} | Nombre: {mascota.verNombre()}")
        else:
            print("No hay felinos registrados.")    
        
   
import datetime
caninos = {}
felinos = {}

def main():
    servicio_hospitalario = sistemaV()
    # sistma=sistemaV()
    while True:
        menu=int(input('''\nIngrese una opción: 
                       \n1- Ingresar una mascota 
                       \n2- Ver fecha de ingreso 
                       \n3- Ver número de mascotas en el servicio 
                       \n4- Ver medicamentos que se están administrando
                       \n5- Eliminar mascota 
                       \n6- Eliminar medicamento
                       \n7- Ver mascotas registradas por tipo
                       \n8- Salir 
                       \nUsted ingresó la opción: ''' ))
        if menu==1: # Ingresar una mascota 
            if servicio_hospitalario.verNumeroMascotas() >= 10:
                print("No hay espacio ...") 
                continue
            historia=int(input("Ingrese la historia clínica de la mascota: "))
            #   verificacion=servicio_hospitalario.verDatosPaciente(historia)
            if servicio_hospitalario.verificarExiste(historia) == False:
                nombre=input("Ingrese el nombre de la mascota: ")
                tipo=input("Ingrese el tipo de mascota (felino o canino): ")
                peso=int(input("Ingrese el peso de la mascota: "))
                # aviso de ingreso de fecha incorrecta
                while True:
                    fecha=input("Ingrese la fecha de ingreso (dia/mes/año): ")
                    try:
                        fecha=datetime.datetime.strptime( fecha,"%d/%m/%Y")
                        break
                    except ValueError:
                        print("Formato incorrecto.(dia/mes/año)")
                
                nm=int(input("Ingrese cantidad de medicamentos: "))

                lista_med=[]

                for _ in range(nm):
                    nombre_medicamentos = input("Ingrese el nombre del medicamento: ")        
                    dosis = int(input("Ingrese la dosis: ")) 
                    medicamento = Medicamento()
                    medicamento.asignarNombre(nombre_medicamentos)
                    medicamento.asignarDosis(dosis)

                    # verificar medicamento
                    medicamento_existe=False
                    for med in lista_med:
                        if med.verNombre()==nombre_medicamentos:
                            print("este medicamento ya existe")
                            medicamento_existe =True
                            break
                    if not medicamento_existe:    
                        lista_med.append(medicamento)
                    else:
                        continue  

                   
                
                mas= Mascota()
                mas.asignarNombre(nombre)
                mas.asignarHistoria(historia)
                mas.asignarPeso(peso)
                mas.asignarTipo(tipo)
                mas.asignarFecha(fecha)
                mas.asignarLista_Medicamentos(lista_med)
                servicio_hospitalario.ingresarMascota(mas)
                servicio_hospitalario.registrarMascota(mas)

            else:
                print("Ya existe la mascota con el numero de histoira clinica")

        elif menu==2: # Ver fecha de ingreso
            q = int(input("Ingrese la historia clínica de la mascota: "))
            fecha = servicio_hospitalario.verFechaIngreso(q)
            # if servicio_hospitalario.verificarExiste == True
            if fecha != None:
                print("La fecha de ingreso de la mascota es: " + fecha.strftime("%d/%m/%Y"))
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")
            
        elif menu==3: # Ver número de mascotas en el servicio 
            numero=servicio_hospitalario.verNumeroMascotas()
            print("El número de pacientes en el sistema es: " + str(numero))

        elif menu==4: # Ver medicamentos que se están administrando
            q = int(input("Ingrese la historia clínica de la mascota: "))
            medicamento = servicio_hospitalario.verMedicamento(q) 
            if medicamento != None: 
                print("Los medicamentos suministrados son: ")
                for m in medicamento:   
                    print(f"\n- {m.verNombre()} (Dosis:{m.verDosis()})")
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")

        
        elif menu == 5: # Eliminar mascota
            q = int(input("Ingrese la historia clínica de la mascota: "))
            resultado_operacion = servicio_hospitalario.eliminarMascota(q) 
            if resultado_operacion == True:
                print("Mascota eliminada del sistema con exito")
            else:
                print("No se ha podido eliminar la mascota")

        elif menu==6:# eliminar medicamento
            
            q = int(input("Ingrese la historia clínica de la mascota: "))
            nombre_medicamento = input("Ingrese el nombre del medicamento a eliminar: ")
            if servicio_hospitalario.eliminarMedicamento(q, nombre_medicamento):
                print("Medicamento eliminado")
            else:
                print("Medicamento no existe") 

        elif menu == 7:  # Ver mascotas registradas por tipo
            servicio_hospitalario.verMascotasPorTipo()
                
        elif  menu==8:
            print("Usted ha salido del sistema de servicio de hospitalización...")
            break
        
        else:
            print("Usted ingresó una opción no válida, intentelo nuevamente...")

if __name__=='__main__':
    main()





            

                

