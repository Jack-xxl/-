import streamlit as st

# Title
st.title("天赋测试与职业规划助手")

# Introduction
st.write("欢迎使用天赋测试与职业规划助手！根据您的回答，我们将为您生成个性化的职业建议和发展路径。")

# Step 1: Personality Test
st.header("性格测试")
questions_personality = [
    "你喜欢独立工作而不是团队合作？",
    "你通常会基于直觉而非逻辑做决定？",
]
answers_personality = []
for q in questions_personality:
    answer = st.radio(q, ["非常同意", "同意", "中立", "不同意", "非常不同意"])
    answers_personality.append(answer)

# Step 2: Interest Test
st.header("兴趣测试")
questions_interest = [
    "你喜欢研究科学问题？",
    "你愿意帮助他人解决社会问题？",
]
answers_interest = []
for q in questions_interest:
    answer = st.radio(q, ["非常同意", "同意", "中立", "不同意", "非常不同意"])
    answers_interest.append(answer)

# Step 3: Ability Test
st.header("能力测试")
questions_ability = [
    "你擅长快速学习新工具或软件？",
    "你能清晰表达自己的想法并说服他人？",
]
answers_ability = []
for q in questions_ability:
    answer = st.radio(q, ["非常同意", "同意", "中立", "不同意", "非常不同意"])
    answers_ability.append(answer)

# Calculate Results
if st.button("提交测试"):
    st.success("测试完成！")
    st.write("根据您的回答，我们推荐以下职业方向：")
    st.write("- 人工智能工程师")
    st.write("- 心理咨询师")
    st.write("详细职业路径与学习建议将在完整版本中提供。")
