# Git環境のセットアップ

- 分散型バージョン管理システム

## Git for Windows Portable版

- インストール 参考記事 : https://qiita.com/ryo-sato/items/6c6553a7c2db9b96ce1d
  - https://git-scm.com/download/win
  - 任意のフォルダに展開する。
  - 環境変数にgitの実行ファイルが保存されたフォルダC:\PortableGit\binを追加する。

## gitの必須初期設定
- PS C:\Users\Shigehiro\Desktop\python_emb\source\learing\multiprocess_guiautomation> git config --global user.name "Shigehiro Arimoto"
- PS C:\Users\Shigehiro\Desktop\python_emb\source\learing\multiprocess_guiautomation> git config --global user.email email_address

## ローカルリポジトリの作成
- ローカルリポジトリを新規作成する場合
    - VS CODE上で、「リポジトリを初期化する」を実行し、バージョン管理をしたいフォルダを指定する。
    - VS CODEのソース管理メニュー→リモート→「リモートの追加」機能により、現在のローカルリポジトリをリモートリポジトリに関連付けが可能となる。
- 既存のリモートリポジトリを複製してローカルリポジトリを新規作成する場合
    - リポジトリ先を指定してGit Cloneを実行することで、ローカルリポジトリを作成することができる。
VSCODE
## GIT向けVSCODE拡張機能
- GIT Graph

## git操作方法
- gitignoreファイル
  - バージョン管理の対象外とするフォルダやファイルを指定する。
- init
  - Gitリポジトリの新規作成
- folk
  - 他者が公開しているリモートリポジトリを自身のリモートリポジトリとしてコピーする。
- clone
  - 既存のリモートリポジトリを複製し、ローカルリポジトリとして新規作成する。
- stage
  - 次回のコミットに含める変更を指定するコマンド。
- commit
  - ローカルリポジトリに変更内容を登録する。
- checkout
  - 過去のコミット、別ブランチに移動する。ローカルリポジトリの各ファイルの内容が変更される。
  - コミットしていないファイル、編集内容がある場合、チェックアウトに失敗または強制的に上書きされてしまう。一時退避する場合はstashを利用する。
- push
  - ローカルリポジトリの変更をリモートリポジトリに反映させる。
- pull
  - リモートリポジトリで起きた変更をローカルリポジトリに取り込む。
  - VS CODE上からPULLを実行すると、現在チェックアウトしているブランチのみ更新される。
    - [2022-03-29T12:01:07.288Z] > git pull --tags origin conflicttest [967ms]
  - リモートリポジトリにある全てのブランチについて、履歴を知りたい場合は、git pull --allと実行する。またはfetchする。
- fetch
  - リモートリポジトリの最新状態を取得しリモート追跡ブランチに同期させる。ローカルリポジトリのブランチは一切変更されない。
    - リモート追跡ブランチ：ローカルリポジトリ内に存在する。リモートリポジトリをローカルにミラーリングしたもの。読み取り専用。main/origin
  - Pull = fetch + merge(リモート追跡ブランチをローカルブランチにマージ)
- remote
  - ローカルリポジトリに紐づけるリモートリポジトリを追加・変更・削除する。
- branch
  - 並行世界を作るための機能。その正体は単にコミットを指す単純なポインタである。
  - master,mainブランチは本流を意味し、本番用の最新版に使う場合が多い。
  - branchの作成
    - Git graph上で作成可能。branchの起点となるコミットを選択して、右クリック→Create Branch。
  - pushすることでリモートリポジトリに、ローカルに作成したbranchが反映される。

- merge
  - merge先のブランチにチェックアウトする。
  - gitGraph上からmerge元となるブランチとコミットを選択して、「Mearge into current branch」を実行する。
  - 衝突が発生した場合は別途対応が必要。

- conflict
  - 同一ファイルの同一行に異なる変更が施され、Pull、mergeができない状態のこと。
    - Pull時
      - 未ステージ、未コミットのファイルに対しconflictが発生した場合、PULLが失敗する。
      - commit後、PULLを実行した時にconflictが発生する場合
        - fatal: Need to specify how to reconcile divergent branches.が発生してPULLに失敗する。→gitの下記設定が必要。
          - hint:   git config pull.rebase false  # merge
          - hint:   git config pull.rebase true   # rebase
          - hint:   git config pull.ff only       # fast-forward only
    - branchのmerge時
      - 
  - conflictの対処方法
    - conflictが発生したファイルは、!マークが付与されている。エディタでファイルを本来の内容に編集した後にコミットする。

- Pull Request
  - githubの機能。
  - folkで作成したリモートリポジトリから、本流のリモートリポジトリに対して、変更を提案する。


-origin
    - ローカルリポジトリにおけるリモートリポジトリを示す名前。Clone時にGitが自動的につける名前。
```
PS C:\Python\Repository\TestingGit> git remote -v
origin  https://github.com/ShigehiroArimoto/TestingGit (fetch)
origin  https://github.com/ShigehiroArimoto/TestingGit (push)
```

- head
  - 現在使用しているブランチの先頭を示す名前
  - origin/headはリモートリポジトリの先頭

- Tag
  - 
- revert
  - 過去のコミットを打ち消す。コミット自体を削除するわけではなく、反対の内容を新規コミットすることで、過去の変更を打ち消す。

- squash
- stash
  - 未コミットの変更を一時退避する機能。

- cherry pick
 