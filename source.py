import json

user_data = {
    "user_id": 1,
    "username": "sarah_jones",
    "email": "sarah.jones1984@gmail.com",
    "password_hash": "$2a$10$7X9y7h9pQ8PjI9NwYy27fY8v/h0vKqPUSIM9OfLxxkP8YwXTIyO8W",  # Fake password hash
    "address": "1280 Elm Street, San Francisco, CA 94107",
    "phone": "+1 (415) 555-2324",
    "dob": "1984-04-12"
}

api_key = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"  # API Key

credit_card = "4111 1111 1111 1111"  # Fake credit card

private_key = """
-----BEGIN RSA PRIVATE KEY-----
MIIBOgIBAAJBAKj34GkxFhD90vcNLYLInFEX6Ppy1tPf9Cnzj4p4WGeKLs1Pt8Qu
KUpRKfFLfRYC9AIKjbJTWit+CqvjWYzvQwECAwEAAQJAIJLixBy2qpFoS4DSmoEm
o3qGy0t6z09AIJtH+5OeRV1be+N4cDYJKffGzDa88vQENZiRm0GRq6a+HPGQMd2k
TQIhAKMSvzIBnni7ot/OSie2TmJLY4SwTQAevXysE2RbFDYdAiEBCUEaRQnMnbp7
9mxDXDf6AU0cN/RPBjb9qSHDcWZHGzUCIG2Es59z8ugGrDY+pxLQnwfotadxd+Uy
v/Ow5T0q5gIJAiEAyS4RaI9YG8EWx/2w0T67ZUVAw8eOMB6BIUg0Xcu+3okCIBOs
/5OiPgoTdSy7bcF9IGpSE8ZgGKzgYQVZeN97YE00
-----END RSA PRIVATE KEY-----
"""

print(json.dumps(user_data, indent=4))

transaction = {
    "transaction_id": "TXN00987",
    "user_id": 1,
    "amount": 259.45,
    "status": "Completed",
    "credit_card": credit_card
}

print(transaction)

print("Private Key: ", private_key)
