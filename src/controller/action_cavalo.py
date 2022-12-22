

# Aqui estão todas as logicas e regras para
# descrever a regra de negocio

class ActionControllerCavalo:
    def action_cavalo(self, body, comida) -> bool:
        if (
            comida != "feno"(body, dict)
            or "message" not in body
        ): return False

        response = body["message"]

        if response == comida == "feno": 
            return "Feno é de preferência do cavalo."
        else: return "Essa comida não é de preferência do cavalo."

    # Obter informação de comida do corpo da requisição
