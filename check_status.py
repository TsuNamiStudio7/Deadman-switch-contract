from web3 import Web3

# Connect to an Ethereum node
w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))

# DeadManSwitch contract address and ABI
contract_address = '0xYourContractAddressHere'
contract_abi = '[...]'  # ABI of the DeadManSwitch contract

# Initialize contract
contract = w3.eth.contract(address=contract_address, abi=contract_abi)

# Function to check the status of the dead man's switch
def check_status():
    status = contract.functions.checkStatus().call()
    if status:
        print("The owner is still active.")
    else:
        print("The owner has not activated the switch in time. Action will be triggered.")

# Example: check the status
check_status()
