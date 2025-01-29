from setuptools import find_packages, setup

package_name = 'package_py'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Maco',
    maintainer_email='macorisd@uma.es',
    description='Beginner client libraries tutorials practica package',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'node_py = package_py.node_py:main'
        ],
    },
)
