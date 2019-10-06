from backlog.base import BacklogAPI

import logging as lgg

logger = lgg.getLogger(__name__)
logger.setLevel(lgg.INFO)
stream_handler = lgg.StreamHandler()
stream_handler.setLevel(lgg.INFO)
logger.addHandler(stream_handler)


class Issue:
    @classmethod
    def list(client, namespace):
        """list issue

        カスタム属性のパラメータ指定は非対応

        :param client: backlog api client
        :type client: backlog.base.BacklogAPI
        :param namespace: args
        :type namespace: argparse.ArgumentParser
        :return: dict
        """
        params_mapping = {
            'projectId': 'projectId[]',
            'issueTypeId': 'issueTypeId[]',
            'categoryId': 'categoryId[]',
            'versionId': 'versionId[]',
            'milestoneId': 'milestoneId[]',
            'statusId': 'statusId[]',
            'priorityId': 'priorityId[]',
            'assigneeId': 'assigneeId[]',
            'createdUserId': 'createdUserId[]',
            'resolutionId': 'resolutionId[]',
            'parentChild': 'parentChild',
            'attachment': 'attachment',
            'sharedFile': 'sharedFile',
            'sort': 'sort',
            'order': 'order',
            'offset': 'offset',
            'count': 'count',
            'createdSince': 'createdSince',
            'createdUntil': 'createdUntil',
            'updatedSince': 'updatedSince',
            'updatedUntil': 'updatedUntil',
            'startDateSince': 'startDateSince',
            'startDateUntil': 'startDateUntil',
            'dueDateSince': 'dueDateSince',
            'dueDateUntil': 'dueDateUntil',
            'id': 'id[]',
            'parentIssueId': 'parentIssueId[]',
            'keyword': 'keyword'
        }

        param = {}
        for k, attr_name in params_mapping.items():
            arg = getattr(namespace, k, None)
            if arg is None:
                continue

            param[attr_name] = arg

        return client.issue.list(**param)

    @classmethod
    def get(client, namespace):
        """get project

        :param client: backlog api client
        :type client: backlog.base.BacklogAPI
        :param namespace: args
        :type namespace: argparse.ArgumentParser
        :return: dict
        """
        issueIdOrKey = getattr(namespace, 'issueIdOrKey')

        return client.issue.get(issueIdOrKey=issueIdOrKey)
