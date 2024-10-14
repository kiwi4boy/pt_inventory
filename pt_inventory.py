from getpass import getpass
from json import loads
from re import findall

def parse_orig_str(s: str):
    extract_inventory = """\\\\"inventory\\\\"\\s*:\\s*\\[.*?\\]"""
    texts = [
        t for t in findall(extract_inventory, s)
        if '[]' not in t
    ]
    texts = texts[0].replace('\\"', '"')
    return loads('{' + texts + '}')['inventory']


def format_pt_inventory(pt_inv):
    return ', '.join(
        f"{pt_item['tier']['name']}: {pt_item['availableCount']}"
        for pt_item in pt_inv
    )



s = getpass('Enter inventory line: ')
s = parse_orig_str(s)
s = format_pt_inventory(s)

print(s)