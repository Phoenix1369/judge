def check(process_output, judge_output, file=False,
          line=False, line_sep='\n', token_sep=None, **kwargs):

    if file:
        import re
        return  sorted(filter(None, re.split(token_sep), process_output)) ==
                sorted(filter(None, re.split(token_sep), judge_output))

    process_lines = filter(None, process_output.split(line_sep))
    judge_lines = filter(None, judge_output.split(line_sep))

    from functools import partial
    from itertools import izip
    import string

    if len(process_lines) != len(judge_lines):
        return False

    process_tokens = map(partial(string.split, sep=token_sep), process_lines)
    judge_tokens = map(partial(string.split, sep=token_sep), judge_lines)

    for i in xrange(len(judge_tokens)):
        process_tokens[i].sort()
        judge_tokens[i].sort()

    if line:
        process_lines.sort()
        judge_lines.sort()

    for process_token, judge_token in izip(process_lines, judge_lines):
        if process_token != judge_token:
            return False
    return True
