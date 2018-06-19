from django.db import models

__all__ = (
    'TwitterUser',
    'Relation',
)


class TwitterUser(models.Model):
    """
    User 간의 관계는 2종류로 나뉨
    follow
    block

    관계를 나타내는 Relation클래스 사용(중계 모델)
    """
    name = models.CharField(max_length=50)
    relations = models.ManyToManyField(
        'self',
        symmetrical=False,
        through='Relation',
    )

    def __str__(self):
        return self.name

    @property
    def following_relations(self):
        # 내가 follow하고 있는 Relation들을 리턴
        # (내가 Relation의 from_user이며, relation_type이 'f'인 경우)

        # return Relation.objects.filter(from_user=self, relation_type='f')
        return self.relations_by_from_user.filter(relation_type='f')

    @property
    def follower_relations(self):
        # 내가 follow하고 있는 Relation들을 리턴
        # (내가 Relation의 to_user이며, relation_type이 'f'인 경우)

        # return Relation.objects.filter(to_user=self, relation_type='f')
        return self.relations_by_to_user.filter(relation_type='f')

    @property
    def block_relations(self):
        # 내가 block하고 있는 Relation들을 리턴
        # (내가 Relation의 from_user이며, relation_type이 'b'인 경우)
        # return Relation.objects.filter(from_user=self, relation_type='b')
        return self.relations_by_from_user.filter(relation_type='b')


class Relation(models.Model):
    """
    TwitterUser간의 MTM관계를 정의
        from_user
        to_user
        follow인자, block인자를 전달
    """
    CHOICES_RELATION_TYPE = (
        ('f', 'Follow'),
        ('b', 'Block'),
    )
    from_user = models.ForeignKey(
        TwitterUser,
        on_delete=models.CASCADE,
        related_name='relations_by_from_user',
    )
    to_user = models.ForeignKey(
        TwitterUser,
        on_delete=models.CASCADE,
        related_name='relations_by_to_user',
    )

    # 입력 값을 제한하는 choices 옵션 추가
    relation_type = models.CharField(
        max_length=1,
        choices=CHOICES_RELATION_TYPE,
    )

    # 관계의 생성일을 기록
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # get_FOO_display() 함수를 사용해서 choices를 사용한 필드의 출력값을 사용
        return 'from({}), to({}), {}'.format(
            self.from_user.name,
            self.to_user.name,
            self.get_relation_type_display(),
        )
