from hdwallet import BIP84HDWallet
from hdwallet.cryptocurrencies import BitcoinMainnet
import json

wallet = BIP84HDWallet(cryptocurrency=BitcoinMainnet)


data_keys = []

with open('words4.txt', "r") as f:

    for line in f:
        data_keys.extend(line.split())


for i in data_keys:
    wallet.from_mnemonic(mnemonic='blossom educate state course sick fresh color divide number soap please pull glide weather join grit depart dynamic tenant leopard alter piano slight room', passphrase=i)
    address = wallet.address()
    if address == 'bc1qcyrndzgy036f6ax370g8zyvlw86ulawgt0246r':
        print("Success", i)
        break
    else:
        print("address :", address)
# # Opening JSON file
# with open('words_dictionary.json') as json_file:
#     data = json.load(json_file)
#     data_keys = list(data.keys())
#     for i in data_keys:
#         wallet.from_mnemonic(mnemonic='blossom educate state course sick fresh color divide number soap please pull glide weather join grit depart dynamic tenant leopard alter piano slight room', passphrase=i)
#         address = wallet.address()
#         if address == 'bc1qcyrndzgy036f6ax370g8zyvlw86ulawgt0246r':
#             print("Success", i)
#             break
#         else:
#             print("address :", address)


#wallet.from_public_key(public_key='021209b131dfbd1efcfe15b1d1e92002653f5fc98e9ff6cb73a0d70153dbe58463')
#wallet.from_seed('4dee23381f5ead3f9c36681a544aef9b300f6d88ace5bde198dc5f6a4971f187c16e3c68a1480751fc4824913b2a1a58bbd9e05a061af5b67aee6266184b2a17')
