#!/usr/bin/env python
# coding: utf-8

# ## **데이터 분석 실습: 목적 중심 분석 프레임워크**
# 
# ### **🎯 실습 개요**
# 
# 실제 산업 현장의 문제를 데이터로 해결하는 전 과정을 경험합니다.
# 
# **"무엇을 위해 분석하는가?"** 에서 시작하여 **"현장에서 어떻게 활용할 것인가?"** 까지 체계적으로 접근합니다.
# 
# **핵심 철학**: 완벽한 모델보다는 실무에서 바로 활용 가능한 명확한 인사이트 도출
# 
# ---
# 
# ### **STEP 1: 미션 선택 및 비즈니스 상황 이해**
# 
# #### **📊 미션 선택**
# 
# 두 개의 현실적인 비즈니스 상황 중 하나를 선택하여 진행합니다.
# 
# **🚜 Mission A: 건설장비 예지보전 시스템**
# 
# 상황: 대형 건설회사의 장비관리팀장으로서 굴삭기, 불도저 등 핵심 장비의 갑작스러운 고장으로 인한 공사 지연과 막대한 손실을 해결해야 합니다.
# 
# 현재 문제점:
# 
# - 월평균 3-4건의 예상치 못한 장비 고장으로 공사 중단
# - 건당 평균 2억원의 손실 (수리비 + 공사지연비)
# - 과도한 예방정비로 인한 불필요한 비용 발생
# 
# **데이터: 1,000개 건설장비 부품의 센서 데이터 및 잔여 수명 정보**
# 
# **⚙️ Mission B: 제조장비 이상탐지 시스템**
# 
# 상황: 자동화 제조라인을 운영하는 생산관리자로서 장비 고장으로 인한 생산 중단을 최소화하여 납기를 맞추고 품질을 유지해야 합니다.
# 
# 현재 문제점:
# 
# - 주요 생산라인 1일 중단 시 약 5억원의 생산 손실
# - 장비 고장으로 인한 제품 품질 불량률 증가
# - 긴급 수리 시 정상 수리 대비 3배의 비용 발생
# 
# **데이터: 7,672개 제조장비의 센서 데이터 및 고장 여부 정보**

# In[ ]:





# In[ ]:





# In[ ]:





# ---

# ### **STEP 2: 데이터 탐색 및 분석 목표 설정**
# 
# #### **2-1. 데이터 전체 구조 파악**
# 
# - 선택한 미션의 데이터 파일 로드
# - 기본 정보 확인 (행/열 수, 변수 타입, 결측값 등)
# - 각 변수의 의미 그리고 변수의 값 범위에 대한 이해

# In[2]:


import pandas as pd

# 데이터 불러오기
df = pd.read_csv("construction_machine_data.csv")

# 1. 데이터의 행과 열 수 확인
print("데이터 크기(행, 열):", df.shape)

# 2. 변수 타입 확인
print("\n각 변수의 타입:")
print(df.dtypes)

# 3. 결측값(비어있는 값) 확인
print("\n결측값 개수:")
print(df.isnull().sum())

# 4. 데이터 프레임 상위 5개 행 미리보기
print("\n데이터 샘플:")
print(df.head())

# 5. 각 변수(컬럼)별 기초 통계(숫자 변수만)
print("\n기초 통계 정보:")
print(df.describe())


# In[ ]:





# In[ ]:





# ---

# #### **2-2. 예측 대상(Y변수) 결정**
# 
# **데이터를 실제로 확인한 후 결정:**
# 
# Mission A 예시:
# 
# - Remaining_Useful_Life(잔존 수명) 자체를 예측
# 
# Mission B 예시:
# 
# - faulty(정상/비정상 유무) 변수 활용한 고장/정상 분류

# In[5]:


import pandas as pd

# 데이터 불러오기
df = pd.read_csv("construction_machine_data.csv")

# 전체 구조 확인
print("데이터 크기(행, 열):", df.shape)


# In[6]:


print("컬럼 이름:", df.columns.tolist())
print("컬럼 데이터 타입:\n", df.dtypes)
print("\n상위 5개 데이터 샘플:\n", df.head())


# In[7]:


print("컬럼별 결측값 개수:\n", df.isnull().sum())


# ----

# ### **STEP 3: 데이터 현황 파악**
# 
# #### **3-1. 예측 대상 변수(Y) 특성 분석**
# 
# **분포와 패턴 파악:**
# 
# - 예측 대상의 분포가 어떻게 되어 있는가? [예측 대상이 잔존 수명으로 구성되는 경우]
#     - 이상값이나 특이한 패턴이 있는가?
# - 예측 대상 그룹별로 차이가 있는가? [예측 대상이 정상/비정상 유무로 구성되는 경우]

# In[11]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

plt.rcParams["axes.unicode_minus"] = False
plt.rc("font", family = "NanumBarunGothic")

# 데이터 불러오기
# df = pd.read_csv("construction_machine_data.csv") # 이전에 이미 실행되었습니다.

plt.figure(figsize=(8,5))

# 오류가 발생한 'RUL'을 실제 컬럼명 'Remaining_Useful_Life'로 수정합니다.
plt.hist(df['Remaining_Useful_Life'], bins=30, color='skyblue', edgecolor='black')

plt.title('잔존 수명(Remaining Useful Life) 분포')
plt.xlabel('잔존 수명(Days)')
plt.ylabel('부품 개수')
plt.show()


# In[ ]:





# In[ ]:





# ---

# 
# #### **3-2. 설명 변수(X)들의 특성 분석**
# 
# **X변수의 의미 해석 예시:**
# 
# - 변수의 범위는 어느 정도인가?
#     - 변수의 범위가 타당한 값 안에 분포되어 있는가? (ex. 타당하지 않는 범위 = 사람의 나이는 0세에서 100세인데, 값은 -20세에서 200세로 분포되어 있음)
# - 변수가 어느 정도로 퍼져있는가?
#     - 심각하게 퍼져있는가? 아니면 하나의 값 주위로 몰려있는가?
# - 변수에서 이상값이 나타나는가?
#     - 변수가 이상값인 경우 다른 변수들의 분포에서 특이 패턴이 보이는가?
# - 변수들 간 연관성이 있어 보이는가?

# In[12]:


import matplotlib.pyplot as plt
import seaborn as sns

# 분석할 숫자형 변수 리스트
numeric_cols = ['Vibration', 'Temperature', 'Pressure', 'Operating_Hours']

# 박스플롯(Boxplot)으로 이상값 확인
plt.figure(figsize=(15, 4))
for i, col in enumerate(numeric_cols):
  plt.subplot(1, len(numeric_cols), i+1)
  sns.boxplot(y=df[col], color='skyblue')
  plt.title(col)
plt.tight_layout()
plt.show()


# In[13]:


# 숫자형 변수들 간의 상관관계 행렬 계산
corr_matrix = df[numeric_cols].corr()

# 히트맵으로 시각화
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap of Sensor Data')
plt.show()


# In[ ]:





# ----

# ### **STEP 4: 현장 기반 가설 수립**
# 
# #### **4-1. 업무 경험 기반 가설**
# 
# 상식적이고 논리적인 가설들을 세워보세요:
# 
# 공통적인 가설 방향:
# 
# - 시간 요인: 사용 시간이 많을수록 문제 발생 확률 증가
# - 환경 요인: 극한 조건(고온, 고압 등)에서 위험 증가
# - 장비 특성: 특정 타입이나 위치에서 문제 빈발
# - 복합 요인: 여러 조건이 동시에 발생할 때 위험 급증
# 
# 구체적 가설 예시:
# 
# - "온도가 평상시보다 20% 이상 높으면 고장 위험 증가"
# - "진동과 압력이 동시에 상승하면 즉시 점검 필요"
# - "특정 제조사 장비가 다른 장비보다 고장률 높음"
# 
# #### **4-2. 복합 상황 가설**
# 
# 여러 요인이 결합된 상황에 대한 가설:
# 
# - 어떤 조건들이 함께 나타날 때 가장 위험한가?
# - 특정 그룹에서만 나타나는 패턴이 있을 것인가?
# 
# #### **4-3. 검증 우선순위 설정**
# 
# 가설들을 다음 기준으로 우선순위 매기기:
# 
# - 비즈니스 임팩트 크기
# - 검증 난이도

# In[ ]:





# In[ ]:





# In[ ]:





# ----

# ### **STEP 5: 가설 검증을 위한 시각화 탐색**
# 
# #### **5-1. 예측 대상 변수 이해하기**
# 
# 우리가 예측하려는 것부터 파악:
# 
# - Y변수의 분포는 어떻게 생겼는가?
# - 어떤 값들이 많고, 어떤 값들이 적은가?
# - 이상하거나 특별한 패턴이 보이는가?
# 
# 간단한 질문들:
# 
# - Mission A: 수명이 짧은 부품과 긴 부품의 비율은?
# - Mission B: 정상과 고장의 비율은 얼마나 될까?

# In[14]:


import matplotlib.pyplot as plt
import pandas as pd

# 이전에 데이터를 로드했지만, 명확성을 위해 다시 로드합니다.
# 실제 노트북 환경에서는 이전에 로드한 df 변수를 그대로 사용하면 됩니다.
df = pd.read_csv("construction_machine_data.csv")

plt.figure(figsize=(10, 6))
plt.hist(df['Remaining_Useful_Life'], bins=50, color='skyblue', edgecolor='black')
plt.title('Distribution of Remaining Useful Life (RUL)')
plt.xlabel('Remaining Useful Life (Days)')
plt.ylabel('Number of Components')
plt.grid(axis='y', alpha=0.75)
plt.show()


# In[16]:


# 이전에 df와 median_rul은 이미 정의되었습니다.

# 중앙값을 기준으로 비율 계산 (오타 수정)
short_life_count = df[df['Remaining_Useful_Life'] <= median_rul].shape[0]
long_life_count = df[df['Remaining_Useful_Life'] > median_rul].shape[0]

total_count = df.shape[0]

# 결과 출력
print(f"잔존 수명의 중앙값: {median_rul}일")
print(f"---")
print(f"수명이 짧은 부품 (중앙값 이하): {short_life_count}개 (비율: {(short_life_count/total_count):.2%})")
print(f"수명이 긴 부품 (중앙값 초과):  {long_life_count}개 (비율: {(long_life_count/total_count):.2%})")



# In[ ]:





# ----

# #### **5-2. 한 번에 하나씩, 관계 찾아보기**
# 
# **각 센서값이 결과에 어떤 영향을 주는지 하나씩 확인:**
# 
# **연속형 변수들 (온도, 압력, 진동 등):**
# 
# 산점도 그려보기: X축에 센서값, Y축에 예측대상
# 
# "값이 높아질수록 위험해지나?" "특정 구간에서 급변하나?"
# 
# **범주형 변수들 (장비타입, 위치 등):**
# 
# 그룹별 박스플롯 그리기
# "어떤 타입이 가장 위험한가?" "위치별로 차이가 있나?"
# 
# 핵심은 패턴 발견:
# 
# - 명확한 관계가 보이는 변수는?
# - 관계가 없어 보이는 변수는?
# - 예상과 다른 결과가 나온 변수는?

# In[17]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# 데이터가 로드된 df 변수가 있다고 가정합니다.
# df = pd.read_csv("construction_machine_data.csv")

# 분석할 연속형 변수 리스트
numeric_cols = ['Operating_Hours', 'Vibration', 'Temperature', 'Pressure']
target_col = 'Remaining_Useful_Life'

# 각 변수별 산점도 그리기
for col in numeric_cols:
    plt.figure(figsize=(8, 5))
    sns.scatterplot(x=df[col], y=df[target_col], alpha=0.5)
    plt.title(f'Relationship between {col} and RUL', fontsize=15)
    plt.xlabel(col, fontsize=12)
    plt.ylabel('Remaining Useful Life (Days)', fontsize=12)
    plt.grid(True)
    plt.show()


# In[18]:


plt.figure(figsize=(10, 7))
sns.boxplot(x='Component_Type', y='Remaining_Useful_Life', data=df)
plt.title('RUL Distribution by Component Type', fontsize=15)
plt.xlabel('Component Type', fontsize=12)
plt.ylabel('Remaining Useful Life (Days)', fontsize=12)
plt.xticks(rotation=15)
plt.show()


# In[19]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# 데이터가 로드된 df 변수가 있다고 가정합니다.
# df = pd.read_csv("construction_machine_data.csv")

plt.figure(figsize=(12, 8))

# 다차원 산점도 그리기
sns.scatterplot(
    data=df,
    x='Temperature',
    y='Vibration',
    hue='Component_Type',  # 색상으로 부품 종류 구분
    size='Remaining_Useful_Life',  # 크기로 잔존 수명 표현
    sizes=(20, 250),  # 점 크기 범위
    alpha=0.7,  # 투명도
    palette='viridis'  # 색상 팔레트
)

plt.title('Temperature vs. Vibration Analysis (Dot size indicates RUL)', fontsize=16)
plt.xlabel('Temperature (°C)', fontsize=12)
plt.ylabel('Vibration (mm/s)', fontsize=12)
plt.legend(title='Component & RUL', bbox_to_anchor=(1.02, 1), loc='upper left')
plt.grid(True)
plt.show()


# 
# ------

# 
# #### **5-3. 2개 변수 조합으로 새로운 발견**
# 
# 가장 중요해 보이는 변수 2개를 골라서:
# 
# 색깔로 구분된 산점도 만들기
# 
# - "온도가 높으면서 동시에 진동도 클 때는?"
# - "특정 장비에서만 나타나는 특별한 패턴이 있나?"
# 
# 찾아볼 것들:
# 
# - 단독으로는 안 보이던 패턴이 조합에서 나타나는가?
# - 위험한 조합과 안전한 조합을 구분할 수 있는가?

# In[20]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# 데이터가 로드된 df 변수가 있다고 가정합니다.
# df = pd.read_csv("construction_machine_data.csv")

plt.figure(figsize=(12, 8))

# 다차원 산점도 그리기
sns.scatterplot(
    data=df,
    x='Temperature',
    y='Vibration',
    hue='Component_Type',          # 색상: 부품 종류
    size='Remaining_Useful_Life',  # 크기: 잔존 수명
    sizes=(20, 250),               # 점 크기 범위 (작은점 ~ 큰점)
    alpha=0.7,
    palette='viridis'
)

plt.title('Temperature vs. Vibration Analysis (Dot size indicates RUL)', fontsize=16)
plt.xlabel('Temperature (°C)', fontsize=12)
plt.ylabel('Vibration (mm/s)', fontsize=12)
plt.legend(title='Component & RUL', bbox_to_anchor=(1.02, 1), loc='upper left')
plt.grid(True)
plt.show()


# In[ ]:





# In[ ]:





# ---

# ### **STEP 6: 분석하면서 알게 된 것들 정리**
# 
# #### **6-1. 눈에 띄는 특징들**
# 
# 그래프를 보면서 발견한 것들:
# 
# - 생각했던 대로 나온 것들
# - 예상과 다르게 나온 것들
# - 처음 알게 된 것들
# - 특별히 인상 깊었던 것들
# 
# 예시:
# 
# - "온도가 80도 넘으면 고장이 많이 남"
# - "A타입 장비가 B타입보다 고장률이 2배 높음"
# - "진동 수치가 7 이상일 때 위험함"
# 
# #### **6-2. 처음에 생각했던 것과 비교**
# 
# 내 예상과 실제 데이터 비교:
# 
# - 맞았던 예상들
# - 틀렸던 예상들
# - 반반 맞은 것들
# 
# #### **6-3. 어떤 요소가 가장 중요한지**
# 
# Y변수에 영향을 주는 요소들 순위 매기기:
# 
# - 1등: 가장 큰 영향을 주는 변수
# - 2등, 3등: 그 다음으로 중요한 변수들
# - 생각보다 별로 중요하지 않은 변수들
# 
# 판단 기준:
# 
# - 그래프에서 관계가 뚜렷하게 보이는가?

# In[ ]:





# In[ ]:





# In[ ]:





# --------

# # **프로젝트 결과 제출**
# 데이터 분석 결과를 Streamlit 기반으로 구현한 웹 앱 최종 결과물을 제출해봅시다.
# 
# Stream Cloud에 배포한 웹 애플리케이션 URL (https://{이름}.streamlit.app/ 형태)
# 
# ---

# **Stream Cloud에 배포한 URL**
# 
# **링크:** 

# 
# ---
