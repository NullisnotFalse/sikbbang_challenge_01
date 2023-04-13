from django.db import models
#from user.models import UserModel


class QnaModel(models.Model):
    class Meta:
        db_table = "Qna_register"
#    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
