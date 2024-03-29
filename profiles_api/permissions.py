from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    ''' Allow User to Update their own profile '''

    def has_object_permission(self, request, view, obj):
        ''' Check user is trying to change their own profile '''
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.id == request.user.id
    

class UpdateOwnStatus(permissions.BasePermission):
    ''' Allow User to Update their own Status '''

    def has_object_permission(self, request, view, obj):
        ''' Check user is trying to change their own status '''
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user_profile.id == request.user.id