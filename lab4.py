# MIT 6.034 Lab 4: Rule-Based Systems
# Written by 6.034 staff

from production import IF, AND, OR, NOT, THEN, DELETE, forward_chain, pretty_goal_tree
from data import *
import pprint

pp = pprint.PrettyPrinter(indent=1)
pprint = pp.pprint

#### Part 1: Multiple Choice #########################################

ANSWER_1 = '2'

ANSWER_2 = '4'

ANSWER_3 = '2'

ANSWER_4 = '0'

ANSWER_5 = '3'

ANSWER_6 = '1'

ANSWER_7 = '0'

#### Part 2: Transitive Rule #########################################

# Fill this in with your rule 
transitive_rule = IF( AND("(?x) beats (?y)", "(?y) beats (?z)" ), THEN("(?x) beats (?z)" ) )

# You can test your rule by uncommenting these pretty print statements
#  and observing the results printed to your screen after executing lab1.py
# pprint(forward_chain([transitive_rule], abc_data))
# pprint(forward_chain([transitive_rule], poker_data))
# pprint(forward_chain([transitive_rule], minecraft_data))


#### Part 3: Family Relations #########################################

# Define your rules here. We've given you an example rule whose lead you can follow:
friend_rule = IF( AND("person (?x)", "person (?y)"), THEN ("friend (?x) (?y)", "friend (?y) (?x)") )

sibling_rule = IF( AND("parent (?x) (?y)", "parent (?x) (?z)"), THEN("sibling (?y) (?z)"))

child_rule = IF(("parent (?x) (?y)"), THEN("child (?y) (?x)"))

cousin_rule = IF(AND("parent (?x) (?y)", "parent (?w) (?z)", "sibling (?x) (?w)", NOT("sibling (?y) (?z)")), THEN("cousin (?y) (?z)"))

grandparent_rule = IF(AND("parent (?x) (?y)", "parent (?y) (?z)"), THEN("grandparent (?x) (?z)"))

grandchild_rule = IF(AND("child (?x) (?y)", "child (?y) (?z)"), THEN("grandchild (?x) (?z)"))



# Add your rules to this list:
family_rules = [ friend_rule, sibling_rule, child_rule, cousin_rule, grandparent_rule, grandchild_rule]

# Uncomment this to test your data on the Simpsons family:
# pprint(forward_chain(family_rules, simpsons_data, verbose=False))

# These smaller datasets might be helpful for debugging:
# pprint(forward_chain(family_rules, sibling_test_data, verbose=True))
# pprint(forward_chain(family_rules, grandparent_test_data, verbose=True))

# The following should generate 14 cousin relationships, representing 7 pairs
# of people who are cousins:
# harry_potter_family_cousins = [
#     relation for relation in
#     forward_chain(family_rules, harry_potter_family_data, verbose=False)
#     if "cousin" in relation ]

# To see if you found them all, uncomment this line:
# pprint(harry_potter_family_cousins)


#### Part 4: Backward Chaining #########################################

# Import additional methods for backchaining
from production import PASS, FAIL, match, populate, simplify, variables

def backchain_to_goal_tree(rules, hypothesis):
    """
    Takes a hypothesis (string) and a list of rules (list
    of IF objects), returning an AND/OR tree representing the
    backchain of possible statements we may need to test
    to determine if this hypothesis is reachable or not.

    This method should return an AND/OR tree, that is, an
    AND or OR object, whose constituents are the subgoals that
    need to be tested. The leaves of this tree should be strings
    (possibly with unbound variables), *not* AND or OR objects.
    Make sure to use simplify(...) to flatten trees where appropriate.
    """
    # pprint(rules)
    # print()
    # pprint(hypothesis)

    match_chain = OR()

    for rule in rules:
        matched = match(rule.consequent(), hypothesis)
        if matched is not None:
            populated = populate(rule.antecedent(), matched)
            if type(populated) is str:
                match_chain = OR(match_chain, populated)
            else:
                for i in range(len(populated)):
                    populated[i] = backchain_to_goal_tree(rules, populated[i])

                    match_chain = OR(match_chain, populated)

    return simplify(OR(hypothesis, match_chain))

# Uncomment this to test out your backward chainer:
# pretty_goal_tree(backchain_to_goal_tree(zookeeper_rules, 'opus is a penguin'))


#### Survey #########################################

NAME = "Theodore Calabrese"
COLLABORATORS = ""
HOW_MANY_HOURS_THIS_LAB_TOOK = None
WHAT_I_FOUND_INTERESTING = "Logical thinking can be fun"
WHAT_I_FOUND_BORING = "Not much"
SUGGESTIONS = ""


###########################################################
### Ignore everything below this line; for testing only ###
###########################################################

# The following lines are used in the tester. DO NOT CHANGE!
print("(Doing forward chaining. This may take a minute.)")
transitive_rule_poker = forward_chain([transitive_rule], poker_data)
transitive_rule_abc = forward_chain([transitive_rule], abc_data)
transitive_rule_minecraft = forward_chain([transitive_rule], minecraft_data)
family_rules_simpsons = forward_chain(family_rules, simpsons_data)
family_rules_harry_potter_family = forward_chain(family_rules, harry_potter_family_data)
family_rules_sibling = forward_chain(family_rules, sibling_test_data)
family_rules_grandparent = forward_chain(family_rules, grandparent_test_data)
family_rules_anonymous_family = forward_chain(family_rules, anonymous_family_test_data)
family_rules_black = forward_chain(family_rules, black_data)

# pprint(backchain_to_goal_tree((IF(AND('(?x) has hair'), THEN('(?x) is a mammal')), IF(AND('(?x) gives milk'), THEN('(?x) is a mammal')), IF(AND('(?x) has feathers'), THEN('(?x) is a bird')), IF(AND('(?x) flies', '(?x) lays eggs'), THEN('(?x) is a bird')), IF(AND('(?x) is a mammal', '(?x) eats meat'), THEN('(?x) is a carnivore')), IF(AND('(?x) is a mammal', '(?x) has pointed teeth', '(?x) has claws', '(?x) has forward-pointing eyes'), THEN('(?x) is a carnivore')), IF(AND('(?x) is a mammal', '(?x) has hoofs'), THEN('(?x) is an ungulate')), IF(AND('(?x) is a mammal', '(?x) chews cud'), THEN('(?x) is an ungulate')), IF(AND('(?x) is a carnivore', '(?x) has tawny color', '(?x) has dark spots'), THEN('(?x) is a cheetah')), IF(AND('(?x) is a carnivore', '(?x) has tawny color', '(?x) has black stripes'), THEN('(?x) is a tiger')), IF(AND('(?x) is an ungulate', '(?x) has long legs', '(?x) has long neck', '(?x) has tawny color', '(?x) has dark spots'), THEN('(?x) is a giraffe')), IF(AND('(?x) is an ungulate', '(?x) has white color', '(?x) has black stripes'), THEN('(?x) is a zebra')), IF(AND('(?x) is a bird', '(?x) does not fly', '(?x) has long legs', '(?x) has long neck', '(?x) has black and white color'), THEN('(?x) is an ostrich')), IF(AND('(?x) is a bird', '(?x) does not fly', '(?x) swims', '(?x) has black and white color'), THEN('(?x) is a penguin')), IF(AND('(?x) is a bird', '(?x) is a good flyer'), THEN('(?x) is an albatross'))), 'opus is a penguin'))

# backchain_to_goal_tree((IF(AND('(?x) has hair'), THEN('(?x) is a mammal')), IF(AND('(?x) gives milk'), THEN('(?x) is a mammal')), IF(AND('(?x) has feathers'), THEN('(?x) is a bird')), IF(AND('(?x) flies', '(?x) lays eggs'), THEN('(?x) is a bird')), IF(AND('(?x) is a mammal', '(?x) eats meat'), THEN('(?x) is a carnivore')), IF(AND('(?x) is a mammal', '(?x) has pointed teeth', '(?x) has claws', '(?x) has forward-pointing eyes'), THEN('(?x) is a carnivore')), IF(AND('(?x) is a mammal', '(?x) has hoofs'), THEN('(?x) is an ungulate')), IF(AND('(?x) is a mammal', '(?x) chews cud'), THEN('(?x) is an ungulate')), IF(AND('(?x) is a carnivore', '(?x) has tawny color', '(?x) has dark spots'), THEN('(?x) is a cheetah')), IF(AND('(?x) is a carnivore', '(?x) has tawny color', '(?x) has black stripes'), THEN('(?x) is a tiger')), IF(AND('(?x) is an ungulate', '(?x) has long legs', '(?x) has long neck', '(?x) has tawny color', '(?x) has dark spots'), THEN('(?x) is a giraffe')), IF(AND('(?x) is an ungulate', '(?x) has white color', '(?x) has black stripes'), THEN('(?x) is a zebra')), IF(AND('(?x) is a bird', '(?x) does not fly', '(?x) has long legs', '(?x) has long neck', '(?x) has black and white color'), THEN('(?x) is an ostrich')), IF(AND('(?x) is a bird', '(?x) does not fly', '(?x) swims', '(?x) has black and white color'), THEN('(?x) is a penguin')), IF(AND('(?x) is a bird', '(?x) is a good flyer'), THEN('(?x) is an albatross'))), 'opus is a penguin')

