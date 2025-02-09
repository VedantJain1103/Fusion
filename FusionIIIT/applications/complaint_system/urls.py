from django.conf.urls import url,include

from . import views

app_name = 'complaint'

urlpatterns = [

    url(r'^$', views.check, name='complaint'),
    url(r'^login/$', views.login1, name='complaint'),
    url(r'^user/$', views.user),
    url(r'^user/caretakerfb/$' , views.caretaker_feedback),
    url(r'^user/(?P<complaint_id>[0-9]+)/$', views.submitfeedback),
    url(r'^user/detail/(?P<detailcomp_id1>[0-9]+)/$', views.detail,name='detail'),
    url(r'^user/check_complaint/$', views.save_comp),   
    
    # caretaker
    url(r'^caretaker/$', views.caretaker, name='caretaker'),
    url(r'^caretaker/feedback/(?P<feedcomp_id>[0-9]+)/$', views.feedback_care),
    url(r'^caretaker/pending/(?P<cid>[0-9]+)/$', views.resolvepending),
    url(r'^caretaker/detail/(?P<detailcomp_id1>[0-9]+)/$', views.detail),
    url(r'^caretaker/search_complaint$', views.search_complaint),
    url(r'^caretaker/(?P<complaint_id>[0-9]+)/(?P<status>[0-9]+)/$', views.changestatus),
 
    # secincharge
    url(r'^secincharge/$', views.section_incharge, name='secincharge'),
    url(r'^secincharge/feedback/(?P<feedcomp_id>[0-9]+)/$', views.feedback_care),
    url(r'^secincharge/worker_id_know_more/(?P<wid>[0-9]+)/complaint_reassign/(?P<cid>[0-9]+)/discharge_worker/$', views.discharge_worker,name='discharge_worker'),
    url(r'^secincharge/worker_id_know_more/(?P<work_id>[0-9]+)/$', views.worker_id_know_more, name='come_back_to_this'),
    url(r'^secincharge/worker_id_know_more/(?P<wid>[0-9]+)/complaint_reassign/(?P<iid>[0-9]+)/$', views.complaint_reassign, name='complaint_reassign'),
    url(r'^secincharge/detail2/(?P<detailcomp_id1>[0-9]+)/$', views.detail2,name='detail2'),  
    url(r'^secincharge/worker_id_know_more/(?P<work_id>[0-9]+)/removew/$', views.removew),
    url(r'^secincharge/(?P<comp_id1>[0-9]+)/$', views.assign_worker,name='assign_worker'),
    url(r'^secincharge/deletecomplaint/(?P<comp_id1>[0-9]+)/$', views.deletecomplaint),

    # supervisor
    url(r'^supervisor/$', views.supervisor),
    url(r'^supervisor/feedback/(?P<feedcomp_id>[0-9]+)/$', views.feedback_super),
    url(r'^supervisor/caretaker_id_know_more/(?P<caretaker_id>[0-9]+)/$', views.caretaker_id_know_more),
    url(r'^supervisor/caretaker_id_know_more/(?P<caretaker_id>[0-9]+)/complaint_reassign_super/(?P<iid>[0-9]+)/$', views.complaint_reassign_super, name = 'complaint_reassign_super'),
    url(r'^supervisor/detail3/(?P<detailcomp_id1>[0-9]+)/$', views.detail3, name = 'detail3'),  
    
    # api's for complaint system
    url(r'^api/',include('applications.complaint_system.api.urls'))

]