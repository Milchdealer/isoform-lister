from time import sleep
import argparse

import requests
from bs4 import BeautifulSoup as bs

UNIPROT_URL = "https://www.uniprot.org/uniprot/?query={}&sort=score"
UNIPROT_ID_PAGE = "https://www.uniprot.org/uniprot/{}"

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--searchlist",
        type=str,
        help="Path to file which contains a list of gene names.\nDefault: searchlist.txt",
        default="searchlist.txt",
    )
    parser.add_argument(
        "--organism",
        type=str,
        help="Specify organism to search for by common name.\nDefault: MOUSE",
        default="MOUSE",
    )
    parser.add_argument(
        "--output",
        type=str,
        help="Path to file where to store the results.\nDefault: results.txt",
        default="results.txt",
    )
    args = parser.parse_args()
    ORGANISM = args.organism.upper()

    searchterms = []
    with open(args.searchlist) as f:
        for line in f:
            searchterms.append(line)

    entries = []
    for searchterm in searchterms:
        searchresults = requests.get(UNIPROT_URL.format(searchterm))
        soup = bs(searchresults.text, "html.parser")
        tbody = soup.find("tbody")
        for row in tbody.find_all("tr"):
            columns = [td for td in row.find_all("td")]
            entry_name = columns[2].encode_contents().decode("UTF-8")
            if not entry_name.endswith(ORGANISM):
                continue
            gene_name = columns[5].find("strong").encode_contents().decode("UTF-8")
            if not gene_name:
                continue
            entry = columns[1].find("a").encode_contents().decode("UTF-8")
            entries.append({"search_term": searchterm.strip(), "uniprot_id": entry})
            break
        sleep(0.5)

    results = []
    for entry in entries:
        result = entry.copy()

        id_page = requests.get(UNIPROT_ID_PAGE.format(entry["uniprot_id"]))
        soup = bs(id_page.text, "html.parser")
        isoform_container = soup.find("h3", id="mapped-isoform-headers")
        if not isoform_container:
            print("Can't find isoform container for {}".format(entry))
            continue
        table = isoform_container.next_sibling
        while table and table.name != "table":
            table = table.next_sibling
        if table is None:
            continue
        entry_list = []
        for row in table.find_all("tr"):
            columns = [td for td in row.find_all("td")]
            if len(columns) <= 1:
                continue
            entry = columns[1]
            entry_list.append(entry.find("a").encode_contents().decode("UTF-8"))

        result.update({"entries": entry_list})
        results.append(result)
        sleep(0.5)

    with open(args.output, "w") as f:
        for result in results:
            f.write(result["uniprot_id"])
            f.write(" ")
            f.write(" ".join(result["entries"]))
            f.write("\n")
