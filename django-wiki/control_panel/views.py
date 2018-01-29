# from django.shortcuts import render
# from django.contrib.auth.models import User, Group
# from django.apps import apps
#
# def overview(request):
#     app_list = []
#     app_list.append(apps.get_model(app_label=User._meta.app_label, model_name="User"))
#     app_list.append(apps.get_model(app_label=Group._meta.app_label, model_name="Group"))
#
#     return render(request, "control_panel_overview.html", {'app_list': app_list})
