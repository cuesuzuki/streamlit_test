import streamlit as st
import  pandas as pd
import  numpy as np
from PIL import Image


# # タイトルを表示する
st.title("Streamlit スーパー入門！ その２")

"""
## 3. レイアウトを整える
"""

"""
#### 1. チェックボックス
"""
st.write('チェックボックス：画像表示の切替')

# if文の分岐コード(True,False)を書かなくてよい。
if st.checkbox('show Image'):
    img = Image.open('eva_sea.png')
    st.image(img, caption = 'cueplanning.inc', use_column_width=True)

"""
## 1. インターフェイスをサイドバーに移動する
"""

"""
#### 2. セレクトボックス
"""
option = st.sidebar.selectbox(
    'あなたが好きな数字を教えてください',
    list(range(1,11))
)
'あたなの好きな数字は、', option ,'です。'

"""
### 3. テキスト入力
"""
text = st.sidebar.text_input('あなたの趣味をおしえてちょうだい！')
'あなたの趣味：', text

"""
### 4. スライダー
"""
condition = st.sidebar.slider('あなたの今の調子はどう？',1,100,50)
'今の調子は：', condition
