class Pessoa:
    def __init__(self, nome = None, idade=46):
        self.idade = idade
        self.nome = nome


    def cumprimentar(self):
        return f'Olá {self.nome}'


if __name__ == '__main__':
    p = Pessoa('Luciano')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    p.nome = 'Jesus'
    print(p.nome)
    print(p.idade)
