import pandas as pd
import numpy as np

dfs = pd.read_html('https://10fastfingers.com/typing-test/german', flavor='html5lib')
xlWriter = pd.ExcelWriter('Output.xlsx', engine='xlsxwriter')
workbook = xlWriter.book

for i, df in enumerate(dfs):
    for col in df.columns[1:]:                  # UPDATE ONLY NUMERIC COLS 
        df.loc[df[col] == '-', col] = np.nan    # REPLACE HYPHEN WITH NaNs
        df[col] = df[col].astype(float)         # CONVERT TO FLOAT   

    df.to_excel(xlWriter, sheet_name='Sheet{}'.format(i))

xlWriter.save()