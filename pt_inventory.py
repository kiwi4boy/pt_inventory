from json import loads
import re

def parse_orig_str(s: str):
    texts = [
        t for t in re.findall("""\\"inventory\\":\[.*?\]""", s)
        if '[]' not in t
    ]
    texts = texts[0].replace('\\"', '"')
    return loads('{' + texts + '}')['inventory']


def extract_pt_inventory(pt_inv):
    return {
        pt_item['tier']['name']: pt_item['availableCount']
        for pt_item in pt_inv
    }



s = input('Enter inventory line: ')
s = parse_orig_str(s)
s = extract_pt_inventory(s)

print(s)