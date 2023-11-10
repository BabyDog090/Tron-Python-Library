# Originally from: https://github.com/ethereum/web3.py
#

from eth_utils import ValidationError

from .deterministic import HDPath

TRON_DEFAULT_PATH = "m/44'/195'/0'/0/0"


def _import_mnemonic():
    try:
        from mnemonic import Mnemonic
    except ImportError as e:
        raise ImportError("Run `pip install tronpy[mnemonic]` to use mnemonic!") from e
    return Mnemonic


def generate_mnemonic(num_words: int, lang: str) -> str:
    Mnemonic = _import_mnemonic()
    words2strength = {12: 128, 15: 160, 18: 192, 21: 224, 24: 256}
    try:
        return Mnemonic(lang).generate(words2strength[num_words])
    except KeyError as e:
        raise ValueError(f"{num_words} not a valid number of words! Choose from {tuple(words2strength.keys())}") from e
