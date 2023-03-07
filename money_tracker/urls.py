from django.urls import path
from money_tracker.views import show_tracker
from money_tracker.views import create_transaction
from money_tracker.views import show_xml #sesuaikan dengan nama fungsi yang dibuat
from money_tracker.views import show_json #sesuaikan dengan nama fungsi yang dibuat
from money_tracker.views import show_xml_by_id, show_json_by_id #sesuaikan dengan nama fungsi yang dibuat
from money_tracker.views import register #sesuaikan dengan nama fungsi yang dibuat
from money_tracker.views import login_user #sesuaikan dengan nama fungsi yang dibuat
from money_tracker.views import logout_user #sesuaikan dengan nama fungsi yang dibuat


app_name = 'money_tracker'

urlpatterns = [
    path('', show_tracker, name='show_tracker'),
    path('create', create_transaction, name='create_transaction'),
    path('json/', show_json, name='show_json'), #sesuaikan dengan nama fungsi yang dibuat
    path('xml/', show_xml, name='show_xml'), #sesuaikan dengan nama fungsi yang dibuat
    path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'),

    path('register/', register, name='register'), #sesuaikan dengan nama fungsi yang dibuat

    path('login/', login_user, name='login'), #sesuaikan dengan nama fungsi yang dibuat


    path('logout/', logout_user, name='logout'), #sesuaikan dengan nama fungsi yang dibuat






]



