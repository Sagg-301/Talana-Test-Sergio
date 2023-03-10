# TalanaKombat

## Description

This is a Python command-line interface (CLI) tool that simulates a fight beetween two Kombatants. Python 3.9+ is required. The use of virtual envs is recommended

## Installation

Clone the repository:
git clone https://github.com/Sagg-301/Talana-Test-Sergio.git

### Docker

Build the image from the root directory with the following command:

```sh
sudo docker build . -t talana_kombat
```

### Python

Install the required packages:

```sh
pip install -r requirements.txt
```

## Usage

### Docker

To run with dockers, just run it with the docker run command. Here are some examples:

```sh
docker run talana_kombat '{
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
docker run talana_kombat '{
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

### Python

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
