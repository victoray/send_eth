import blocksmith as blocksmith
from web3 import Web3


def send(out, HTTPProvider, to_address, gwei=5, gas=21000):
    w3 = Web3(Web3.HTTPProvider(HTTPProvider))

    for a in out:
        try:
            address = Web3.toChecksumAddress(blocksmith.EthereumWallet.generate_address(a))
            balance = w3.eth.getBalance(address)
            gas_price = w3.toWei(str(gwei), 'gwei')
            amount = balance - (gas_price * gas)

            nonce = w3.eth.getTransactionCount(address)
            tx = {
                'nonce': w3.toHex(nonce),
                'to': to_address,
                'value': w3.toHex(amount),
                'gas': w3.toHex(gas),
                'gasPrice': w3.toHex(gas_price),
            }
            if amount > 0:
                print('Eth', w3.fromWei(balance, 'ether'))
                signed_tx = w3.eth.account.signTransaction(tx, a)

                tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)

                print(w3.toHex(tx_hash))

        except:
            pass
