import streamlit as st

st.set_page_config(page_title="卡卡", page_icon="🦈")


def home():
    import streamlit as st

    st.write("# 欢迎你来到这里，我是卡卡")
    st.markdown(
        """
    你需要的就在这里，脱离繁杂的事务，把功夫用在到把上——————卡卡！
    ### 看看这里！
    - 县政府网站 [淳化县政府网站] （http://www.snchunhua.gov.cn/index.html）
    ### 点点这里？？？
    - 全国人大网站 [中国人大网] （http://www.npc.gov.cn/npc/index.html）

    """
    )


home()
