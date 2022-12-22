

# Aqui estão todas as logicas e regras para
# descrever a regra de negocio


class ActionControllerGirafa:
    def action_girafa(self, body, comida) -> bool:
        if (
            comida != "folhas"(body, dict)
            or "message" not in body
        ): return False

        response = body["message"]

        if response == comida == "folhas": 
            return "Folhas é de preferência da girafa."
        else: return "Essa comida não é de preferência da girafa."

    # Obter informação de comida do corpo da requisição
