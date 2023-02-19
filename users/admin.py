from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django import forms
from django.contrib.auth.models import Group
from django.utils.safestring import mark_safe

from users.models import *

class UserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        if bool(self.cleaned_data['workPhone']):
            user.workPhone = self.cleaned_data['workPhone'].replace(" ", "")

        if bool(self.cleaned_data['personalPhone']):
            user.personalPhone = self.cleaned_data['personalPhone'].replace(" ", "")

        if bool(self.cleaned_data['whatsapp']):
            user.whatsapp = self.cleaned_data['whatsapp'].lower();
        
        if bool(self.cleaned_data['instagram']):
            user.instagram = self.cleaned_data['instagram'].lower();
        
        if bool(self.cleaned_data['facebook']):
            user.facebook = self.cleaned_data['facebook'].lower();
        
        if bool(self.cleaned_data['linkedin']):
            user.linkedin = self.cleaned_data['linkedin'].lower();
        
        if bool(self.cleaned_data['telegram']):
            user.telegram = self.cleaned_data['telegram'].lower();
        
        if bool(self.cleaned_data['snapchat']):
            user.snapchat = self.cleaned_data['snapchat'].lower();
        
        if bool(self.cleaned_data['tiktok']):
            user.tiktok = self.cleaned_data['tiktok'].lower();
        
        if bool(self.cleaned_data['twitter']):
            user.twitter = self.cleaned_data['twitter'].lower();
        
        if bool(self.cleaned_data['youtube']):
            user.youtube = self.cleaned_data['youtube'].lower();
        
        if bool(self.cleaned_data['email']):
            user.email = self.cleaned_data['email'];
        else:
            user.email = None;
        if 'password' in self.changed_data:
            user.set_password(self.cleaned_data["password"]);
        if commit:
            user.save()
        return user


fieldsets = (
        (None, {'fields': (
            'is_superuser',
            'is_staff',
            'fullname',
            'company',
            'position',
            'workPhone',
            'personalPhone',
            'email',
            'workEmail',
            'workWebsite',
            'otherWebsite',
            'fontFamily',
            'avatar',
            'avatarHidden',
            'bg',
            'uniqueId',
            'whatsapp',
            'instagram',
            'facebook',
            'linkedin',
            'telegram',
            'snapchat',
            'tiktok',
            'twitter',
            'youtube',
            'resetPasswordUUID',
            'resetPasswordDate',
            'title',
            'subtitle',
            'description',
            'address',
            'password',
        )}),
        )


class CustomUserAdmin(UserAdmin):
    search_fields = ['email'];
    add_form = UserCreationForm
    form = UserCreationForm
    list_display = ['uniqueId', 'email', 'get_avatar_photo']
    list_display_links = ['email', 'uniqueId']
    ordering = ("-id",)

    def get_avatar_photo(self, object):
        if object.avatar:
            return mark_safe(f"<img src='{object.avatar.url}' width=50>");

    get_avatar_photo.short_description = "Аватар"

    fieldsets = fieldsets

    add_fieldsets = fieldsets


class UserImageAdmin(admin.ModelAdmin):
    list_display = ['user', 'image']
    list_filter = ['user']

@admin.register(SaveContactCount)
class SaveContactCountAdmin(admin.ModelAdmin):
    ...


admin.site.register(User, CustomUserAdmin);
admin.site.unregister(Group);
admin.site.register(UserImage, UserImageAdmin);
admin.site.register(UserVideo);

