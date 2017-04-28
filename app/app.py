from graphviz import Digraph
from ciscoconfparse import CiscoConfParse
import trigger
from trigger.acl import parse
import socket
import re


def force_parse(line, quiet=False, attempt=0):
    try:
        return parse(line)
    except trigger.exceptions.ParseError as error:
        attempt += 1
        if attempt > 1:
            if not quiet:
                print('Could not force parse: "{}"'.format(obj.text))
            return None
        else:
            new_line = re.sub('access-list\s(\w+)\s(extended\s)*', 'access-list 1 ', line)
            if not quiet:
                print('Force parsing: "{}" into "{}"'.format(line, new_line))
            return force_parse(new_line, quiet, attempt)


def plot_connection(dot, protocols, source_addresses, source_port, destination_addresses, destination_port):
    protocol = protocols[0]
    source_address = str(source_addresses[0])
    destination_address = str(destination_addresses[0])
    source_port = source_port[0]
    destination_port = destination_port[0]

    if source_address == destination_address:
        destination_address = destination_address + ' '

    if source_port is not '*':
        protocol = socket.getservbyport(int(source_port))
    elif destination_port is not '*':
        protocol = socket.getservbyport(int(destination_port))
    else:
        protocol = str(protocol)

    dot.node(source_address, source_address)
    dot.node(destination_address, destination_address)
    dot.edge(source_address, destination_address, label=' {} '.format(protocol))


def generate_graph_file(file_name):
    config = CiscoConfParse('../input/{}.ios'.format(file_name))

    dot = Digraph(comment='Access list visualization', strict='true')

    for obj in config.find_objects('access-list'):
        if 'permit' in obj.text:
            acl_parsed = force_parse(obj.text, quiet=True)
            if acl_parsed:
                for acl in acl_parsed.terms:
                    acl = acl.match

                    protocol = acl['protocol'] if 'protocol' in acl else ['*']
                    source_address = acl['source-address'] if 'source-address' in acl else ['*']
                    source_port = acl['source-port'] if 'source-port' in acl else ['*']
                    destination_address = acl['destination-address'] if 'destination-address' in acl else ['*']
                    destination_port = acl['destination-port'] if 'destination-port' in acl else ['*']

                    plot_connection(dot, protocol, source_address, source_port, destination_address, destination_port)

    dot.render('../output/{}.pv'.format(file_name))


generate_graph_file('access-lists2')
