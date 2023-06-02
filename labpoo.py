# Exemplos de herança, polimorfismo e encapsulamento

# Classe base (ou classe Pai) que representa um Animal
class Animal:
    def __init__(self, nome):
        self.__nome = nome  # Encapsulamento: atributo privado

    def fazer_som(self):
        pass  # Método abstrato

    def obter_nome(self):
        return self.__nome


# Subclasses (ou classes filhas) que herdam de Animal

# Subclasse Cachorro
class Cachorro(Animal):
    def fazer_som(self):
        return "Au au!"


# Subclasse Gato
class Gato(Animal):
    def fazer_som(self):
        return "Miau!"


# Subclasse Vaca
class Vaca(Animal):
    def fazer_som(self):
        return "Moo!"


# Função para interagir com o Animal sem conhecer a classe específica

def interagir_com_animal(animal):
    print(f'O animal {animal.obter_nome()} faz {animal.fazer_som()}\n')


# Instanciando as subclasses

cachorro = Cachorro("Totó")
gato = Gato("Lili")
vaca = Vaca("Mimosa")

# Chamando a função de interação com animais

interagir_com_animal(cachorro)  # Polimorfismo: Cachorro é um tipo de Animal
interagir_com_animal(gato)  # Polimorfismo: Gato é um tipo de Animal
interagir_com_animal(vaca)  # Polimorfismo: Vaca é um tipo de Animal
