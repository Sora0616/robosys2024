# robosys2024
ロボットシステム学で利用するリポジトリ

# combnation -  nCr の計算(組み合わせ)
[![test](https://github.com/Sora0616/robosys2024/actions/workflows/test.combination.yml/badge.svg)](https://github.com/Sora0616/robosys2024/actions/workflows/test.combination.yml)


# 概要
このコマンドは、組み合わせの計算を行うことができるコマンドです。


# 必要なソフトウェア
- Ubuntu 20.04
- Python
   - テスト済みバージョン: 3.7 ~ 3.11

# テスト環境
- Ubuntu 20.04
- Python 3.7 ~ 3.11

# 利用方法について
## 1.実行前の準備
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

## 2.実行方法
ターミナルで以下のコマンドを入力し、実行してください。
```
$ echo 5 3 | ./comb.py
```
今回入力した数字は、"5 3"でnCrと計算されるものにn = 5, r = 3を代入して計算します。ただし、n > r, r >= 0, nとｒが整数であることで実行することができます。

## 3.実行例について
- 実行例(成功)
```
$ echo 5 3 | ./comb.py
```
- 実行結果
```
5C3 = 10
```

- 実行例(失敗例1)
```
$ echo 5 6 | ./comb.py
```
- 実行結果
```
無効な入力: 5 6
```
本来、nCrの計算ではn > rであるが、ここではn < rとなっているため、無効な入力と出力されます。

- 実行例(失敗例2)
```
$ echo -5 -3 | ./comb.py
```
- 実行結果
```
無効な入力: -5 -3
```
組み合わせの計算は、ｎ個の中からｒ個選ぶ組み合わせを計算するため負の定数に対する定義がされていません。よって、無効な入力と出力されます。

- 実行例(失敗例3)
```
$ echo 6.2 3.3 | ./comb.py
```
- 実行結果
```
無効な入力: 6.2 3.3
```
特定の要素の数からいくつかの要素を選ぶ計算のため正の整数に対してのみ計算ができます。そのため、無効な入力と出力されます。

- 実行例(失敗例4)
```
$ echo 5/4 1/2 | ./comb.py
```
- 実行結果
```
無効な入力: 5/4 1/2
```
失敗例３と同様に正の整数に対してのみ計算ができるため、無効な入力と出力されます。

- 実行例(失敗例5)
```
$ echo 5 a | ./comb.py
```
- 実行結果
```
無効な入力: 5 a
```
数字以外の文字が入力されたため、無効な入力と出力されます。

- 実行例(失敗例6)
```
$ echo | ./comb.py
```
- 実行結果
```
無効な入力: 
```
文字が入力されず空白なため、無効な入力と出力されます。

# 作成者
千葉工業大学 先進工学部未来ロボティクス学科 23C1115 平野蒼空

# LICENSE・著作権
- このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許  可されます。
-  このパッケージのコードの一部は、下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを、本人の許可を得て自身の著作としたものです。
     - [ryuichiueda/slides_marp/tree/master/robosys_2024](https://github.com/ryuichiueda/slides_marp/tree/master/robosys2024)

© 2024 Sora Hirano
