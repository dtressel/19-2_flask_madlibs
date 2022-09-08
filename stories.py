"""Madlibs Stories."""
storyList = []

class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, name, words, text):
        """Create story with words and template text."""

        self.name = name
        self.prompts = words
        self.template = text
        storyList.append(self)
        

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story1 = Story(
    "Once Upon a time",
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

story2 = Story(
    "Murder mystery",
    ["date", "male_name", "adjective", "building", "female_name", "plural_noun", "thing"],
    """On the dawn of {date}, {male_name} came across a {adjective} sight. On the steps
    of the {building}, there lay {female_name}, lifeless, covered with {plural_noun}. 
    To the right, lay the murder weapon, a {thing}. Who could have done such a thing?"""
)