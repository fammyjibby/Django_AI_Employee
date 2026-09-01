from django.contrib import admin
from SupportAgent.models import Conversation, Message, AgentLog

# Register your models here.
admin.site.register(Conversation)
admin.site.register(Message)
admin.site.register(AgentLog)
