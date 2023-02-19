# http://tinyurl.com/jhrvs94  

def hangman(word):
    wrong = 0  #プレーヤーが何回間違えたのかを数える変数
    stages = ["",
              "________        ",
              "|               ",
              "|       |       ",
              "|       o       ",
              "       /|\      ",
              "       / \      ",
              "                "
              ]
    rletters = list(word)   #変数wordに入る文字列のリスト
    board = ["_"] * len(word)   #文字列を構成する文字の数
    win = False
    print("ハングマンへようこそ！")          
    while wrong < len(stages) - 1:
        print("\n")    #ハングマンへようこその下に空行開ける
        msg = "1文字を予想してね"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)  #文字列のインデックス値を格納
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
            print(" ".join(board))
            e = wrong + 1
            print("\n".join(stages[0:e]))
            if "_" not in board:
                print("あなたの勝ち！")
                print(" ".join(board))
                win = True
                break
        if not win:
            print("\n".join(stages[0:wrong+1]))
            print("あなたの負け！正解は {}.".format(word))


hangman("apple")            
