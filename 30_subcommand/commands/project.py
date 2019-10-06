from backlog.base import BacklogAPI

import logging as lgg

logger = lgg.getLogger(__name__)
logger.setLevel(lgg.INFO)
stream_handler = lgg.StreamHandler()
stream_handler.setLevel(lgg.INFO)
logger.addHandler(stream_handler)


class Project:
    @classmethod
    def list(cls, client, namespace):
        """list project

        :param client: backlog api client
        :type client: backlog.base.BacklogAPI
        :param namespace: args
        :type namespace: argparse.ArgumentParser
        :return: dict
        """
        archived = getattr(namespace, 'archived', False)

        return client.project.list(archived=archived)

    @classmethod
    def get(cls, client, namespace):
        """get project

        :param client: backlog api client
        :type client: backlog.base.BacklogAPI
        :param namespace: args
        :type namespace: argparse.ArgumentParser
        :return: dict
        """
        projectIdOrKey = getattr(namespace, 'projectIdOrKey', None)

        return client.project.get(projectIdOrKey=projectIdOrKey)
