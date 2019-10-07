import argparse

def main():
    """argparse tutorial 2

    https://docs.python.org/ja/3/howto/argparse.html
    01をargparseで書き直してみる
    """

    # https://docs.python.org/ja/3/library/argparse.html#argumentparser-objects
    parser = argparse.ArgumentParser(
        description="This is argparse tutorial - 02"
    )

    # 別の書き方（位置引数を使うバターン）
    # 今回の例では、cli.pyの次に来る引数の宣言になる。
    # help上では"message"という名前で出力される（metavarを使わない場合）
    parser.add_argument(
        "message",
        type=str,
        default='world',
        # metavar='MESSAGE STR',
        help='出力する文字列'
    )

    # 与えられた実行時の引数をパース
    args = parser.parse_args()

    # ロジック部分の処理
    message = args.message
    print(f'hello, {message.upper()}')


if __name__ == '__main__':
    main()