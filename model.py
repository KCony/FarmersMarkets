import io
with io.open('Data/Export.csv', mode="r", encoding="utf-8") as f:
    print(f.read())
""" pylint на строку докуемнтации ругается? """
