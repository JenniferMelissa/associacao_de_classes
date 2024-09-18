#ossociacao de classes
#voce tem duas classes completamente diferentes
#atributos e metodos diferentes, uma nao gerda nada da outra mas tem uma ligacao, quando um ou mais  atributos dessa classe e o tipo dela é o de outra classe
#é quando um atributo pega os dados de outra classe
#atributo de uma classe é outra classe 

class Aluno:
    def __init__(self, nome, matricula, cpf):
        self.__nome      = nome         #private
        self.__matricula = matricula    #private
        self.__cpf       = cpf          #private

    #metodos de acesso pois sao atributos private
    @property
    def nome(self):
        return self.__name
    
    @nome.setter
    def nome (self, nome):
        self.__nome = nome 

    @property
    def matricula(self):
        return self.__matricula
    
    @matricula.setter
    def matricula (self, matricula):
        self.__matricula = matricula 

    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf (self, cpf):
        self.__cpf = cpf 

class Curso:
    def __init__(self, nome, duracao, turno):
        self.__nome    = nome
        self.__duracao = duracao
        self.__turno   = turno
    
    #metodos de acesso
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome (self, nome):
        self.__nome = nome

    @property
    def duracao(self):
        return self.__duracao
    
    @duracao.setter
    def duracao (self, duracao):
        self.__duracao = duracao

    @property
    def turno(self):
        return self.__turno
    
    @turno.setter
    def turno (self, turno):
        self.__turno = turno
