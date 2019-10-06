# argparse-tutorials

ちょっとした作業の自動化スクリプトを書いたので社内に展開したい、そんな時に。

argparseを使うだけで、「CLIっぽい」見た目のツールが簡単に作れます。

自前でsys.argvをパースするお手製スクリプトからは卒業しましょう。

本レポジトリでは、ユーザーに `python command.py arg1 arg2` のようなPython感丸出しのインタフェースを公開しなくて済むようになるためのやり方を紹介します。

推奨環境: Python 3.6以上


## 対象読者

- Pythonの基本的な文法やpipの使い方を理解している
- ちょっとした作業を自動化したい／自動化するスクリプトを書いたことがある
- 自作の自動化スクリプトを社内に展開したい
    - 展開したいけどもうちょっと見栄えの良いツールにしたい
    - いい感じのコマンドラインインタフェースを提供したい
- argparse を知らない／使い方がよくわからない
- setup.py の用法がよくわからない


## License

These codes are licensed under CC0.

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)