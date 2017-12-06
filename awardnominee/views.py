from django.shortcuts import render, HttpResponseRedirect
from awardnominee.models import AwardNominee

def awards(request):
    if (request.method == "POST"):
        vote(request.POST.get("skit"))
        return HttpResponseRedirect('awards.html')
    return render(request, 'awards.html', {"votes": loadvotes()})

def loadvotes():
    voteset = AwardNominee.objects.all()
    votes = [v for v in voteset]
    votes.sort(key = lambda vote: vote.votecount, reverse=True)
    return votes

def vote(skit):
    entry = AwardNominee.objects.get(skitname=skit)
    entry.votecount = entry.votecount + 1
    entry.save()