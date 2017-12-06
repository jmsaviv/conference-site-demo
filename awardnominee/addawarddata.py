from awardnominee.models import AwardNominee

nom = AwardNominee(
    skitname="Rick James",
    nomineedescription="Charlie Murphy recounts hanging out with Rick James back in the 80s",
    nomineepic="images/rickjamespic.jpeg",
    votecount=4
)

nom.save()

nom = AwardNominee(
    skitname="Player Haters Ball",
    nomineedescription="Player haters from around the globe compete for the coveted title of 'Hater of the Year'",
    nomineepic="images/playerhater.jpeg",
    votecount=10
)

nom.save()

nom = AwardNominee(
    skitname="Prince",
    nomineedescription="Charlie Murphy tells the story about the time Prince beat him in basketball",
    nomineepic="images/prince.jpeg",
    votecount=15
)

nom.save()