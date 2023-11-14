from lib.gratitudes import *

def test_gratitudes_smiles():
    gratitudes = Gratitudes()
    gratitudes.add("your smiles")
    result = gratitudes.format()
    assert result == "Be grateful for: your smiles"

def test_gratitues_sunshine():
    gratitudes = Gratitudes()
    gratitudes.add("sunshine")
    result = gratitudes.format()
    assert result == "Be grateful for: sunshine"