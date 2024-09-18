from modulo import *

if __name__ == '__main__':
    aluno1 = Aluno('','','')

    aluno1.nome      = input('Informe o nome do 1º aluno: ')
    aluno1.matricula = input('Informe a matricula do 1º aluno: ')
    aluno1.cpf       = input('Informe o CPF do 1º aluno: ')

    aluno2 = Aluno('','','')

    aluno2.nome      = input('Informe o nome do 2º aluno: ')
    aluno2.matricula = input('Informe a matricula do 2º aluno: ')
    aluno2.cpf       = input('Informe o CPF do 2º aluno: ')

    #instanciar curso
    curso1 = Curso('',0,'')

    curso1.nome = input('Informe o nome do curso: ')
    curso1.duracao = int(input('Informe a duração do curso: '))
    curso1.turno = input('Informe o turno: ')

    #cadastrando alunos instanciados no curso instanciado
    aluno1.inscrever_curso(curso1)
    aluno2.inscrever_curso(curso1)

    #saida de dados
    print(f'Aluno {aluno1.nome} de matricula {aluno1.matricula} está inscrito no curso {aluno1.listar_cursos()}.')
    print(f'Aluno {aluno2.nome} de matricula {aluno2.matricula} está inscrito no curso {aluno2.listar_cursos()}.')
