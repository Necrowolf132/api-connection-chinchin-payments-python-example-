import requests
import json
from Utils import CustomFloatEncoder


class OrderRequests:
    def __init__(self, base_url: str):
        """
        Inicializa la clase con la URL base.

        :param base_url: URL base para las solicitudes.
        """
        self.base_url = base_url.rstrip('/') + '/cmer/v1/order'

    def get(self, query: str, headers: dict = None) -> dict:
        """
        Realiza una solicitud GET.

        :param query: Query de la solicitud.
        :param headers: Encabezados de la solicitud.
        :return: Diccionario con el código de estado y la respuesta.
        """
        url = self.base_url + query
        try:
            response = requests.get(url, headers=headers)
            return {
                'status': response.status_code,
                'response': response.json() if response.text else None
            }
        except requests.RequestException as e:
            return {'error': str(e)}

    def post(self, body: dict, headers: dict = None) -> dict:
        """
        Realiza una solicitud POST.

        :param body: Cuerpo de la solicitud.
        :param headers: Encabezados de la solicitud.
        :return: Diccionario con el código de estado y la respuesta.
        """
        url = self.base_url
        try:
            # Realizar la solicitud POST
            response = requests.post(
                url,
                data=json.dumps(body, ensure_ascii=False,  separators=(',', ':') ,cls=CustomFloatEncoder),
                headers=headers
            )

            # Imprimir los encabezados de la solicitud con fines demostrativos
            print("Imprimimos los Headers de la solicitud post con fines demostrativos")
            print(response.request.headers)
            print("\n")

            return {
                'status': response.status_code,
                'response': response.json() if response.text else None
            }
        except requests.RequestException as e:
            return {'error': str(e)}
