# robosys2024
ロボットシステム学で利用するリポジトリ

# combnationコマンド -  nCr (組み合わせ)の計算
[![test](https://github.com/Sora0616/robosys2024/actions/workflows/test.combination.yml/badge.svg)](https://github.com/Sora0616/robosys2024/actions/workflows/test.combination.yml)


## 概要
ターミナル上で組み合わせの計算を行うことができるコマンドです。

## 必要なソフトウェア
- Ubuntu 20.04
- Python
   - テスト済みバージョン: 3.7 ~ 3.11

## テスト環境
- Ubuntu 20.04
- Python 3.7 ~ 3.11

## 利用方法について
### 1.実行前の準備
0.Git Hubをダウンロードしていない方はダウンロードしてください。
```
$ sudo apt install git
```

1.ターミナルで以下のコマンドを入力し、リポジトリをクローンしてください。
```
$ git clone git@github.com:Sora0616/robosys2024.git
```

2.ターミナルで以下のコマンドを入力し、ディレクトリを移動してください。
```
$ cd robosys2024
```

3.ターミナルで以下のコマンドを入力し、スクリプトを実行可能状態にしてください。
```
$ chmod +x combination.py
```

### 2.実行方法
ターミナルで以下のコマンドを入力し、実行してください。
```
$ echo 5 3 | ./combnation.py
```
実行結果
```
5C3 = 10
```
今回入力した数字は、"5 3"でnCrと計算されるものにn = 5, r = 3を代入して計算します。ただし、n > r, r >= 0, nとｒが整数であることで実行することができます。

## 作成者
千葉工業大学 先進工学部未来ロボティクス学科 23C1115 平野蒼空

## LICENSE・著作権
- このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許  可されます。
-  このパッケージのコードの一部は、下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを、本人の許可を得て自身の著作としたものです。
     - [ryuichiueda/slides_marp/tree/master/robosys_2024](https://github.com/ryuichiueda/slides_marp/tree/master/robosys2024)

© 2024 Sora Hirano
