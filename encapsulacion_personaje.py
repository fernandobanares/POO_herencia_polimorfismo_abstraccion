class Personaje:
    
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.__nombre = nombre
        self.__fuerza = fuerza
        self.__inteligencia = inteligencia
        self.__defensa = defensa
        self.__vida = vida
        
    def atributos(self):
        print(self.__nombre, ':', sep='')
        print('·Fuerza', self.__fuerza)
        print('·Inteligencia', self.__inteligencia)
        print('·Defensa', self.__defensa)
        print('·Vida', self.__vida)
    
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.__fuerza = self.__fuerza + fuerza
        self.__inteligencia = self.__inteligencia + inteligencia
        self.__defensa = self.__defensa + defensa
        
    def esta_vivo(self):
        return self.__vida > 0
    
    def morir(self):
        self.vida = 0
        print(self.__nombre, 'ha muerto')
        
    def daño(self, enemigo):
        return self.__fuerza - enemigo.defensa
    
    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida = enemigo.vida -daño
        print(f'{self.__nombre}, ha realizado {daño} puntos de daño a {enemigo.__nombre}')
        if enemigo.esta_vivo():
            print(f'La vida de {enemigo.__nombre} es {enemigo.vida}')
        else:
            enemigo.morir()
                 
    @property
    def fuerza(self):
        return self.__fuerza   
    @fuerza.setter
    def fuerza(self, fuerza):
        if fuerza < 0:
            print('Error, has introducido un valor negativo')
        else:
            self.__fuerza = fuerza 
        
    
mi_personaje = Personaje('Fernando', 10, 1, 5, 100)
mi_enemigo = Personaje('Enemy', 8, 5, 3, 5)
# mi_personaje.morir()
# mi_personaje.atributos()
# print(mi_personaje.daño(mi_enemigo))
# mi_personaje.atacar(mi_enemigo)
# mi_enemigo.atributos()

print(mi_personaje.fuerza)
mi_personaje.fuerza = 5
mi_personaje.atributos()
