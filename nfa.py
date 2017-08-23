
"""
-------------------------------------------------------
Non-Deterministic Finite State Automata 
-------------------------------------------------------
Preconditions:
set_states (Python set): set of states in the NFA.
set_alphabet (Python set): set of all possible characters the automaton recognizes.
transition_state (Python dictionary): the transition fn is represented as follows:
delta = {(state_i element of set_states, char a element of sigma): new state element of set_states}
start_state (string): element of set_states.
set_final_states (Python set): set of accept state. Each element of this set is element of set_states.
Postconditions:
Initializes NFA object
-------------------------------------------------------
"""

class NFA:

    def __init__(self, set_states, set_alphabet, transition_dict, start_state, set_final_states):
        self.Q = set_states
        self.sigma = set_alphabet
        self.delta = transition_dict
        self.q1 = start_state
        self.F = set_final_states
        return

    def visit(self, old_state, s):
        """
        Parameters
        ----------
        old_state: The current state str
        s: The alphabet being evaluated
        If there is a transition rule (oldstate, s) in self.delta, then transition.

        This function returns a list of strings of new states that the transition rule leads us to.
        """
        if (old_state, s) not in self.delta:
            return None

        str_list_of_new_states = self.delta[(old_state, s)]

        return str_list_of_new_states

    def recursive_process_string(self, str):
        current_state = self.q1
       
        return self.helper_recursion(current_state, str)

    def helper_recursion(self, old_state, str):

        # Base Case
        if len(str) == 0:
            if old_state in self.F:
                return True
            return False

        # Iterative Case
        # Getting the next alphabet and preparing the `str` for the next recursive step
        ret_val = False
        if str[0] in self.sigma:
          list_of_new_states = self.visit(old_state, str[0])
          if list_of_new_states:
            for ns_node in list_of_new_states:
                if ret_val == False:
                    ret_val = self.helper_recursion(ns_node, str[1:]) # ********

        return ret_val
