from decimal import Decimal
from eth_account import Account
from web3 import Web3


def waterfall(private_keys_list):
    with open('rpc.txt', 'r', encoding='utf-8') as rpc_file:
        web3 = Web3(Web3.HTTPProvider(rpc_file.read()))

    for i in range(1, len(private_keys_list)):
        current_gwei = web3.fromWei(web3.eth.gas_price, 'gwei')+3
        gas_will_cost_x_eth = web3.fromWei(
            Decimal(21000 * current_gwei) * (Decimal(10) ** 9), 'ether')

        from_address = Account.from_key(private_keys_list[i-1]).address
        from_balance = web3.fromWei(web3.eth.get_balance(from_address), 'ether')

        if web3.isAddress(private_keys_list[i]):
            to_address = private_keys_list[i]
        else:
            to_address = Account.from_key(private_keys_list[i]).address

        # print(from_balance)
        # print(gas_will_cost_x_eth)
        # print('-')
        # input(from_balance-gas_will_cost_x_eth)

        print(f'{from_address} -> {to_address}')

        nonce = web3.eth.getTransactionCount(from_address)
        tx = {
            'nonce': nonce,
            'to': to_address,
            'value': web3.toWei(from_balance-gas_will_cost_x_eth, 'ether'),
            'gas': 21000,
            'gasPrice': web3.toWei(current_gwei, 'gwei')
        }
        # print(f"Receiver will get: {from_balance-gas_will_cost_x_eth}")
        # print(f"Gas will cost: {gas_will_cost_x_eth}")
        # sign and send the transaction
        signed_tx = web3.eth.account.sign_transaction(tx, private_keys_list[i-1])
        web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        input('Press enter to next step: ')


if __name__ == '__main__':
    p_k_list = open('wallets.txt', 'r', encoding='utf-8').read().split('\n')
    waterfall(p_k_list)
