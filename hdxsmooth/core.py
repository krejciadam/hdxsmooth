class Fragment:
    def __init__(self, positions, deuteration):
        self.positions = positions
        self.start = min(positions)
        self.end = max(positions)
        self.deuteration = deuteration

    def effective_length(self):
        return len(self.positions)


def make_fragment_map(fragments, start=1, end=None):
    if start is None:
        start = min(frag.start for frag in fragments)
    if end is None:
        end = max(frag.end for frag in fragments)
    map = {}
    for position in range(start, end + 1):
        map[position] = []
    for fragment in fragments:
        for pos in fragment.positions: #start +1 because N-terminus is never deuterated
            map[pos].append(fragment)
    return map


def position_deuteration(fragments):
    tot_length = sum((frag.effective_length()) for frag in fragments)
    deut = sum((tot_length / (frag.effective_length())) * frag.deuteration for frag in fragments) \
           / sum(tot_length / (frag.effective_length()) for frag in fragments)
    return deut

def calculate_denaturation(fragments, start=1, end=None):
    map = make_fragment_map(fragments, start, end)
    return{key:position_deuteration(value) if value else 0 for key, value in map.items()}


def find_prolines(seq):
    return [i for i, letter in enumerate(seq) if letter == 'P']