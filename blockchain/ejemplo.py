from web3 import Web3

# Conectar a una red Ethereum (puede ser Mainnet, Testnet o Local)
infura_url = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"  # Reemplaza con tu URL de Infura
web3 = Web3(Web3.HTTPProvider(infura_url))

# Verificar si la conexión es exitosa
if web3.isConnected():
    print("Conectado a Ethereum")
else:
    print("No se pudo conectar a Ethereum")
    exit()

# Dirección de una cuenta (ejemplo público)
cuenta = "0x742d35Cc6634C0532925a3b844Bc454e4438f44e"

# Consultar el balance de la cuenta
balance_wei = web3.eth.get_balance(cuenta)
balance_ether = web3.fromWei(balance_wei, 'ether')

print(f"Balance de la cuenta {cuenta}: {balance_ether} ETH")