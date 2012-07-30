collective.twitterportlet tests
===============================

First of all we need to import the expander:

    >>> from collective.twitterportlet.portlet import expand_tweet

Then we need to start testing tweets, first a reply:

    >>> tweet = """@testuser this is my reply"""
    >>> expand_tweet(tweet)
    '<a href="http://twitter.com/testuser">@testuser</a> this is my reply'

Now a hash tag:

    >>> tweet = """this is my reply #Plone"""
    >>> expand_tweet(tweet)
    'this is my reply <a href="http://twitter.com/search?q=%23Plone">#Plone</a>'

Now a URL:

    >>> tweet = """Check out this http://www.google.com"""
    >>> expand_tweet(tweet)
    'Check out this <a href="http://www.google.com">http://www.google.com</a>'

Now a reply with a mention:

    >>> tweet = """@testuser have you met @anotheruser"""
    >>> expand_tweet(tweet)
    '<a href="http://twitter.com/testuser">@testuser</a> have you met <a href="http://twitter.com/anotheruser">@anotheruser</a>'

Now a reply with a hashtag:

    >>> tweet = """@testuser working on #Plone"""
    >>> expand_tweet(tweet)
    '<a href="http://twitter.com/testuser">@testuser</a> working on <a href="http://twitter.com/search?q=%23Plone">#Plone</a>'

Now a reply with a URL:

    >>> tweet = """@testuser check out this http://www.google.com"""
    >>> expand_tweet(tweet)
    '<a href="http://twitter.com/testuser">@testuser</a> check out this <a href="http://www.google.com">http://www.google.com</a>'

Now a tweet with a URL followed by a dot:

    >>> tweet = """Check out this http://www.google.com."""
    >>> expand_tweet(tweet)
    'Check out this <a href="http://www.google.com">http://www.google.com</a>.'

Now a tweet with an email:

    >>> tweet = """Mail me username@email.com"""
    >>> expand_tweet(tweet)
    'Mail me <a href="mailto:username@email.com">username@email.com</a>'

Now a tweet with link to a photo album from the Plone business Facebook page:

    >>> tweet = """http://www.facebook.com/pages/Plone/8385399421?ref=ts&v=wall#!/album.php?aid=-3&id=8385399421"""
    >>> expand_tweet(tweet)
    '<a href="http://www.facebook.com/pages/Plone/8385399421?ref=ts&v=wall#!/album.php?aid=-3&id=8385399421">http://www.facebook.com/pages/Plone/8385399421?ref=ts&v=wall#!/album.php?aid=-3&id=8385399421</a>'
