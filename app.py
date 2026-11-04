# 🧪 [실습 2-2] Colab 안에서 용어 하나 물어보기 (요청 1번)
app_test = open_app()
app_test.text_input[0].input("API").run()
app_test.button[0].click().run()               # [설명 듣기] → 이때 Gemini 요청이 나감
print(app_test.error[0].value if app_test.error else app_test.markdown[-1].value)
