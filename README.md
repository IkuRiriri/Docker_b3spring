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
~~~bash
$ docker container run hello-world
~~~
実行後，`Hello from Docker!`という文字列が確認できたら成功．

<details><summary>解説</summary>

~~~bash
$ docker container run [options] (Image) [command]
~~~
`docker container run`は，Docker Imageからコンテナを作成するためのコマンドである．
</details>

### Ubuntu コンテナの起動
~~~bash
$ docker container run –it ubuntu:latest bash
~~~
実行後，プロンプトが切り替わり操作待ちになっていることが確認できたら成功

~~~bash
root@id:/# ls
~~~

~~~bash
root@id:/# head -n 4 /etc/os-release
~~~