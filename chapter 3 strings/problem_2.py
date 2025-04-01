letter = '''Dear <|Name|>,
            you are selected!
            <|Date|>'''

print(letter.replace("<|Name|>" ,  "MODx").replace("<|Date|>" ,  "21 Dec"))

