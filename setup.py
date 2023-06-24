from setuptools import setup, find_namespace_packages # type: ignore


def main() -> None:
    pkgs = find_namespace_packages('src')
    pkg = min(pkgs)
    return setup(
        name=pkg,
        zip_safe=False,
        packages=pkgs,
        package_dir={'': 'src'},
        package_data={pkg: ['py.typed']},

        install_requires=[
            'pocket', # pocket API bindings
        ],
        extras_require={
            'testing': ['pytest'],
            'linting': ['pytest', 'mypy', 'lxml'], # lxml for mypy coverage report
        },
    )


if __name__ == '__main__':
    main()
