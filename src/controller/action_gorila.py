
# Aqui estão todas as logicas e regras para
# descrever a regra de negocio

class ActionControllerGorila:
    def action_gorila(self, body, comida) -> bool:
        if (
            comida != "banana"(body, dict)
            or "message" not in body
        ): return False

        response = body["message"]

        if response == comida == "banana": 
            return "Banana é de preferência do gorila."
        else: return "Essa comida não é de preferência do gorila."

    # Obter informação de comida do corpo da requisição
 
