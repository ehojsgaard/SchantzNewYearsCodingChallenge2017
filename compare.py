#!/usr/local/bin/python3
import os
import sys

import numpy as np

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

reference_filename = os.path.join(__location__, 'Santas-pension-projection.txt')
solution_filename = sys.argv[1]

reference_projection = np.genfromtxt(reference_filename, delimiter='\t', dtype=[('year', int), ('reserve', float)])
solution_projection = np.genfromtxt(solution_filename, delimiter='\t', dtype=[('year', int), ('reserve', float)])

if not solution_projection['year'].size == reference_projection['year'].size:
     sys.exit('Solution rows %u, expected %u' % (solution_projection['year'].size, reference_projection['year'].size))

for n in range(0,55):
    if not solution_projection['year'][n] == reference_projection['year'][n]:
        sys.exit(
            'Solution line %u has year = %u, expected %u' % (n+1, solution_projection['year'][n], reference_projection['year'][n]))

    if not np.isclose(solution_projection['reserve'][n], reference_projection['reserve'][n], rtol=1.e-3, atol=0):
        difference = abs(solution_projection['reserve'][n] - reference_projection['reserve'][n])
        sys.exit(
            'Solution year %u has reserve = %f which diverges %.55f%% from the reference reserve %f' % (
                solution_projection['year'][n], solution_projection['reserve'][n], 100*difference/reference_projection['reserve'][n], reference_projection['reserve'][n]))

print("Solution matches")