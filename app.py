TOPIC = “AI를 이용하여 과제를 제출해도 되는가?"
PRO_PROMPT = f"""너는 토론 대회의 찬성 측 토론자 '찬성봇' 이야. 토론 주제는 '{TOPIC}' 이야.
규칙 1. 항상 찬성 입장을 지킨다.
규칙 2. 상대가 말했다면 먼저 한 문장으로 반박하고, 그다음 새 근거를 하나 든다.
규칙 3. 존댓말로 3문장 이내로 말한다. 실제 통계 숫자를 지어내지 않는다."""
CON_PROMPT = ...                                  # 같은 모양 · '반대' 입장
pro_history = []    # 찬성봇의 기록
con_history = []    # 반대봇의 기록

def debate_turn(my_history, my_prompt, heard):
    send_list = my_history + [{"type": "user_input", "content": [{"type": "text", "text": heard}]}]
    reply = client.interactions.create(model=MODEL_NAME, store=False,
                                       system_instruction=my_prompt, input=send_list)
    my_history[:] = send_list + [step.model_dump() for step in reply.steps]
    return reply.output_text
