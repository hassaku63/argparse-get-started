# Example 20

ex.20で作成したソースをPythonパッケージの体裁にしてみる。


最も大きな変化は、

- ユーザーが `pip install ...` の形式で利用できるようになる
- `python cli.py` という呼び出し方ではなく、任意の名前を持つCLIコマンドとして利用できるようになる
- (その気になれば)PyPIに登録して世の中に自分のプロダクトを公開できる [^1]

[^1]: ここでやっている内容をそのままupするとレポジトリを汚すので、もしやるなら検証用環境の https://test.pypi.org/ か、PyPIのローカルサーバー([pypiserver](https://pypi.org/project/pypiserver/))などを利用してください


## ポイント

- setup.pyを書けばとりあえず「自作パッケージ」の開発はできる
- setup関数の重要な引数たち
    - `name` がパッケージの名前 (PyPIへの登録名になる)
    - `install_requires` で自作パッケージの依存関係を宣言できる(本例ではバージョン指定をしていないが、本来は固定値のバージョンを指定する方が良い)
    - `entry_points.console_scripts`　以下に「提供するコマンド名」と対応する「プログラムのエントリポイント」を指定することでCLIを提供できるようになる
    - `packages` パッケージディレクトリを指定。本例では、ソースのツリーから `tests*` を除くディレクトリを検索する
- あるディレクトリを、パッケージが入ったディレクトリとしてPython に扱わせるには、ファイル `__init__.py` が必要 [^2]

[^2]: Python公式ドキュメントより引用 https://docs.python.org/ja/3.6/tutorial/modules.html#packages


# その他補足

自分以外のチームメンバーに使ってもらう想定があるなら、できるだけバージョニングは付与しましょう。

指針として、 [Semantic Versioning 2.0.0](https://semver.org/lang/ja/) の概要を読むと良いです。

エラー原因の迅速な特定のためにも、バージョニングは必要です。継続的に利用されうるだけの価値を持ったツールであるならば、是非バージョニングの導入を検討してみてください。

少なくとも、バージョニングがしっかりしていればユーザーの不具合報告に対してメンテナが再現性を確保するのは容易になります（ロギングも重要なので、バージョニングだけで解決する問題ではないですが...）。


# Links

setup.py

- https://docs.python.org/ja/3.6/distutils/setupscript.html

entry_points (日本語資料少ない)

- https://packaging.python.org/guides/distributing-packages-using-setuptools/#entry-points
- https://setuptools.readthedocs.io/en/latest/setuptools.html#automatic-script-creation