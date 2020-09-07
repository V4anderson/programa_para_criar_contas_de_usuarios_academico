class Pessoa():
    def __init__(self, id, nome, dt_nasc, phone, email):
        self.id = id
        self.nome = nome
        self.dt_nasc = dt_nasc
        self.phone = phone
        self.email = email

    def indo(self):
        return " Está indo para faculdade. "

    def vindo(self):
        return " Está vindo da faculdade. "


class Aluno(Pessoa):
        super().__init__(id, nome, dt_nasc, phone, email)

    def estudando(self):
        return " Pois ela(e) Está estudando. "
    def formado(self):
        return " Pois ela(e) Está formado. "

class Responsavel(Pessoa):
    def __init__(self, id, nome, aluno, dt_nasc, phone, email):
        self.aluno = aluno
        super().__init__(id, nome, dt_nasc, phone, email)

    def responsavel(self,aluno):
        return " É responsavel por "+aluno

class Professor(Pessoa):
    def __init__(self, id, cod_professor, discplicina, nome, dt_nasc, phone, email):
        self.cod_professor = cod_professor
        self.disciplina = discplicina
        super().__init__(id, nome, dt_nasc, phone, email)

    def ministra(self,disciplina):
        return " Ministra aula no curso de "+disciplina

class Coordenador(Pessoa):
    def __init__(self, id, nome, dt_nasc, phone, email, cod_coordenador, nome_curso):
        self.cod_coordenador = cod_coordenador
        self.nome_curso = nome_curso
        super().__init__(id, nome, dt_nasc, phone, email)

    def coordena(self):
        return " Coordena o curso de "

    
class Diretor(Pessoa):
    def __init__(self, id, cod_diretor, nome_da_faculdade, nome, dt_nasc, phone, email):
        self.cod_diretor = cod_diretor
        self.nome_da_faculdade = nome_da_faculdade
        super().__init__(id, nome, dt_nasc, phone, email)

    def diretor(self, nome_da_faculdade):
        return "Diretor da faculdade "+nome_da_faculdade