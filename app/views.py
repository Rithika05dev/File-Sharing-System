from django.shortcuts import render, redirect
from .models import File, FileShare
from django.contrib.auth.models import User


def upload_file(request):

    if request.method == 'POST':

        uploaded_file = request.FILES['file']

        # Check existing file

        existing_file = File.objects.filter(
            filename=uploaded_file.name
        ).first()

        if existing_file:

            version_number = existing_file.version + 1

        else:

            version_number = 1

        # Create new file

        File.objects.create(
            file=uploaded_file,
            filename=uploaded_file.name,
            uploaded_by=User.objects.first(),
            version=version_number
        )

        return redirect('/')

    return render(request, 'upload.html')


def my_files(request):

    query = request.GET.get('q')

    if query:

        files = File.objects.filter(
            filename__icontains=query,
            deleted=False
        ).order_by('-created_at')

    else:

        files = File.objects.filter(
            deleted=False
        ).order_by('-created_at')

    return render(request, 'files.html', {
        'files': files
    })


def delete_file(request, id):

    file = File.objects.get(id=id)

    file.deleted = True

    file.save()

    return redirect('my_files')


def share_file(request, id):

    file = File.objects.get(id=id)

    users = User.objects.all()

    if request.method == 'POST':

        user_id = request.POST['user']

        permission = request.POST['permission']

        shared_user = User.objects.get(id=user_id)

        FileShare.objects.create(
            file=file,
            shared_with=shared_user,
            permission=permission
        )

        return redirect('/shared/')

    return render(request, 'share.html', {
        'file': file,
        'users': users
    })


def shared_files(request):

    shared = FileShare.objects.order_by('-id')

    return render(request, 'shared.html', {
        'shared_files': shared
    })


def starred(request):

    starred_files = File.objects.filter(
        starred=True,
        deleted=False
    ).order_by('-created_at')

    return render(request, 'starred.html', {
        'files': starred_files
    })


def trash(request):

    trash_files = File.objects.filter(
        deleted=True
    ).order_by('-created_at')

    return render(request, 'trash.html', {
        'files': trash_files
    })


def restore_file(request, id):

    file = File.objects.get(id=id)

    file.deleted = False

    file.save()

    return redirect('trash')


def permanent_delete(request, id):

    file = File.objects.get(id=id)

    file.delete()

    return redirect('trash')


def settings_page(request):

    return render(request, 'settings.html')


def toggle_star(request, id):

    file = File.objects.get(id=id)

    file.starred = not file.starred

    file.save()

    return redirect('my_files')