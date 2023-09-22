def process_data():
    import streamlit as st
    import pandas as pd
    import os

    st.markdown("# 📝 数据处理")
    
    tab1, tab2, tab3 = st.tabs(["Excel表格纵向合并分类求和", "Excel表格横向合并", "other"])

    with tab1:
        st.header("纵向合并分类求和")
        st.markdown(: red[请上传格式一致的表格,就是相同样式的表格,默认列标题在第一行即没有表头名称]

        def merge_excel_files_h(input_files, output_file, row_number):  # excel表格合并
            data = pd.read_excel(input_files[0], header=(row_number - 1))
            for file in input_files[1:]:
                new_data = pd.read_excel(file, header=(row_number - 1))
                data = pd.concat([data, new_data])
            data.to_excel(output_file, index=True)

        def create_new_excel_file(
            input_data, output_file, columns_groupby, columns_sum
        ):
            new_data = input_data.groupby(columns_groupby).agg({columns_sum: "sum"})
            new_data.to_excel(output_file, index=True)

        def download_file_h(file, name):
            with open(file, "rb") as f:
                st.download_button(
                    label=f"下载 {name}",
                    data=f,
                    file_name=f"{name}.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                )
                # mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

        # UI
        "### 上传Excel文件进行合并分类汇总"
        uploaded_files_h = st.file_uploader(
            "上传Excel文件", type=["xlsx", "xls"], accept_multiple_files=True
        )
        if uploaded_files_h:
            row_number1 = st.number_input("确定合并excel列名称所在的行", value=1)
            merged_file = "merged.xlsx"
            merge_excel_files_h(uploaded_files_h, merged_file, row_number1)  # 合并excel函数
            st.write("文件合并成功!")
            columns_to_groupby = st.multiselect(
                "选择分类的列名称", list(pd.read_excel(merged_file).columns)
            )
            columns_to_sum = st.selectbox(
                "选择求和列名称", list(pd.read_excel(merged_file).columns)
            )
            st.write({columns_to_sum})
            if columns_to_sum and columns_to_groupby:
                st.write("...进行分类合并...")
                summary_file = "summary.xlsx"
                new_file = "new_file.xlsx"
                create_new_excel_file(
                    pd.read_excel(merged_file),
                    new_file,
                    columns_to_groupby,
                    columns_to_sum,
                )
                st.write("分类合并完成！")
                download_file_h(new_file, "New Excel File")
                st.write("下载成功!")
            else:
                st.write("请选择分类列和计算列.")
        else:
            st.write("请上传Excel文件???.")

    with tab2:
        st.header("横向合并")
        st.markdown(: red[请上传格式一致的表格，就是相同样式的表格,默认列标题在第一行即没有表头名称]

        def merge_excel_files_h(input_files, output_file,row_number):
            data = pd.read_excel(input_files[0],header=(row_number - 1))
            columns_1 = st.selectbox("选择横向合并的连接列名称1", list(data.columns))
            columns_2 = st.selectbox("选择横向合并的连接列名称2", list(data.columns))

            for file in input_files[1:]:
                new_data = pd.read_excel(file)
                data = pd.merge(data, new_data, on=[columns_1, columns_2], how="outer")
            data.to_excel(output_file, index=True)

        def download_file_h(file, name):
            with open(file, "rb") as f:
                st.download_button(
                    label=f"下载 {name}",
                    data=f,
                    file_name=f"{name}.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                )
                # mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

        # UI
        "### 上传Excel文件进行横向合并分类汇总"
        uploaded_files_h = st.file_uploader(
            "上传Excel文件!", type=["xlsx", "xls"], accept_multiple_files=True
        )
        merged_file_h = "mergedA.xlsx"
        if uploaded_files_h:
            row_number2 = st.number_input("确定合并excel列名称所在的行", value=1)
            st.write("横向合并Excel文件...")
            merge_excel_files_h(uploaded_files_h, merged_file_h,row_number2)
            st.write("文件合并成功!")
            st.write(merged_file_h)
            st.write("合并完成！")
            download_file_h(merged_file_h, "Merged Excel File")
            st.write("下载成功!")

        else:
            st.write("请上传Excel文件???.")

    with tab3:
        st.header("other")


process_data()
