# Tarea 2 Wilman Tasinchano

import random

# Lista de 30 Pokémon conocidos con sus estadísticas base (simplificadas)
pokemon_lista = [
    ("Pikachu", "Eléctrico", 55, 40, 90, 35),
    ("Charizard", "Fuego", 84, 78, 100, 78),
    ("Blastoise", "Agua", 83, 100, 78, 79),
    ("Bulbasaur", "Planta", 49, 49, 45, 45),
    ("Squirtle", "Agua", 48, 65, 43, 44),
    ("Jigglypuff", "Normal", 45, 20, 20, 115),
    ("Eevee", "Normal", 55, 50, 55, 55),
    ("Snorlax", "Normal", 110, 65, 30, 160),
    ("Mewtwo", "Psíquico", 110, 90, 130, 106),
    ("Gengar", "Fantasma", 65, 60, 110, 60),
    ("Machamp", "Lucha", 130, 80, 55, 90),
    ("Alakazam", "Psíquico", 50, 45, 120, 55),
    ("Dragonite", "Dragón", 134, 95, 80, 91),
    ("Lugia", "Psíquico/Volador", 90, 130, 110, 106),
    ("Moltres", "Fuego/Volador", 100, 90, 90, 90),
    ("Articuno", "Hielo/Volador", 90, 100, 85, 90),
    ("Zapdos", "Eléctrico/Volador", 90, 85, 100, 90),
    ("Gyarados", "Agua/Volador", 125, 79, 81, 95),
    ("Tyranitar", "Roca/Siniestro", 134, 110, 61, 100),
    ("Machop", "Lucha", 80, 50, 35, 70),
    ("Lanturn", "Agua/Eléctrico", 58, 58, 67, 125),
    ("Arbok", "Veneno", 85, 69, 80, 60),
    ("Rhydon", "Roca/Tierra", 130, 120, 40, 105),
    ("Venusaur", "Planta/Veneno", 82, 83, 80, 80),
    ("Chikorita", "Planta", 49, 49, 45, 45),
    ("Totodile", "Agua", 65, 64, 43, 50),
    ("Cyndaquil", "Fuego", 60, 50, 65, 39),
    ("Piplup", "Agua", 51, 53, 40, 53),
    ("Luxray", "Eléctrico", 120, 79, 70, 80),
]

# Función para elegir un Pokémon aleatorio de la lista
def elegir_pokemon_aleatorio():
    nombre, tipo, ataque, defensa, velocidad, ps = random.choice(pokemon_lista)
    # Crear el Pokémon correspondiente según su tipo
    if tipo == "Fuego":
        return Fuego(nombre, ataque, defensa, velocidad, ps)
    elif tipo == "Agua":
        return Agua(nombre, ataque, defensa, velocidad, ps)
    elif tipo == "Planta":
        return Planta(nombre, ataque, defensa, velocidad, ps)
    elif tipo == "Eléctrico":
        return Electrico(nombre, ataque, defensa, velocidad, ps)
    elif tipo == "Normal":
        return Pokemon(nombre, tipo, ataque, defensa, velocidad, ps)
    elif tipo == "Fantasma":
        return Pokemon(nombre, tipo, ataque, defensa, velocidad, ps)
    elif tipo == "Lucha":
        return Pokemon(nombre, tipo, ataque, defensa, velocidad, ps)
    elif tipo == "Psíquico":
        return Pokemon(nombre, tipo, ataque, defensa, velocidad, ps)
    elif tipo == "Dragón":
        return Pokemon(nombre, tipo, ataque, defensa, velocidad, ps)
    elif tipo == "Roca":
        return Pokemon(nombre, tipo, ataque, defensa, velocidad, ps)
    elif tipo == "Veneno":
        return Pokemon(nombre, tipo, ataque, defensa, velocidad, ps)
    elif tipo == "Siniestro":
        return Pokemon(nombre, tipo, ataque, defensa, velocidad, ps)
    elif tipo == "Hielo":
        return Pokemon(nombre, tipo, ataque, defensa, velocidad, ps)
    elif tipo == "Tierra":
        return Pokemon(nombre, tipo, ataque, defensa, velocidad, ps)
    elif tipo == "Volador":
        return Pokemon(nombre, tipo, ataque, defensa, velocidad, ps)
    else:
        # Si el tipo no es reconocido, retornamos un Pokémon genérico
        return Pokemon(nombre, tipo, ataque, defensa, velocidad, ps)

# Definir las clases de tipo de Pokémon como en el código anterior
class Pokemon:
    def __init__(self, nombre, tipo, ataque, defensa, velocidad, ps):
        self.nombre = nombre
        self.tipo = tipo
        self.ataque = ataque
        self.defensa = defensa
        self.velocidad = velocidad
        self.ps = ps

    def atributos(self):
        print(self.nombre, ":", sep="")
        print("·Tipo:", self.tipo)
        print("·Ataque:", self.ataque)
        print("·Defensa:", self.defensa)
        print("·Velocidad:", self.velocidad)
        print("·Puntos de Salud (PS):", self.ps)

    def esta_vivo(self):
        return self.ps > 0

    def recibir_dano(self, dano):
        self.ps -= dano
        if self.ps < 0:
            self.ps = 0
        print(self.nombre, "ha recibido", dano, "puntos de daño. PS restantes:", self.ps)

    def atacar(self, enemigo):
        dano = max(self.ataque - enemigo.defensa, 1)  # El daño mínimo es 1
        dano = self.calcular_bonus_tipo(enemigo, dano)
        enemigo.recibir_dano(dano)
        return dano

    def calcular_bonus_tipo(self, enemigo, dano):
        ventajas = {
            'Fuego': ['Planta', 'Hielo'],
            'Agua': ['Fuego', 'Tierra'],
            'Planta': ['Agua', 'Tierra'],
            'Electrico': ['Agua', 'Volador'],
            'Tierra': ['Fuego', 'Roca'],
        }

        if enemigo.tipo in ventajas.get(self.tipo, []):
            print(f"{self.nombre} tiene ventaja sobre {enemigo.nombre} debido al tipo.")
            dano *= 1.5  # Aumentamos el daño un 50% si hay ventaja de tipo
        return dano

class Fuego(Pokemon):
    def __init__(self, nombre, ataque, defensa, velocidad, ps):
        super().__init__(nombre, "Fuego", ataque, defensa, velocidad, ps)

class Agua(Pokemon):
    def __init__(self, nombre, ataque, defensa, velocidad, ps):
        super().__init__(nombre, "Agua", ataque, defensa, velocidad, ps)

class Planta(Pokemon):
    def __init__(self, nombre, ataque, defensa, velocidad, ps):
        super().__init__(nombre, "Planta", ataque, defensa, velocidad, ps)

class Electrico(Pokemon):
    def __init__(self, nombre, ataque, defensa, velocidad, ps):
        super().__init__(nombre, "Electrico", ataque, defensa, velocidad, ps)

class Combate:
    def __init__(self, pokemon_1, pokemon_2):
        self.pokemon_1 = pokemon_1
        self.pokemon_2 = pokemon_2

    def luchar(self):
        turno = 0
        while self.pokemon_1.esta_vivo() and self.pokemon_2.esta_vivo():
            print(f"\nTurno {turno}:")
            if self.pokemon_1.velocidad >= self.pokemon_2.velocidad:
                print(">>> Acción de", self.pokemon_1.nombre)
                self.pokemon_1.atacar(self.pokemon_2)
                if self.pokemon_2.esta_vivo():
                    print(">>> Acción de", self.pokemon_2.nombre)
                    self.pokemon_2.atacar(self.pokemon_1)
            else:
                print(">>> Acción de", self.pokemon_2.nombre)
                self.pokemon_2.atacar(self.pokemon_1)
                if self.pokemon_1.esta_vivo():
                    print(">>> Acción de", self.pokemon_1.nombre)
                    self.pokemon_1.atacar(self.pokemon_2)
            turno += 1

        if self.pokemon_1.esta_vivo():
            print("\n¡Ha ganado!", self.pokemon_1.nombre)
        elif self.pokemon_2.esta_vivo():
            print("\n¡Ha ganado!", self.pokemon_2.nombre)
        else:
            print("\n¡Es un empate!")


# Seleccionar dos Pokémon aleatorios de la lista
pokemon_1 = elegir_pokemon_aleatorio()
pokemon_2 = elegir_pokemon_aleatorio()

# Mostrar atributos de los Pokémon seleccionados
pokemon_1.atributos()
pokemon_2.atributos()

# Realizar combate
combate = Combate(pokemon_1, pokemon_2)
combate.luchar()

