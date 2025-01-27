import streamlit as at
import random
from PIL import Image

# クイズの問題と対応する画像のパスを辞書に格納
quiz_data = [
    {"image": "1man.jpeg", "question": "この牌の名前は何ですか？", "answer": "イーマン"},
    {"image": "1p.jpeg", "question": "この牌の名前は何ですか？", "answer": "イーピン"},
    {"image": "1s.jpeg", "question": "この牌の名前は何ですか？", "answer": "イーソー"},
    {"image": "2man.jpeg", "question": "この牌の名前は何ですか？", "answer": "リャンマン"},
    {"image": "2p.jpeg", "question": "この牌の名前は何ですか？", "answer": "リャンピン"},
    {"image": "2s.jpeg", "question": "この牌の名前は何ですか？", "answer": "リャンゾー"},
    {"image": "3man.jpeg", "question": "この牌の名前は何ですか？", "answer": "サンマン"},
    {"image": "3p.jpeg", "question": "この牌の名前は何ですか？", "answer": "サンピン"},
    {"image": "3s.jpeg", "question": "この牌の名前は何ですか？", "answer": "サンソー"},
    {"image": "4man.jpeg", "question": "この牌の名前は何ですか？", "answer": "スーマン"},
    {"image": "4p.jpeg", "question": "この牌の名前は何ですか？", "answer": "スーピン"},
    {"image": "4s.jpeg", "question": "この牌の名前は何ですか？", "answer": "スーソー"},
    {"image": "5man.jpeg", "question": "この牌の名前は何ですか？", "answer": "ウーマン"},
    {"image": "5p.jpeg", "question": "この牌の名前は何ですか？", "answer": "ウーピン"},
    {"image": "5s.jpeg", "question": "この牌の名前は何ですか？", "answer": "ウーソー"},
    {"image": "6man.jpeg", "question": "この牌の名前は何ですか？", "answer": "ローマン"},
    {"image": "6p.jpeg", "question": "この牌の名前は何ですか？", "answer": "ローピン"},
    {"image": "6s.jpeg", "question": "この牌の名前は何ですか？", "answer": "ローソー"},
    {"image": "7man.jpeg", "question": "この牌の名前は何ですか？", "answer": "チーマン"},
    {"image": "7p.jpeg", "question": "この牌の名前は何ですか？", "answer": "チーピン"},
    {"image": "7s.jpeg", "question": "この牌の名前は何ですか？", "answer": "チーソー"},
    {"image": "8man.jpeg", "question": "この牌の名前は何ですか？", "answer": "パーマン"},
    {"image": "8p.jpeg", "question": "この牌の名前は何ですか？", "answer": "パーピン"},
    {"image": "8s.jpeg", "question": "この牌の名前は何ですか？", "answer": "パーソー"},
    {"image": "9man.jpeg", "question": "この牌の名前は何ですか？", "answer": "キュウマン"},
    {"image": "9p.jpeg", "question": "この牌の名前は何ですか？", "answer": "キュウピン"},
    {"image": "9s.jpeg", "question": "この牌の名前は何ですか？", "answer": "キュウソー"}
    
    
]

# 初回実行時にセッション状態を初期化
if "current_question" not in st.session_state:
    st.session_state.current_question = 0  # 現在の質問インデックス
    st.session_state.score = 0  # スコアの初期化
    st.session_state.selected_questions = random.sample(quiz_data, 5)  # ランダムに5問を選択
    st.session_state.answers = []  # ユーザーの回答記録

# タイトル
st.title("麻雀牌クイズアプリ")

# 進捗バー
total_questions = len(st.session_state.selected_questions)
current_question = st.session_state.current_question
st.progress((current_question / total_questions))

# クイズを表示
if current_question < total_questions:
    question_data = st.session_state.selected_questions[current_question]
    st.subheader(f"問題 {current_question + 1}: {question_data['question']}")

    # 画像を表示
    try:
        img = Image.open(question_data["image"])
        st.image(img, caption="麻雀牌", use_container_width=True)
    except FileNotFoundError:
        st.error(f"画像が見つかりません: {question_data['image']}")

    # ユーザーの回答を入力
    user_answer = st.text_input("回答を入力してください：", key=f"answer_{current_question}")

    # 次へ進むボタン
    if st.button("次へ進む"):
        st.session_state.answers.append(user_answer.strip())  # 回答を保存
        if user_answer.strip() == question_data["answer"]:
            st.session_state.score += 1
        st.session_state.current_question += 1  # 次の質問へ
else:
    # クイズ終了画面
    st.subheader("クイズ終了！")
    st.write(f"あなたのスコアは {st.session_state.score}/{total_questions} です！")

    # スコアの詳細表示
    for i, question_data in enumerate(st.session_state.selected_questions):
        correct = "✅" if st.session_state.answers[i] == question_data["answer"] else "❌"
        st.write(f"問題 {i + 1}: {question_data['question']} ({correct})")
        st.write(f"あなたの回答: {st.session_state.answers[i]}")
        st.write(f"正解: {question_data['answer']}")
        st.write("---")

    # リスタートボタン
    if st.button("もう一度プレイ"):
        del st.session_state.current_question
        del st.session_state.score
        del st.session_state.selected_questions
        del st.session_state.answers
