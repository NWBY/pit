from setuptools import setup, find_packages

setup(
    name='pit',
    version='0.1.0',
    description="CLI that makes common git commands simpler",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points="""
        [console_scripts]
        pit=cli.scripts.pit:cli
    """,
)
