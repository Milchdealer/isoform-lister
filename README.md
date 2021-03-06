# Isoform Lister
Uses gene names saved as a list in `.txt` to lookup all isoform entry list IDs, specific to organism (common name, used in Entry ID column), and creates an isoform list, aligned with initial gene name row.

The `.txt` list is newline delimited.

## Output Format
Output is the initial gene name, followed by the isoform entries for that gene. Thus a row can have N (>=2) columns, separated by space.

## Requirements
* `python3`
* `venv` (if you want to run in `venv`)

## Setup (venv)
```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Setup (global)
```sh
pip install requests beautifulsoup4
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
