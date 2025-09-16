# streamlit, pandas, plotly.express 라이브러리를 불러옵니다.
# plotly.express는 인터랙티브 차트를 만들기 위해 사용됩니다.
import streamlit as st
import pandas as pd
import plotly.express as px

# --- 페이지 설정 ---
# st.set_page_config()는 페이지의 제목, 아이콘, 레이아웃 등을 설정합니다.
# layout="wide"는 페이지를 넓게 사용하여 대시보드에 더 많은 공간을 확보합니다.
st.set_page_config(
    page_title="건설 장비 예지보전 대시보드",
    page_icon="🚜",
    layout="wide",
)

# --- 데이터 로딩 ---
# 데이터를 불러오는 함수를 정의합니다.
# @st.cache_data 데코레이터는 데이터 로딩을 캐싱하여 앱 성능을 향상시킵니다.
# 한 번 로드된 데이터는 변경되지 않는 한 다시 로드하지 않습니다.
@st.cache_data
def load_data():
    # 파일 경로를 현재 파일과 동일한 위치로 수정했습니다.
    df = pd.read_csv('construction_machine_data.csv')
    return df

# 데이터 로드 함수를 호출하여 데이터프레임을 생성합니다.
df = load_data()


# --- 사이드바 (Sidebar) ---
# st.sidebar는 화면 왼쪽에 사이드바를 생성합니다.
# 주로 필터나 설정 옵션을 배치하는 데 사용됩니다.
st.sidebar.header('⚙️ 필터 옵션')

# 부품 유형(Component_Type) 필터
# st.multiselect를 사용하여 여러 부품 유형을 동시에 선택할 수 있는 위젯을 생성합니다.
component_types = df['Component_Type'].unique()
selected_components = st.sidebar.multiselect(
    '부품 유형 선택',
    options=component_types,
    default=component_types  # 기본값으로 모든 유형을 선택
)

# 사용 시간(Operating_Hours) 필터
# st.slider를 사용하여 사용 시간 범위를 선택할 수 있는 슬라이더를 생성합니다.
min_hours = int(df['Operating_Hours'].min())
max_hours = int(df['Operating_Hours'].max())
hour_range = st.sidebar.slider(
    '사용 시간(Hours) 범위 선택',
    min_value=min_hours,
    max_value=max_hours,
    value=(min_hours, max_hours)  # 기본값으로 전체 범위 선택
)

# 센서 데이터(진동, 온도, 압력) 필터
# st.expander를 사용하여 센서 필터들을 접고 펼 수 있는 섹션을 만듭니다.
with st.sidebar.expander("📊 센서 데이터 필터"):
    # 진동(Vibration) 슬라이더
    min_vib = float(df['Vibration'].min())
    max_vib = float(df['Vibration'].max())
    vib_range = st.slider('진동(Vibration) 범위', min_vib, max_vib, (min_vib, max_vib))

    # 온도(Temperature) 슬라이더
    min_temp = float(df['Temperature'].min())
    max_temp = float(df['Temperature'].max())
    temp_range = st.slider('온도(Temperature) 범위', min_temp, max_temp, (min_temp, max_temp))

    # 압력(Pressure) 슬라이더
    min_press = float(df['Pressure'].min())
    max_press = float(df['Pressure'].max())
    press_range = st.slider('압력(Pressure) 범위', min_press, max_press, (min_press, max_press))


# --- 데이터 필터링 ---
# 사이드바에서 선택된 필터 조건에 따라 원본 데이터를 필터링합니다.
filtered_df = df[
    (df['Component_Type'].isin(selected_components)) &
    (df['Operating_Hours'].between(hour_range[0], hour_range[1])) &
    (df['Vibration'].between(vib_range[0], vib_range[1])) &
    (df['Temperature'].between(temp_range[0], temp_range[1])) &
    (df['Pressure'].between(press_range[0], press_range[1]))
]


# --- 메인 페이지 ---
# 대시보드의 메인 제목을 설정합니다.
st.title('🚜 건설 장비 예지보전 대시보드')
st.write("이 대시보드는 건설 장비의 센서 데이터와 잔존 수명(RUL)을 분석하여, 장비의 상태를 모니터링하고 예측하는 것을 돕습니다.")


# --- 탭(Tabs) 구성 ---
# st.tabs를 사용하여 여러 분석 내용을 독립된 탭으로 구성합니다.
tab1, tab2, tab3 = st.tabs(['📊 대시보드 개요', '📈 RUL 분포 및 관계 분석', '🧮 상관관계 분석'])


# --- 탭 1: 대시보드 개요 ---
with tab1:
    st.header('데이터 요약')
    
    # st.columns를 사용하여 화면을 여러 열로 나눕니다. 여기서는 3개의 열을 생성합니다.
    col1, col2, col3 = st.columns(3)

    # 각 컬럼에 주요 요약 통계(KPI)를 st.metric으로 표시합니다.
    with col1:
        st.metric(label="총 부품 수", value=f"{filtered_df.shape[0]} 개")
    with col2:
        st.metric(label="평균 잔존 수명(RUL)", value=f"{filtered_df['Remaining_Useful_Life'].mean():.1f} 일")
    with col3:
        st.metric(label="평균 사용 시간", value=f"{filtered_df['Operating_Hours'].mean():.1f} 시간")

    st.markdown("---") # 구분선
    
    # 두 개의 컬럼을 생성하여 데이터 미리보기와 부품 유형별 RUL 분포를 나란히 표시합니다.
    col1, col2 = st.columns([0.6, 0.4]) # 컬럼의 너비 비율을 6:4로 설정
    
    with col1:
        st.subheader("필터링된 데이터 미리보기")
        st.dataframe(filtered_df.head(10)) # 필터링된 데이터의 상위 10개를 표로 보여줍니다.
        
    with col2:
        st.subheader("부품 유형별 잔존 수명(RUL)")
        # 부품 유형별 잔존 수명의 분포를 박스 플롯으로 시각화합니다.
        fig = px.box(filtered_df, x='Component_Type', y='Remaining_Useful_Life', title='부품 유형별 RUL 분포')
        st.plotly_chart(fig, use_container_width=True) # use_container_width=True는 차트를 컬럼 너비에 맞춥니다.


# --- 탭 2: RUL 분포 및 관계 분석 ---
with tab2:
    st.header('잔존 수명(RUL) 분포 및 센서 데이터와의 관계')
    
    # 2개의 컬럼을 생성합니다.
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("잔존 수명(RUL) 분포")
        # RUL의 분포를 히스토그램으로 시각화합니다.
        fig_hist = px.histogram(filtered_df, x='Remaining_Useful_Life', nbins=50, title='RUL 분포')
        st.plotly_chart(fig_hist, use_container_width=True)
    
    with col2:
        st.subheader("사용 시간에 따른 RUL")
        # 사용 시간과 RUL의 관계를 산점도로 시각화합니다.
        fig_scatter_hours = px.scatter(filtered_df, x='Operating_Hours', y='Remaining_Useful_Life', 
                                       title='사용 시간에 따른 RUL', color='Component_Type')
        st.plotly_chart(fig_scatter_hours, use_container_width=True)
        
    st.markdown("---")
    
    st.subheader("주요 센서 데이터와 RUL의 관계 (산점도)")
    # 사용자가 X축 변수를 선택할 수 있는 selectbox를 생성합니다.
    sensor_options = ['Vibration', 'Temperature', 'Pressure']
    selected_sensor = st.selectbox('X축으로 사용할 센서 선택:', sensor_options)
    
    # 선택된 센서와 RUL의 관계를 산점도로 시각화합니다. 색상은 부품 유형으로 구분합니다.
    fig_scatter_sensor = px.scatter(
        filtered_df, 
        x=selected_sensor, 
        y='Remaining_Useful_Life', 
        color='Component_Type',
        title=f'{selected_sensor}와(과) 잔존 수명(RUL)의 관계'
    )
    st.plotly_chart(fig_scatter_sensor, use_container_width=True)


# --- 탭 3: 상관관계 분석 ---
with tab3:
    st.header('센서 데이터 간 상관관계 분석')
    st.write("아래 히트맵은 주요 숫자형 변수들 간의 상관관계를 보여줍니다. 값이 1에 가까울수록 강한 양의 상관관계, -1에 가까울수록 강한 음의 상관관계를 의미합니다.")
    
    # 분석할 숫자형 변수 리스트를 정의합니다.
    numeric_cols = ['Vibration', 'Temperature', 'Pressure', 'Operating_Hours', 'Remaining_Useful_Life']
    
    # 상관관계 행렬을 계산합니다.
    corr_matrix = filtered_df[numeric_cols].corr()
    
    # 상관관계 행렬을 히트맵으로 시각화합니다.
    fig_heatmap = px.imshow(
        corr_matrix,
        text_auto=True,  # 히트맵에 상관계수 값을 표시
        aspect="auto",
        color_continuous_scale='RdBu_r', # 색상 스케일 설정
        title='주요 변수 간 상관관계 히트맵'
    )
    st.plotly_chart(fig_heatmap, use_container_width=True)
