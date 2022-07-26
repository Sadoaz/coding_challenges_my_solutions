import hashlib
import itertools

def sha256_cracker(hash, chars):
    for x in set(["".join(x) for x in itertools.permutations(chars)]):
        if hashlib.sha256(x.encode('ascii')).hexdigest() == hash:
            return x
        
    return None