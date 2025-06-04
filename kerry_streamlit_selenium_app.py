
    import streamlit as st
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    import time

    def setup_driver():
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        return webdriver.Chrome(options=chrome_options)

    def query_kerry_status(tracking_number):
        try:
            driver = setup_driver()
            driver.get("https://www.kerrytj.com/zh/checking")

            input_box = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "txtTrackNo"))
            )
            input_box.clear()
            input_box.send_keys(tracking_number)

            submit_button = driver.find_element(By.ID, "btnSearch")
            submit_button.click()

            # 等待結果出現
            status_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".tracking .table"))
            )

            table_text = status_element.text
            driver.quit()
            return table_text.strip()

        except Exception as e:
            driver.quit()
            return f"❌ 查詢失敗（{tracking_number}）：{e}"

    st.set_page_config(page_title="Kerry 大榮物流真實查詢", layout="centered")
    st.title("🚚 Kerry 大榮物流真實查詢工具")
    st.markdown("請輸入多筆物流單號（每行一筆），我會幫你查詢實際配送狀態。")

    input_text = st.text_area("輸入物流單號", height=200)

    if st.button("開始查詢"):
        if input_text.strip():
            tracking_numbers = [line.strip() for line in input_text.splitlines() if line.strip()]
            st.subheader("📦 查詢結果")
            for num in tracking_numbers:
                with st.spinner(f"查詢中：{num}"):
                    result = query_kerry_status(num)
                    st.markdown(f"**{num}**：
```
{result}
```")
        else:
            st.warning("請至少輸入一筆單號")
