import pandas as pd

class StockModel:
    def __init__(self):
        self

    def model(self):
        code_df = pd.read_html("", header = "0")[0]
        code_df.종목코드 = code_df.종목코드.map('{:06d}'.format) #종목코드 6자리
        code_df = code_df.rename(columns={'회사명 : ':'name', '종목코드':'code'})
        print(code_df.head())

