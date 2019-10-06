# Example 03

[python-backlog](https://pypi.org/project/python-backlog/)を使って、Backlog APIをラップする簡単なCLIを作ってみる。

この例では、特定プロジェクトの配下にあるすべてのwikiをjson形式で列挙して標準出力に返すのみの仕様。


## how to use

APIの認証情報を持つyamlファイルのパス指定と、プロジェクト名(もしくはキー)の指定を必要とする

```plain
$ python cli.py -h
usage: cli.py [-h] [-c conf_file. default: conf.yml] -p PROJECT_ID_OR_KEY

This is argparse tutorial - 10 簡易版Backlog CLIのようなもの

optional arguments:
  -h, --help            show this help message and exit
  -c conf_file. (default: conf.yml), --conf conf_file. (default: conf.yml)
  -p PROJECT_ID_OR_KEY, --project PROJECT_ID_OR_KEY

```

yamlファイルの指定方式は `cond.default.yml` の通り

```yaml
---
space: foo
api_key: foobarbuzz

```