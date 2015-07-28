from django.shortcuts import render
from operator import itemgetter

from models import *

def full_list(request):
    query_set = Tools.objects.all()

    results_list = []

    for result in query_set:

        results_dict = {}
        results_dict['name'] = result.name
        results_dict['author'] = result.author
        results_dict['url'] = result.url
        results_dict['description'] = result.description
        if result.year_developed == None:
            results_dict['year'] = "Unknown"
        else:
            results_dict['year'] = result.year_developed

        results_list.append(results_dict)

    sorted_results_list = sorted(results_list, key=itemgetter('name'))
    num_results = len(sorted_results_list)

    return render(request, "results.html", {'lResults':sorted_results_list,'numResults':num_results})

def search_results(request):
    answer_dict = {'errors': False}

    result_list1 = []
    result_list2 = []
    result_list3 = []
    final_result_list = []

    #POST answer to question 1
    if 'question1group' in request.POST and request.POST['question1group']:
        question1 = request.POST['question1group']
        if question1 == 1:
            answer_dict['q1_1'] = True
        else:
            answer_dict['q1_2'] = True

        q = Community_Size.objects.filter(selection=question1)

        for entry in q:
            result_list1.append(entry.toolname)
    else:
        #Return error - they have to provide a selection
        answer_dict['errors'] = True
        answer_dict['error_q1'] = True


    #Get answer to question 2
    question2 = []

    #First check for all of the above
    if 'question2_5' in request.POST and request.POST['question2_5']:
        answer_dict['q2_5'] = True
        question2 = [1,2,3,4]
    else:
        if 'question2_1' in request.POST and request.POST['question2_1']:
            answer_dict['q2_1'] = True
            question2.append(1)

        if 'question2_2' in request.POST and request.POST['question2_2']:
            answer_dict['q2_2'] = True
            question2.append(2)

        if 'question2_3' in request.POST and request.POST['question2_3']:
            answer_dict['q2_3'] = True
            question2.append(3)

        if 'question2_4' in request.POST and request.POST['question2_4']:
            answer_dict['q2_4'] = True
            question2.append(4)

    if len(question2) == 0:
        answer_dict['errors'] = True
        answer_dict['error_q2'] = True

    # For each selection in question2
    for i in question2:
        # Pull a database result showing all the tools with this selection
        q = Assessment_Focus.objects.filter(selection=i)

        # For each entry in the query set from result_set1
        for result in result_list1:
            # Compare the toolname to each entry in the database query above
            for entry in q:
                if result == entry.toolname:
                    #If they are the same, save it to a new result_set
                    # But make sure its not already in there
                    bFound = False
                    for x in result_list2:
                        if x == result:
                            bFound = True
                            break

                    if not bFound:
                        result_list2.append(result)

    #Get answer to question 3
    question3 = []

    #First check for all of the above
    if 'question3_6' in request.POST and request.POST['question3_6']:
        answer_dict['q3_6'] = True
        question3 = [1,2,3,4,5]
    else:
        if 'question3_1' in request.POST and request.POST['question3_1']:
            answer_dict['q3_1'] = True
            question3.append(1)

        if 'question3_2' in request.POST and request.POST['question3_2']:
            answer_dict['q3_2'] = True
            question3.append(2)

        if 'question3_3' in request.POST and request.POST['question3_3']:
            answer_dict['q3_3'] = True
            question3.append(3)

        if 'question3_4' in request.POST and request.POST['question3_4']:
            answer_dict['q3_4'] = True
            question3.append(4)

        if 'question3_5' in request.POST and request.POST['question3_5']:
            answer_dict['q3_5'] = True
            question3.append(5)

    if len(question3) == 0:
        answer_dict['errors'] = True
        answer_dict['error_q3'] = True

    #For each selection in question3
    for i in question3:
        # Pull a database result showing all the tools with this selection
        q = Audience.objects.filter(selection=i)

        # For each entry in the query set from result_set2
        for result in result_list2:
            # Compare the toolname to each entry in the database query above
            for entry in q:
                if result == entry.toolname:
                    # If they are the same, save it to a new result_set
                    # But make sure its not already in there
                    bFound = False
                    for x in result_list3:
                        if x == result:
                            bFound = True
                            break

                    if not bFound:
                        result_list3.append(result)

    # The result_set is widdled down based on the first three questions
    # Now, we want to display all of the tools for each selection below
    answer_provided = False

    # Topic: Transportation
    if 'question4_1' in request.POST and request.POST['question4_1']:
        answer_provided = True
        answer_dict['q4_1'] = True

        # Find all tools for this topic
        q = Topics.objects.filter(q_transportation=1)

        # Now see if any of the tools in our results set is in this query set
        for entry in q:
            for result in result_list3:
                if result == entry.toolname:
                    # This tool makes it to the final set
                    final_result_list.append(result)
                    break

    # Topic: Housing
    if 'question4_2' in request.POST and request.POST['question4_2']:
        answer_provided = True
        answer_dict['q4_2'] = True

        # Find all tools for this topic
        q = Topics.objects.filter(q_housing=1)

        # Now see if any of the tools in our results set is in this query set
        for entry in q:
            for result in result_list3:
                if result == entry.toolname:
                    # Make sure this tool isnt already in our final_result_set
                    bFound = False
                    for final in final_result_list:
                        if result == final:
                            bFound = True
                            break

                    # If it wasnt found at this point, add it
                    if not bFound:
                        final_result_list.append(result)

    # Topic: Investment
    if 'question4_3' in request.POST and request.POST['question4_3']:
        answer_provided = True
        answer_dict['q4_3'] = True

        # Find all tools for this topic
        q = Topics.objects.filter(q_investment=1)

        # Now see if any of the tools in our results set is in this query set
        for entry in q:
            for result in result_list3:
                if result == entry.toolname:
                    # Make sure this tool isnt already in our final_result_set
                    bFound = False
                    for final in final_result_list:
                        if result == final:
                            bFound = True
                            break

                    # If it wasnt found at this point, add it
                    if not bFound:
                        final_result_list.append(result)

    # Topic: Compact
    if 'question4_4' in request.POST and request.POST['question4_4']:
        answer_provided = True
        answer_dict['q4_4'] = True

        # Find all tools for this topic
        q = Topics.objects.filter(q_compact=1)

        # Now see if any of the tools in our results set is in this query set
        for entry in q:
            for result in result_list3:
                if result == entry.toolname:
                    # Make sure this tool isnt already in our final_result_set
                    bFound = False
                    for final in final_result_list:
                        if result == final:
                            bFound = True
                            break

                    # If it wasnt found at this point, add it
                    if not bFound:
                        final_result_list.append(result)

    # Topic: Health
    if 'question4_5' in request.POST and request.POST['question4_5']:
        answer_provided = True
        answer_dict['q4_5'] = True

        # Find all tools for this topic
        q = Topics.objects.filter(q_health=1)

        # Now see if any of the tools in our results set is in this query set
        for entry in q:
            for result in result_list3:
                if result == entry.toolname:
                    # Make sure this tool isnt already in our final_result_set
                    bFound = False
                    for final in final_result_list:
                        if result == final:
                            bFound = True
                            break

                    # If it wasnt found at this point, add it
                    if not bFound:
                        final_result_list.append(result)

    # Topic: Preservation
    if 'question4_6' in request.POST and request.POST['question4_6']:
        answer_provided = True
        answer_dict['q4_6'] = True

        # Find all tools for this topic
        q = Topics.objects.filter(q_preservation=1)

        # Now see if any of the tools in our results set is in this query set
        for entry in q:
            for result in result_list3:
                if result == entry.toolname:
                    # Make sure this tool isnt already in our final_result_set
                    bFound = False
                    for final in final_result_list:
                        if result == final:
                            bFound = True
                            break

                    # If it wasnt found at this point, add it
                    if not bFound:
                        final_result_list.append(result)

    if not answer_provided:
        #return render_to_response("questions.html", {"errors":True, "error_q4":True})
        answer_dict['errors'] = True
        answer_dict['error_q4'] = True

    if answer_dict['errors']:
        return render(request, 'questions.html', answer_dict)


    # Create a list of dictionary object with final results
    lResults = []

    for result in final_result_list:
        q = Tools.objects.get(name=result)

        dResults = {}
        dResults['name'] = q.name
        dResults['author'] = q.author
        dResults['url'] = q.url
        dResults['description'] = q.description
        if q.year_developed == None:
            dResults['year'] = ""
        else:
            dResults['year'] = q.year_developed

        lResults.append(dResults)

    sorted_results_list = sorted(lResults, key=itemgetter('name'))
    num_results = len(sorted_results_list)

    return render(request, "results.html", {'lResults':sorted_results_list,'numResults':num_results})


