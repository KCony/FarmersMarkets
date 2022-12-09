"""
pylint на строку докуемнтации ругается?

09.12.2022
"""
import io


with io.open('Data/Export.csv', mode="r", encoding="utf-8") as f:
    print(f.read())
