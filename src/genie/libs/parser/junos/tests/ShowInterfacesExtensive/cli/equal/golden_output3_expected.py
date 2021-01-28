expected_output = {'interface-information': {'physical-interface': [{'admin-status': {'@junos:format': 'Enabled'},
                                                   'bpdu-error': 'None',
                                                   'current-physical-address': '2c:6b:f5:d6:f8:c0',
                                                   'ethernet-mac-statistics': {'input-broadcasts': '0',
                                                                               'input-multicasts': '0',
                                                                               'output-broadcasts': '0',
                                                                               'output-multicasts': '0'},
                                                   'hardware-physical-address': '2c:6b:f5:d6:f8:c0',
                                                   'if-config-flags': {'iff-snmp-traps': True,
                                                                       'internal-flags': '0x4000'},
                                                   'if-device-flags': {'ifdf-present': True,
                                                                       'ifdf-running': True},
                                                   'if-flow-control': 'Disabled',
                                                   'ingress-queue-counters': {'interface-cos-short-summary': {'intf-cos-num-queues-in-use': '4',
                                                                                                              'intf-cos-num-queues-supported': '8',
                                                                                                              'intf-cos-queue-type': 'Ingress '
                                                                                                                                     'queues'},
                                                                              'queue': [{'forwarding-class-name': 'best-effort',
                                                                                         'queue-counters-queued-packets': '0',
                                                                                         'queue-counters-total-drop-packets': '0',
                                                                                         'queue-counters-trans-packets': '0',
                                                                                         'queue-number': '0'},
                                                                                        {'forwarding-class-name': 'expedited-forwarding',
                                                                                         'queue-counters-queued-packets': '0',
                                                                                         'queue-counters-total-drop-packets': '0',
                                                                                         'queue-counters-trans-packets': '0',
                                                                                         'queue-number': '1'},
                                                                                        {'forwarding-class-name': 'assured-forwarding',
                                                                                         'queue-counters-queued-packets': '0',
                                                                                         'queue-counters-total-drop-packets': '0',
                                                                                         'queue-counters-trans-packets': '0',
                                                                                         'queue-number': '2'},
                                                                                        {'forwarding-class-name': 'network-control',
                                                                                         'queue-counters-queued-packets': '0',
                                                                                         'queue-counters-total-drop-packets': '0',
                                                                                         'queue-counters-trans-packets': '0',
                                                                                         'queue-number': '3'}]},
                                                   'input-error-list': {'framing-errors': '0',
                                                                        'input-discards': '0',
                                                                        'input-drops': '0',
                                                                        'input-errors': '0',
                                                                        'input-giants': '0',
                                                                        'input-resource-errors': '0',
                                                                        'input-runts': '0'},
                                                   'interface-flapped': {'#text': '2021-01-08 '
                                                                                  '00:13:28 '
                                                                                  'JST '
                                                                                  '(00:03:32 '
                                                                                  'ago)'},
                                                   'link-level-type': 'Ethernet',
                                                   'local-index': '159',
                                                   'logical-interface': [{'address-family': [{'address-family-flags': {'ifff-sendbcast-pkt-to-re': True},
                                                                                              'address-family-name': 'inet',
                                                                                              'generation': '172',
                                                                                              'interface-address': {'generation': '164',
                                                                                                                    'ifa-broadcast': '10.0.0.255',
                                                                                                                    'ifa-destination': '10.0.0/24',
                                                                                                                    'ifa-flags': {'ifaf-is-default': True,
                                                                                                                                  'ifaf-is-preferred': True,
                                                                                                                                  'ifaf-is-primary': True},
                                                                                                                    'ifa-local': '10.0.0.1'},
                                                                                              'intf-curr-cnt': '0',
                                                                                              'intf-dropcnt': '0',
                                                                                              'intf-unresolved-cnt': '0',
                                                                                              'max-local-cache': '75000',
                                                                                              'mtu': '1500',
                                                                                              'new-hold-limit': '75000',
                                                                                              'route-table': '0'},
                                                                                             {'address-family-flags': {'ifff-is-primary': True},
                                                                                              'address-family-name': 'inet6',
                                                                                              'generation': '166',
                                                                                              'interface-address': [{'ifa-destination': '2001:10::/64',
                                                                                                                     'ifa-flags': {'ifaf-is-default': True,
                                                                                                                                   'ifaf-is-preferred': True,
                                                                                                                                   'ifaf-is-primary': True},
                                                                                                                     'ifa-local': '2001:10::1'},
                                                                                                                    {'ifa-destination': 'fe80::/64',
                                                                                                                     'ifa-flags': {'ifaf-is-preferred': True},
                                                                                                                     'ifa-local': 'fe80::2e6b:f5ff:fed6:f8c0'}],
                                                                                              'intf-curr-cnt': '0',
                                                                                              'intf-dropcnt': '0',
                                                                                              'intf-unresolved-cnt': '0',
                                                                                              'max-local-cache': '75000',
                                                                                              'mtu': '1500',
                                                                                              'new-hold-limit': '75000',
                                                                                              'route-table': '0'},
                                                                                             {'address-family-flags': {'ifff-is-primary': True},
                                                                                              'address-family-name': 'inet6',
                                                                                              'generation': '166',
                                                                                              'interface-address': [{'ifa-destination': '2001:10::/64',
                                                                                                                     'ifa-flags': {'ifaf-is-default': True,
                                                                                                                                   'ifaf-is-preferred': True,
                                                                                                                                   'ifaf-is-primary': True},
                                                                                                                     'ifa-local': '2001:10::1'},
                                                                                                                    {'ifa-destination': 'fe80::/64',
                                                                                                                     'ifa-flags': {'ifaf-is-preferred': True},
                                                                                                                     'ifa-local': 'fe80::2e6b:f5ff:fed6:f8c0'}],
                                                                                              'intf-curr-cnt': '0',
                                                                                              'intf-dropcnt': '0',
                                                                                              'intf-unresolved-cnt': '0',
                                                                                              'max-local-cache': '75000',
                                                                                              'mtu': '1500',
                                                                                              'new-hold-limit': '75000',
                                                                                              'route-table': '0'},
                                                                                             {'address-family-flags': {'ifff-is-primary': True},
                                                                                              'address-family-name': 'multiservice',
                                                                                              'generation': '174',
                                                                                              'mtu': 'Unlimited',
                                                                                              'policer-information': {},
                                                                                              'route-table': '0'}],
                                                                          'encapsulation': 'ENET2',
                                                                          'if-config-flags': {'iff-snmp-traps': True,
                                                                                              'iff-up': True,
                                                                                              'internal-flags': '0x4004000'},
                                                                          'lag-traffic-statistics': {'aggregate-member-info': {'aggregate-member-count': '3'},
                                                                                                     'if-distribution-list-information': [{'if-list': [{'if-child-name': 'ge-0/0/0',
                                                                                                                                                        'if-status': 'Up'},
                                                                                                                                                       {'if-child-name': 'ge-0/0/4',
                                                                                                                                                        'if-status': 'Up'},
                                                                                                                                                       {'if-child-name': 'ge-0/0/6',
                                                                                                                                                        'if-status': 'Up'}],
                                                                                                                                           'list-status': 'Active',
                                                                                                                                           'list-type': 'Primary'},
                                                                                                                                          {'list-status': 'Down',
                                                                                                                                           'list-type': 'Backup'},
                                                                                                                                          {'list-status': 'Down',
                                                                                                                                           'list-type': 'Standby'}],
                                                                                                     'lag-adaptive-statistics': {'adaptive-adjusts': '0',
                                                                                                                                 'adaptive-scans': '0',
                                                                                                                                 'adaptive-updates': '0'},
                                                                                                     'lag-bundle': {'input-bps': '3432',
                                                                                                                    'input-bytes': '145843',
                                                                                                                    'input-packets': '1696',
                                                                                                                    'input-pps': '4',
                                                                                                                    'output-bps': '0',
                                                                                                                    'output-bytes': '1322',
                                                                                                                    'output-packets': '17',
                                                                                                                    'output-pps': '0'},
                                                                                                     'lag-lacp-info': [{'lacp-port-key': '1',
                                                                                                                        'lacp-port-number': '1',
                                                                                                                        'lacp-port-priority': '127',
                                                                                                                        'lacp-role': 'Actor',
                                                                                                                        'lacp-sys-priority': '127',
                                                                                                                        'lacp-system-id': '2c:6b:f5:d6:f8:c0',
                                                                                                                        'name': 'ge-0/0/0.0'},
                                                                                                                       {'lacp-port-key': '1',
                                                                                                                        'lacp-port-number': '1',
                                                                                                                        'lacp-port-priority': '127',
                                                                                                                        'lacp-role': 'Partner',
                                                                                                                        'lacp-sys-priority': '127',
                                                                                                                        'lacp-system-id': '2c:6b:f5:18:ef:c0',
                                                                                                                        'name': 'ge-0/0/0.0'},
                                                                                                                       {'lacp-port-key': '1',
                                                                                                                        'lacp-port-number': '2',
                                                                                                                        'lacp-port-priority': '127',
                                                                                                                        'lacp-role': 'Actor',
                                                                                                                        'lacp-sys-priority': '127',
                                                                                                                        'lacp-system-id': '2c:6b:f5:d6:f8:c0',
                                                                                                                        'name': 'ge-0/0/4.0'},
                                                                                                                       {'lacp-port-key': '1',
                                                                                                                        'lacp-port-number': '2',
                                                                                                                        'lacp-port-priority': '1',
                                                                                                                        'lacp-role': 'Partner',
                                                                                                                        'lacp-sys-priority': '1',
                                                                                                                        'lacp-system-id': '00:00:00:00:00:00',
                                                                                                                        'name': 'ge-0/0/4.0'},
                                                                                                                       {'lacp-port-key': '1',
                                                                                                                        'lacp-port-number': '3',
                                                                                                                        'lacp-port-priority': '127',
                                                                                                                        'lacp-role': 'Actor',
                                                                                                                        'lacp-sys-priority': '127',
                                                                                                                        'lacp-system-id': '2c:6b:f5:d6:f8:c0',
                                                                                                                        'name': 'ge-0/0/6.0'},
                                                                                                                       {'lacp-port-key': '1',
                                                                                                                        'lacp-port-number': '3',
                                                                                                                        'lacp-port-priority': '1',
                                                                                                                        'lacp-role': 'Partner',
                                                                                                                        'lacp-sys-priority': '1',
                                                                                                                        'lacp-system-id': '00:00:00:00:00:00',
                                                                                                                        'name': 'ge-0/0/6.0'}],
                                                                                                     'lag-lacp-statistics': [{'illegal-rx-packets': '0',
                                                                                                                              'lacp-rx-packets': '0',
                                                                                                                              'lacp-tx-packets': '0',
                                                                                                                              'unknown-rx-packets': '0'},
                                                                                                                             {'illegal-rx-packets': '0',
                                                                                                                              'lacp-rx-packets': '0',
                                                                                                                              'lacp-tx-packets': '0',
                                                                                                                              'unknown-rx-packets': '0'},
                                                                                                                             {'illegal-rx-packets': '0',
                                                                                                                              'lacp-rx-packets': '0',
                                                                                                                              'lacp-tx-packets': '0',
                                                                                                                              'unknown-rx-packets': '0'}],
                                                                                                     'lag-link': [{'input-bps': '3256',
                                                                                                                   'input-bytes': '124466',
                                                                                                                   'input-packets': '1347',
                                                                                                                   'input-pps': '4',
                                                                                                                   'name': 'ge-0/0/0.0',
                                                                                                                   'output-bps': '0',
                                                                                                                   'output-bytes': '1322',
                                                                                                                   'output-packets': '17',
                                                                                                                   'output-pps': '0'},
                                                                                                                  {'input-bps': '176',
                                                                                                                   'input-bytes': '21377',
                                                                                                                   'input-packets': '349',
                                                                                                                   'input-pps': '0',
                                                                                                                   'name': 'ge-0/0/4.0',
                                                                                                                   'output-bps': '0',
                                                                                                                   'output-bytes': '0',
                                                                                                                   'output-packets': '0',
                                                                                                                   'output-pps': '0'},
                                                                                                                  {'input-bps': '0',
                                                                                                                   'input-bytes': '0',
                                                                                                                   'input-packets': '0',
                                                                                                                   'input-pps': '0',
                                                                                                                   'name': 'ge-0/0/6.0',
                                                                                                                   'output-bps': '0',
                                                                                                                   'output-bytes': '0',
                                                                                                                   'output-packets': '0',
                                                                                                                   'output-pps': '0'}],
                                                                                                     'lag-marker': [{'illegal-rx-packets': '0',
                                                                                                                     'marker-response-tx-packets': '0',
                                                                                                                     'marker-rx-packets': '0',
                                                                                                                     'unknown-rx-packets': '0'},
                                                                                                                    {'illegal-rx-packets': '0',
                                                                                                                     'marker-response-tx-packets': '0',
                                                                                                                     'marker-rx-packets': '0',
                                                                                                                     'unknown-rx-packets': '0'},
                                                                                                                    {'illegal-rx-packets': '0',
                                                                                                                     'marker-response-tx-packets': '0',
                                                                                                                     'marker-rx-packets': '0',
                                                                                                                     'unknown-rx-packets': '0'}]},
                                                                          'local-index': '320',
                                                                          'name': 'ae0.0',
                                                                          'snmp-index': '542'}],
                                                   'loopback': 'Disabled',
                                                   'mac-rewrite-error': 'None',
                                                   'minimum-bandwidth-in-aggregate': '1bps',
                                                   'minimum-links-in-aggregate': '1',
                                                   'mtu': '1514',
                                                   'name': 'ae0',
                                                   'oper-status': 'Up',
                                                   'output-error-list': {'carrier-transitions': '0',
                                                                         'mtu-errors': '0',
                                                                         'output-drops': '0',
                                                                         'output-errors': '0',
                                                                         'output-resource-errors': '0'},
                                                   'pad-to-minimum-frame-size': 'Disabled',
                                                   'queue-counters': {'interface-cos-short-summary': {'intf-cos-num-queues-in-use': '4',
                                                                                                      'intf-cos-num-queues-supported': '8',
                                                                                                      'intf-cos-queue-type': 'Egress '
                                                                                                                             'queues'},
                                                                      'queue': [{'forwarding-class-name': 'best-effort',
                                                                                 'queue-counters-queued-packets': '1',
                                                                                 'queue-counters-total-drop-packets': '0',
                                                                                 'queue-counters-trans-packets': '1',
                                                                                 'queue-number': '0'},
                                                                                {'forwarding-class-name': 'expedited-forwarding',
                                                                                 'queue-counters-queued-packets': '0',
                                                                                 'queue-counters-total-drop-packets': '0',
                                                                                 'queue-counters-trans-packets': '0',
                                                                                 'queue-number': '1'},
                                                                                {'forwarding-class-name': 'assured-forwarding',
                                                                                 'queue-counters-queued-packets': '0',
                                                                                 'queue-counters-total-drop-packets': '0',
                                                                                 'queue-counters-trans-packets': '0',
                                                                                 'queue-number': '2'},
                                                                                {'forwarding-class-name': 'network-control',
                                                                                 'queue-counters-queued-packets': '1336',
                                                                                 'queue-counters-total-drop-packets': '0',
                                                                                 'queue-counters-trans-packets': '1336',
                                                                                 'queue-number': '3'}]},
                                                   'snmp-index': '539',
                                                   'source-filtering': 'Disabled',
                                                   'speed': '1Gbps',
                                                   'statistics-cleared': 'Never',
                                                   'stp-traffic-statistics': {'stp-input-bytes-dropped': '0',
                                                                              'stp-input-packets-dropped': '0',
                                                                              'stp-output-bytes-dropped': '0',
                                                                              'stp-output-packets-dropped': '0'},
                                                   'traffic-statistics': {'input-bps': '3432',
                                                                          'input-bytes': '227807',
                                                                          'input-packets': '2357',
                                                                          'input-pps': '4',
                                                                          'ipv6-transit-statistics': {'input-bytes': '912',
                                                                                                      'input-packets': '14',
                                                                                                      'output-bytes': '0',
                                                                                                      'output-packets': '0'},
                                                                          'output-bps': '2120',
                                                                          'output-bytes': '173544',
                                                                          'output-packets': '1341',
                                                                          'output-pps': '2'}}]}}