import streamlit as st

st.set_page_config(page_title="卡卡", page_icon="🦈")


def home():
    import streamlit as st

    st.write("# :rainbow[欢迎你来到这里，我是kaka]")
    st.markdown(
        """
    **你需要的就在这里，脱离繁杂的事务，把功夫用在到把上——————kaka！**

    - 淳化县政府网站 http://www.snchunhua.gov.cn/index.html
    
    - 中国人大网 http://www.npc.gov.cn/npc/index.html
    """
    )


home()
