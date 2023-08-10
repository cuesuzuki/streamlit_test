import streamlit as st
import  pandas as pd
import  numpy as np
from PIL import Image


# # タイトルを表示する
st.title("Streamlit スーパー入門！ その１")

"""
---
# 1. Streamlitの基本
---
"""

st.write('Display Image')

img = Image.open('eva_sea.png')
st.image(img, caption = 'エヴァンゲリオンの海', use_column_width=True)


# テキストを表示する
st.write('DataFrame')

df = pd.DataFrame({
    '1列目': [1,2,3,4],
    '2列目': [10,20,30,40]
})

# データフレームを表示する（その１）
# write()は引数を指定できない
st.write(df)

# データフレームを表示する（その2）
st.dataframe(df)

# データフレームを表示する（その3）
# 引数を指定して、各種のサイズ指定ができる
st.dataframe(df, width=300, height=150)

# 引数を指定して、列にハイライトを追加する
st.dataframe(df.style.highlight_max(axis=0))

# 静的なテーブルの場合
# st.table(df.style.highlight_max(axis=0))

"""
# 章
## 節
### 項

```python
import streamlit as st
import  pandas as pd
import  numpy as np
```

1. import streamlit as st
2. import  pandas as pd
3. import  numpy as np
"""

df1 = pd.DataFrame(
    np.random.rand(10,6),
    columns = ['a','b','c','d','e','f']
)

df1

st.line_chart(df1)
st.bar_chart(df1)
st.area_chart(df1)

# 座標情報を指定して地図上に位置を表示する
df2 = pd.DataFrame(
    np.random.rand(100,2)/[50] + [35.69, 139.70],
    columns = ['lat','lon']
)
df2
st.map(df2)

"""
---
# 2. インタラクティブな「ウィジェット」を使う！
---

### （サンプル・ウィジェット）
1. チェックボックス
2. セレクトボックス
3. テキスト入力
4. スライダー
"""

"""
### 1. チェックボックス
"""
st.write('チェックボックス：画像表示の切替')

# if文の分岐コード(True,False)を書かなくてよい。
if st.checkbox('show Image'):
    img = Image.open('ロゴ_モーション.gif')
    st.image(img, caption = 'cueplanning.inc', use_column_width=True)

"""
### 2. セレクトボックス
"""
st.write('セレクトボックス：')

option = st.selectbox(
    'あなたが好きな数字を教えてください',
    list(range(1,11))
)
'あたなの好きな数字は、', option ,'です。'

"""
### 3. テキスト入力
"""

text = st.text_input('あなたの趣味をおしえてちょうだい！')

'あなたの趣味：', text


"""
### 4. スライダー
"""

condition = st.slider('あなたの今の調子はどう？',1,100,50)
'今の調子は：', condition
