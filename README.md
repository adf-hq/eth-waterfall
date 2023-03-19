# ETH Waterfall

Fastest way to waterfall your ETH's through the wallets

## Installation

Just clone the repository ```git clone https://github.com/adf-hq/eth-waterfall.git``` 

Then install ```pip install -r requirements.txt```

## Usage

For start using script, just input your wallets private keys into the ```wallets.txt``` file, one line - one private key, also you can input just address right after private key line, but script will be stopped after sending ETH's to wallet without private key

Also you need to input rpc url into the ```rpc.txt``` file, example: 

```https://eth-mainnet.g.alchemy.com/v2/m70yPmN38AuTp_A7w-N7YfbgMWNF0```

After theese two steps are done, you can start falling, just run the ```main.py``` file.

After each transaction sent, script will be wait for you pressing enter, and start next step only after you did this

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.