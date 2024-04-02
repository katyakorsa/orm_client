from distutils.core import setup

REQUIRES = [
    'allure-pytest',
    'sqlalchemy',
    'structlog'
]

setup(
    name='orm_client',
    version='1.1.1',
    packages=['orm_client'],
    url='https://github.com/katyakorsa/orm_client.git',
    license='MIT',
    author='Ekaterina Korsakova',
    author_email='',
    install_requires=REQUIRES,
    description='ORM client with logging and allure'
)
