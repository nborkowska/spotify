#! /usr/bin/env python

import random

maxTestCase = 100
maxVotes = 500
maxCompetitors = 100

output = open('catvsdog_in', 'w')
output.write('%d\n' % maxTestCase)

cat, dog = 'C', 'D'
speciesChoices = [cat, dog]
numberChoices = xrange(1,maxCompetitors+1)
votesChoices = xrange(1,maxVotes+1)

for c in xrange(maxTestCase):
    noCats = random.choice(numberChoices)
    noDogs = random.choice(numberChoices)
    noVotes = random.choice(votesChoices)
    output.write('%d %d %d\n' % (noCats, noDogs, noVotes))
    for x in xrange(noVotes):
        species = random.choice(speciesChoices)
        if species == dog:
            competitor = cat
        else:
            competitor = dog
        one, two = random.choice(numberChoices), random.choice(numberChoices)
        output.write('%s%d %s%d\n' % (species, one, competitor, two))

