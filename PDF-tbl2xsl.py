#!/usr/bin/env python3

'''
    Converting PDF tables to xls
    Created by argv1 https://github.com/argv1/CSV-cleaning/PDF-tbl2xsl.py
'''

import pandas as pd
import pdfplumber
from styleframe import StyleFrame

def fetch_tables(input_file):
    content = []
    with pdfplumber.open(input_file) as pdf:
        for i,_ in enumerate(pdf.pages):
            page = pdf.pages[i]
            for table in page.extract_tables():
                if(table is not None) and ("Data field" in table[0][0]):
                    content.append(table[1:])
    return(content)  



def main():
    file_path = "K:/OneDrive/Programme/_current/techem2tbl/"
    input_file = file_path + "input.pdf"
    output_file = file_path + "data.xlsx"

    content = fetch_tables(input_file)

    flattened = [val for sublist in content for val in sublist]
    df = pd.DataFrame(flattened,columns=['Data field', 'Explanation'])
    StyleFrame(df).to_excel(output_file).save()

if __name__  == "__main__":
    main()