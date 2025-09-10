class Athlete:

    def __init__(self, id: int, name: str, surname: str, position: str, price: float, score: float, avg_score: float, status: str):


        """
        Inicializa os atributos do atleta

            id: ID do atleta
            name: Nome do atleta
            position: Posição do atleta
            price: Preço do atleta
            score: Pontuação do atleta
            avg_score: Média de pontuação do atleta
            status: Status do atleta
        """

        self.id = id
        self.name = name
        self.surname = surname
        self.position = position
        self.price = price
        self.score = score
        self.avg_score = avg_score
        self.status = status

    def __str__(self):

        """
        Retorna uma string com os dados do atleta
        """

        return f" Atleta: {self.name} \n Apelido: {self.surname} \n Posição: {self.position} \n Preço: {self.price} \n Pontuação: {self.score} \n Média de Pontuação: {self.avg_score} \n Status: {self.status}"
