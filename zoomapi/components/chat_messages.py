"""Zoom.us REST API Python Client -- Chat Messages component"""

from zoomapi import util
from zoomapi.components import base


class ChatMessagesComponentV2(base.BaseComponent):
    """Component dealing with all chat messages related matters"""

    # list user's chat messages
    def list(self, **kwargs):
        util.require_keys(kwargs, "user_id")
        return self.get_request(
                "/chat/users/{}/messages".format(kwargs.get("user_id")), params=kwargs
        )

    # send a chat message
    def post(self, **kwargs):
        util.require_keys(kwargs, "message")
        return self.post_request("/chat/users/me/messages", data=kwargs)

    # update a message
    def update(self, **kwargs):
        util.require_keys(kwargs, "message")
        util.require_keys(kwargs, "messageId")
        return self.put_request(
                "/chat/users/me/messages/{}".format(kwargs.get("messageId")), data=kwargs
        )

    # delete a message
    def delete(self, **kwargs):
        util.require_keys(kwargs, "messageId")
        return self.delete_request(
                "/chat/users/me/messages/{}".format(kwargs.get("messageId")), params=kwargs
        )
