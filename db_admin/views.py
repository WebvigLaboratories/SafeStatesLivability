from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test

from livability.models import *

@login_required
def editEntry(request, entryId):
    dReturn = {}

    try:
        tool = Tools.objects.get(id = entryId)
        dReturn['tool'] = tool
    except Tools.DoesNotExist:
        messages.error(request, "The tool with the id [%s] cannot be found" % entryId)
        return redirect("admin_list")

    dReturn['communitySize'] = Community_Size.objects.filter(toolname = tool)
    dReturn['assessmentFocus'] = Assessment_Focus.objects.filter(toolname = tool)
    dReturn['audience'] = Audience.objects.filter(toolname = tool)
    dReturn['topics'] = Topics.objects.get(toolname = tool)

    return render(request, "editEntry.html", dReturn)

@login_required
def listEntries(request):
    dReturn = {}

    tools = Tools.objects.all()
    dReturn['tools'] = tools

    return render(request, "listEntries.html", dReturn)

@login_required
def showEntry(request, entryId):
    dReturn = {}

    try:
        tool = Tools.objects.get(id = entryId)
        dReturn['tool'] = tool
    except Tools.DoesNotExist:
        messages.error(request, "The tool with the id [%s] cannot be found" % entryId)
        return redirect("admin_list")

    dReturn['communitySize'] = Community_Size.objects.filter(toolname = tool)
    dReturn['assessmentFocus'] = Assessment_Focus.objects.filter(toolname = tool)
    dReturn['audience'] = Audience.objects.filter(toolname = tool)
    dReturn['topics'] = Topics.objects.get(toolname = tool)

    return render(request, "showEntry.html", dReturn)