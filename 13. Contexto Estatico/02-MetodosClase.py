# Manejo de metodos de clase estaticos en Python 3

class MiClase:
    
    #Declaracion de Variables de Clase
    variable_clase = "Variable Clase"
    
    # 
    def __init__(self):
        self.variable_instancia = "Variable Instancia"
        
    # Este metodo se asocia a la clase como tal por lo tanto no necesita utilizar o recibir valores
    # Las declaraciones de metodos estaticos no pueden recibir el parametro self
    # Este decorador se utiliza para crear un metodo estatico
    # Tampoco se pueden llamar a las variables de instancia desde este decorador
    @staticmethod
    def metodo_estatico():
        print("Metodo Estatico")
        # Para acceder a una variable de clase se debe utilizar la clase como tal y llamar a la variable declarada
        print(MiClase.variable_clase)

    # Este decorador se utiliza para crear un metodo de clase
    # Este decorador a diferencia recibe un parametro, el cual hace referencia a la clase
    # Tampoco se pueden llamar a las variables de instancia desde este decorador
    @classmethod
    def metodo_clase(cls):
        print("Metodo de clase: " + str(cls))
        print(cls.variable_clase)
    
    # Un metodo de instancia no cuenta con ningun decorador
    # Los metodos de instancia si pueden llamar a los metodos estaticos ya que una vez que se crea el objeto estos son creados
    def metodo_instancia(self):
        print("____________________")
        self.metodo_estatico()
        self.metodo_clase()
        print(self.variable_clase)
        print(self.variable_instancia)
        
    # Nota: Para poder acceder a las variables de clase es recomendable utilizar el @classmethod debido a que este nos proporciona una instancia de la misma para poder llamar a las variables
    
# Solo es necesario llamar a la clase y el metodo para poder acceder al mismo
MiClase.metodo_estatico()
MiClase.metodo_clase()

# Creacion de objeto
# Desde el contexto de instancia (Objeto) podemos acceder al contexto estatico, ya sean variables o metodos
o = MiClase()
o.metodo_instancia()