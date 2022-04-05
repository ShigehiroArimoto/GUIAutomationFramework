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

## GIT向けVSCODE拡張機能
- GIT Graph

## git操作方法
- gitignoreファイル
  - バージョン管理の対象外とするフォルダやファイルを指定する。
- init
  - Gitリポジトリの新規作成

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
  - 衝突したマージをキャンセルする場合は以下のコマンドを実行する。
```
PS C:\Python\Repository\TestingGit> git reset --hard HEAD
HEAD is now at 0091949 Merge branch 'rebase_test'
```

  - merge処理には3種類の方法が存在する。
    - fast forward(早送り)
      - マージコミットは作成されず、ブランチの位置を移動するだけとなる。
    - non fast forward
      - マージによりマージコミットが作成される。枝分かれした履歴が保持されるため、後から作業の振り返りがしやすい。
    - rebase
      - すでにリモートリポジトリにPushされているブランチに対するrebaseは避けること。rebaseにより新しいコミットに作り変えられるため、pushできなくなってしまうため。
      - ローカルリポジトリの中に存在するブランチにのみrebaseを行うこと。

- conflict
  - 同一ファイルの同一行に異なる変更が施され、Pull、mergeができない状態のこと。
  - conflictが発生したファイルは、!マークが付与されている。エディタでファイルを本来の内容に編集した後にコミットする。
  - Pull時のconflict
    - 未ステージ、未コミットのファイルに対しconflictが発生した場合、PULLが失敗する。
    - commit後、PULLを実行した時にconflictが発生する場合
      - fatal: Need to specify how to reconcile divergent branches.が発生してPULLに失敗する。→gitの下記設定が必要。
        - hint:   git config pull.rebase false  # merge
        - hint:   git config pull.rebase true   # rebase
        - hint:   git config pull.ff only       # fast-forward only
      - rebaseはリスクがある。merge設定にしておく方が無難。
  - branch merge時のconflict
      - エディタで衝突した箇所を編集し、コミットを実行する。

- origin
    - ローカルリポジトリにおけるリモートリポジトリを示す名前。Clone時にGitが自動的につける名前。
```
PS C:\Python\Repository\TestingGit> git remote -v
origin  https://github.com/ShigehiroArimoto/TestingGit (fetch)
origin  https://github.com/ShigehiroArimoto/TestingGit (push)
```

- head
  - 現在作業している場所を示すポインタ。唯一の存在。
  - origin/headはリモートリポジトリの先頭

- Tag
  - コミットに目印となる文字列を割り当てる機能。リリースポイントに使用することが多い。
  - タグにはlight weightとannotedの2種類が存在する。
  - GitHub上ではタグが一覧化され、各タグのリポジトリ内容をアーカイブファイルとしてダウンロードすることができる機能がある。
  
- revert
  - 過去のコミットを打ち消す。コミット自体を削除するわけではなく、反対の内容を新規コミットすることで、過去の変更を打ち消す。

- stash
  - 未コミットの変更を一時退避する機能。
  - 作業途中で別ブランチへのチェックアウトが必要な時に使用する。作業後にブランチへ復帰した後に、stashを適用することで、編集中の内容が復元される。

- cherry pick
  - ブランチ全体をマージするのではなく、ブランチ上にある特定のコミットだけを選択してマージする機能。

- detached head状態
  - HEADがブランチでなくコミットIDを直接指し示している状態。ブランチ不在の状態。過去のコミットにCheckoutすることで発生する。
  - detachde HEAD状態で実行したコミットは、checkoutを実行すると参照できなくなってしまう。
  - branchを新規作成することで問題を回避できる。

## GitHubの機能
- folk
  - 他者が公開しているリモートリポジトリを自身のリモートリポジトリとしてコピーする。
- Pull Request
  - githubの機能。
  - folkで作成したリモートリポジトリから、本流のリモートリポジトリに対して、変更を提案する。
