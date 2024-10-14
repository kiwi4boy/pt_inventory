from json import loads

def parse_orig_str(s: str, head='"text": "', tail='\\n",'):
    return (
        s.strip()
        .removeprefix(head)
        .removesuffix(tail)
        .replace('\\"', '"')
    )


def load_pt_inventory(s):
    return loads(s)['data']['me']['trainingInfo']['personalTrainingInfo']['inventory']


def extract_pt_inventory(pt_inv):
    return {
        pt_item['tier']['name']: pt_item['availableCount']
        for pt_item in pt_inv
    }


s = input('Enter inventory line: ')
s = parse_orig_str(s)
s = load_pt_inventory(s)
s = extract_pt_inventory(s)

print(s)