from django.template.defaultfilters import pluralize

def generate_question_revision_summary(old_revision, new_revision, wikified):
    """
    Generates a summary message based on the differences between the given
    QuestionRevision objects.
    """
    summary = []
    wikified_summary = _generate_wikified_summary(wikified)
    if wikified_summary is not None:
        summary.append(wikified_summary)
    if old_revision.title != new_revision.title:
        summary.append(u'modified title')
    body_summary = _generate_body_summary(old_revision, new_revision)
    if body_summary is not None:
        summary.append(body_summary)
    if old_revision.tagnames != new_revision.tagnames:
        summary.append(u'modified tags')
    return u'; '.join(summary)

def generate_answer_revision_summary(old_revision, new_revision, wikified):
    """
    Generates a summary message based on the differences between the given
    AnswerRevision objects.
    """
    summary = []
    wikified_summary = _generate_wikified_summary(wikified)
    if wikified_summary is not None:
        summary.append(wikified_summary)
    body_summary = _generate_body_summary(old_revision, new_revision)
    if body_summary is not None:
        summary.append(body_summary)
    return u'; '.join(summary)

def _generate_body_summary(old_revision, new_revision):
    """
    Generates a summary message based on the differences between the
    ``text`` attributes of the given revision objects, or ``None``
    if they are identical.
    """
    summary = None
    if old_revision.text != new_revision.text:
        change = len(new_revision.text) - len(old_revision.text)
        if not change:
            summary = u'modified body'
        else:
            if change > 0:
                body_summary = u'added %s character%s to body'
            else:
                body_summary = u'removed %s character%s from body'
                change = change * -1
            summary = body_summary % (change, pluralize(change))
    return summary

def _generate_wikified_summary(wikified):
    """Generates a summary message for enabling wiki mode."""
    if wikified:
        return u'put into wiki mode'
    return None
