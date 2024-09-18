#ossociacao de classes
#voce tem duas classes completamente diferentes
#atributos e metodos diferentes, uma nao gerda nada da outra mas tem uma ligacao, quando um ou mais  atributos dessa classe e o tipo dela é o de outra classe
#é quando um atributo pega os dados de outra classe
#atributo de uma classe é outra classe 

class Aluno:
    def __init__(self, nome, matricula, cpf):
        self.__nome           = nome         #private
        self.__matricula      = matricula    #private
        self.__cpf            = cpf          #private
        self.cursos_inscritos = []           #associativo

    #metodos de acesso pois sao atributos private
    @property
    def nome(self):
        return self.__nome
    
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

    #METODOS DE ACESSO
    def inscrever_curso(self, curso):
        if curso not in self.cursos_inscritos:
            self.cursos_inscritos.append(curso)
            curso.adicionar_aluno(self)

    def listar_cursos(self):
        lista = []
        for curso in self.cursos_inscritos:
            lista.append(curso.nome)
            return lista


class Curso:
    def __init__(self, nome, duracao, turno):
        self.__nome    = nome
        self.__duracao = duracao
        self.__turno   = turno
        self.alunos_inscritos = [] #asssociando a classe curso à classe alunos: ASSOCIACAO
        #varios valores que vem de uma classe, pra cada aluno inscrito ele tera 3 atriutos diferentes(nome, duracao, turno), por isso cria uma lista
        #os dados de alunos estao protegidos dentro da classe aluno, por isso nao é private

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

    #METODO DE ACAO
    def adicionar_aluno(self, aluno): #jogar um aluno para a lista
        if aluno not in self.alunos_inscritos:
            self.alunos_inscritos.append(aluno)
            aluno.inscrever_curso(self)
            
    def listar_alunos(self):
        lista = []
        for aluno in self.alunos_inscritos:
            lista.append(aluno.nome)
        return lista
