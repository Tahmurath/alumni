from django.shortcuts import render
from django.views import generic
from .models import Student
from django.shortcuts import Http404
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from .forms import StudentForm
from django.http import HttpResponseRedirect
from users.forms import NewStdForm
from users.forms import NewStdVerifyForm
from users.forms import EtelaateFardi
from users.models import User, Sabteahval
# import hashlib
from django.urls import reverse
# from django.views.decorators.csrf import csrf_protect

import datetime
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.forms.models import model_to_dict
from django.contrib import messages
from django.shortcuts import redirect
from jalali_date import datetime2jalali, date2jalali


# Create your views here.


class StudentDetailView(generic.DetailView):
    model = Student
    context_object_name = 'student'
    template_name = 'students/student.html'


class StudentListView(PermissionRequiredMixin, LoginRequiredMixin, generic.ListView):

    def handle_no_permission(self):
        # add custom message
        return redirect('/accounts/login/?next=/students/list')
        # return HttpResponseRedirect(reverse_lazy('login'))
        # messages.error(self.request, 'You have no permission')
        # return super(StudentListView, self).handle_no_permission()

    permission_required = 'students.can_see_all_students'
    raise_exception = True
    model = Student
    paginate_by = 5
    context_object_name = 'student_list'
    # queryset = Student.objects.filter(title__icontains='war')[:5]
    template_name = 'students/student_list.html'


@permission_required('students.can_see_all_students')
def test(request):
    context = {
        'num_students': 12,
    }

    return render(request, 'test.html', context=context)


def student_detail_view(request, primary_key):
    try:
        student = Student.objects.get(pk=primary_key)
    except Student.DoesNotExist:
        raise Http404('Book does not exist')

    return render(request, 'students/student.html', context={'student': student})


def book_detail_view(request, primary_key):
    student = get_object_or_404(Student, pk=primary_key)
    return render(request, 'students/student.html', context={'student': student})


class StudentCreate(CreateView):
    model = Student
    # fields = '__all__'
    form_class = StudentForm
    success_url = reverse_lazy('students')
    # initial = {'date_of_death': '05/01/2018'}


class StudentUpdate(UpdateView):
    model = Student
    form_class = StudentForm
    # fields = ['center_id', 'field_id', 'std_code', 'term_id', 'military_id', 'start_date', 'stop_date']

    success_url = reverse_lazy('students')


class StudentDelete(DeleteView):
    model = Student
    success_url = reverse_lazy('students')


def edit_student(request, primary_key):
    student = get_object_or_404(Student, pk=primary_key)
    # student = Student()
    # try:
    #     student = Student.objects.get(pk=primary_key)
    # except student.DoesNotExist:
    #     raise Http404("Question does not exist")

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = StudentForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            # student_instance.due_back = form.cleaned_data['renewal_date']
            student.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse_lazy('students'))

    # If this is a GET (or any other method) create the default form.
    else:
        # proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        # form = AddStudentForm(initial=model_to_dict(student))
        form = StudentForm(instance=student)

    context = {
        'form': form,
        'student': student,
    }

    return render(request, 'students/student_form.html', context)


def new_student_verify(request, primary_key, hashcode):
    # jalali_join = datetime2jalali(request.user.date_joined).strftime('%y/%m/%d _ %H:%M:%S')
    user = get_object_or_404(User.objects.prefetch_related(
        'student_set__center', 'student_set__field'), pk=primary_key)

    if hashcode != user.getUserHash():
        return HttpResponseRedirect(reverse_lazy('newstdstart'))

    form_view = NewStdForm()
    form_verif = False
    verif = False
    # user

    if request.method == 'POST':
        form_verif = NewStdVerifyForm(request.POST)

        if form_verif.is_valid():

            form_verif.instance.person_id = primary_key

            form_verif.save()

            return redirect('/students/student/' + str(primary_key) + '/newstdverify/' + user.getUserHash())
            # return HttpResponseRedirect(reverse_lazy('students'))
            # sabteahval = Sabteahval()
        else:
            form_verif = NewStdVerifyForm(initial=request.POST)
    else:
        # form_verif = NewStdVerifyForm(instance=user)
        form_verif = NewStdVerifyForm()

    try:
        verif = Sabteahval.objects.get(person_id=primary_key)
    except Sabteahval.DoesNotExist:
        form_verif.fields['first_name'].help_text = user.first_name
        form_verif.fields['last_name'].help_text = user.last_name
        form_verif.fields['person_father_name'].help_text = user.person_father_name
        form_verif.fields['person_shen_number'].help_text = user.person_shen_number
        form_verif.fields['person_born_date'].help_text = user.person_born_date
        form_verif.fields['person_melli_code'].help_text = user.person_melli_code
        mobile_num = len(user.mobile_number)
        if 13 >= mobile_num >= 10:
            form_verif.fields['mobile_number'].help_text = user.mobile_number[-11:-7] + "####" + user.mobile_number[-3:]

    if verif:
        verif.hided_phone = verif.mobile_number[-11:-7] + "####" + verif.mobile_number[-3:]

    verified = True

    context = {
        'form_view': form_view,
        'form_verif': form_verif,
        'user': user,
        'verif': verif,
        'verified': verified,
    }

    return render(request, 'new_student_verify.html', context)


def new_student_continue(request, primary_key):
    user = get_object_or_404(User, pk=primary_key)

    from django.conf import settings


    # user.first_name = settings.MEDIA_ROOT

    if request.method == 'POST':
        # form = Etelaate_fardi(request.POST or None, instance=user)
        form = EtelaateFardi(request.POST, request.FILES, instance=user)

        if form.is_valid():
            # user = form.save(commit=False)
            if form.save():
                return redirect('/');

        else:

            form = EtelaateFardi(request.POST)

    else:
        form = EtelaateFardi(instance=user)

    context = {
        'form': form,
        'user': user,
    }

    return render(request, 'new_student_continue.html', context)


def new_student_start(request):
    # if User.is_authenticated

    user = False
    if request.method == 'POST':
        form = NewStdForm(request.POST)

        if form.is_valid():
            # student = User.objects.filter(request.POST)
            user = User.objects.filter(first_name__exact=form.data['first_name'],
                                       last_name__exact=form.data['last_name'],
                                       person_melli_code__exact=form.data['person_melli_code'],
                                       person_gender__exact=form.data['person_gender']).prefetch_related(
                'student_set__center', 'student_set__field')
    else:
        form = NewStdForm()

    context = {
        'form': form,
        'user_list': user,
    }

    return render(request, 'new_student_start.html', context)
