from fcm_django.models import FCMDevice


class FCM:
    def send_notification(user_id, title, message, data):
        try:
            device = FCMDevice.objects.get(pk=user_id)
            result = device.send_message(title=title, body=message, data=data)
            return result
        except:
            pass
