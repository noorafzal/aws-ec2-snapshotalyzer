from setuptools import setup

setup(
    name='snapshotalyzer-30000',
    version='0.1',
    author="Afzal Noor",
    author_email="noor.afzal21@gmail.com",
    description="SnapshotAlyzer 30000 is a tool to manage AWS EC2 snapshots",
    license="GPLv3",
    packages=['shotty'],
    url="https://github.com/noorafzal/aws-ec2-snapshotalyzer",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
        '''
)
