from rest_framework import permissions



class UpdateOwnProfile(permissions.BasePermission):
    """ Allow users to edit their own profiles """

    def has_object_permission(self, request, view, obj):
        """ Check user has permissions to edit their own profiles """

        #checks if the action falls under SAFE_METHODS : GET
        if request.method in permissions.SAFE_METHODS:
            return True

        #Comparing the id of the user allowed to make changes is same as the
        #Id of the validated user
        #Will only allow edits for the profile the user is logged in with
        return obj.id == request.user.id
