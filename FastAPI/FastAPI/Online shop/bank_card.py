from cryptography.fernet import Fernet  
from gunicorn import app
from passlib.context import CryptContext
import uvicorn
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# alias for compatibility if other modules expect 'bcrypt'
bcrypt = pwd_context
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Example usage of password hashing and encryption
password = "**_00==++_password"
hashed_password = bcrypt.hash(password)
verified = bcrypt.verify(password, hashed_password)

# Encrypt the password
encrypted_password = cipher_suite.encrypt(password.encode())

# Decrypt the password
decrypted_password = cipher_suite.decrypt(encrypted_password).decode()

# Bank card information handling
class BankCard:
    def __init__(self, card_number: str, expiration_date: str, cvv: str):
        self.card_number = self.encrypt_card_number("144854009974")  # Example card number
        self.expiration_date = self.encrypt_expiration_date("12/30")  # Example expiration date
        self.cvv = self.encrypt_cvv("004")  # Example CVV

    def encrypt_card_number(self, card_number: str) -> str:
        return cipher_suite.encrypt(card_number.encode()).decode()

    def decrypt_card_number(self) -> str:
        return cipher_suite.decrypt(self.card_number.encode()).decode()

    def encrypt_cvv(self, cvv: str) -> str:
        return cipher_suite.encrypt(cvv.encode()).decode()

    def decrypt_cvv(self) -> str:
        return cipher_suite.decrypt(self.cvv.encode()).decode()
    
# Bank account number verification
def verify_bank_account_number(account_number: str) -> bool:
    # Simple check for length and numeric characters
    return len(account_number) == 10 and account_number.isdigit()

# Example usage of BankCard class    
bank_card = BankCard("1234567890", "12/25", "123")
print(bank_card.decrypt_card_number())
print(bank_card.decrypt_cvv())

print(verify_bank_account_number("1234567890"))

bank_name = "Revolut"
supported_banks = ["Revolut", "Monzo", "Starling", "HSBC", "Barclays"]
def is_supported_bank(bank_name: str) -> bool:
    return bank_name in supported_banks


print(is_supported_bank("Revolut"))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
