def get_general_settings(file_path):
    misconduct = gangs = decay = visibility = failure_conditions = events = False

    with open(file_path, 'r') as file:
        for line in file:
            # General:
            if 'EnabledMisconduct' in line and 'true' in line.lower():
                misconduct = True
            elif 'EnabledGangs' in line and 'true' in line.lower():
                gangs = True
            elif 'EnabledDecay' in line and 'true' in line.lower():
                decay = True
            elif 'EnabledVisibility' in line and 'true' in line.lower():
                visibility = True
            elif 'FailureConditions' in line and 'true' in line.lower():
                failure_conditions = True
            elif 'EnabledEvents' in line and 'true' in line.lower():
                events = True
    return misconduct, gangs, decay, visibility, failure_conditions, events


def get_finance_settings(file_path):
    balance = bank_loan = credit_rating = ownership = unlimited_funds = 0
    with open(file_path, 'r') as file:
        for line in file:
            # Finance:
            if 'Balance' in line:
                balance = line.replace('Balance', '')
                balance = balance.strip()
            elif 'BankLoan' in line and 'BankLoans' not in line:  # extra check for interference with research
                bank_loan = line.replace('BankLoan', '')
                bank_loan = bank_loan.strip()
            elif 'BankCreditRating' in line:
                credit_rating = line.replace('BankCreditRating', '')
                credit_rating = credit_rating.strip()
            elif 'Ownership' in line:
                ownership = line.replace('Ownership', '')
                ownership = ownership.strip()
            elif 'UnlimitedFunds' in line:
                if 'true' in line.lower():
                    unlimited_funds = True
                else:
                    unlimited_funds = False

    return balance, bank_loan, credit_rating, ownership, unlimited_funds


def get_research_settings(file_path):
    maintainance = security = legal = mental_health = finance = cctv = remote_access = health = cleaning = grounds_keeping = \
        clone = deployment = patrols = dogs = prison_labour = education = land_expansion = contraband = policy = armoury = \
        body_armour = tazers = tazers_for_everyone = bank_loans = lower_taxes_1 = lower_taxes_2 = extra_grant = \
        advanced_management = death_row = permanent_punishment = remove_min_cell_size = reduce_execution_liability = \
        legal_prep = legal_defense = 0.0

    with open(file_path, 'r') as old_file:
        for line in old_file:
            if 'Desired' in line:
                # Desired only occurs in the save-file in the research block + 1 other place.

                # example of a typical line:
                # >>BEGIN None       Desired false  Progress 1.000000  END<<
                # it should therefore be possible to extract the ^ float using the following:
                for s in line.split(' '):
                    try:
                        fl = float(s) * 100
                    except ValueError:
                        pass
                if 'Maintainance' in line:
                    maintainance = fl
                elif 'Security' in line:
                    security = fl
                elif 'Legal' in line and 'Prep' not in line and 'Defense' not in line:
                    legal = fl
                elif 'MentalHealth' in line:
                    mental_health = fl
                elif 'Finance' in line:
                    finance = fl
                elif 'Cctv' in line:
                    cctv = fl
                elif 'RemoteAccess' in line:
                    remote_access = fl
                elif 'Health' in line:
                    health = fl
                elif 'Cleaning' in line:
                    cleaning = fl
                elif 'GroundsKeeping' in line:
                    grounds_keeping = fl
                elif 'Clone' in line:
                    clone = fl
                elif 'Deployment' in line:
                    deployment = fl
                elif 'Patrols' in line:
                    patrols = fl
                elif 'Dogs' in line:
                    dogs = fl
                elif 'PrisonLabour' in line:
                    prison_labour = fl
                elif 'Education' in line:
                    education = fl
                elif 'LandExpansion' in line:
                    land_expansion = fl
                elif 'Contraband' in line:
                    contraband = fl
                elif 'Policy' in line:
                    policy = fl
                elif 'Armoury' in line:
                    armoury = fl
                elif 'BodyArmour' in line:
                    body_armour = fl
                elif 'Tazers' in line and 'ForEveryone' not in line:
                    tazers = fl
                elif 'TazersForEveryone' in line:
                    tazers_for_everyone = fl
                elif 'BankLoans' in line:
                    bank_loans = fl
                elif 'LowerTaxes1' in line:
                    lower_taxes_1 = fl
                elif 'LowerTaxes2' in line:
                    lower_taxes_2 = fl
                elif 'ExtraGrant' in line:
                    extra_grant = fl
                elif 'AdvancedManagement' in line:
                    advanced_management = fl
                elif 'Deathrow' in line:
                    death_row = fl
                elif 'PermanentPunishment' in line:
                    permanent_punishment = fl
                elif 'RemoveMinCellSize' in line:
                    remove_min_cell_size = fl
                elif 'ReduceExecutionLiability' in line:
                    reduce_execution_liability = fl
                elif 'LegalPrep' in line:
                    legal_prep = fl
                elif 'LegalDefense' in line:
                    legal_defense = fl

    return maintainance, security, legal, mental_health, finance, cctv, remote_access, health, cleaning, \
           grounds_keeping, clone, deployment, patrols, dogs, prison_labour, education, land_expansion, contraband, \
           policy, armoury, body_armour, tazers, tazers_for_everyone, bank_loans, lower_taxes_1, lower_taxes_2, \
           extra_grant, advanced_management, death_row, permanent_punishment, remove_min_cell_size, \
           reduce_execution_liability, legal_prep, legal_defense
