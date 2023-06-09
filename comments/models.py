from django.db import models
from user.models import UserModel
from challenge.models import ChallengeModel

# Create your models here.


class CommentModel(models.Model):
    class Meta:
        db_table = "my_comment"

    comment_challenge = models.ForeignKey(
        ChallengeModel, on_delete=models.CASCADE)
    # UserModel의 id값을 참조해서 comment_writer에 담음.
    comment_writer = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    comment_created_at = models.DateTimeField(
        auto_now_add=True)  # 이게 이미 날짜 찍는거
    # 개행을 할 수 있도록 TextField로 한다. CharField가 아니라.
    comment_content = models.TextField(max_length=200)
    # DB이미지필드에 이미지이름을 넣으며 동시에 이미지 실물은 media의 하위폴더 images/ 경로로 저장.
    comment_image = models.ImageField(
        upload_to='images/', blank=True, null=True)
