import argparse

def main():
    """argparse tutorial 1

    https://docs.python.org/ja/3/howto/argparse.html
    00をargparseで書き直してみる
    """

    # https://docs.python.org/ja/3/library/argparse.html#argumentparser-objects
    parser = argparse.ArgumentParser(
        description="This is argparse tutorial - 01"
    )

    # コマンドラインパーサが受け付ける引数を定義する
    # この例では -m <msg>, --message <msg> の形式で指定可能な引数を定義している
    parser.add_argument(
        "-m",
        "--message",
        type=str,
        dest='msg',
        default='world',
        help="出力する文字列"
    )

    # 与えられた実行時の引数をパース
    args = parser.parse_args()

    # ロジック部分の処理
    message = args.msg
    print(f'hello, {message.upper()}')


if __name__ == '__main__':
    main()