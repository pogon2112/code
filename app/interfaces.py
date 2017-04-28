"""Interface parsing and plotting from previously rejected version"""

from graphviz import Digraph
from ciscoconfparse import CiscoConfParse


def interfaces_extract(config):
    networks = {}

    for obj in config.find_objects('interface'):
        if obj.has_child_with('ip address'):
            name = obj.re_match_typed(regex=r'interface\s(\S+)/\d+', default='UNKNOWN')
            name_id = obj.re_match_typed(regex=r'interface\s\S+/(\d+)', result_type=int, default=-1)

            addr_line = obj.re_search_children('ip address')[0]

            addr = addr_line.re_match_typed(regex=r'ip\saddress\s(\d+.\d+.\d+.\d+)')
            addr_mask = addr_line.re_match_typed(regex=r'ip\saddress\s\d+.\d+.\d+.\d+\s(\d+.\d+.\d+.\d+)',
                                                 default='NONE')

            if name not in networks:
                networks[name] = []

            networks[name].append((name, name_id, addr, addr_mask))

    return networks


def interfaces_visualise(networks):
    dot = Digraph(comment='Network visualization')

    for name in networks:
        dot.node(name, name)

        for subnet in networks[name]:
            subnet_name = '{}/{}'.format(name, subnet[1])
            dot.node(subnet_name, subnet[2])
            dot.edge(name, subnet_name)

    return dot
