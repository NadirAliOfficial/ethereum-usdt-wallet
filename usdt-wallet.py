# pip install eth-account
from eth_account import Account

# Create a new Ethereum account
account = Account.create()

# Extract private key and wallet address
private_key = account.key.hex()
wallet_address = account.address

print("Your new wallet has been created!")
print("Wallet Address:", wallet_address)
print("Private Key:", private_key)
