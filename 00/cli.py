import sys

def main(argv):
    """argparse tutorial 00

    まずは最も原始的な方法から。
    $ python cli.py arg1
    のように実行する

    :param argv: sys.argv
    :type argv: list of string
    """

    # 引数の個数をチェック
    assert len(argv) >= 2

    # CLIのロジック部分
    message = argv[1]
    print(f'hello, {message.upper()}')

if __name__ == '__main__':
    main(sys.argv)