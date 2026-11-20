from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
 
key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
 
with open("rsa_key.p8", "wb") as f:
    f.write(key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption(),
    ))
 
public_pem = key.public_key().public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo,
)
with open("rsa_key.pub", "wb") as f:
    f.write(public_pem)
 
one_line = "".join(
    line for line in public_pem.decode().splitlines() if "-----" not in line
)
print("Created rsa_key.p8 and rsa_key.pub")
print("Public key for Snowflake (copy everything on the next line):")
print(one_line)