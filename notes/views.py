#-*- coding: utf-8 -*-

from django.shortcuts import render_to_response, redirect
from django.contrib import messages
from django.template import RequestContext
from django.contrib.auth.models import User, Group

from notes.models import Note
from notes.forms import NoteForm


def from_group(user, group):
    """True/False if is in one group"""
    return bool(user.groups.filter(name=group))


def list_notes(request):
    """list notes"""
    # if user is in group 'bppp' show all messages
    if from_group(request.user, 'bppp'):
        top_notes = Note.objects.filter(on_top=True)
        notes = Note.objects.filter(on_top=False)
    else:
        # else show only public
        top_notes = Note.objects.filter(public=True, on_top=True)
        notes = Note.objects.filter(public=True, on_top=False)
    return render_to_response(
        'notes/list.html',
        {'top_notes': top_notes, 'notes': notes},
        context_instance=RequestContext(request),
    )


def list_my_notes(request):
    """list notes where the user is the author"""
    if not from_group(request.user, 'bppp'):
        top_notes = Note.objects.filter(public=True, on_top=True)
        notes = Note.objects.filter(public=True, on_top=False)
        return redirect('/notes/')
    top_notes = Note.objects.filter(author=request.user, on_top=True)
    notes = Note.objects.filter(author=request.user, on_top=False)
    return render_to_response(
        'notes/list.html',
        {'top_notes': top_notes, 'notes': notes},
        context_instance=RequestContext(request),
    )


def create_note(request):
    """create note"""
    # if user is in bppp group
    if not from_group(request.user, 'bppp'):
        notes = Note.objects.all()
        return redirect('/notes/')
    if request.method == "GET":
        form = NoteForm()
        return render_to_response(
            'notes/create.html',
            {'form': form},
            context_instance=RequestContext(request)
        )
    elif request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = Note.objects.create(
                name=form.cleaned_data['name'],
                content=form.cleaned_data['content'],
                public=form.cleaned_data['public'],
                on_top=form.cleaned_data['on_top'],
                author=request.user
            )
            note.save()
            return redirect('/notes/' + str(note.id) + "/")
        else:
            return render_to_response(
                'notes/create.html',
                {'form': form},
                context_instance=RequestContext(request))
        return redirect('/notes/')


def show_note(request, id):
    """show note"""
    # if private redirect
    note = Note.objects.get(id=id)
    if not from_group(request.user, 'bppp') and not note.public:
        return redirect('/notes/')
    return render_to_response(
        'notes/note.html',
        {'note': note},
        context_instance=RequestContext(request),
    )


def edit_note(request, id):
    """edit note"""
    note = Note.objects.get(id=id)
    # check if user is the author
    if request.user != note.author:
        return redirect('/notes/' + id + "/")
    # work with the author
    if request.method == "GET":
        form = NoteForm(instance=note)
        return render_to_response(
            'notes/edit.html',
            {'note': note, 'form': form},
            context_instance=RequestContext(request))
        return redirect('/notes/' + id + "/")
    elif request.method == "POST":
        if request.user != note.author:
            return redirect('/notes/' + id + "/")
        form = NoteForm(request.POST)
        if form.is_valid():
            note.name = form.cleaned_data['name']
            note.content = form.cleaned_data['content']
            note.public = form.cleaned_data['public']
            note.on_top = form.cleaned_data['on_top']
            note.save()
            message = u"Редактирование" + note.name + \
                u" успешно завершено! ;)"
            messages.success(request, message)
            return redirect('/notes/' + id + "/")


def remove_confirm(request, id):
    """confirm remove"""
    if not from_group(request.user, 'bppp'):
        notes = Note.objects.all()
        return redirect('/notes/')
    note = Note.objects.get(id=id)
    return render_to_response(
        'notes/confirm.html',
        {'note': note},
        context_instance=RequestContext(request)
    )


def remove_note(request, id):
    """delete note"""
    if not from_group(request.user, 'bppp'):
        notes = Note.objects.all()
        return redirect('/notes/' + id + "/")
    note = Note.objects.get(id=id)
    if request.user.id != note.author.id:
        return redirect('/notes/' + id + "/")
    message = u"Записка" + note.name + u" удалена была, мой мастер!"
    messages.success(request, message)
    note.delete()
    return redirect('/notes/')
