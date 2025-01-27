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
if "selected_questions" not in st.session_state:
    st.session_state.selected_questions = random.sample(quiz_data, 5)  # ランダムに5問を選択
    st.session_state.score = 0  # スコアの初期化
    st.session_state.answered = [False for _ in st.session_state.selected_questions]  # 各問題の回答状態を初期化

# 現在のスコア
st.title("麻雀牌クイズアプリ")
score = st.session_state.score

# クイズを表示
for i, data in enumerate(st.session_state.selected_questions, start=1):
    st.subheader(f"問題 {i}: {data['question']}")

    # 画像をローカルから読み込む
    try:
        img = Image.open(data["image"])
        st.image(img, caption="麻雀牌", use_container_width=True)
    except FileNotFoundError:
        st.error(f"画像が見つかりません: {data['image']}")
        continue

    # ユーザーの回答を入力
    user_answer = st.text_input(f"回答を入力してください（問題 {i}）", key=f"q{i}")

    # 正誤判定
    if not st.session_state.answered[i - 1]:  # まだ回答していない場合のみボタンを表示
        if st.button(f"問題 {i} の回答を確認", key=f"check{i}"):
            if user_answer.strip() == data["answer"]:
                st.success("正解です！")
                st.session_state.score += 1  # スコアを更新
            else:
                st.error(f"残念、不正解です。正解は「{data['answer']}」です。")
            st.session_state.answered[i - 1] = True  # 回答済みに設定
    else:
        st.info("この問題はすでに回答済みです。")

# 最終スコアを表示
if all(st.session_state.answered):  # 全問題が回答済みか確認
    st.write(f"あなたのスコアは {st.session_state.score}/{len(st.session_state.selected_questions)} です！")

# クイズを開始
start_quiz()
