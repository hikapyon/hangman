import getpass

print("ハングマンへようこそ")
p1_name = input("出題者の名前を入力してね")
p2_name = input("解答者の名前を入力してね")
word = getpass.getpass("プレイヤー1は出題する動物の名前を入力してください(入力した文字は表示されません）")
print("""




















""")



def hangman(w):
    wrong = 0 #間違えた数
    stages =["",                       
            "___________         ",
            "|          |        ",
            "|          0        ",
            "|         /|\        ",
            "|         / \     　　",
    ]#間違えるたびにこのイラストが完成していく
    rletters = list(w)#wordをリスト化してrlettersのリストを作成
    board = ["_"] * len(w) #当てる文字列
    win = False

    while wrong < len(stages) -1: #間違えた数が5回まで続ける
        msg = "解答者は動物の名前を１文字予想してね！"
        char = input(msg) #プレイヤーが予想した文字
        if char in rletters: #charがrlettersに含まれていた時
            cind = rletters.index(char) #何番目の文字に含まれていたか
            board[cind] = char #boardのcind番目に文字を追加
            rletters[cind] = "$" #あてられたもじを＄に置き換え
            if "_" in board:
                print("正解!")
                print(" ".join(board)) #boardを表示
        
        else: #charがrlettersに含まれていなかったとき
            wrong += 1
            print(" ".join(board))
            e = wrong + 1   
            print("\n".join(stages[1:e])) #stagesを１行表示
        if "_" not in board:
            print("正解は{}でした。{}の勝ちです".format(w,p2_name))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("{}の勝ちです！正解は {}.".format(p1_name,w))

hangman(word)

        