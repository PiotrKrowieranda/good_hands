# from django.contrib.auth.backends import ModelBackend
# from leave_it.views import LoginView
#
# class CustomEmailAuthBackend(ModelBackend):
#     def authenticate(self, request, email=None, password=None, **kwargs):
#         try:
#             user = self.user_model.objects.get(email=email)
#             if user.check_password(password):
#                 return user
#         except self.user_model.DoesNotExist:
#             return None