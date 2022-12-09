import io

""" pylint на строку докуемнтации ругается? """
with io.open('Data/Export.csv', mode="r", encoding="utf-8") as f:
    print(f.read())
