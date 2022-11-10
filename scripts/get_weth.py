from brownie import interface, config, network
from scripts.utils import get_account

def get_weth():
    account = get_account()
    weth = interface.IWeth(config["networks"][network.show_active()]["weth_token"])
    tx = weth.deposit({"from":account, "value":0.01*10**18})
    tx.wait(1)
    print("received 0.01 eth")

def main():
    get_weth()