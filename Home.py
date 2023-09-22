import streamlit as st
from streamlit_chat import message

import SparkApi


st.set_page_config(page_title="卡卡", page_icon="🦈")


st.write("# :rainbow[欢迎你来到这里，我是kaka]")
st.markdown("**你需要的就在这里，脱离繁杂的事务，把功夫用在到把上——————kaka！**")

# 以下密钥信息从控制台获取

appid = st.secrets["appid"]  # 填写控制台中获取的 APPID 信息
api_secret = st.secrets["api_secret"]  # 填写控制台中获取的 APISecret 信息
api_key = st.secrets["api_key"]  # 填写控制台中获取的 APIKey 信息

# 用于配置大模型版本，默认“general/generalv2”
# domain = "general"   # v1.5版本
domain = "generalv2"  # v2.0版本
# 云端环境的服务地址
# Spark_url = "ws://spark-api.xf-yun.com/v1.1/chat"  # v1.5环境的地址
Spark_url = "ws://spark-api.xf-yun.com/v2.1/chat"  # v2.0环境的地址

text = []  # 用于存储对话内容的列表

def getText(role, content):
    """
    构造包含角色和内容的对话信息，并添加到对话列表中
    
    参数：
    role (str): 对话角色，可以是 "user"（用户）或 "assistant"（助手）
    content (str): 对话内容
    
    返回值：
    text (list): 更新后的对话列表
    """
    jsoncon = {}
    jsoncon["role"] = role
    jsoncon["content"] = content
    text.append(jsoncon)
    return text

def getlength(text):
    """
    计算对话列表中所有对话内容的字符长度之和
    
    参数：
    text (list): 对话列表
    
    返回值：
    length (int): 对话内容的字符长度之和
    """
    length = 0
    for content in text:
        temp = content["content"]
        leng = len(temp)
        length += leng
    return length

def checklen(text):
    """
    检查对话列表中的对话内容字符长度是否超过限制（8000个字符）
    如果超过限制，删除最早的对话内容，直到满足字符长度限制
    
    参数：
    text (list): 对话列表
    
    返回值：
    text (list): 更新后满足字符长度限制的对话列表
    """
    while getlength(text) > 8000:
        del text[0]
    return text

if __name__ == '__main__':
    # 在 Streamlit 网页上显示欢迎文本
    
    st.markdown(":rat: :ox: :tiger2: :rabbit2: :dragon: :snake: :racehorse: :goat: :monkey: :rooster: :dog2: :pig2:")
    
    # 初始化对话历史和生成的响应列表
    if 'generated' not in st.session_state:
        st.session_state['generated'] = []
    if 'past' not in st.session_state:
        st.session_state['past'] = []
    
    # 获取用户输入的问题
    user_input = st.text_input("请输入您的问题:", key='input')
    
    if user_input:
        # 构造用户输入的对话信息
        question = checklen(getText("user", user_input))
        
        # 调用 SparkApi 中的函数进行问题回答
        SparkApi.answer = ""
        print("星火:", end="")
        SparkApi.main(appid, api_key, api_secret, Spark_url, domain, question)
        output = getText("assistant", SparkApi.answer)
        
        # 将用户输入和生成的响应添加到对话历史和生成的响应列表中
        st.session_state['past'].append(user_input)
        st.session_state['generated'].append(str(output[1]['content']))
        
    if st.session_state['generated']:
        # 在网页上显示对话历史和生成的响应
        for i in range(len(st.session_state['generated']) - 1, -1, -1):
            message(st.session_state["generated"][i], key=str(i))
            message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')

#main()

st.markdown(
    """
    - 淳化县政府网站 http://www.snchunhua.gov.cn/index.html
    
    - 中国人大网 http://www.npc.gov.cn/npc/index.html
    """
    )
