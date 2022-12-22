
# Aqui estão todas as logicas e regras para
# descrever a regra de negocio


class ActionControllerLeao:
    def action_leao(self, body, comida) -> bool:
        if (
            comida != "carne"(body, dict)
            or "message" not in body
        ): return False

        response = body["message"]

        if response == comida == "carne": 
            return "Carne é de preferência do leão."
        else: return "Essa comida não é de preferência do leão."

    # Obter informação de comida do corpo da requisição
