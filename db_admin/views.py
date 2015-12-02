from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from livability.models import *
from forms import *

@login_required
def editEntry(request, entryId):
    dReturn = {}
    dReturn['entryId'] = entryId

    try:
        tool = Tools.objects.get(id = entryId)
    except Tools.DoesNotExist:
        messages.error(request, "The tool with the id [%s] cannot be found" % entryId)
        return redirect("admin_list")

    communitySizeUrban = False
    communitySizeRural = False
    assessmentFocusDevelopment = False
    assessmentFocusPhysical = False
    assessmentFocusPolicy = False
    assessmentFocusWalkability = False
    audienceElected = False
    audienceLaypersons = False
    audiencePlanners = False
    audienceProfessionals = False
    audienceSchool = False
    topicTransportation = False
    topicHousing = False
    topicInvestment = False
    topicCompact = False
    topicHealth = False
    topicPreservation = False

    if request.method == 'POST':
        form = EditForm(request.POST)
        dReturn['form'] = form

        form.is_valid()
        cd = form.cleaned_data

        tool.name = cd['name']
        tool.author = cd['author']
        tool.url = cd['url']
        if cd['yearDeveloped'] != "":
            tool.year_developed = cd['yearDeveloped']
        else:
            tool.year_developed = None

        tool.description = cd['description']
        tool.save()

        communitySizeList = Community_Size.objects.filter(toolname = tool)
        for item in communitySizeList:
            item.delete()

        if 'communitySizeUrban' in cd:
                communitySize = Community_Size(toolname=tool, selection=1)
                communitySize.save()
        if 'communitySizeRural' in cd:
            communitySize = Community_Size(toolname=tool, selection=2)
            communitySize.save()

        assessmentFocusList = Assessment_Focus.objects.filter(toolname = tool)
        for item in assessmentFocusList:
            item.delete()

        if 'assessmentFocusDevelopment' in cd:
            assessmentFocus = Assessment_Focus(toolname=tool, selection=1)
            assessmentFocus.save()
        if 'assessmentFocusPhysical' in cd:
            assessmentFocus = Assessment_Focus(toolname=tool, selection=2)
            assessmentFocus.save()
        if 'assessmentFocusPolicy' in cd:
            assessmentFocus = Assessment_Focus(toolname=tool, selection=3)
            assessmentFocus.save()
        if 'assessmentFocusWalkability' in cd:
            assessmentFocus = Assessment_Focus(toolname=tool, selection=4)
            assessmentFocus.save()

        audienceList = Audience.objects.filter(toolname = tool)
        for item in audienceList:
            item.delete()

        if 'audienceElected' in cd:
            audience = Audience(toolname=tool, selection=1)
            audience.save()
        if 'audienceLaypersons' in cd:
            audience = Audience(toolname=tool, selection=2)
            audience.save()
        if 'audienePlanners' in cd:
            audience = Audience(toolname=tool, selection=3)
            audience.save()
        if 'audienceProfessionals' in cd:
            audience = Audience(toolname=tool, selection=4)
            audience.save()
        if 'audienceSchool' in cd:
            audience = Audience(toolname=tool, selection=5)
            audience.save()

        topics = Topics.objects.get(toolname = tool)
        if 'topicTransportation' in cd:
            topics.q_transportation = 1
        else:
            topics.q_transportation = 0

        if 'topicHousing' in cd:
            topics.q_housing = 1
        else:
            topics.q_housing = 0

        if 'topicPreservation' in cd:
            topics.q_preservation = 1
        else:
            topics.q_preservation = 0

        if 'topicHousing' in cd:
            topics.q_housing = 1
        else:
            topics.q_housing = 0

        if 'topicCompact' in cd:
            topics.q_compact = 1
        else:
            topics.q_compact = 0

        if 'topicInvestment' in cd:
            topics.q_investment = 1
        else:
            topics.q_investment = 0

        topics.save()

        messages.success(request, "Updated this entry")
        return redirect(reverse('admin_show', args=[entryId]))

    else:
        communitySizeList = Community_Size.objects.filter(toolname = tool)
        for item in communitySizeList:
            if item.selection == 1:
                communitySizeUrban = True
            elif item.selection == 2:
                communitySizeRural = True

        assessmentFocusList = Assessment_Focus.objects.filter(toolname = tool)
        for item in assessmentFocusList:
            if item.selection == 1:
                assessmentFocusDevelopment = True
            elif item.selection == 2:
                assessmentFocusPhysical = True
            elif item.selection == 3:
                assessmentFocusPolicy = True
            elif item.selection == 4:
                assessmentFocusWalkability = True

        audienceList = Audience.objects.filter(toolname = tool)
        for item in audienceList:
            if item.selection == 1:
                audienceElected = True
            elif item.selection == 2:
                audienceLaypersons = True
            elif item.selection == 3:
                audiencePlanners = True
            elif item.selection == 4:
                audienceProfessionals = True
            elif item.selection == 5:
                audienceSchool = True

        topics = Topics.objects.get(toolname = tool)
        if topics.q_transportation == 1:
            topicTransportation = True
        if topics.q_health == 1:
            topicHealth = True
        if topics.q_preservation == 1:
            topicPreservation = True
        if topics.q_housing == 1:
            topicHousing = True
        if topics.q_compact == 1:
            topicCompact = True
        if topics.q_investment == 1:
            topicInvestment = True


        form = EditForm(initial={
            'yearDeveloped': tool.year_developed,
            'name': tool.name,
            'author': tool.author,
            'url': tool.url,
            'description': tool.description,
            'communitySizeUrban': communitySizeUrban,
            'communitySizeRural': communitySizeRural,
            'assessmentFocusDevelopment': assessmentFocusDevelopment,
            'assessmentFocusPhysical': assessmentFocusPhysical,
            'assessmentFocusPolicy': assessmentFocusPolicy,
            'assessmentFocusWalkability': assessmentFocusWalkability,
            'audienceElected': audienceElected,
            'audienceLaypersons': audienceLaypersons,
            'audiencePlanners': audiencePlanners,
            'audienceProfessionals': audienceProfessionals,
            'audienceSchool': audienceSchool,
            'topicTransportation': topicTransportation,
            'topicHousing': topicHousing,
            'topicInvestment': topicInvestment,
            'topicCompact': topicCompact,
            'topicHealth': topicHealth,
            'topicPreservation': topicPreservation,
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