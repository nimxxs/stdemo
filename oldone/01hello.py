import streamlit as st
import time

print(st.__version__)

# 제목 위젯
st.title('제목')
st.header('헤더')
st.subheader('소제목')

# 텍스트 위젯
st.text('옥지얌 빵빵아')

# 수식 위젯
st.latex(r''' e^{i\pi} + 1 = 0''')

# 코드 위젯
st.code('for i in range(8): foo()')

# 버튼 위젯
if st.button('클릭해봐라'):
    st.write('Hello, World!!')

if st.checkbox("쳌쳌 마이크 원투원투"):
    st.write('안녕하세요 감사해요 잘있어요 다시만나요')

option1 = st.radio("골라봐", ["치킨", "피자"])
st.write('선택사항 : ', option1)

option2 = st.selectbox("골라봐", ["찍먹", "부먹"])
st.write('선택사항 : ', option2)

option3 = st.multiselect("무엇을 사고 싶어?", ["milk", "apples", "potatoes"]) # 다중선택
st.write('선택사항 : ', option3)

# 입력 위젯
text1 = st.text_input("First name")
st.write('입력내용 : ', text1)
text1a = st.text_input("your password", type='password')
st.write('입력내용 : ', text1a)

nums = st.number_input("Pick a number", 0, 10)
st.write('입력내용 : ', nums)

text2 = st.text_area("Text to translate")
st.write('입력내용 : ', text2)

date1 = st.date_input("Your birthday")
st.write('오늘 날짜 : ', date1)

time1 = st.time_input("Meeting time")
st.write('오늘 시간 : ', time1)

st.file_uploader("Upload a CSV")

# UI 위젯
slider1 = st.slider("Pick a number", 0, 100)
st.write('선택한 값 : ', slider1)

slider2 = st.select_slider("Pick a size", ["S", "M", "L"])
st.write('선택한 사이즈 : ', slider2)

# progress, status 위젯
st.snow()
st.toast('Warming up...')
st.error('Error message')
st.warning('Warning message')
st.info('Info message')
st.success('Success message')

# with st.spinner(text='In progress'):
#     time.sleep(3)
#     st.success('Done')
#
# bar = st.progress(0)
# for i in range(0, 100+1, 10):
#     time.sleep(1)
#     bar.progress(i)

# 사이드바 위젯
st.sidebar.radio('Select one:', [1, 2])

# 레이아웃 위젯
col1, col2 = st.columns(2)
col1.write("This is column 1")
col2.write("This is column 2")

# 탭 위젯
tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
tab1.write("this is tab 1")
tab2.write("this is tab 2")