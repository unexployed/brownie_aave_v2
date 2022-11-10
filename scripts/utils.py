from brownie import accounts, network, config, Contract

FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]
TESTNET =["goerli"]

def get_account(index=None, id=None):
    if index:
        return accounts[index]
    if id:
        return accounts.load(id)
    if network.show_active() in TESTNET:
        return accounts.load("goerli_dev_1")
    if network.show_active() in FORKED_LOCAL_ENVIRONMENTS or LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]