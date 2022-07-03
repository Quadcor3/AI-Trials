#choose_calc: (card_milestones, pull(estimated remaining round)*benefit(income, endpoints, milestone)) - cost, global_mod_learn, standard_projects, Global_benefits, tile_benefits, 

#est_round:

#defins:
benefit_mod=0

#utils
def benefit_if():
    if benefit_mod == 1:
        return 1


#benefit
def benefit():
    print("Benefit Test")
    if benefit_if == 1:
