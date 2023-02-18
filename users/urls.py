from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from users.views import UserMVS, UserLoginView, ResetPasswordMVS, UpdateUserAvatarView, DownloadVCF, \
    CustomTokenRefreshView, UserImageMVS, UserImagesMVS, ShowHideAvatarView, UserVideoMVS, UserVideosMVS, \
    SaveContactCountListAPiView, SaveContactCountRetrieveAPIView, SaveContactCountCreateAPIView

from .views import SendMailAPIView, SendMailUserApiView

userPlural = {
    'get': 'list',
    'post': 'create'
}

useSingle = {
    'get': 'retrieve',
    'patch': 'update'
}

useSingle2 = {
    'get': 'retrieve',
    'post': 'create',
}

useSingle3 = {
    'get': 'retrieve',
    'patch': 'update',
    'post': 'create',
    'delete': 'destroy'
}

urlpatterns = [
    path('', UserMVS.as_view(userPlural)),
    path('avatar/', UpdateUserAvatarView.as_view()),
    path('<uuid:uniqueId>/', UserMVS.as_view(useSingle)),
    path('images/<uuid:uniqueId>/', UserImagesMVS.as_view(useSingle2)),
    path('image/<int:pk>/', UserImageMVS.as_view(useSingle3)),
    path('videos/<uuid:uniqueId>/', UserVideosMVS.as_view(useSingle2)),
    path('video/<int:pk>/', UserVideoMVS.as_view(useSingle3)),

    path('login/', UserLoginView.as_view()),
    path('check/', CustomTokenRefreshView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),

    path('reset-password/', ResetPasswordMVS.as_view({'post': 'create'})),
    path('reset-password/<uuid:resetPasswordUUID>/', ResetPasswordMVS.as_view({'get': 'retrieve', 'patch': 'update'})),
    path('save-contact/<uuid:uniqueId>/', DownloadVCF.as_view()),
    path('send-mail-message/',  SendMailAPIView.as_view()),
    path('send-mail-order/', SendMailUserApiView.as_view()),
    path('avatar-flip/<uuid:uniqueId>/', ShowHideAvatarView.as_view()),

    path('save-contact/counts/', SaveContactCountListAPiView.as_view()),
    path('save-contact/count/', SaveContactCountCreateAPIView.as_view()),
    path('save-contact/count/<uuid:uniqueId>/', SaveContactCountRetrieveAPIView.as_view()),


] 
