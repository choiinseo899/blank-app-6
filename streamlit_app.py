import streamlit as st
import pandas as pd
import pydeck as pdk
import plotly.express as px

# ========================
# 페이지 설정
# ========================
st.set_page_config(
    page_title="물러서는 땅, 다가오는 바다", 
    page_icon="🌊",
    layout="wide"
)

# ========================
# 제목 및 서론
# ========================
st.title("물러서는 땅, 다가오는 바다: 해수면 상승의 위험과 우리만의 대처법")
st.markdown("""
인류의 기술이 발전함과 동시에 세상은 황폐해져 가고 있습니다.  
기온 상승, 북극과 남극 빙하의 녹음, 해수면 상승 등으로 우리의 삶의 터전이 위협받고 있습니다.  
이 대시보드는 청소년들에게 해수면 상승의 위험성과 대처법을 알리고자 제작되었습니다.
""")

# ========================
# 본론 1: 해수면 상승 지도
# ========================
st.header("2050년 예상 해수면 상승 지도")

cities_data = pd.DataFrame({
    "도시": ["인천", "광주", "전주", "부산"],
    "위도": [37.456, 35.159, 35.821, 35.179],
    "경도": [126.705, 126.851, 127.147, 129.075],
    "해수면_위험": [70, 50, 30, 60]
})

layer = pdk.Layer(
    "ScatterplotLayer",
    data=cities_data,
    get_position='[경도, 위도]',
    get_radius='해수면_위험*1000',
    get_fill_color='[0, 0, 255, 140]',
    pickable=True
)

view_state = pdk.ViewState(
    latitude=36,
    longitude=127,
    zoom=6,
    pitch=0
)

r = pdk.Deck(
    layers=[layer],
    initial_view_state=view_state,
    tooltip={"text": "{도시}\n위험 수치: {해수면_위험}"}
)

st.pydeck_chart(r)

# ========================
# 본론 2: 설문 데이터 시각화
# ========================
st.header("청소년 해수면 인식 설문 결과")

survey_data = pd.DataFrame({
    "인식수준": ["낮음", "보통", "높음"],
    "인원수": [40, 30, 10]
})

fig = px.pie(
    survey_data,
    names="인식수준",
    values="인원수",
    title="청소년 인식 수준 비율",
    hole=0.3
)
fig.update_traces(textposition='inside', textinfo='percent+label')
st.plotly_chart(fig, use_container_width=True)

# ========================
# 결론 및 대처 방안
# ========================
st.header("대처 방안")
st.markdown("""
**온실가스 감축**  
- 화석 연료 사용 줄이기, 태양광·풍력 사용 확대  
- 에너지 효율 높은 제품 사용, 건물 단열 강화  

**해안 지역 적응 및 보호**  
- 방파제, 해안 방조제 건설  
- 자연 해안선 복원 (맹그로브 숲, 갯벌 등)  
- 연안 관리 계획 수립 및 안전한 이주 계획  

**개인 실천**  
- 에너지 절약, 자원 재활용  
- 환경 문제 관심과 참여
""")
