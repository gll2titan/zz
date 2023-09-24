def in_data():
    import streamlit as st
    from playwright.sync_api import sync_playwright
    import openpyxl

    st.markdown("# 💾 数据录入")
    st.markdown(":rainbow[目前不可用,请不要使用!] :balloon:")

    def in_data_m():
        # 读取上传的Excel文件
        uploaded_file = st.file_uploader("上传Excel文件", type="xlsx")

        if uploaded_file is not None:
            # 读取Excel文件内容
            workbook = openpyxl.load_workbook(uploaded_file)
            worksheet = workbook.active

            # 获取A1单元格的内容
            a1_value = worksheet["A1"].value

            # 启动Playwright控制浏览器
            with sync_playwright() as playwright:
                browser = playwright.chromium.launch(headless=True)
                context = browser.new_context()
                page = context.new_page()

                # 使用百度进行搜索a1单元格的内容
                page.goto("https://www.baidu.com/")
                page.click('input[name="wd"]')
                page.fill('input[name="wd"]', a1_value)
                page.click("text=百度一下")

                # 获取搜索结果
                search_result = page.inner_text("h3.t")

                # 显示搜索结果
                st.write("搜索结果：")
                st.write(search_result)

                # 关闭浏览器
                browser.close()

    in_data_m()


in_data()
