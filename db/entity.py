# db/models.py

from datetime import datetime
# 候选人
class Candidate:
    def __init__(self, candidate_id=None, name=None, alias=None, gender=None, ethnicity=None, birthplace=None,
                 birthdate=None, university=None, party=None, degree=None, education=None, works=None,
                 achievements=None, networth=None):
        self.candidate_id = candidate_id
        self.name = name
        self.alias = alias
        self.gender = gender
        self.ethnicity = ethnicity
        self.birthplace = birthplace
        self.birthdate = birthdate
        self.university = university
        self.party = party
        self.degree = degree
        self.education = education
        self.works = works
        self.achievements = achievements
        self.networth = networth

    def __repr__(self):
        return f"Candidate({self.candidate_id}, {self.name})"

# 候选人列表
class CandidateList:
    def __init__(self, candidate_list_id=None, candidate_id=None, election_date=None):
        self.candidate_list_id = candidate_list_id
        self.candidate_id = candidate_id
        self.election_date = election_date

    def __repr__(self):
        return f"CandidateList({self.candidate_list_id}, {self.candidate_id})"

# 退选的候选人
class WithdrawnCandidates:
    def __init__(self, withdrawn_candidates_id=None, candidate_id=None, election_date=None, withdraw_reason=None,
                 withdraw_date=None):
        self.withdrawn_candidates_id = withdrawn_candidates_id
        self.candidate_id = candidate_id
        self.election_date = election_date
        self.withdraw_reason = withdraw_reason
        self.withdraw_date = withdraw_date

    def __repr__(self):
        return f"WithdrawnCandidates({self.withdrawn_candidates_id}, {self.candidate_id})"

# 选举进程
class ElectionProcess:
    def __init__(self, process_id=None, candidate_id=None, time=None, process_description=None):
        self.process_id = process_id
        self.candidate_id = candidate_id
        self.time = time
        self.process_description = process_description

    def __repr__(self):
        return f"ElectionProcess({self.process_id}, {self.candidate_id})"

# 事件
class Event:
    def __init__(self, event_id=None, start_time=None, end_time=None, content=None):
        self.event_id = event_id
        self.start_time = start_time
        self.end_time = end_time
        self.content = content

    def __repr__(self):
        return f"Event({self.event_id}, {self.start_time}, {self.content})"

# 选举事件
class ElectionEvent:
    def __init__(self, election_event_id=None, event_id=None, candidate_id=None):
        self.election_event_id = election_event_id
        self.event_id = event_id
        self.candidate_id = candidate_id

    def __repr__(self):
        return f"ElectionEvent({self.election_event_id}, {self.event_id}, {self.candidate_id})"

# 投票情况
class ElectionVotes:
    def __init__(self, vote_id=None, candidate_id=None, time=None, region=None, votes_count=None, result=None):
        self.vote_id = vote_id
        self.candidate_id = candidate_id
        self.time = time
        self.region = region
        self.votes_count = votes_count
        self.result = result

    def __repr__(self):
        return f"ElectionVotes({self.vote_id}, {self.candidate_id}, {self.region})"

# 财团
class Corporation:
    def __init__(self, corporation_id=None, name=None, history=None, members=None, wealth=None):
        self.corporation_id = corporation_id
        self.name = name
        self.history = history
        self.members = members
        self.wealth = wealth

    def __repr__(self):
        return f"Corporation({self.corporation_id}, {self.name})"

# 财团支持
class CandidateSupport:
    def __init__(self, support_id=None, candidate_id=None, corporation_id=None, support_amount=None, support_date=None):
        self.support_id = support_id
        self.candidate_id = candidate_id
        self.corporation_id = corporation_id
        self.support_amount = support_amount
        self.support_date = support_date

    def __repr__(self):
        return f"CandidateSupport({self.support_id}, {self.candidate_id}, {self.corporation_id})"
