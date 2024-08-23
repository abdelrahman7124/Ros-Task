from setuptools import setup

package_name = 'ultrasonic_sensor'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='your_name',
    maintainer_email='your_email@example.com',
    description='Description of ultrasonic_sensor',
    license='License',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'ultrasonic_publisher = ultrasonic_sensor.ultrasonic_publisher:main',
            'ultrasonic_subscriber = ultrasonic_sensor.ultrasonic_subscriber:main',
        ],
    },
)
