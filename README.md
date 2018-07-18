# World Cup Lottery

To run the lottery, make sure you are on a Unix system with Python 2.7 installed.

First, clone this repository by running:

```
git clone https://github.com/bethereumproject/world_cup_lottery
```

Navigate into the repository and run the following command with the correct seed generated by our smart contract. Instructions on how to generate the seed can be found [here](https://github.com/bethereumproject/lottery/tree/master/smart_contracts). The block we will use is block number 3663000, which had not been mined at the time this commit was made.

```
python lottery.py <seed here> > winners.json
```

The winners.json file should now contain the results of the lottery. To check that your generated result matches ours, simply run:

```
cat winners.json | md5sum
```

The output should be: `Unknown Yet`

