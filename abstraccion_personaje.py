class Personaje:
    
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
        
    def atributos(self):
        print(self.__nombre, ':', sep='')
        print('·Fuerza', self.fuerza)
        print('·Inteligencia', self.inteligencia)
        print('·Defensa', self.defensa)
        print('·Vida', self.vida)
    
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa
        
    def esta_vivo(self):
        return self.vida > 0
    
    def morir(self):
        self.vida = 0
        print(self.__nombre, 'ha muerto')
        
    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa
    
    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida = enemigo.vida -daño
        print(f'{self.__nombre}, ha realizado {daño} puntos de daño a {enemigo.__nombre}')
        if enemigo.esta_vivo():
            print(f'La vida de {enemigo.__nombre} es {enemigo.vida}')
        else:
            enemigo.morir()
                 
        
        
    
mi_personaje = Personaje('Fernando', 10, 1, 5, 100)
mi_enemigo = Personaje('Enemy', 8, 5, 3, 5)
# mi_personaje.morir()
# mi_personaje.atributos()
# print(mi_personaje.daño(mi_enemigo))
mi_personaje.atacar(mi_enemigo)
mi_enemigo.atributos()
