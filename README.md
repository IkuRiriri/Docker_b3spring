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

<details><summary>Dockerコマンドの解説</summary>

~~~bash
$ docker container run [options] (Image) [command]
~~~
`docker container run`は，Docker Imageからコンテナを作成するためのコマンドである．
指定された`hello-world`イメージが自分のデバイスの中に存在しない場合は，Docker hubから自動的にダウンロードされる．
</details>

### Ubuntu コンテナの起動
~~~bash
$ docker container run -it ubuntu:latest bash
~~~
実行後，プロンプトが切り替わり操作待ちになっていることが確認できたら成功．
コンテナ内のUbuntuに対していくつかのコマンドを実行してみよう．

~~~bash
root@id:/# ls
bin  boot  dev  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
~~~

~~~bash
root@id:/# head -n 4 /etc/os-release
PRETTY_NAME="Ubuntu 24.04.1 LTS"
NAME="Ubuntu"
VERSION_ID="24.04"
VERSION="24.04.1 LTS (Noble Numbat)"
~~~

上記のコマンドでは，コンテナ内のUbuntuのバージョンが確認できる．2025/02/25の実行時は，`Ubuntu 24.04.1 LTS`であった．

他にも任意のコマンドを試してみてほしい．

<details><summary>Dockerコマンドの解説</summary>

`-it`は，コンテナに対して，対話操作を行うためのオプションである．
また，指定するImageを`ubuntu:latest`としたが，`:`以降はTag情報を指定する．Tagには一般的にバージョン情報やイメージのサイズなどの情報が含まれることが多く，Tagを指定することで任意のイメージを指定できる．Tagを省略した場合や今回のように指定した場合は，`:latest`Tagが用いられる．これは一般的に最新のバージョンを指定するため，研究に使用するなどの目的でバージョンを指定する必要がある場合は，適切なTagの指定を推奨する．
</details>

### コンテナ一覧の確認
ubuntuコンテナを操作していたターミナルを開いたまま，別のターミナルを開いてコンテナ一覧を確認しよう．

~~~bash
$ docker container ls
CONTAINER ID   IMAGE           COMMAND   CREATED          STATUS          PORTS     NAMES
ad788fd3572a   ubuntu:latest   "bash"    17 seconds ago   Up 17 seconds             sad_curie
~~~

先ほど実行したubuntuコンテナが表示されていると思われる．STATUSのカラムをみると，起動中であることを示す`Up`と，起動時間が表示されている．
続いて，全てのコンテナ一覧を確認しよう．

~~~bash
$ docker container ls --all
CONTAINER ID   IMAGE          COMMAND    CREATED          STATUS                      PORTS   NAMES
796c6a393008   hello-world    "/hello"   2 minutes ago    Exited (0) 2 minutes ago            elated_bell
5caa85f1d8ea   ubuntu:latest  "bash"     3 minutes ago    Up 3 minutes                        jovial_burnell
~~~

ubuntuコンテナの他に終了済みのHelloWorldコンテナが確認できる．HelloWorldコンテナはメッセージの出力後，自動的に終了する．