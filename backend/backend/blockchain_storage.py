# from web3 import Web3

# def store_prescription_on_blockchain(prescription_data):
#     w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))
#     contract_address = "YOUR_CONTRACT_ADDRESS"
#     abi = "YOUR_CONTRACT_ABI"
#     contract = w3.eth.contract(address=contract_address, abi=abi)
#     tx_hash = contract.functions.storePrescription(prescription_data).transact()
#     return w3.toHex(tx_hash)
