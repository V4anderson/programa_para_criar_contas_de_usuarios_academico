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
    def __init__(self, id, matricula, nome, dt_nasc, phone, email):
        super().__init__(id, nome, dt_nasc, phone, email)

    def estudando(self):
        return " Pois ela(e) Está estudando. "
    def formado(self):
        return " Pois ela(e) Está formado. "

class Responsavel(Pessoa):
    def __init__(self, id, nome, aluno, dt_nasc, phone, email):
        super().__init__(id, nome, dt_nasc, phone, email)

    def responsavel(self,aluno):
        return " É responsavel por "+aluno

class Professor(Pessoa):
    def __init__(self, id, cod_professor, discplicina, nome, dt_nasc, phone, email):
        super().__init__(id, nome, dt_nasc, phone, email)

    def ministra(self,disciplina):
        return " Ministra aula no curso de "+disciplina

class Coordenador(Pessoa):
    def __init__(self, id, cod_coordenador, nome_curso, nome, dt_nasc, phone, email):
        super().__init__(id, nome, dt_nasc, phone, email)

    def coordena(self,nome_curso):
        return " Coordena o curso de "+nome_curso


class Diretor(Pessoa):
    def __init__(self, id, cod_diretor, nome_da_faculdade, nome, dt_nasc, phone, email):
        super().__init__(id, nome, dt_nasc, phone, email)

    def diretor(self, nome_da_faculdade):
        return "Diretor da faculdade "+nome_da_faculdade