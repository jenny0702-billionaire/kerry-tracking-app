
import streamlit as st

st.set_page_config(page_title="Kerry 大榮多筆物流查詢", layout="centered")

st.title("🚚 Kerry 大榮物流單查詢工具")
st.markdown("請在下方輸入多筆物流單號，每行一筆，按下查詢即可獲得模擬查詢結果。")

input_text = st.text_area("輸入物流單號（每行一筆）", height=200)

def query_kerry_tracking(number):
    # 模擬查詢回傳
    return f"✅ 模擬查詢成功（單號：{number}）"

if st.button("查詢物流狀態"):
    if input_text.strip():
        tracking_numbers = [line.strip() for line in input_text.strip().splitlines() if line.strip()]
        st.subheader("📦 查詢結果")
        for num in tracking_numbers:
            result = query_kerry_tracking(num)
            st.markdown(f"- **{num}**：{result}")
    else:
        st.warning("請輸入至少一筆物流單號")
