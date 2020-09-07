from modelo_class import Aluno
from modelo_class import Responsavel

object1 = Aluno(116, 184620, "","17/10/1995",81993480779,"vandersonsilva@faculdadedetimbauba.edu.br")
object2 = Responsavel(101,"","","03/07/1964",81991535704,"valdecipardal@hotmail.com")


object1.nome = input("Digit o nome do aluno: ")
print(object1.nome+object1.indo()+object1.estudando())
print(object1.nome+object1.vindo()+object1.formado())

object2.nome = input("Digite o nome do Responsavel: ")
print(object2.nome+object2.responsavel(object1.nome))