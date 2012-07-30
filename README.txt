Introduction
============

A Twitter portlet for Plone. This portlet allows you to track the 'tweets' of a
particular user. You can add as many portlets as you like. The tweets are cached
for one minute.

Add to your buildout::

  eggs =
      collective.twitterportlet
  ....
  zcml =
      collective.twitterportlet

Install this portlet into your Plone site using the Add products in Site Setup.
Add Twitter portlets wherever you need, using the 'Manage portlets' interface.

The above 'zcml' step is not required in Plone 3.3+
