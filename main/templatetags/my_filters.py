from django import template

register = template.Library()


def counts_getter(topic, entry_counts):
    return entry_counts[topic.pk]


register.filter('counts_getter', counts_getter)
