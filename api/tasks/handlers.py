from functools import singledispatch
from typing import Callable

from lib.app_lib.enums import NotificationType
from lib.app_lib.messages.message import RenameFileRequest
from lib.app_lib.log import get_logger
from lib.app_lib.services.main import Service
from lib.app_lib.services.notification_service import NotificationService

from app.tools import send_to_all
from tasks.models import File

logger = get_logger('tasks.handlers')


@singledispatch
def handler(
        request,
        service: Service,
        notifications: 'NotificationService',
        message_ack: Callable
):
    """
    Generic handler

    Args:
        request (Request): _request_
        service (Service): _service_
        notifications (NotificationService): _notification_service_
        message_ack (Callable): _message_ack_
    """
    logger.warning('Unregister type[%s]', type(request))
    message_ack()


@handler.register
def _(
        request: 'RenameFileRequest',
        service: Service,
        notifications: 'NotificationService',
        message_ack: Callable
):
    """

    Args:
        request (RenameFileRequest): _description_
        service (Service): _description_
        notifications (NotificationService): _description_
        message_ack (Callable): _description_
    """
    instance = File.objects.get(pk=request.id)
    _name = ""
    _extension = ""

    try:
        values = instance.name.split('.')
        _name = values[0]
        _extension = values[1]
    except Exception as e:
        logger.info(e)

    instance.name = _name
    instance.extension = _extension
    instance.save()

    send_to_all(
        data={"action": "update_files"},
        notifications=notifications,
        notification_type=NotificationType.UPDATE_FILES
    )
    message_ack()
