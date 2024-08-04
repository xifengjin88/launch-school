from candidate import Candidate

class Election:
    def __init__(self, candidates):
        self.candidates = candidates

    def results(self):
        result = ''
        total = 0
        max_vote = float("-inf")
        winner = None
        for candidate in self.candidates:
            result += f'{candidate.name}: {candidate._vote} votes\n'
            total += candidate._vote
            if candidate._vote > max_vote:
                max_vote = candidate._vote
                winner = candidate

        result += f'\n{winner.name} won: {(max_vote / total) * 100}% of the votes.'
        return result


if __name__ == '__main__':
    mike_jones = Candidate('Mike Jones')
    susan_dore = Candidate('Susan Dore')
    kim_waters = Candidate('Kim Waters')

    candidates = {
        mike_jones,
        susan_dore,
        kim_waters,
    }

    votes = [
        mike_jones,
        susan_dore,
        mike_jones,
        susan_dore,
        susan_dore,
        kim_waters,
        susan_dore,
        mike_jones,
    ]

    for candidate in votes:
        candidate += 1

    election = Election(candidates)
    print(election.results())