from setuptools import setup, find_packages

requires = [
    'pyramid',
    'waitress',
    'sqlalchemy',
    'alembic',
    'psycopg2-binary',
    'zope.sqlalchemy',
    'plaster-pastedeploy',
    'pyramid-tm',
    'transaction',
]

setup(
    name='matakuliah-api',
    version='0.1',
    description='Aplikasi API Manajemen Matakuliah dengan Pyramid Framework',
    author='',
    author_email='',
    url='',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    entry_points={
        'paste.app_factory': [
            'main = matakuliah_api:main',
        ],
    },
)

