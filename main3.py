import streamlit as st
import  pandas as pd
import  numpy as np
from PIL import Image

import time

# # タイトルを表示する
st.title("Streamlit スーパー入門！ その3")

"""
### 4. プログレスバーの表示 
"""
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(30):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress((i + 1)/30)
    time.sleep(0.1)

'Done!!!'

"""
## 3. レイアウトを整える
---
### 2. 2カラムのレイアウトに変更する
"""

left_column, right_column = st.columns(2)

button = left_column.button('右カラムに文字を表示する')
if button:
    right_column.write('ここは右カラム')


"""
### 3. エキスパンダーを追加する 
"""

expander = st.expander('問い合わせ1')
expander.write('問い合わせ内容1の回答')

expander = st.expander('問い合わせ2')
expander.write('問い合わせ内容2の回答')

expander = st.expander('問い合わせ3')
expander.write('問い合わせ内容3の回答')
