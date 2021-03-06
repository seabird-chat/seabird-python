# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: seabird.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import AsyncGenerator, Dict, List, Optional

import betterproto
import grpclib

from . import common


@dataclass
class Event(betterproto.Message):
    # Events sent by chat backends.
    message: common.MessageEvent = betterproto.message_field(1, group="inner")
    private_message: common.PrivateMessageEvent = betterproto.message_field(
        2, group="inner"
    )
    mention: common.MentionEvent = betterproto.message_field(3, group="inner")
    command: common.CommandEvent = betterproto.message_field(4, group="inner")
    action: common.ActionEvent = betterproto.message_field(5, group="inner")
    private_action: common.PrivateActionEvent = betterproto.message_field(
        6, group="inner"
    )
    # Events sent by plugins and other clients. Generally, these are only needed
    # for special cases.
    send_message: "SendMessageEvent" = betterproto.message_field(7, group="inner")
    send_private_message: "SendPrivateMessageEvent" = betterproto.message_field(
        8, group="inner"
    )
    perform_action: "PerformActionEvent" = betterproto.message_field(9, group="inner")
    perform_private_action: "PerformPrivateActionEvent" = betterproto.message_field(
        10, group="inner"
    )


@dataclass
class SendMessageEvent(betterproto.Message):
    """
    SendMessageEvent will be emitted whenever a plugin or other client calls
    SendMessage. Note that this will be emitted every time SendMessage is
    called, not when it succeeds. The additional sender param refers to the
    client sending the message.
    """

    sender: str = betterproto.string_field(1)
    inner: "SendMessageRequest" = betterproto.message_field(2)


@dataclass
class SendPrivateMessageEvent(betterproto.Message):
    """
    SendPrivateMessageEvent will be emitted whenever a plugin or other client
    calls SendPrivateMessage. Note that this will be emitted every time
    SendPrivateMessage is called, not when it succeeds.The additional sender
    param refers to the client sending the message.
    """

    sender: str = betterproto.string_field(1)
    inner: "SendPrivateMessageRequest" = betterproto.message_field(2)


@dataclass
class PerformActionEvent(betterproto.Message):
    """
    PerformActionEvent will be emitted whenever a plugin or other client calls
    PerformAction. Note that this will be emitted every time PerformAction is
    called, not when it succeeds. The additional sender param refers to the
    client sending the message.
    """

    sender: str = betterproto.string_field(1)
    inner: "PerformActionRequest" = betterproto.message_field(2)


@dataclass
class PerformPrivateActionEvent(betterproto.Message):
    """
    PerformPrivateActionEvent will be emitted whenever a plugin or other client
    calls PerformPrivateAction. Note that this will be emitted every time
    PerformPrivateAction is called, not when it succeeds. The additional sender
    param refers to the client sending the message.
    """

    sender: str = betterproto.string_field(1)
    inner: "PerformPrivateActionRequest" = betterproto.message_field(2)


@dataclass
class StreamEventsRequest(betterproto.Message):
    # A registry of commands this plugin responds to. A plugin MUST register all
    # commands it responds to in order to receive those events. The
    # CommandMetadata's name MUST match the map key, or an error will be
    # returned. NOTE: help is a reserved command and cannot be registered by
    # plugins.
    commands: Dict[str, "CommandMetadata"] = betterproto.map_field(
        1, betterproto.TYPE_STRING, betterproto.TYPE_MESSAGE
    )


@dataclass
class CommandMetadata(betterproto.Message):
    """
    CommandMetadata groups together a command's name along with short in-line
    help and the full private help. An example for the "help" command might be
    a name of "help", a short_help of "<command>" and an long help of "With no
    arguments, lists all available commands. With an argument, display the long
    help for an item."
    """

    name: str = betterproto.string_field(1)
    short_help: str = betterproto.string_field(2)
    full_help: str = betterproto.string_field(3)


@dataclass
class PerformActionRequest(betterproto.Message):
    """Perform an action in a given channel."""

    channel_id: str = betterproto.string_field(1)
    text: str = betterproto.string_field(2)


@dataclass
class PerformActionResponse(betterproto.Message):
    pass


@dataclass
class PerformPrivateActionRequest(betterproto.Message):
    """Perform an action in a private message."""

    user_id: str = betterproto.string_field(1)
    text: str = betterproto.string_field(2)


@dataclass
class PerformPrivateActionResponse(betterproto.Message):
    pass


@dataclass
class SendMessageRequest(betterproto.Message):
    """Send a message to a given a channel."""

    channel_id: str = betterproto.string_field(1)
    text: str = betterproto.string_field(2)


@dataclass
class SendMessageResponse(betterproto.Message):
    pass


@dataclass
class SendPrivateMessageRequest(betterproto.Message):
    """Send a private message to a given user."""

    user_id: str = betterproto.string_field(1)
    text: str = betterproto.string_field(2)


@dataclass
class SendPrivateMessageResponse(betterproto.Message):
    pass


@dataclass
class JoinChannelRequest(betterproto.Message):
    """Request to join a channel."""

    backend_id: str = betterproto.string_field(1)
    # NOTE: this channel_name is the only place name is used for an identifier -
    # all other times channels will be referred to by ID.
    channel_name: str = betterproto.string_field(2)


@dataclass
class JoinChannelResponse(betterproto.Message):
    pass


@dataclass
class LeaveChannelRequest(betterproto.Message):
    """Request to leave a channel."""

    channel_id: str = betterproto.string_field(1)
    exit_message: str = betterproto.string_field(2)


@dataclass
class LeaveChannelResponse(betterproto.Message):
    pass


@dataclass
class ListBackendsRequest(betterproto.Message):
    """Request to list all connected backends."""

    pass


@dataclass
class ListBackendsResponse(betterproto.Message):
    backends: List[common.Backend] = betterproto.message_field(1)


@dataclass
class BackendInfoRequest(betterproto.Message):
    """Get info about a specific connected backend."""

    backend_id: str = betterproto.string_field(1)


@dataclass
class BackendInfoResponse(betterproto.Message):
    backend: common.Backend = betterproto.message_field(1)
    metadata: Dict[str, str] = betterproto.map_field(
        2, betterproto.TYPE_STRING, betterproto.TYPE_STRING
    )


@dataclass
class ListChannelsRequest(betterproto.Message):
    backend_id: str = betterproto.string_field(1)


@dataclass
class ListChannelsResponse(betterproto.Message):
    channels: List[common.Channel] = betterproto.message_field(1)


@dataclass
class ChannelInfoRequest(betterproto.Message):
    channel_id: str = betterproto.string_field(1)


@dataclass
class ChannelInfoResponse(betterproto.Message):
    channel: common.Channel = betterproto.message_field(1)


@dataclass
class UpdateChannelInfoRequest(betterproto.Message):
    channel_id: str = betterproto.string_field(1)
    topic: str = betterproto.string_field(2)


@dataclass
class UpdateChannelInfoResponse(betterproto.Message):
    pass


@dataclass
class CoreInfoRequest(betterproto.Message):
    """A request for metadata about the running core instance."""

    pass


@dataclass
class CoreInfoResponse(betterproto.Message):
    """Metadata about the running core instance."""

    startup_timestamp: int = betterproto.uint64_field(1)
    current_timestamp: int = betterproto.uint64_field(2)


@dataclass
class CommandsRequest(betterproto.Message):
    pass


@dataclass
class CommandsResponse(betterproto.Message):
    commands: Dict[str, "CommandMetadata"] = betterproto.map_field(
        1, betterproto.TYPE_STRING, betterproto.TYPE_MESSAGE
    )


class SeabirdStub(betterproto.ServiceStub):
    async def stream_events(
        self, *, commands: Optional[Dict[str, "CommandMetadata"]] = None
    ) -> AsyncGenerator[Event, None]:
        request = StreamEventsRequest()
        request.commands = commands

        async for response in self._unary_stream(
            "/seabird.Seabird/StreamEvents",
            request,
            Event,
        ):
            yield response

    async def perform_action(
        self, *, channel_id: str = "", text: str = ""
    ) -> PerformActionResponse:
        """Chat actions"""

        request = PerformActionRequest()
        request.channel_id = channel_id
        request.text = text

        return await self._unary_unary(
            "/seabird.Seabird/PerformAction",
            request,
            PerformActionResponse,
        )

    async def perform_private_action(
        self, *, user_id: str = "", text: str = ""
    ) -> PerformPrivateActionResponse:
        request = PerformPrivateActionRequest()
        request.user_id = user_id
        request.text = text

        return await self._unary_unary(
            "/seabird.Seabird/PerformPrivateAction",
            request,
            PerformPrivateActionResponse,
        )

    async def send_message(
        self, *, channel_id: str = "", text: str = ""
    ) -> SendMessageResponse:
        request = SendMessageRequest()
        request.channel_id = channel_id
        request.text = text

        return await self._unary_unary(
            "/seabird.Seabird/SendMessage",
            request,
            SendMessageResponse,
        )

    async def send_private_message(
        self, *, user_id: str = "", text: str = ""
    ) -> SendPrivateMessageResponse:
        request = SendPrivateMessageRequest()
        request.user_id = user_id
        request.text = text

        return await self._unary_unary(
            "/seabird.Seabird/SendPrivateMessage",
            request,
            SendPrivateMessageResponse,
        )

    async def join_channel(
        self, *, backend_id: str = "", channel_name: str = ""
    ) -> JoinChannelResponse:
        request = JoinChannelRequest()
        request.backend_id = backend_id
        request.channel_name = channel_name

        return await self._unary_unary(
            "/seabird.Seabird/JoinChannel",
            request,
            JoinChannelResponse,
        )

    async def leave_channel(
        self, *, channel_id: str = "", exit_message: str = ""
    ) -> LeaveChannelResponse:
        request = LeaveChannelRequest()
        request.channel_id = channel_id
        request.exit_message = exit_message

        return await self._unary_unary(
            "/seabird.Seabird/LeaveChannel",
            request,
            LeaveChannelResponse,
        )

    async def update_channel_info(
        self, *, channel_id: str = "", topic: str = ""
    ) -> UpdateChannelInfoResponse:
        request = UpdateChannelInfoRequest()
        request.channel_id = channel_id
        request.topic = topic

        return await self._unary_unary(
            "/seabird.Seabird/UpdateChannelInfo",
            request,
            UpdateChannelInfoResponse,
        )

    async def list_backends(self) -> ListBackendsResponse:
        """Chat backend introspection"""

        request = ListBackendsRequest()

        return await self._unary_unary(
            "/seabird.Seabird/ListBackends",
            request,
            ListBackendsResponse,
        )

    async def get_backend_info(self, *, backend_id: str = "") -> BackendInfoResponse:
        request = BackendInfoRequest()
        request.backend_id = backend_id

        return await self._unary_unary(
            "/seabird.Seabird/GetBackendInfo",
            request,
            BackendInfoResponse,
        )

    async def list_channels(self, *, backend_id: str = "") -> ListChannelsResponse:
        """Chat connection introspection"""

        request = ListChannelsRequest()
        request.backend_id = backend_id

        return await self._unary_unary(
            "/seabird.Seabird/ListChannels",
            request,
            ListChannelsResponse,
        )

    async def get_channel_info(self, *, channel_id: str = "") -> ChannelInfoResponse:
        request = ChannelInfoRequest()
        request.channel_id = channel_id

        return await self._unary_unary(
            "/seabird.Seabird/GetChannelInfo",
            request,
            ChannelInfoResponse,
        )

    async def get_core_info(self) -> CoreInfoResponse:
        """Seabird introspection"""

        request = CoreInfoRequest()

        return await self._unary_unary(
            "/seabird.Seabird/GetCoreInfo",
            request,
            CoreInfoResponse,
        )

    async def registered_commands(self) -> CommandsResponse:
        request = CommandsRequest()

        return await self._unary_unary(
            "/seabird.Seabird/RegisteredCommands",
            request,
            CommandsResponse,
        )
