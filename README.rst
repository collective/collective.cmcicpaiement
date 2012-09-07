Introduction
============

This addon provide components to create the UI that will let you make a simple
paiement process to the `CM CIC paiement <https://www.cmcicpaiement.fr/>`_ 
solution

It can't be use alone, you must provide custom implementation for
your contents

Status: under development

Components
==========

Aller form
----------

This addon add a base Browser to build an "Aller" form. The idea
is to adapt and implement the current context and request to be an order.

An order must provide following elements:

* montant: the amount of the order
* reference: the id of the order

You can achieve this in many way: Having a cart done with simplecartjs
with an Order content type that will provide thoses information. 
You will then just have to create the view inheriting from 
collective.cmcicpaiement.aller.AllerForm , implements montant and reference
method and call aller_form in your template to render the paid button that
will do the job.

Retour
------

This addon manage the "Retour" phase and response to the bank.
It use the zope event infrastructure to notify the system of paiements.

The retour URL must be configured by the bank and must be:

  yoursite.com/@@cmcic_retour


Credits
=======

|makinacom|_

* `Planet Makina Corpus <http://www.makina-corpus.org>`_
* `Contact Makina-Corpus <mailto:python@makina-corpus.org>`_

.. |makinacom| image:: http://depot.makina-corpus.org/public/logo.gif
.. _makinacom:  http://www.makina-corpus.com
