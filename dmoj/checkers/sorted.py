def check(process_output, judge_output, file=False,
          line=False, line_sep='\n', token_sep=None, **kwargs):

    if file:
        from re import split as resplit
        return  sorted(filter(None, resplit(token_sep), process_output)) ==
                sorted(filter(None, resplit(token_sep), judge_output))

    process_lines = filter(None, process_output.split(line_sep))
    judge_lines = filter(None, judge_output.split(line_sep))

    if len(process_lines) != len(judge_lines):
        return False

    from functools import partial
    from itertools import izip
    from string import split as ssplit

    for i in xrange(len(judge_lines)):
        process_lines[i] = ssplit(process_lines[i], sep=token_sep)
        judge_lines[i] = ssplit(judge_lines[i], sep=token_sep)
        process_lines[i].sort()
        judge_lines[i].sort()

    if line:
        process_lines.sort()
        judge_lines.sort()

    for process_token, judge_token in izip(process_lines, judge_lines):
        if process_token != judge_token:
            return False
    return True
