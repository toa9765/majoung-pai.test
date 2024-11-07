pip install matplotlib pillow
import os
import random
from PIL import Image
import matplotlib.pyplot as plt

# クイズの問題と対応する画像のパスを辞書に格納
quiz_data = [
    {"image": "https://github.com/toa9765/majoung-pai.test/blob/main/1man.jpeg", "question": "この牌の名前は何ですか？", "answer": "イーマン"},
    {"image": "https://github.com/toa9765/majoung-pai.test/blob/main/1p.jpeg", "question": "この牌の名前は何ですか？", "answer": "イーピン"},
    {"image": "https://github.com/toa9765/majoung-pai.test/blob/main/1s.jpeg", "question": "この牌の名前は何ですか？", "answer": "イーソー"},
    {"image": "https://github.com/toa9765/majoung-pai.test/blob/main/2man.jpeg", "question": "この牌の名前は何ですか？", "answer": "リャンマン"},
    {"image": "https://github.com/toa9765/majoung-pai.test/blob/main/2p.jpeg", "question": "この牌の名前は何ですか？", "answer": "リャンピン"},
    {"image": "https://github.com/toa9765/majoung-pai.test/blob/main/2s.jpeg", "question": "この牌の名前は何ですか？", "answer": "リャンゾー"},
    {"image": "https://github.com/toa9765/majoung-pai.test/blob/main/3man.jpeg", "question": "この牌の名前は何ですか？", "answer": "サンマン"},
    {"image": "https://github.com/toa9765/majoung-pai.test/blob/main/3p.jpeg", "question": "この牌の名前は何ですか？", "answer": "サンピン"},
    {"image": "https://github.com/toa9765/majoung-pai.test/blob/main/3s.jpeg", "question": "この牌の名前は何ですか？", "answer": "サンソー"},
    {"image": "https://github.com/toa9765/majoung-pai.test/blob/main/4man.jpeg", "question": "この牌の名前は何ですか？", "answer": "スーマン"},
    {"image": "https://github.com/toa9765/majoung-pai.test/blob/main/4p.jpeg", "question": "この牌の名前は何ですか？", "answer": "スーピン"},
    {"image": "https://github.com/toa9765/majoung-pai.test/blob/main/4s.jpeg", "question": "この牌の名前は何ですか？", "answer": "スーソー"},
    {"image": "https://github.com/toa9765/majoung-pai.test/blob/main/5man.jpeg", "question": "この牌の名前は何ですか？", "answer": "ウーマン"},
    {"image": "https://github.com/toa9765/majoung-pai.test/blob/main/5p.jpeg", "question": "この牌の名前は何ですか？", "answer": "ウーピン"},
    {"image": "https://github.com/toa9765/majoung-pai.test/blob/main/5s.jpeg", "question": "この牌の名前は何ですか？", "answer": "ウーソー"},
    {"image": "https://github.com/toa9765/majoung-pai.test/blob/main/6man.jpeg", "question": "この牌の名前は何ですか？", "answer": "ローマン"},
    {"image": "https://github.com/toa9765/majoung-pai.test/blob/main/6p.jpeg", "question": "この牌の名前は何ですか？", "answer": "ローピン"},
    {"image": "https://github.com/toa9765/majoung-pai.test/blob/main/6s.jpeg", "question": "この牌の名前は何ですか？", "answer": "ローソー"},
    {"image": "https://github.com/toa9765/majoung-pai.test/blob/main/7man.jpeg", "question": "この牌の名前は何ですか？", "answer": "チーマン"},
    {"image": "https://github.com/toa9765/majoung-pai.test/blob/main/7p.jpeg", "question": "この牌の名前は何ですか？", "answer": "チーピン"},
    {"image": "https://github.com/toa9765/majoung-pai.test/blob/main/7s.jpeg", "question": "この牌の名前は何ですか？", "answer": "チーソー"},
    {"image": "https://github.com/toa9765/majoung-pai.test/blob/main/8man.jpeg", "question": "この牌の名前は何ですか？", "answer": "パーマン"},
    {"image": "https://github.com/toa9765/majoung-pai.test/blob/main/8p.jpeg", "question": "この牌の名前は何ですか？", "answer": "パーピン"},
    {"image": "https://github.com/toa9765/majoung-pai.test/blob/main/8s.jpeg", "question": "この牌の名前は何ですか？", "answer": "パーソー"},
    {"image": "https://github.com/toa9765/majoung-pai.test/blob/main/9man.jpeg", "question": "この牌の名前は何ですか？", "answer": "キュウマン"},
    {"image": "https://github.com/toa9765/majoung-pai.test/blob/main/9p.jpeg", "question": "この牌の名前は何ですか？", "answer": "キュウピン"},
    {"image": "https://github.com/toa9765/majoung-pai.test/blob/main/9s.jpeg", "question": "この牌の名前は何ですか？", "answer": "キュウソー"}
    
    
]

# クイズを開始する関数
def start_quiz():
    print("クイズを開始します！")
    
    # ユーザーに出題する問題数を入力させる
    total_questions = len(quiz_data)
    while True:
        try:
            num_questions = int(input(f"出題する問題数を入力してください（最大 {total_questions} 問）："))
            if 1 <= num_questions <= total_questions:
                break
            else:
                print(f"1 から {total_questions} の範囲で入力してください。")
        except ValueError:
            print("数値を入力してください。")

    # スコアの初期化と問題をランダムに選択
    score = 0
    selected_questions = random.sample(quiz_data, num_questions)  # ランダムに指定された数だけ選ぶ

    # 各問題を表示
    for i, data in enumerate(selected_questions, start=1):
        # 画像を読み込み
        img = Image.open(data["image"])

        # Matplotlibで画像を表示
        plt.imshow(img)
        plt.axis('off')  # 軸を非表示
        plt.show()

        # 問題文を表示し、ユーザーに回答を求める
        print(f"\n問題 {i}: {data['question']}")
        user_answer = input("あなたの答え: ")

        # 答えを判定
        if user_answer.strip() == data["answer"]:
            print("正解です！")
            score += 1
        else:
            print(f"残念、不正解です。正解は {data['answer']} です。")

    # 最終スコアを表示
    print(f"\nクイズ終了！あなたのスコアは {score}/{num_questions} です。")

# クイズを開始
start_quiz()
