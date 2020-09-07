
from modelo_class import Aluno
from modelo_class import Responsavel
from modelo_class import Professor
from modelo_class import Coordenador
from modelo_class import Diretor



object1 = Aluno(0, "","","","")
object2 = Responsavel(0,"","","",0,"")
object3 = Professor(10, "2020", "Linguagem de Programação","Messias","07-09-1992","(83)7528-3680","messiasprofessor@facet.com")
object4 = Coordenador(28,"Messias","07-09-1992","(83)7528-3680","messiascoordenador@facet.com",2025, "Gestão da TI")
object5 = Diretor(0, 3055,"FACET Faculdade de Timbaúba","MESSIAS","03-03-1985","(81)9966-8896","facet@facet.edu.br")
#Criando conta de Usuarios...
# db_tb_aluno = {'ID':[],'MATRICULA':[],'NOME':[],'DATA_NASCIMENTO':[],'TELEFONE':[],'EMAIL':[]}

# def criaraluno():
#     object1.id +=1
#     db_tb_aluno['ID'].append(object1.id) 

#     object1.matricula = int(object1.id * 3)
#     db_tb_aluno['MATRICULA'].append(object1.matricula)

#     object1.nome = input("Digite o nome do aluno: ")
#     db_tb_aluno['NOME'].append(object1.nome)

#     object1.dt_nasc = input("Digite a data de nascimento: ")
#     db_tb_aluno['DATA_NASCIMENTO'].append(object1.dt_nasc)

#     object1.phone = input("Digite numero de Telefone: ")
#     db_tb_aluno['TELEFONE'].append(object1.phone)

#     object1.email = input("Digite o Email: ")
#     db_tb_aluno['EMAIL'].append(object1.email)

# def listaraluno():
#     for cont in range(len(db_tb_aluno['ID'])):
#         print(str(db_tb_aluno['MATRICULA'][cont])+' '+db_tb_aluno['NOME'][cont]+' '+db_tb_aluno['DATA_NASCIMENTO'][cont])
#         print('\n')


