import streamlit as st
from openai import OpenAI

API_KEY = "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"

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=API_KEY,
)

def gpt_request(user_content, LL_MODEL="deepseek/deepseek-chat-v3-0324:free"):
    system_content = 'Определели семантику текста. Ответь одним словом: "положительно", "отрицательно" или "нейтрально".'
    messages = []
    messages.append({"role": "system", "content": system_content})
    messages.append({"role": "user", "content": user_content})

    response = client.chat.completions.create(
        model=LL_MODEL,
        messages=messages,
        temperature=0
    )
    return response.choices[0].message.content

# Интерфейс Streamlit
st.title("Определение семантики текста")

user_input = st.text_area("Введите текст", height=200)
if st.button("Отправить"):
    if not API_KEY:
        st.error("Пожалуйста, укажи API-ключ.")
    elif not user_input.strip():
        st.warning("Введите текст для отправки.")
    else:
        try:
            reply = gpt_request(user_input)
            st.success("Ответ от модели:")
            st.markdown(reply)
        except Exception as e:
            st.error(f"Ошибка: {e}")
