"""Zoom.us REST API Python Client -- Chat Messages component"""

from zoomapi import util
from zoomapi.components import base

class ChatChannelsComponentV2(base.BaseComponent):
    """Component dealing with all chat channels related matters"""

    # list all the channels
    def list(self, **kwargs):
        return self.get_request("/chat/users/me/channels")

    # create a channel
    def create(self, **kwargs):
        return self.post_request("chat/users/me/channels", data=kwargs)
    
    # get a channel
    def get(self, **kwargs):
        util.require_keys(kwargs, "channelId")
        return self.get_request(
                "/chat/channels/{}".format(kwargs.get("channelId")), params=kwargs
        )

    # update channel name
    def update(self, **kwargs):
        util.require_keys(kwargs, "channelId")
        util.require_keys(kwargs, "name")
        print(kwargs.get("name"))
        return self.patch_request(
                "/chat/channels/{}".format(kwargs.get("channelId")), data=kwargs
        )
    
    # delete a channel
    def delete(self, **kwargs):
        util.require_keys(kwargs, "channelId")
        return self.delete_request(
                "/chat/channels/{}".format(kwargs.get("channelId")), params=kwargs
        )
    
    # list the channel members 
    def members(self, **kwargs):
        util.require_keys(kwargs, "channelId")
        return self.get_request(
                "/chat/channels/{}/members".format(kwargs.get("channelId")), params=kwargs
        )

    # invite new member
    def invite(self, **kwargs):
        util.require_keys(kwargs, "channelId")
        return self.post_request(
                "/chat/channels/{}/members".format(kwargs.get("channelId")), data=kwargs
        )

    # join a channel
    def join(self, **kwargs):
        util.require_keys(kwargs, "channelId")
        return self.post_request(
                "/chat/channels/{}/members/me".format(kwargs.get("channelId"))
        )
    
    # leave the channel
    def leave(self, **kwargs):
        util.require_keys(kwargs, "channelId")
        return self.delete_request(
                "/chat/channels/{}/members/me".format(kwargs.get("channelId"))
        )

    # remove a member
    def remove(self, **kwargs):
        util.require_keys(kwargs, "channelId")
        util.require_keys(kwargs, "memberId")

        return self.delete_request(
                "/chat/channels/{}/members/{}".format(kwargs.get("channelId"),kwargs.get("memberId"))
        )
    
    
