from os import remove, close
from shutil import move
from tempfile import mkstemp


def write_research_line(file, param, researchval):
    # writes a line to the file in research format, based on the type of research and whether the user would like it to
    # be researched (this function was longer in a previous version, but I didn't feel like replacing the function calls
    # with just the one line)
    file.write('    BEGIN ' + param + '  Desired false  Progress ' + "{:1.7f}".format(researchval / 100) + '  END\n')


# These are all the variables: They get a default (0 or False) because it is easier with testing
def write_general_settings(file, misconduct, gangs, decay, visibility, failure_conditions, events):
    file.write('EnabledMisconduct ' + str(misconduct) + '\n')
    file.write('EnabledGangs ' + str(gangs) + '\n')
    file.write('EnabledDecay ' + str(decay) + '\n')
    file.write('EnabledVisibility ' + str(visibility) + '\n')
    file.write('FailureConditions ' + str(failure_conditions) + '\n')
    file.write('EnabledEvents ' + str(events) + '\n')


def write_all_to_file(file_path,
                      misconduct, gangs, decay, visibility, failure_conditions, events,  # general
                      balance, bank_loan, credit_rating, ownership, unlimited_funds,  # Finance
                      maintainance, security, legal, mental_health, finance, cctv,
                      remote_access, health, cleaning, grounds_keeping, clone, deployment,
                      patrols, dogs, prison_labour, education, land_expansion, contraband,
                      policy, armoury, body_armour, tazers, tazers_for_everyone, bank_loans,
                      lower_taxes_1, lower_taxes_2, extra_grant, advanced_management, death_row,
                      permanent_punishment, remove_min_cell_size, reduce_execution_liability,
                      legal_prep, legal_defense  # research
                      ):
    # Create temp file
    fh, abs_path = mkstemp()

    # The save files we are working with are only 20.000 - 100.000 lines long; we therefore don't have to worry about
    # speed. That is why it opens and closes a file for every block it writes. (this was tested with files up to
    # 1.870.900 lines long: this results in a max. execution time of about 12 seconds, which isn't too bad, imho)
    with open(abs_path, 'a') as new_file:
        with open(file_path, 'r') as old_file:
            for line in old_file:
                # General:
                if 'EnabledMisconduct' in line:
                    write_general_settings(new_file, misconduct, gangs, decay, visibility, failure_conditions, events)
                elif 'EnabledGangs' in line or 'EnabledDecay' in line or 'EnabledVisibility' in line \
                        or 'FailureConditions' in line or 'UnlimitedFunds' in line or 'EnabledEvents' in line:
                    continue # All these conditions are handled by the function above, this continue makes sure that the line doesn't get copied

                # Finance:
                elif 'Balance' in line:
                    new_file.write('Balance ' + str(balance) + '\n')
                elif 'BankLoan' in line and 'BankLoans' not in line: # extra check for interference with research
                    new_file.write('BankLoan ' + str(bank_loan) + '\n')
                elif 'BankCreditRating' in line:
                    new_file.write('BankCreditRating ' + str(credit_rating) + '\n')
                elif 'Ownership' in line:
                    new_file.write('Ownership ' + str(ownership) + '\n')

                # research: (some of the research keywords occur elsewhere in the file. the Desired check makes sure
                # that this does not interfere) (Desired occurs only once besides the research block and doesn't interfere)
                elif 'Desired' in line:
                    if 'Maintainance' in line:
                        write_research_line(new_file, 'Maintainance', maintainance)
                    elif 'Security' in line:
                        write_research_line(new_file, 'Security', security)
                    elif 'Legal' in line and 'Prep' not in line and 'Defense' not in line:
                        write_research_line(new_file, 'Legal', legal)
                    elif 'MentalHealth' in line:
                        write_research_line(new_file, 'MentalHealth', mental_health)
                    elif 'Finance' in line:
                        write_research_line(new_file, 'Finance', finance)
                    elif 'Cctv' in line:
                        write_research_line(new_file, 'Cctv', cctv)
                    elif 'RemoteAccess' in line:
                        write_research_line(new_file, 'RemoteAccess', remote_access)
                    elif 'Health' in line:
                        write_research_line(new_file, 'Health', health)
                    elif 'Cleaning' in line:
                        write_research_line(new_file, 'Cleaning', cleaning)
                    elif 'GroundsKeeping' in line:
                        write_research_line(new_file, 'GroundsKeeping', grounds_keeping)
                    elif 'Clone' in line:
                        write_research_line(new_file, 'Clone', clone)
                    elif 'Deployment' in line:
                        write_research_line(new_file, 'Deployment', deployment)
                    elif 'Patrols' in line:
                        write_research_line(new_file, 'Patrols', patrols)
                    elif 'Dogs' in line:
                        write_research_line(new_file, 'Dogs', dogs)
                    elif 'PrisonLabour' in line:
                        write_research_line(new_file, 'PrisonLabour', prison_labour)
                    elif 'Education' in line:
                        write_research_line(new_file, 'Education', education)
                    elif 'LandExpansion' in line:
                        write_research_line(new_file, 'LandExpansion', land_expansion)
                    elif 'Contraband' in line:
                        write_research_line(new_file, 'Contraband', contraband)
                    elif 'Policy' in line:
                        write_research_line(new_file, 'Policy', policy)
                    elif 'Armoury' in line:
                        write_research_line(new_file, 'Armoury', armoury)
                    elif 'BodyArmour' in line:
                        write_research_line(new_file, 'BodyArmour', body_armour)
                    elif 'Tazers' in line and 'ForEveryone' not in line:
                        write_research_line(new_file, 'Tazers', tazers)
                    elif 'TazersForEveryone' in line:
                        write_research_line(new_file, 'TazersForEveryone', tazers_for_everyone)
                    elif 'BankLoans' in line:
                        write_research_line(new_file, 'BankLoans', bank_loans)
                    elif 'LowerTaxes1' in line:
                        write_research_line(new_file, 'LowerTaxes1', lower_taxes_1)
                    elif 'LowerTaxes2' in line:
                        write_research_line(new_file, 'LowerTaxes2', lower_taxes_2)
                    elif 'ExtraGrant' in line:
                        write_research_line(new_file, 'ExtraGrant', extra_grant)
                    elif 'AdvancedManagement' in line:
                        write_research_line(new_file, 'AdvancedManagement', advanced_management)
                    elif 'Deathrow' in line:
                        write_research_line(new_file, 'Deathrow', death_row)
                    elif 'PermanentPunishment' in line:
                        write_research_line(new_file, 'PermanentPunishment', permanent_punishment)
                    elif 'RemoveMinCellSize' in line:
                        write_research_line(new_file, 'RemoveMinCellSize', remove_min_cell_size)
                    elif 'ReduceExecutionLiability' in line:
                        write_research_line(new_file, 'ReduceExecutionLiability', reduce_execution_liability)
                    elif 'LegalPrep' in line:
                        write_research_line(new_file, 'LegalPrep', legal_prep)
                    elif 'LegalDefense' in line:
                        write_research_line(new_file, 'LegalDefense', legal_defense)

                # default:
                else:
                    new_file.write(line)

    # close writers
    close(fh)

    # Remove original file
    remove(file_path)
    # Move new file
    move(abs_path, file_path)


def write_general_to_file(file_path, misconduct, gangs, decay, visibility,
                          failure_conditions, events):
    # Create temp file
    fh, abs_path = mkstemp()

    # The save files we are working with are only 20.000 - 100.000 lines long; we therefore don't have to worry about
    # speed. That is why it opens and closes a file for every block it writes. (this was tested with files up to
    # 1.870.900 lines long: this results in a max. execution time of about 12 seconds, which isn't too bad, imho)
    with open(abs_path, 'a') as new_file:
        with open(file_path, 'r') as old_file:
            for line in old_file:
                # General:
                if 'EnabledMisconduct' in line:
                    write_general_settings(new_file, misconduct, gangs, decay, visibility, failure_conditions, events)
                elif 'EnabledGangs' in line or 'EnabledDecay' in line or 'EnabledVisibility' in line \
                        or 'FailureConditions' in line or 'EnabledEvents' in line:
                    continue # All these conditions are handled by the function above, this continue makes sure that the line doesn't get copied
                else:
                    new_file.write(line)

    # close writers
    close(fh)

    # Remove original file
    remove(file_path)
    # Move new file
    move(abs_path, file_path)


def write_finance_to_file(file_path, balance, bank_loan, credit_rating, ownership, unlimited_funds):
    # Create temp file
    fh, abs_path = mkstemp()

    # The save files we are working with are only 20.000 - 100.000 lines long; we therefore don't have to worry about
    # speed. That is why it opens and closes a file for every block it writes. (this was tested with files up to
    # 1.870.900 lines long: this results in a max. execution time of about 12 seconds, which isn't too bad, imho)
    with open(abs_path, 'a') as new_file:
        with open(file_path, 'r') as old_file:
            for line in old_file:
                # Finance:
                if 'Balance' in line:
                    new_file.write('Balance ' + str(balance) + '\n')
                elif 'BankLoan' in line and 'BankLoans' not in line: # extra check for interference with research
                    new_file.write('BankLoan ' + str(bank_loan) + '\n')
                elif 'BankCreditRating' in line:
                    new_file.write('BankCreditRating ' + str(credit_rating) + '\n')
                elif 'Ownership' in line:
                    new_file.write('Ownership ' + str(ownership) + '\n')
                elif 'UnlimitedFunds' in line:
                    new_file.write('UnlimitedFunds ' + str(unlimited_funds) + '\n')
                else:
                    new_file.write(line)

    # close writers
    close(fh)

    # Remove original file
    remove(file_path)
    # Move new file
    move(abs_path, file_path)


def write_research_to_file(file_path, maintainance, security, legal, mental_health, finance, cctv, remote_access,
                           health, cleaning, grounds_keeping, clone, deployment, patrols, dogs, prison_labour,
                           education, land_expansion, contraband, policy, armoury, body_armour, tazers,
                           tazers_for_everyone, bank_loans, lower_taxes_1, lower_taxes_2, extra_grant,
                           advanced_management, death_row, permanent_punishment, remove_min_cell_size,
                           reduce_execution_liability, legal_prep, legal_defense):
    # Create temp file
    fh, abs_path = mkstemp()

    # The save files we are working with are only 20.000 - 100.000 lines long; we therefore don't have to worry about
    # speed. That is why it opens and closes a file for every block it writes. (this was tested with files up to
    # 1.870.900 lines long: this results in a max. execution time of about 12 seconds, which isn't too bad, imho)
    with open(abs_path, 'a') as new_file:
        with open(file_path, 'r') as old_file:
            for line in old_file:
                # research: (some of the research keywords occur elsewhere in the file. the Desired check makes sure
                # that this does not interfere) (Desired occurs only once besides the research block and doesn't interfere)
                if 'Desired' in line:
                    if 'Maintainance' in line:
                        write_research_line(new_file, 'Maintainance', maintainance)
                    elif 'Security' in line:
                        write_research_line(new_file, 'Security', security)
                    elif 'Legal' in line and 'Prep' not in line and 'Defense' not in line:
                        write_research_line(new_file, 'Legal', legal)
                    elif 'MentalHealth' in line:
                        write_research_line(new_file, 'MentalHealth', mental_health)
                    elif 'Finance' in line:
                        write_research_line(new_file, 'Finance', finance)
                    elif 'Cctv' in line:
                        write_research_line(new_file, 'Cctv', cctv)
                    elif 'RemoteAccess' in line:
                        write_research_line(new_file, 'RemoteAccess', remote_access)
                    elif 'Health' in line:
                        write_research_line(new_file, 'Health', health)
                    elif 'Cleaning' in line:
                        write_research_line(new_file, 'Cleaning', cleaning)
                    elif 'GroundsKeeping' in line:
                        write_research_line(new_file, 'GroundsKeeping', grounds_keeping)
                    elif 'Clone' in line:
                        write_research_line(new_file, 'Clone', clone)
                    elif 'Deployment' in line:
                        write_research_line(new_file, 'Deployment', deployment)
                    elif 'Patrols' in line:
                        write_research_line(new_file, 'Patrols', patrols)
                    elif 'Dogs' in line:
                        write_research_line(new_file, 'Dogs', dogs)
                    elif 'PrisonLabour' in line:
                        write_research_line(new_file, 'PrisonLabour', prison_labour)
                    elif 'Education' in line:
                        write_research_line(new_file, 'Education', education)
                    elif 'LandExpansion' in line:
                        write_research_line(new_file, 'LandExpansion', land_expansion)
                    elif 'Contraband' in line:
                        write_research_line(new_file, 'Contraband', contraband)
                    elif 'Policy' in line:
                        write_research_line(new_file, 'Policy', policy)
                    elif 'Armoury' in line:
                        write_research_line(new_file, 'Armoury', armoury)
                    elif 'BodyArmour' in line:
                        write_research_line(new_file, 'BodyArmour', body_armour)
                    elif 'Tazers' in line and 'ForEveryone' not in line:
                        write_research_line(new_file, 'Tazers', tazers)
                    elif 'TazersForEveryone' in line:
                        write_research_line(new_file, 'TazersForEveryone', tazers_for_everyone)
                    elif 'BankLoans' in line:
                        write_research_line(new_file, 'BankLoans', bank_loans)
                    elif 'LowerTaxes1' in line:
                        write_research_line(new_file, 'LowerTaxes1', lower_taxes_1)
                    elif 'LowerTaxes2' in line:
                        write_research_line(new_file, 'LowerTaxes2', lower_taxes_2)
                    elif 'ExtraGrant' in line:
                        write_research_line(new_file, 'ExtraGrant', extra_grant)
                    elif 'AdvancedManagement' in line:
                        write_research_line(new_file, 'AdvancedManagement', advanced_management)
                    elif 'Deathrow' in line:
                        write_research_line(new_file, 'Deathrow', death_row)
                    elif 'PermanentPunishment' in line:
                        write_research_line(new_file, 'PermanentPunishment', permanent_punishment)
                    elif 'RemoveMinCellSize' in line:
                        write_research_line(new_file, 'RemoveMinCellSize', remove_min_cell_size)
                    elif 'ReduceExecutionLiability' in line:
                        write_research_line(new_file, 'ReduceExecutionLiability', reduce_execution_liability)
                    elif 'LegalPrep' in line:
                        write_research_line(new_file, 'LegalPrep', legal_prep)
                    elif 'LegalDefense' in line:
                        write_research_line(new_file, 'LegalDefense', legal_defense)

                # default:
                else:
                    new_file.write(line)

    # close writers
    close(fh)

    # Remove original file
    remove(file_path)
    # Move new file
    move(abs_path, file_path)