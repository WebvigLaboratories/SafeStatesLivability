from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test

from livability.models import *
from forms import *

@login_required
def editEntry(request, entryId):
    dReturn = {}

    try:
        tool = Tools.objects.get(id = entryId)
    except Tools.DoesNotExist:
        messages.error(request, "The tool with the id [%s] cannot be found" % entryId)
        return redirect("admin_list")

    communitySize = ""
    assessmentFocus = ""
    audience = ""

    communitySizeList = Community_Size.objects.filter(toolname = tool)
    for item in communitySizeList:
        communitySize = item.selection

    assessmentFocusList = Assessment_Focus.objects.filter(toolname = tool)
    for item in assessmentFocusList:
        assessmentFocus = item.selection

    audienceList = Audience.objects.filter(toolname = tool)
    for item in audienceList:
        audience = item.selection

    topics = Topics.objects.get(toolname = tool)

    form = EditForm(initial={
        'yearDeveloped': tool.year_developed,
        'name': tool.name,
        'author': tool.author,
        'url': tool.url,
        'description': tool.description,
        'communitySize': communitySize,
        'assessmentFocus': assessmentFocus,
        'audience': audience,
        'topicTransportation': topics.q_transportation,
        'topicHousing': topics.q_housing,
        'topicInvestment': topics.q_investment,
        'topicCompact': topics.q_compact,
        'topicHealth': topics.q_health,
        'topicPreservation': topics.q_preservation
    })

    dReturn['form'] = form

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