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

### コンテナの停止
ubuntuコンテナを停止させてみよう．先ほどコンテナの一覧を表示させた際に，出力されたコンテナ名で指定することができる．

~~~bash
$ docker container stop jovial_burnell

$ docker container ls --all
CONTAINER ID   IMAGE          COMMAND    CREATED          STATUS                      PORTS   NAMES
796c6a393008   hello-world    "/hello"   2 minutes ago    Exited (0) 2 minutes ago            elated_bell
5caa85f1d8ea   ubuntu:latest  "bash"     3 minutes ago    Exited (0) 1 minutes ago            jovial_burnell
~~~

コンテナの一覧を確認すると，ubuntuコンテナのSTATUSが変化していることがわかる．また，対話操作をしていたターミナルを確認すると，コンテナが終了していることがわかる．

### コンテナの削除
先ほど停止したコンテナを削除してみよう．
~~~bash
$ docker container rm jovial_burnell

$ docker container ls --all
CONTAINER ID   IMAGE          COMMAND    CREATED          STATUS                      PORTS   NAMES
796c6a393008   hello-world    "/hello"   2 minutes ago    Exited (0) 2 minutes ago            elated_bell
~~~
コンテナを削除することができた．

なお，起動中のコンテナを直接削除したい場合は，`-f` コマンドをつけることで，強制的に削除することが可能である．

## Dockerfileについて
Dockerfile を使用することで，任意のイメージを作成することができる．また，配布が容易であり，どのようなコンテナであるかのドキュメント代わりにもなる．

### Dockerfile の例
`./dockerfile_example`はDockerを使用して作成した環境下で画像処理を行うサンプルプログラムである．実行してみよう．

~~~bash
$ cd dockerfile_example
$ docker image build --rm –t mycv2 .
$ docker container run --rm --mount type=bind,source=$(pwd),target=/app mycv2
~~~

`dockerfile_example/output`にそれぞれグレースケール画像とエッジ画像が出力されていることを確認したら，成功です．

<details><summary>Dockerコマンドの解説</summary>

`docker image build`で DockerfileからImageを作成することができる．`--rm`オプションは，途中で作成される中間Imageを削除するためのコマンドであり，`-t`オプションで作成したイメージに名前をつけることができる．

今回使用するプログラムは，画像を出力するため，`--mount`オプションでバインドマウントを行ってコンテナ内のディレクトリとホストディレクトリを同期させている．
</details>