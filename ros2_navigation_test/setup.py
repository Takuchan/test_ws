from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'ros2_navigation_test'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),

        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*.urdf')),
        (os.path.join('share',package_name,'rviz'),glob('rviz/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='tk',
    maintainer_email='takuchanpp@gmail.com',
    description='独自urdfファイルを用いてRvizとGazebo上にオブジェクト配置してプログラムを実行する',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
