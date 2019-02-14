setup(
    name='py-db-migration',
    version='0.0.1',
    description='Python CLI tool to migrate from old database to new database',
    long_description=readme,
    author='Koichi Taura',
    author_email='taura.koichi@gmail.com',
    url='https://github.com/Taurin190/py-db-migration',
    license=license,
    packages=[''],
    install_requires=[
        'configparser',
        'pymongo',
        'MySQLdb'
    ]
)