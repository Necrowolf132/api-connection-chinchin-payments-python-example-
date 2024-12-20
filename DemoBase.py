import json
from OrderResquests import OrderRequests
from Auth import Authentication

# URL base de la api
base_url = "https://sandbox-gprd.pagochinchin.com"

# Instanciar clases para autenticar y firmar, y para realizar consultas respectivamente 
order_requests = OrderRequests(base_url)
auth_instance = Authentication("Your api secret key", "Your api public key")
# Ejemmplo:
# auth_instance = Authentication("xxxxx01810ed9b97510c0c0c81fxxxxx", "xxxxxf430202a5153e7e9dcc341bxxxx")


# Crear cuerpo de la solicitud POST
post_body = {
    # Ejemmplo:
    # "idMembership": "xxxx94a9954eee09a91eexxxx",
    "idMembership": "Your id Membership",
    "externalReference": "ORDEN-123456",
    "clientOwner": "J413198282",
    "amount": "10.00",
    "currency": "BS",
    "expirationMs": 1200000,
    "showItems": True,
    "payingUser": {
        "firstName": "prueba",
        "secondName": "prueba",
        "lastname": "prueba",
        "surname": "prueba",
        "email": "prueba@gmail.com",
        "phoneNumberCode": "3524",
        "phoneNumber": "490523",
        "documentId": "V145234253"
    },
    "items": [
        {
            "name": "sushi",
            "image": "https://s1.eestatic.com/2021/05/27/como/584453709_186431572_1706x960.jpg",
            "description": "sushi",
            "quantity": "2",
            "price": "5",
            "totalPrice": "10"
        }
    ],
    "metadata": {
        "prueba": "Esto es una prueba de metadata"
    },
    "successUrl": "https://www.pagochinchin.com/success",
    "returnUrl": "https://www.pagochinchin.com/back",
    "errorUrl": "https://www.pagochinchin.com/error"
}

# Hacer la solicitud POST
print("Ejemplo de consulta post (Respuesta)") 
post_response = order_requests.post(post_body, auth_instance.sign_request('/cmer/v1/order', post_body))
print("Respuesta: \n")
print(post_response)

# Hacer la solicitud GET
print("\nEjemplo de consulta get (Respuesta)")
get_response = order_requests.get("?idOrder=6765c3d3cf16e35461b5ed79", auth_instance.sign_request('/cmer/v1/order', {"idOrder": "6765c3d3cf16e35461b5ed79"}))
print("Respuesta: \n")
print(get_response)
