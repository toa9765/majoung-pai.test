import os
import random
from PIL import Image
import matplotlib.pyplot as plt

# クイズの問題と対応する画像のパスを辞書に格納
quiz_data = [
    {"image": "/content/1man.jpeg", "question": "この牌の名前は何ですか？", "answer": "イーマン"},
    {"image": "/content/1p.jpeg", "question": "この牌の名前は何ですか？", "answer": "イーピン"},
    {"image": "/content/1s.jpeg", "question": "この牌の名前は何ですか？", "answer": "イーソー"},
    {"image": "/content/2man.jpeg", "question": "この牌の名前は何ですか？", "answer": "リャンマン"},
    {"image": "/content/2p.jpeg", "question": "この牌の名前は何ですか？", "answer": "リャンピン"},
    {"image": "/content/2s.jpeg", "question": "この牌の名前は何ですか？", "answer": "リャンゾー"},
    {"image": "/content/3man.jpeg", "question": "この牌の名前は何ですか？", "answer": "サンマン"},
    {"image": "/content/3p.jpeg", "question": "この牌の名前は何ですか？", "answer": "サンピン"},
    {"image": "/content/3s.jpeg", "question": "この牌の名前は何ですか？", "answer": "サンソー"},
    {"image": "/content/4man.jpeg", "question": "この牌の名前は何ですか？", "answer": "スーマン"},
    {"image": "/content/4p.jpeg", "question": "この牌の名前は何ですか？", "answer": "スーピン"},
    {"image": "/content/4s.jpeg", "question": "この牌の名前は何ですか？", "answer": "スーソー"},
    {"image": "/content/5man.jpeg", "question": "この牌の名前は何ですか？", "answer": "ウーマン"},
    {"image": "/content/5p.jpeg", "question": "この牌の名前は何ですか？", "answer": "ウーピン"},
    {"image": "/content/5s.jpeg", "question": "この牌の名前は何ですか？", "answer": "ウーソー"},
    {"image": "/content/6man.jpeg", "question": "この牌の名前は何ですか？", "answer": "ローマン"},
    {"image": "/content/6p.jpeg", "question": "この牌の名前は何ですか？", "answer": "ローピン"},
    {"image": "/content/6s.jpeg", "question": "この牌の名前は何ですか？", "answer": "ローソー"},
    {"image": "/content/7man.jpeg", "question": "この牌の名前は何ですか？", "answer": "チーマン"},
    {"image": "/content/7p.jpeg", "question": "この牌の名前は何ですか？", "answer": "チーピン"},
    {"image": "/content/7s.jpeg", "question": "この牌の名前は何ですか？", "answer": "チーソー"},
    {"image": "/content/8man.jpeg", "question": "この牌の名前は何ですか？", "answer": "パーマン"},
    {"image": "/content/8p.jpeg", "question": "この牌の名前は何ですか？", "answer": "パーピン"},
    {"image": "/content/8s.jpeg", "question": "この牌の名前は何ですか？", "answer": "パーソー"},
    {"image": "/content/9man.jpeg", "question": "この牌の名前は何ですか？", "answer": "キュウマン"},
    {"image": "/content/9p.jpeg", "question": "この牌の名前は何ですか？", "answer": "キュウピン"},
    {"image": "/content/9s.jpeg", "question": "この牌の名前は何ですか？", "answer": "キュウソー"}
    
    
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
