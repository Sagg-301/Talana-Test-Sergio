# TalanaKombat

## Description

This is a Python command-line interface (CLI) tool that simulates a fight beetween two kombatants.

### Installation

Clone the repository:
git clone https://github.com/Sagg-301/Talana-Test-Sergio.git

Install the required packages:

```sh
pip install -r requirements.txt
```

### Usage

To use the tool, simply run the command python main.py followed by the appropriate arguments. Here are some examples:

```sh
python main.py '{
	"player1": {
		"movimientos": ["D", "DSD", "S", "DSD", "SD"],
		"golpes": ["K", "P", "", "K", "P"]
	},
	"player2": {
		"movimientos": ["SA", "SA", "SA", "ASA", "SA"],
		"golpes": ["K", "", "K", "P", "P"]
	}
}'
```

```sh
python main.py '{
	"player1": {
		"movimientos": ["DSD", "S"],
		"golpes": ["P", ""]
	},
	"player2": {
		"movimientos": ["", "ASA", "DA", "AAA", "", "SA"],
		"golpes": ["P", "", "P", "K", "K", "K"]
	}
}'
```
