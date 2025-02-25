# Dockerとは
Dockerは，コンテナ型の仮想化ソフトウェアの一種である．

## Dockerの利点
Dockerを使用することで以下のような利点がある．
- 単一のマシンに複数の仮想環境を作成できる
- どこでも誰でも同一の環境を作成することができる
- 他の仮想化ソフトウェアと比較して軽量である

## Dockerをつかってみる
本節では，Dockerを実際に触ってみることで，Dockerに対する理解を深めることを目的とする．

### Hello World コンテナの起動
~~~terminal
docker container run hello-world
~~~
実行後，`Hello from Docker!`という文字列が確認できたら成功です．