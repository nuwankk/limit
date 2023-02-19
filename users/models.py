import uuid
from constants.main import parametersForNull
from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.db import models
from users.choices import FONTS
from users.managers import CustomManager
from utils.rename import Rename
from django.core.validators import RegexValidator
from django.core.validators import EmailValidator

avatarRename = Rename('images/avatars/');
bgRename = Rename('images/backgrounds');
userimagesRename = Rename('images/user_images');


FILTER_CHOICES = (
    ('day', 'day'),
    ('month', 'month'),
    ('year', 'year'),
)



# class VideoUser(models.Model):
#    video = models.URLField('video')


class User(AbstractUser):
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users";

    def __str__(self):
        return self.uniqueId.__str__();

    username = None;
    date_joined = None;
    first_name = None;
    last_name = None;
    last_login = None;
    is_active = models.BooleanField(default=True);
    is_staff = models.BooleanField(default=False);
    is_superuser = models.BooleanField(default=False);
    password = models.CharField(max_length=128,
                                default=make_password(settings.DEFAULT_PASSWORD));

    fullname = models.CharField(max_length=300, **parametersForNull);
    company = models.CharField(max_length=300, **parametersForNull);
    position = models.CharField(max_length=300, **parametersForNull);
    # workPhone = models.CharField(max_length=300, **parametersForNull);
    # personalPhone = models.CharField(max_length=300, **parametersForNull);

    workPhone = models.CharField(max_length=300, **parametersForNull);

    personalPhone = models.CharField(max_length=300, **parametersForNull);

    workEmail = models.EmailField(**parametersForNull);
    # video = models.ManyToManyField(VideoUser, verbose_name='Видео', blank=True, null=True, related_name='detail_video')
    # email = models.EmailField(default=None, unique=True, **parametersForNull);

    email = models.EmailField(unique=True, validators=[EmailValidator(message="Please enter a valid email address.")])

    workWebsite = models.URLField(**parametersForNull);
    otherWebsite = models.URLField(**parametersForNull);
    fontFamily = models.CharField(max_length=100, default=FONTS[0][0], choices=FONTS,
                                  **parametersForNull);

    avatar = models.ImageField(upload_to=avatarRename.rename, **parametersForNull);
    avatarHidden = models.BooleanField(default=True)
    bg = models.ImageField(upload_to=bgRename.rename, **parametersForNull);

    uniqueId = models.UUIDField(unique=True, **parametersForNull);

    # socials
    whatsapp = models.URLField(verbose_name="Whatsapp", **parametersForNull);
    instagram = models.URLField(verbose_name="Instagram", **parametersForNull);
    facebook = models.URLField(verbose_name="Facebook", **parametersForNull);
    linkedin = models.URLField(verbose_name="Linkedin", **parametersForNull);
    telegram = models.URLField(verbose_name="Telegram", **parametersForNull);
    # snapchat = models.URLField(verbose_name="Snapchat", **parametersForNull);
    # tiktok = models.URLField(verbose_name="Tiktok", **parametersForNull);
    
    snapchat = models.URLField(verbose_name="Snapchat", **parametersForNull);
    
    tiktok = models.URLField(verbose_name="Tiktok",**parametersForNull);



    twitter = models.URLField(verbose_name="Twitter", **parametersForNull);
    youtube = models.URLField(verbose_name="Youtube", **parametersForNull);
    wechat = models.URLField(verbose_name="Wechat", **parametersForNull);

    resetPasswordUUID = models.UUIDField(**parametersForNull);
    resetPasswordDate = models.BigIntegerField(**parametersForNull);

    welcome = models.CharField(max_length=200, **parametersForNull);
    title = models.CharField(max_length=200, **parametersForNull);
    subtitle = models.CharField(max_length=200, **parametersForNull);
    description = models.TextField(**parametersForNull);
    address = models.CharField(max_length=350, **parametersForNull);

    count_filter_period = models.CharField(max_length=10, choices=FILTER_CHOICES, default='day')

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    objects = CustomManager()

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.id:
            self.uniqueId = uuid.uuid4()
        super(User, self).save(force_insert=False, force_update=False, using=None, update_fields=None)


class UserImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_images')
    image = models.ImageField(upload_to=userimagesRename.rename, blank=True)

    def __str__(self):
        return str(self.user.uniqueId)


class UserVideo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_video')
    image = models.URLField(blank=True)

    def __str__(self):
        return str(self.user.uniqueId)


class SaveContactCount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='save_contact_user')
    count = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} {self.count}'


