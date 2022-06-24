from unittest.mock import Mock
from brownie import FundMe, network, config, MockV3Aggregator
from scripts.helpful_scripts import (
    get_account,
    deploy_mocks,
    LOCAL_BLOCKCHAIN_ENVIRONMENT,
)
from web3 import Web3
import time


def deploy_fund_me():
    account = get_account()
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENT:
        print(f"The active network is {network.show_active()}")
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(price_feed_address, {"from": account})
    time.sleep(1)
    print(f"Contract deployed to {fund_me.address}")


def main():
    deploy_fund_me()


# brownie networks add development mainnet-fork-dev cmd=ganache-cli host=http://127.0.0.1 fork='https://eth-mainnet.alchemyapi.io/v2/4BA5_xKGONhRKffDZ-joAVq2nQvHPC6z' accounts=10 mnemonic=brownie port=8545
