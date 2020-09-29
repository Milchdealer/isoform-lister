# Isoform Lister
Uses gene names saved as a list in `.txt` to lookup all isoform entry list IDs, specific to organism (common name, used in Entry ID column), and creates an isoform list, aligned with initial gene name row.

The `.txt` list is newline delimited.

## Requirements
* `python3`
* `venv`

## Setup
```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage
```sh
usage: main.py [-h] [--searchlist SEARCHLIST] [--organism ORGANISM] [--output OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  --searchlist SEARCHLIST
                        Path to file which contains a list of gene names. Default: searchlist.txt
  --organism ORGANISM   Specify organism to search for by common name. Default: MOUSE
  --output OUTPUT       Path to file where to store the results. Default: results.txt
```

## Contributors
Initial idea goes to Suzuka, who does this tedious work occasionally for her research.
