import time
import json
import hmac
import hashlib
from Utils import CustomFloatEncoder


class Authentication:


    def __init__(self, api_secret_key: str, api_public_key: str):
        """
        Constructor para inicializar las claves.

        :param api_secret_key: Clave secreta para firmar.
        :param api_public_key: Clave pública para el encabezado.
        """
        self.api_secret_key = api_secret_key
        self.api_public_key = api_public_key

    def sign_request(self, path: str, body: dict) -> list:
        """
        Genera una firma para un path dado con un cuerpo específico.

        :param path: Ruta del recurso o servicio.
        :param body: Datos del cuerpo de la solicitud.
        :return: Lista de encabezados con la firma generada.
        """
        # Generar un nonce único basado en el tiempo actual.
        nonce = int(time.time() * 1000)

        # Convertir el cuerpo a formato JSON.
        body_json = "" if not body else json.dumps(body, ensure_ascii=False,  separators=(',', ':'), cls=CustomFloatEncoder)

        # Crear la cadena para firmar todo concatenado.
        signature_string = f"{path}{nonce}{body_json}"

        # Generar la firma utilizando HMAC-SHA384.
        signature = hmac.new(
            self.api_secret_key.encode('utf-8'),
            signature_string.encode('utf-8'),
            hashlib.sha384
        ).hexdigest()

        # Devolver los encabezados con la firma.
        return {
            "api-key": f"{self.api_public_key}",
            "api-nonce": f"{nonce}",
            "api-signature": f"{signature}",
            "Content-Type":"application/json"

        }
  
