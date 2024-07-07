import os
import random
from web3 import Web3
from eth_account import Account

# Arbitrum node sağlayıcısına bağlanma
arbitrum_url = 'https://arb-mainnet.g.alchemy.com/v2/YOUR_API_KEY'
w3 = Web3(Web3.HTTPProvider(arbitrum_url))

def generate_random_private_key():
    return '0x' + ''.join([random.choice('0123456789abcdef') for _ in range(64)])

def check_balance(private_key):
    account = Account.from_key(private_key)
    balance = w3.eth.get_balance(account.address)
    return balance, account.address

def main():
    total_keys = 10000  # Kontrol edilecek toplam key sayısı
    positive_balances = []
    
    for i in range(total_keys):
        private_key = generate_random_private_key()
        balance, address = check_balance(private_key)
        
        if balance > 0:
            positive_balances.append((address, private_key, balance))
            print(f"Address: {address} | Private Key: {private_key} | Balance: {w3.fromWei(balance, 'ether')} ETH")
        
        # İlerleme güncellemesi ve kontrol edilen private key
        print(f"Checked {i + 1}/{total_keys} keys. Current Private Key: {private_key} | Found {len(positive_balances)} addresses with positive balance.")
    
    if positive_balances:
        print("Positive balance addresses found:")
        for address, private_key, balance in positive_balances:
            print(f"Address: {address} | Private Key: {private_key} | Balance: {w3.fromWei(balance, 'ether')} ETH")
    else:
        print("No addresses with positive balance found.")

if __name__ == "__main__":
    main()
