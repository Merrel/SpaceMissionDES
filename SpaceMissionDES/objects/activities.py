# activities.py
from dataclasses import dataclass, field
from objects.events import Event, Failure, Predicate

#######################################################################################################################
# Activities

@dataclass
class Activity:
    name: str
    start: Event
    end: Event
    duration: float
    p_fail: float = 0    # probability that the activity will fail to be completed (i.e. failed launch)
    failure: Event = Failure()
    resource_change: dict = field(default_factory = dict)
    agg_type: str = ""   # either join, dejoin, dropchild, addchild
    agg_params: dict = field(default_factory = dict) 
    # dict of agg params 
    #   FOR join {conops: conops, vehicles: [va, vb], name: "va-vb"}
    #   FOR dejoin N/A
    #   FOR addchild {vehicles: [va, vb]}
    #   FOR dropchild {vehicles: [va, vb]}


@dataclass
class PredicatedActivity:
    name: str
    start: Event
    end: Event
    predicate: Predicate
    # duration: float
    p_fail: float = 0    # probability that the activity will fail to be completed (i.e. failed launch)
    failure: Event = Failure()
    resource_change: dict = field(default_factory = dict)
    agg_type: str = ""
    agg_params: list = field(default_factory = list)

#######################################################################################################################
# ConOps

@dataclass
class ConOps:
    sequence: dict

    def first(self):
        # print(self)
        return self.sequence["INIT"]

    def after(self, current_event):
        # Get the activity which starts with a particular event
        return self.sequence[current_event.name]

    def update(self, additions:dict):
        self.sequence.update(additions)
        return self