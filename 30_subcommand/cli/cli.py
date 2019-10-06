import os
import argparse
import json
import yaml

from backlog.base import BacklogAPI
from commands.issue import Issue
from commands.project import Project

import logging as lgg

logger = lgg.getLogger(__name__)
logger.setLevel(lgg.INFO)
stream_handler = lgg.StreamHandler()
stream_handler.setLevel(lgg.INFO)
logger.addHandler(stream_handler)


def get_parser():
    """Make backlog cli parser

    :return: backlog cli parser
    :rtype: argparse.ArgumentParser
    """
    # https://docs.python.org/ja/3/library/argparse.html#argumentparser-objects
    parser = argparse.ArgumentParser(
        description="""This is argparse tutorial - 30

            サブコマンドを備えた簡易版Backlog CLI
            """
    )

    # 受け入れる引数の宣言
    parser.add_argument(
        '-c',
        '--conf',
        dest='conf',
        type=str,
        default='conf.yml',
        metavar='conf file path',
        help='Default value is "conf.yml". if not found, try get BACKLOG_SPACE and BACKLOG_API_KEY from env vars insted of read from conf'
    )

    #
    # Subcommands
    #
    # NOTE: 任意引数が無指定だった場合のデフォルト値はNoneであることを期待した実装とする
    #
    # TODO: Parser生成ロジックもサブコマンド単位でモジュールにしたい。絵面が汚くて何やってるのかわかりづらい。
    #
    subparsers = parser.add_subparsers()

    #
    # Project subcommand
    #
    project_parser = subparsers.add_parser('project')

    project_subparsers = project_parser.add_subparsers()

    # project list
    project_list_subparser = project_subparsers.add_parser('list', aliases=['ls'])
    project_list_subparser.set_defaults(handler=Project.list)

    # project get
    project_get_subparser  = project_subparsers.add_parser('get')
    project_get_subparser.add_argument('-p', '--project-id-or-key', dest='projectIdOrKey', type=str, required=True)
    project_get_subparser.set_defaults(handler=Project.get)

    #
    # Wiki subcommand
    #
    wiki_parser = subparsers.add_parser('wiki')

    wiki_subparsers = wiki_parser.add_subparsers()

    # wiki list
    wiki_list_parser = wiki_subparsers.add_parser('list', aliases=['ls'])
    wiki_list_parser.add_argument('-p', '--project-id-or-key', dest='projectIdOrKey', type=str, default=None)
    wiki_list_parser.add_argument('-w', '--keyword', dest='keyword', type=str, default=None)
    wiki_list_parser.set_defaults(handler=Issue.list)

    # wiki get
    wiki_get_parser = wiki_subparsers.add_parser('get')
    wiki_get_parser.add_argument('--wiki-id', dest='wikiId', type=str, required=True)
    wiki_get_parser.set_defaults(handler=Issue.get)

    return parser


def invoke_handler(backlog_client, parser, namespace):
    if hasattr(namespace, 'handler'):
        return namespace.handler(backlog_client, namespace)
    else:
        parser.print_help()

    return None


def backlog_get_client(space: str, api_key: str):
    """Return Backlog API Client

    :param space: backlog space (backlog.jpのサブドメイン))
    :type space: str
    :param api_key: backlog api key
    :type api_key: str
    :return: Backlog API Client object
    :rtype: backlog.base.BacklogAPI
    """
    return BacklogAPI(
        space=space,
        api_key=api_key
    )


def try_conf(conf_path: str):
    """confの内容をチェック

    confファイルが存在し、ルートのキーとして 'space', 'api_key' の2つが存在することを期待する
    指定されたパスにconfがなければ環境変数からの取得を試みる

    :param conf_path: path of conf.yml
    :return: 'space', 'api_key' の2つのキーを含むdict
    :rtype: dict
    """
    if not os.path.exists(conf_path):
        logger.info(f'Specified conf {conf_path} is not found. trying get values from environment variables.')
        space = os.environ.get('BACKLOG_SPACE', None)
        api_key = os.environ.get('BACKLOG_API_KEY', None)
        if (space is not None) and (api_key is not None):
            return {
                'space': space,
                'api_key': api_key
            }

        raise FileNotFoundError(f'conf file not found: {conf_path}')

    with open(conf_path, 'r') as conf:
        yml = yaml.load(conf, Loader=yaml.CLoader)

        if not ('space' in yml.keys()):
            raise Exception('conf object does not have "space" key.')

        if not ('api_key' in yml.keys()):
            raise Exception('conf object does not have "api_key" key.')

        return yml


def main():
    """argparse tutorial 30

    Backlog APIを叩いてみるCLIツールを作る

    python-backlogの使用方法は以下のリンクを参照。
    http://blog.serverworks.co.jp/tech/2019/09/06/post-73944/

    API Keyの発行は以下のURLから
    https://<space>.backlog.jp/EditApiSettings.action
    """
    parser = get_parser()

    args = parser.parse_args()

    # client initialization
    conf = try_conf(args.conf)

    backlog_client = backlog_get_client(
        space=conf['space'],
        api_key=conf['api_key']
    )

    ret = invoke_handler(backlog_client, parser, args)

    if ret is not None:
        print(json.dumps(ret))

    return 0


if __name__ == '__main__':
    main()
