from setuptools import setup
from pathlib import Path
import os

# 安全读取 README.md，不区分大小写
def readme():
    root = Path(__file__).parent
    readme_file = None
    for name in os.listdir(root):
        if name.lower() == "readme.md":
            readme_file = root / name
            break
    if readme_file and readme_file.exists():
        return readme_file.read_text(encoding="utf-8")
    return ""  # 文件不存在时返回空字符串

setup(
    name='content-hash',
    description='Python implementation of EIP 1577 content hash',
    long_description=readme(),
    long_description_content_type='text/markdown',
    license='MIT',

    version='1.0.0',

    packages=['content_hash'],

    entry_points={
        'console_scripts': ['content-hash=content_hash.__main__:main'],
    },

    install_requires=[
        'py-cid>=0.3.0,<0.4.0',
        'py-multicodec>=0.2.1,<0.3.0',
        'py-multihash>=0.2.3,<0.3.0',
    ],

    extras_require={
        'lint': ['pylint'],
        'test': ['pytest', 'pytest-cov'],
    },

    python_requires='>= 3.5',

    author='Filip Š',
    author_email='projects@filips.si',
    url='https://github.com/filips123/ContentHashPy/',
    keywords='ethereum, ethereum-name-service, ens, eip1577, web3, decentralized',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: Name Service (DNS)',
        'Topic :: Scientific/Engineering :: Interface Engine/Protocol Translator',
        'Topic :: Security :: Cryptography',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
    ],

    include_package_data=True,
)