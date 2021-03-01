from paver.tasks import task, BuildFailure, needs
from paver.easy import sh


@task
def unit_tests():
    sh('nosetests --with-coverage test/unit')

@task
def lettuce_tests():
    sh('lettuce test/bdd')

@needs('unit_tests', 'lettuce_tests', 'run_pylint', 'sdist')
@task
def default():
    pass
