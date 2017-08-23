from nfa import NFA


'''
NFA D recognizes language:
L(D) = {s | s contains '(A|B)[C]D'}
'''

set_states = set(['s1', 's2', 's3'])
set_alphabet = set(['A', 'B', 'C'])
transition_dict = {('s1', 'A'): ['s2', 's3'], ('s1', 'B'): ['s2','s3'], ('s2', 'C'): ['s3'], ('s3', 'D'): ['s3']}
#transition_dict = {('s1', 'A'): 's2', ('s1', 'A'): 's3', ('s2', 'C'): ['s3'], ('s3', 'D'): ['s3']}
start_state = 's1'
set_final_states = set(['s3'])

set_alphabet = set(['A', 'B', 'C', 'D', 'E'])
transition_dict = {
                ('s1', 'A'): ['s2', 's3'], ('s1', 'B'): ['s2','s3'], ('s1', 'C'): ['s2','s3'], 
                ('s2', 'D'): ['s3'], ('s2', 'E'): ['s3'],
                ('s3', 'F'): ['s3']
                }

set_alphabet = set(['A', 'B', 'C'])
transition_dict = {
                ('s1', 'A'): ['s2', 's4'], ('s1', 'B'): ['s2'], ('s1', 'C'): ['s3'], 
                ('s2', 'B'): ['s3'],
                ('s4', 'B'): ['s2', 's5'],
                ('s5', 'C'): ['s3']
                }


D = NFA(set_states, set_alphabet, transition_dict, start_state, set_final_states)

orig_str = 'ACD'
str = 'ABB'

is_accepted = D.recursive_process_string(str)

if is_accepted:
    print('{0} is accepted by D'.format(str))
else:
    print ('no')
