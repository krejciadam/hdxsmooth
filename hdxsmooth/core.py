class Fragment:
    def __init__(self, start, end, deuteration):
        self.start = start
        self.end = end
        self.deuteration = deuteration
        if start >= end:
            raise ValueError('Fragment start ({}) is greater than end ({})'.format(start, end))
        if deuteration < 0:
            raise ValueError('Negative deuteration level ({})'.format(deuteration))

    def length(self):
        return self.end - self.start + 1


def make_fragment_map(fragments, start=None, end=None):
    if start is None:
        start = min(frag.start for frag in fragments)
    if end is None:
        end = max(frag.end for frag in fragments)
    map = {}
    for position in range(start, end + 1):
        map[position] = []
    for fragment in fragments:
        for pos in range(fragment.start + 1, fragment.end + 1): #start +1 because N-terminus is never deuterated
            map[pos].append(fragment)
    return map

#frag.length() - 1 because N-terminal position does not count
def position_deuteration(fragments):
    tot_length = sum((frag.length() - 1) for frag in fragments)
    deut = sum((tot_length / (frag.length() - 1)) * frag.deuteration for frag in fragments) \
           / sum(tot_length / (frag.length() - 1) for frag in fragments)
    return deut

def calculate_denaturation(fragments, start=None, end=None):
    map = make_fragment_map(fragments, start, end)
    return{key:position_deuteration(value) if value else 0 for key, value in map.items()}