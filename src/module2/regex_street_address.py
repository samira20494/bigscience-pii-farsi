import regex

rulebase = [([
    ("AGE", regex.compile("\S+ years old|\S+\-years\-old|\S+ year old|\S+\-year\-old"), None, None, None),
    ("STREET_ADDRESS", regex.compile(
        '^[\u0600-\u06FF]+(?:[\s0-9()،,-]+[\u0600-\u06FF]+)*$', regex.IGNORECASE), None, None, None),
    ("STREET_ADDRESS", regex.compile('\b(?!(\d)\1{3})[13-9]{4}[1346-9][013-9]{5}\b', regex.IGNORECASE), None, None, None),
], 1),
]

def street_address_match(str):
    addr_regex = rulebase[0][0][1][1]
    addr_match = regex.match(addr_regex, str)
    return addr_match and addr_match.string == str

def postal_code_match(str):
    postal_code_regex = rulebase[0][0][2][1]
    postal_code_match = regex.match(postal_code_regex, str)
    return postal_code_match and postal_code_match.string == str

if __name__  == "__main__":
    addr = "تهران - خیابان سهروردی - بزرگراه 19 شرقی، کوچه 59, پلاک 39525، طبقه ٣"
    addr_regex = rulebase[0][0][1][1]
    addr_match = regex.match(addr_regex, addr)
    print(addr_match and addr_match.string == addr)





# resources for street address:
# https://stackoverflow.com/questions/41441308/regex-for-accepting-persian-characters-in-address
# postal code: https://stackoverflow.com/questions/48719799/iranian-postal-code-validation