palabra = "nn12"
pala = "nn12"
pa = "".join(filter(lambda char: not char.isdigit(), palabra))
pa2 = "".join(filter(lambda char: not char.isdigit(), palabra))
if __name__ == "__main__":
    print(pa == pa2)
