class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        q = deque()
        for w in words: q.append(w)

        tmp, lines, size = [], [], deque()
        tmp_size = 0
        while q:
            wrd = q[0]
            if tmp_size + len(wrd) + len(tmp) <= maxWidth:
                tmp_size += len(wrd)
                tmp.append(q.popleft())
            else:
                lines.append(tmp)
                size.append(tmp_size)
                tmp = []
                tmp_size = 0
        lines.append(tmp)
        size.append(tmp_size)

        res = []
        for line in lines:
            newl = ''
            lsize = size.popleft()
            spc = maxWidth - lsize
            if len(line) == 1:
                newl += line[0]
                newl += ' '*spc
                res.append(newl)
            else:
                nwrd = len(line)
                if line == lines[-1]:
                    for w in line:
                        newl += w
                        newl += ' '*(1 if nwrd > 1 else spc)
                        spc -= 1
                        nwrd -= 1
                else:
                    for w in line:
                        newl += w
                        nxt_spc = (0 if nwrd == 1 else math.ceil(spc/(nwrd - 1)))
                        newl += ' '*nxt_spc
                        spc -= nxt_spc
                        nwrd -= 1
                res.append(newl)
        return res