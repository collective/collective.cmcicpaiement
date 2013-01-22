from setuptools import setup, find_packages

version = '1.0b2.dev0'

setup(name='collective.cmcicpaiement',
      version=version,
      description="CM CIC Paiement for Plone",
      long_description=open("README.rst").read() + "\n" +
                       open("CHANGES.rst").read(),
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Plone",
        "Framework :: Plone :: 4.0",
        "Framework :: Plone :: 4.1",
        "Framework :: Plone :: 4.2",
        ],
      keywords='Plone cmcicpaiement ecommerce',
      author='JeanMichel FRANCOIS aka toutpt',
      author_email='toutpt@gmail.com',
      url='https://github.com/collective/collective.cmcicpaiement/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      extras_require=dict(test=['plone.app.testing']),
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
