from rest_framework import permissions



class IsStaff(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.access == 1:
            return True
        return False


class IsTeacher(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.user.is_teacher:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if obj.teacher.access == 3:
            return True
        return False
        