# robosys2024
ロボットシステム学で利用するリポジトリ

# combinationコマンド 
[![test](https://github.com/Sora0616/robosys2024/actions/workflows/test.combination.yml/badge.svg)](https://github.com/Sora0616/robosys2024/actions/workflows/test.combination.yml)


## 概要
ターミナル上でnCr (組み合わせ)の計算を行うことができるコマンドです。

## 必要なソフトウェア
- Python
   - テスト済みバージョン: 3.7 ~ 3.11

## テスト環境
- Ubuntu 22.04 LTS

## 利用方法について
### 1.実行前の準備
0.Git Hubをダウンロードしていない方はダウンロードしてください。
```
$ sudo apt install git
```

1.ターミナルで以下のコマンドを入力し、リポジトリをクローンしてください。
```
$ git clone https://github.com/Sora0616/robosys2024.git
```

2.ターミナルで以下のコマンドを入力し、ディレクトリを移動してください。
```
$ cd robosys2024
```

3.ターミナルで以下のコマンドを入力し、スクリプトを実行可能状態にしてください。
```
$ chmod +x combination
```

### 2.実行方法
ターミナルで以下のコマンドを出入力し、実行してください。
```
$ echo 5 3 | ./combnation
```
実行結果
```
5C3 = 10
```
今回出入力した数字は、５と３でnCrと計算されるものにn = 5, r = 3を代入して計算します。ただし、n > r, r >= 0, nとｒが整数であることで実行されます。n,r < 0であったり、n,rが小数や分数、あやaなどの数字以外の文字、空白のまま実行した場合、エラーと出入力されます。

## 作成者
千葉工業大学 先進工学部未来ロボティクス学科 23C1115 平野蒼空

## LICENSE・著作権
- このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます。
-  このパッケージのコードの一部は、下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを、本人の許可を得て自身の著作としたものです。
     - [ryuichiueda/slides_marp/tree/master/robosys_2024](https://github.com/ryuichiueda/slides_marp/tree/master/robosys2024)

© 2025 Sora Hirano
