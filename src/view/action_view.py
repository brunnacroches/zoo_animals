# Aqui iremos distrinchar os elementos HTTP e preparar
# Os dados para jogar no controller

from ..controller.action_cavalo import ActionControllerCavalo
from ..controller.action_girafa import ActionControllerGirafa
from ..controller.action_gorila import ActionControllerGorila
from ..controller.action_leao import ActionControllerLeao


class ActionViewCavalo:
    def view_action_cavalo(self, request):
        # Separamos os dados http
        body = request.json
        user_agent = request.headers["User-Agent"]

        # Enviamos os dados separados para o controller
        action_controller_cavalo = ActionControllerCavalo()
        body_validation = action_controller_cavalo.action(body)

        # Retornamos uma resposta adequada para o retorno ao usuario
        # Formatação de dado para HTTP
        return {
            "status_code": 200,
            "data": {
                "validation": body_validation,
                "userAgent": user_agent
            },
            "success": True
        }

class ActionViewGorila:
    def view_action_gorila(self, request):
        # Separamos os dados http
        body = request.json
        user_agent = request.headers["User-Agent"]

        # Enviamos os dados separados para o controller
        action_controller_gorila = ActionControllerGorila()
        body_validation = action_controller_gorila.action(body)

        # Retornamos uma resposta adequada para o retorno ao usuario
        # Formatação de dado para HTTP
        return {
            "status_code": 200,
            "data": {
                "validation": body_validation,
                "userAgent": user_agent
            },
            "success": True
        }

class ActionViewGirafa:
    def view_action_girafa(self, request):
        # Separamos os dados http
        body = request.json
        user_agent = request.headers["User-Agent"]

        # Enviamos os dados separados para o controller
        action_controller_girafa = ActionControllerGirafa()
        body_validation = action_controller_girafa.action(body)

        # Retornamos uma resposta adequada para o retorno ao usuario
        # Formatação de dado para HTTP
        return {
            "status_code": 200,
            "data": {
                "validation": body_validation,
                "userAgent": user_agent
            },
            "success": True
        }

class ActionViewLeao:
    def view_action_leao(self, request):
        # Separamos os dados http
        body = request.json
        user_agent = request.headers["User-Agent"]

        # Enviamos os dados separados para o controller
        action_controller_leao = ActionControllerLeao()
        body_validation = action_controller_leao.action(body)

        # Retornamos uma resposta adequada para o retorno ao usuario
        # Formatação de dado para HTTP
        return {
            "status_code": 200,
            "data": {
                "validation": body_validation,
                "userAgent": user_agent
            },
            "success": True
        }




