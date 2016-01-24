from paver import easy
from paver.shell import sh


@easy.task
@easy.needs('migrate', 'test')
def build():
    sh('flake8 .')


@easy.task
def migrate():
    sh('python manage.py makemigrations')
    sh('python manage.py migrate')


@easy.task
def test():
    sh('python manage.py test')


@easy.task
def run():
    sh('python manage.py runserver')


@easy.task
@easy.consume_args
def pip_install(args):
    sh('pip install {} && pip freeze > ../requirements.txt'.format(args[0]))
