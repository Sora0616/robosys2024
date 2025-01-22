# robosys2024
ロボットシステム学で利用するリポジトリ

# year_end_lottery_simulatorコマンド 
[![test](https://github.com/Sora0616/robosys2024/actions/workflows/test.combination.yml/badge.svg)](https://github.com/Sora0616/robosys2024/actions/workflows/test.combination.yml)


## 概要
ターミナル上で年末ジャンボ宝くじのシミュレーションを行うことができるコマンドです。

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

3.ターミナルで以下のコマンドを出入力し、スクリプトを実行可能状態にしてください。
```
$ chmod +x year_end_lottery_simulator
```

### 2.実行方法
ターミナルで以下のコマンドを出入力し、実行してください。
```
$ echo 90000 | ./year_end_lottery_simulator
```
実行結果
```
購入枚数: 300枚
おつり: 0円
6等: 2枚
7等: 27枚
外れ: 271枚
合計当選金額: 14100円
還元率: 15.67%
```
今回出入力した金額は、年末ジャンボ宝くじのシミュレーションに使用されます。例えば、購入金額が90000円の場合、宝くじを購入し、その結果がシミュレーションされて表示されます。購入金額が300円未満の場合、エラーメッセージは表示されませんが、スクリプトが終了します。宝くじの等級ごとの当選確率と当選金額に基づいてシミュレーションが行われ、結果が表示されます。

## 作成者
千葉工業大学 先進工学部未来ロボティクス学科 23C1115 平野蒼空

## 参照サイト
- https://otokurashi.jp/nenmatsu-jumbo-2024/

## LICENSE・著作権
- このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます。
-  このパッケージのコードの一部は、下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを、本人の許可を得て自身の著作としたものです。
     - [ryuichiueda/slides_marp/tree/master/robosys_2024](https://github.com/ryuichiueda/slides_marp/tree/master/robosys2024)

© 2025 Sora Hirano
