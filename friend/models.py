from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class FriendRequest(models.Model):
    User = get_user_model()
    class Status(models.TextChoices):
        PENDING = "P", _("Pending")
        ACCEPTED = "A", _("Accepted")
        REJECTED = "R", _("Rejected")

    from_user = models.ForeignKey(
        User, related_name="sent_requests", on_delete=models.CASCADE
    )
    to_user = models.ForeignKey(
        User, related_name="received_requests", on_delete=models.CASCADE
    )
    status = models.CharField(
        max_length=20,
        choices=Status,
        default=Status.PENDING,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("from_user", "to_user")

    def __str__(self):
        return f"{self.from_user} -> {self.to_user} [{self.status}]"
