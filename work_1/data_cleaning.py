from encodings import utf_8
from turtle import end_fill
import pandas as pd
import numpy as np
import cn2an
import time
pd.set_option("display.max_columns", None)

df = pd.read_csv("./data/raw_data/A_lvr_land_A.csv")

# 選取欄位
df = df[["鄉鎮市區","交易年月日","總樓層數","建物型態","主要用途"]]

# 重新命名column
df = df.rename(columns={
"鄉鎮市區":"district",
"交易年月日":"date",
"總樓層數":"floor",
"建物型態":"style",
"主要用途":"use"
})

# 新增column，填入城市
df["city"] = pd.NaT
df['city'] = df['city'].fillna("台北市")

# drop解說
df = df.drop(df.index[0]).reset_index(drop=True)

# 更換 date 資料型態，轉為西元
df['date'] = df['date'].astype(int)
df['date'] = df['date'] + 19110000
df['date'] = pd.to_datetime(df['date'], format = "%Y%m%d")

# 正規表示法去掉不要的字
floor = df['floor'].str.split("/").str.get(0).str.split('([\u4e00|\u4e8c|\u4e09|\u56db|\u4e94|\u516d|\u4e03|\u516b|\u4e5d|\u5341]+)(\u5c64)').str.get(1)

# drop 空值
na_index = floor.index[floor.astype(str) == "nan"]
floor = floor.drop(na_index)
df = df.drop(na_index)

# 將中文數字轉為阿拉伯數字
nums = []
for num in floor :
    nums.append(cn2an.cn2an(num))

floor_nums = np.array(nums)
df['floor'] = floor_nums

# 填補use空值為其他
df['use'] = df['use'].fillna('其他')

# 輸出CSV檔
df.to_csv("./data/a_lvr_land_a.csv", index=False)

print('a_lvr_land_a.csv done')