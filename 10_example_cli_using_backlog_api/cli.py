import argparse
import json
import csv

import yaml
from backlog.base import BacklogAPI

def main():
    """argparse tutorial 10

    Backlog APIを叩いてみるCLIツールを作る

    python-backlogの使用方法は以下のリンクを参照。
    http://blog.serverworks.co.jp/tech/2019/09/06/post-73944/

    API Keyの発行は以下のURLから
    https://<space>.backlog.jp/EditApiSettings.action
    """

    # https://docs.python.org/ja/3/library/argparse.html#argumentparser-objects
    parser = argparse.ArgumentParser(
        description="""This is argparse tutorial - 10
        
        簡易版Backlog CLIのようなもの
        """
    )

    # 受け入れる引数の宣言
    parser.add_argument(
        '-c',
        '--conf',
        dest='conf',
        type=argparse.FileType('r'),
        default=open('conf.yml'),
        metavar='conf_file. (default: conf.yml)',
        # help='conf file'
    )

    parser.add_argument(
        '-p',
        '--project',
        dest='project',
        type=str,
        metavar='PROJECT_ID_OR_KEY',
        required=True,
        # help='Project id or key'
    )

    # パース＋ロジック
    args = parser.parse_args()

    conf = yaml.load(args.conf, Loader=yaml.CLoader)
    check_conf(conf)

    backlog_client = backlog_get_client(
        space=conf['space'],
        api_key=conf['api_key']
    )

    # 戻り値はBacklog API V2の仕様に順序
    # https://developer.nulab.com/ja/docs/backlog/api/2/get-wiki-page-list/
    wikis = backlog_list_wikis(
        client=backlog_client,
        project=args.project
    )

    print(json.dumps(wikis))

    return 0



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


def backlog_list_wikis(client: BacklogAPI, project: str):
    """プロジェクト配下のwikiをリストする

    :param client: API Client
    :type client: BacklogAPI
    :param project: プロジェクトIDもくしはプロジェクトキー
    :type project: str
    """
    return client.wiki.list(
        projectIdOrKey=project
    )


def check_conf(conf: dict):
    """confの内容をチェック
    
    :param conf: 'space', 'api_key' の2つのキーが存在することを期待する
    :type conf: dict
    """
    if not ('space' in conf.keys()):
        raise Exception('conf object does not have "space" key.')
        
    if not ('api_key' in conf.keys()):
        raise Exception('conf object does not have "api_key" key.')
        
    return True


if __name__ == '__main__':
    main()
