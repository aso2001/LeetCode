class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        q = deque()
        for w in words: q.append(w)

        line, lines, size, line_size = [], [], deque(), 0
        while q:
            w = q[0]
            if line_size + len(w) + len(line) <= maxWidth:
                line_size += len(w)
                line.append(q.popleft())
            else:
                lines.append(line)
                size.append(line_size)
                line, line_size = [], 0
        lines.append(line)
        size.append(line_size)

        res = []
        for line in lines:
            new_line = ''
            spc = maxWidth - size.popleft()
            num_w = len(line)
            if num_w > 1:
                if line != lines[-1]:
                    for w in line:
                        new_line += w
                        nxt_spc = (0 if num_w == 1 else math.ceil(spc/(num_w - 1)))
                        new_line += ' '*nxt_spc
                        spc -= nxt_spc
                        num_w -= 1
                else:
                    for w in line:
                        new_line += w
                        new_line += ' '*(1 if num_w > 1 else spc)
                        spc -= 1
                        num_w -= 1
            else:
                new_line += line[0]
                new_line += ' '*spc
            res.append(new_line)
        return res