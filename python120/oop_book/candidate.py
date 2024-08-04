class Candidate:
    '''
    name
    implement augmenented plus __iadd__ for tally
    '''

    def __init__(self, name):
        self.name = name
        self._vote = 0

    def __iadd__(self, vote):
        self._vote += vote
        return self

    def __add__(self, vote):
        self._vote += vote
        return self



if __name__ == '__main__':
    candidate = Candidate('xifeng')
    candidate += 1
    candidate += 2
