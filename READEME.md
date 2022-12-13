Exercício N°1:
- Uma fazendo possui 4 animais → Gorila, Leão, Cavalo e Girafa. Cada animal possui um
nome, uma idade e uma comida de preferência segundo a lista abaixo:
        * Gorila → Banana
        * Leão → Carne
        * Cavalo → feno
        * Girafa → folhas

Faça uma API em que cada rota seja relativa a um animal (ex:
http://localhost:5000/animal/gorila) e em cada rota seja enviado pelo cliente uma informação
de comida (body). Caso seja a comida de preferencia, retorne uma informação de
sucesso para o cliente (status code 200), caso contrário envie uma informação de falha
(status code 400)

* exemplo de resposta de sucesso JSON de chamadas:
    Cliente → {
        “comida”: “banana”
}
    Servidor → {
        “Gorila”: “Alberto”,
        “idade”: “3 anos”,
        “comida”: “O gorila come banana!”
    } (status code 200)

    * exemplo de resposta de erro JSON de chamadas:
    Cliente → {
        “comida”: “carne”
    }
    Servidor → {
        “Gorila”: “Alberto”,
        “idade”: “3 anos”,
        “comida”: “Erro! O gorila somente come banana!”
    } (status code 400)


IMPORTANTE:
Para cada animal, tais metodos devem ser obrigatórios na chamada:
    * Gorila → POST
    * Leão → POST
    * Cavalo → PATCH
    * Girafa → PATCH
OBS: O projeto tem como finalidade manusear e entender os elementos básicos de API dentro de
um software.