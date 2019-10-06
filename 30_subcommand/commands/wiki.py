from backlog.base import BacklogAPI

import logging as lgg

logger = lgg.getLogger(__name__)
logger.setLevel(lgg.INFO)
stream_handler = lgg.StreamHandler()
stream_handler.setLevel(lgg.INFO)
logger.addHandler(stream_handler)


class Wiki:
    @classmethod
    def list(cls, client, namespace):
        """list wiki

        https://developer.nulab.com/ja/docs/backlog/api/2/get-wiki-page-list/

        - projectIdOrKey (optional)
        - keyword (optional)

        .. Note::

            指定されなかった任意引数の値はNoneであることを期待する


        :param client: backlog api client
        :type client: backlog.base.BacklogAPI
        :param namespace: args
        :type namespace: argparse.ArgumentParser
        :return: dict
        """
        param = dict([
            (k, v) for k, v in vars(namespace).items() if v is not None
        ])

        return client.wiki.list()

    @classmethod
    def get(cls, client, namespace):
        """get wiki

        .. Note::

            指定されなかった任意引数の値はNoneであることを期待する


        :param client: backlog api client
        :type client: backlog.base.BacklogAPI
        :param namespace: args
        :type namespace: argparse.ArgumentParser
        :return: dict
        """
        projectIdOrKey = namespace.projectIdOrKey

        return client.project.get(projectIdOrKey=projectIdOrKey)
