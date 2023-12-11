from setuptools import find_packages, setup

package_name = 'serial_pkg'

setup(
    name=package_name,
    version='1.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='altair',
    maintainer_email='Altairu@github.com',
    description='TODO: ros2---arduino serial',
    license='TODO: MIT License',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'serial_get_node = serial_pkg.serial_get_node:main',
            'serial_send_node = serial_pkg.serial_send_node:main'
        ],
    },
)
