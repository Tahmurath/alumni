from django.urls import path

from . import views


# from dal import autocomplete


urlpatterns = [
    path('list', views.StudentListView.as_view(), name='students'),
    path('test', views.test, name='test'),
    path('student/<int:pk>', views.StudentDetailView.as_view(), name='student'),
    path('student2/<int:primary_key>', views.student_detail_view, name='student2'),
    path('newstdstart', views.new_student_start, name='newstdstart'),
    path('student/<int:primary_key>/newstdverify/<str:hashcode>', views.new_student_verify, name='newstdverify'),
    path('student/<int:primary_key>/newstdcontinue', views.new_student_continue, name='newstdcontinue'),
    path('student/<int:primary_key>/edit/', views.edit_student, name='edit_student'),
    path('create/', views.StudentCreate.as_view(), name='student_create'),
    path('student/<int:pk>/update/', views.StudentUpdate.as_view(), name='student_update'),
    path('student/<int:pk>/delete/', views.StudentDelete.as_view(), name='student_delete'),
    # url('test-autocomplete/$', autocomplete.Select2QuerySetView.as_view(model=User), name='select2_fk'),
]
