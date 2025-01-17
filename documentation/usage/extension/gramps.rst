The *Gramps* extension
====================
The :py:class:`betty.extension.Gramps` extension loads entities from `Gramps <https://gramps-project.org>`_ family trees into your Betty ancestry.

Enable this extension through Betty Desktop, or in your project's :doc:`configuration file </usage/project/configuration>` as follows:

.. tabs::
   .. tab:: YAML
      .. code-block:: yaml

          extensions:
            betty.extension.Gramps: {}

   .. tab:: JSON
      .. code-block:: json

          {
            "extensions": {
              "betty.extension.Gramps": {}
            }
          }

Configuration
-------------
This extension is configurable through Betty Desktop or in the configuration file:

.. tabs::
   .. tab:: YAML
      .. code-block:: yaml

          extensions:
            betty.extension.Gramps:
              configuration:
                family_trees:
                  - file: ./gramps.gpkg

   .. tab:: JSON
      .. code-block:: json

          {
            "extensions": {
              "betty.extension.Gramps": {
                "configuration" : {
                  "family_trees": [
                    {
                      "file": "./gramps.gpkg"
                    }
                  ]
                }
              }
            }
          }


All configuration options
^^^^^^^^^^^^^^^^^^^^^^^^^
- ``family_trees`` (required): An array defining zero or more Gramps family trees to load. Each item is an object with
  the following keys:

  - ``file`` (required): the path to a *Gramps XML* or *Gramps XML Package* file.

  If multiple family trees contain entities of the same type and with the same ID (e.g. a person with ID ``I1234``) each
  entity will overwrite any previously loaded entity.



Privacy
-------

Gramps has limited built-in support for people's privacy. To fully control privacy for people, as well as events, files,
sources, and citations, add a ``betty:privacy`` attribute to any of these types, with a value of ``private`` to explicitly
declare the data always private or ``public`` to declare the data always public. Any other value will leave the privacy
undecided, as well as person records marked public using Gramps' built-in privacy selector. In such cases, the
``betty.extension.Privatizer`` extension may decide if the data is public or private.

Dates
-----

For unknown date parts, set those to all zeroes and Betty will ignore them. For instance, ``0000-12-31`` will be parsed as
"December 31", and ``1970-01-00`` as "January, 1970".

Event types
-----------

Betty supports the following Gramps event types:

- ``Adopted``
- ``Birth``
- ``Burial``
- ``Baptism``
- ``Conference``
- ``Confirmation``
- ``Correspondence``
- ``Cremation``
- ``Emigration``
- ``Engagement``
- ``Death``
- ``Divorce``
- ``Divorce Filing`` (imported as ``DivorceAnnouncement``)
- ``Funeral``
- ``Immigration``
- ``Marriage``
- ``Marriage Banns`` (imported as ``MarriageAnnouncement``)
- ``Missing``
- ``Occupation``
- ``Residence``
- ``Will``
- ``Retirement``

Event roles
-----------

Betty supports the following Gramps event roles:

- ``Attendee``
- ``Beneficiary``
- ``Celebrant``
- ``Family`` (imported as ``Subject``)
- ``Organizer``
- ``Primary`` (imported as ``Subject``)
- ``Speaker``
- ``Unknown`` (imported as ``Attendee``)
- ``Witness``

Order & priority
----------------

The order of lists of data, or the priority of individual bits of data, can be automatically determined by Betty in
multiple different ways, such as by matching dates, or locales. When not enough details are available, or in case of
ambiguity, the original order is preserved. If only a single item must be retrieved from the list, this will be the
first item, optionally after sorting.

For example, if a place has multiple names (which may be historical or translations), Betty may try to
filter names by the given locale and date, and then indiscriminately pick the first one of the remaining names to
display as the canonical name.

Tips:

- If you want one item to have priority over another, it should come before the other in a list (e.g. be higher up).
- Items with more specific or complete data, such as locales or dates, should come before items with less specific or
  complete data. However, items without dates at all are considered current and not historical.
- Unofficial names or nicknames, should generally be put at the end of lists.
