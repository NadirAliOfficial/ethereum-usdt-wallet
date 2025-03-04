# USDT Wallet Creator

This repository provides a simple Python script to create an Ethereum wallet suitable for holding USDT tokens (ERC-20). The wallet is generated using the [eth-account](https://pypi.org/project/eth-account/) library and can be integrated with [web3.py](https://pypi.org/project/web3/) for further blockchain interactions.

## Features

* Generate a new Ethereum wallet with a secure private key.
* Obtain the wallet address that can be used to receive USDT tokens.
* Easily extend the code to interact with the Ethereum blockchain (e.g., checking balances, sending transactions).

## Prerequisites

* Python 3.6 or later.
* [eth-account](https://pypi.org/project/eth-account/) library.
* [web3.py](https://pypi.org/project/web3/) (optional for blockchain interactions).

## Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/usdt-wallet-creator.git
cd usdt-wallet-creator
```

### Set up a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install the required packages

```bash
pip install eth-account web3
```

## Usage

Run the script to generate a new Ethereum wallet:

```bash
python usdt-wallet.py
```

The script will output a new wallet address and the corresponding private key. Keep your private key secure and never share it.

## Security Warning

The generated private key is printed to the console. In production, use secure methods (such as hardware wallets or encrypted storage) to manage your private keys. Avoid hardcoding sensitive data in your source code.

## Contributing

Feel free to open issues or submit pull requests if you have improvements or suggestions.

## License

This project is licensed under the MIT License. See the LICENSE file for details.