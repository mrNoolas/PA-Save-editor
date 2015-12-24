from os import remove, close
from shutil import move, copy
from tempfile import mkstemp
from tkinter import *
from tkinter import filedialog
from tkinter import ttk


def write_research_line(file, param, researchval):
    # writes a line to the file in research format, based on the type of research and whether the user would like it to
    # be researched (this function was longer in a previous version, but I didn't feel like replacing the function calls
    # with just the one line)
    file.write('    BEGIN ' + param + '  Desired false  Progress ' + "{:1.7f}".format((researchval / 100)) + '  END\n')


# These are all the variables: They get a default (0 or False) because it is easier with testing
def write_general_settings(file, misconduct, gangs, decay, visibility, failure_conditions, events, unlimited_funds):
    file.write('EnabledMisconduct ' + str(misconduct) + '\n')
    file.write('EnabledGangs ' + str(gangs) + '\n')
    file.write('EnabledDecay ' + str(decay) + '\n')
    file.write('EnabledVisibility ' + str(visibility) + '\n')
    file.write('FailureConditions ' + str(failure_conditions) + '\n')
    file.write('EnabledEvents ' + str(events) + '\n')
    file.write('UnlimitedFunds ' + str(unlimited_funds) + '\n')


def write_general_to_file(file_path, misconduct, gangs, decay, visibility,
                          failure_conditions, events, unlimited_funds):
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
                    write_general_settings(new_file, misconduct, gangs, decay, visibility, failure_conditions, events, unlimited_funds)
                elif 'EnabledGangs' in line or 'EnabledDecay' in line or 'EnabledVisibility' in line \
                        or 'FailureConditions' in line or 'EnabledEvents' in line or 'UnlimitedFunds' in line:
                    continue # All these conditions are handled by the function above, this continue makes sure that the line doesn't get copied
                else:
                    new_file.write(line)

    # close writers
    close(fh)

    # Remove original file
    remove(file_path)
    # Move new file
    move(abs_path, file_path)


def write_finance_to_file(file_path, balance, bank_loan, credit_rating, ownership):
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


# The following handles everything to do with the gui. (main)
# variables starting with var are default values; when the user changes the value of a ui element,
# these variables auto change with them. It is therefore very easy to get the current state of ui items.
def gen_set():
    """ This function is called whenever a save-event is requested. The function retrieves all ui-vars and writes the
    data in them to the .prison save file. It also manages the unlimited funds checkbox (it automatically disables the
    balance Entry)"""
    write_general_to_file(save_file_path, bool(var_misconduct.get()), bool(var_gangs.get()), bool(var_decay.get()),
                          bool(var_visibility.get()), bool(var_failure_conditions.get()), bool(var_events.get()),
                          bool(var_unlimited_funds.get()))
    write_finance_to_file(save_file_path, var_balance.get(), var_bank_loan.get(), var_credit_rating.get(),
                          var_ownership.get())
    res_set()

    if var_unlimited_funds.get():
        balance_entry.configure(state=DISABLED)
    else:
        balance_entry.configure(state=NORMAL)


def res_set(var=0):
    global maintainance, security, legal, mental_health, finance, cctv, remote_access, health, cleaning, grounds_keeping, \
        clone, deployment, patrols,  dogs,  prison_labour,  education,  land_expansion, contraband, policy,  armoury, \
        body_armour,  tazers,  tazers_for_everyone,  bank_loans, lower_taxes_1,  lower_taxes_2,  extra_grant, \
        advanced_management,  death_row, permanent_punishment,  remove_min_cell_size,  reduce_execution_liability, \
        legal_prep, legal_defense

    selected = combo_var.get()
    fl = var_research_scale.get()
    if 'Maintainance' in selected:
        maintainance = fl
    elif 'Security' in selected:
        security = fl
    elif 'Legal' in selected and 'Prep' not in selected and 'Defense' not in selected:
        legal = fl
    elif 'Mental Health' in selected:
        mental_health = fl
    elif 'Finance' in selected:
        finance = fl
    elif 'Cctv' in selected:
        cctv = fl
    elif 'Remote Access' in selected:
        remote_access = fl
    elif 'Health' in selected:
        health = fl
    elif 'Cleaning' in selected:
        cleaning = fl
    elif 'Grounds Keeping' in selected:
        grounds_keeping = fl
    elif 'Clone' in selected:
        clone = fl
    elif 'Deployment' in selected:
        deployment = fl
    elif 'Patrols' in selected:
        patrols = fl
    elif 'Dogs' in selected:
        dogs = fl
    elif 'Prison Labour' in selected:
        prison_labour = fl
    elif 'Education' in selected:
        education = fl
    elif 'Land Expansion' in selected:
        land_expansion = fl
    elif 'Contraband' in selected:
        contraband = fl
    elif 'Policy' in selected:
        policy = fl
    elif 'Armoury' in selected:
        armoury = fl
    elif 'BodyArmour' in selected:
        body_armour = fl
    elif 'Tazers' in selected and 'For Everyone' not in selected:
        tazers = fl
    elif 'Tazers For Everyone' in selected:
        tazers_for_everyone = fl
    elif 'Bank Loans' in selected:
        bank_loans = fl
    elif 'Lower Taxes1' in selected:
        lower_taxes_1 = fl
    elif 'Lower Taxes2' in selected:
        lower_taxes_2 = fl
    elif 'Extra Grant' in selected:
        extra_grant = fl
    elif 'Advanced Management' in selected:
        advanced_management = fl
    elif 'Deathrow' in selected:
        death_row = fl
    elif 'Permanent Punishment' in selected:
        permanent_punishment = fl
    elif 'Remove Min Cell Size' in selected:
        remove_min_cell_size = fl
    elif 'Reduce Execution Liability' in selected:
        reduce_execution_liability = fl
    elif 'Legal Prep' in selected:
        legal_prep = fl
    elif 'Legal Defense' in selected:
        legal_defense = fl

    write_research_to_file(save_file_path, maintainance, security, legal, mental_health, finance, cctv, remote_access,
                           health, cleaning, grounds_keeping, clone, deployment, patrols,  dogs,  prison_labour,
                           education,  land_expansion, contraband, policy,  armoury, body_armour,  tazers,
                           tazers_for_everyone,  bank_loans, lower_taxes_1,  lower_taxes_2,  extra_grant,
                           advanced_management,  death_row, permanent_punishment,  remove_min_cell_size,
                           reduce_execution_liability, legal_prep, legal_defense)


def validate_and_save():
    """ This function takes the values in the Entry boxes and checks if it is a valid float. It also organises feedback
     to the user."""

    def isnum(y):
        ch = '0123456789.-'
        for x in y:
            if x not in ch:
                return False
        return True

    a = var_balance.get()
    b = var_bank_loan.get()
    c = var_credit_rating.get()
    d = var_ownership.get()

    if isnum(a) and isnum(b) and isnum(c) and isnum(d):
        try:
            float(a)
            float(b)
            float(c)
            if 100 >= float(d) >= 0:
                gen_set()
                save_result.configure(background='#66ff66')
                var_save_result.set('The data was valid')
            else:
                save_result.configure(background='#ff6666')
                var_save_result.set('% <= 100% ... :|')
        except ValueError:
            save_result.configure(background='#ff6666')
            var_save_result.set('Numbers only! (0123456789.-)')
    else:
        save_result.configure(background='#ff6666')
        var_save_result.set('Numbers only! (0123456789.-)')


def set_default_data(file_path):
    """ :param file_path: the file to write to\n
    This function retrieves predetermined data from a given file, and then asigns the values to the global ui-vars"""
    misconduct, gangs, decay, visibility, failure_conditions, events = get_general_settings(file_path)
    var_misconduct.set(misconduct)
    var_gangs.set(gangs)
    var_decay.set(decay)
    var_visibility.set(visibility)
    var_failure_conditions.set(failure_conditions)
    var_events.set(events)

    balance, bank_loan, credit_rating, ownership, unlimited_funds = get_finance_settings(file_path)
    var_balance.set(balance)
    var_bank_loan.set(bank_loan)
    var_credit_rating.set(credit_rating)
    var_ownership.set(ownership)
    var_unlimited_funds.set(unlimited_funds)

    global maintainance, security, legal, mental_health, finance, cctv, remote_access, health, cleaning, grounds_keeping, \
        clone, deployment, patrols,  dogs,  prison_labour,  education,  land_expansion, contraband, policy,  armoury, \
        body_armour,  tazers,  tazers_for_everyone,  bank_loans, lower_taxes_1,  lower_taxes_2,  extra_grant, \
        advanced_management,  death_row, permanent_punishment,  remove_min_cell_size,  reduce_execution_liability, \
        legal_prep, legal_defense

    maintainance, security, legal, mental_health, finance, cctv, remote_access, health, cleaning, grounds_keeping, \
        clone, deployment, patrols,  dogs,  prison_labour,  education,  land_expansion, contraband, policy,  armoury, \
        body_armour,  tazers,  tazers_for_everyone,  bank_loans, lower_taxes_1,  lower_taxes_2,  extra_grant, \
        advanced_management,  death_row, permanent_punishment,  remove_min_cell_size,  reduce_execution_liability, \
        legal_prep, legal_defense = get_research_settings(file_path)


def select_files():
    """ Get file to read from and file to save to
        This function first asks the user for two files, and then check's whether the file is valid. If the user cancels
        the file-selection proces, () is returned: that is why the check asks for 3 or more characters.
        The program then makes a copy of the given source-file, and keeps the copy as changable output dump
        At set_default_data, the function fills in the blancs in the form using data from the given source-file."""
    open_file_path = filedialog.askopenfilename()
    global save_file_path
    save_file_path = filedialog.asksaveasfilename()

    if len(open_file_path) < 3 or len(save_file_path) < 3:
        raise OSError(10, 'There was a problem while selecting files (FILENAME TOO SHORT)')
    elif not open_file_path.endswith('.prison'):
        raise OSError(11, 'There was a problem while selecting files (FILE 1 WAS NOT A .prison FILE!)')
    elif not save_file_path.endswith('.prison'):
        raise OSError(12, 'There was a problem while selecting files (FILE 2 WAS NOT A .prison FILE!)')

    if open_file_path != save_file_path:  # copy throws an error when this is the case
        # copy
        copy(open_file_path, save_file_path)

    # read data from file:
    set_default_data(save_file_path)

    # show tabs:
    mainframe.add(general_page, text='General/finance')

    # Disable button:
    select_files_button.configure(state=DISABLED)


def combo_update(var=0):
    selected = combo_var.get()

    if 'Maintainance' in selected:
        var_research_scale.set(maintainance)
    elif 'Security' in selected:
        var_research_scale.set(security)
    elif 'Legal' in selected and 'Prep' not in selected and 'Defense' not in selected:
        var_research_scale.set(legal)
    elif 'Mental Health' in selected:
        var_research_scale.set(mental_health)
    elif 'Finance' in selected:
        var_research_scale.set(finance)
    elif 'Cctv' in selected:
        var_research_scale.set(cctv)
    elif 'Remote Access' in selected:
        var_research_scale.set(remote_access)
    elif 'Health' in selected:
        var_research_scale.set(health)
    elif 'Cleaning' in selected:
        var_research_scale.set(cleaning)
    elif 'Grounds Keeping' in selected:
        var_research_scale.set(grounds_keeping)
    elif 'Clone' in selected:
        var_research_scale.set(clone)
    elif 'Deployment' in selected:
        var_research_scale.set(deployment)
    elif 'Patrols' in selected:
        var_research_scale.set(patrols)
    elif 'Dogs' in selected:
        var_research_scale.set(dogs)
    elif 'Prison Labour' in selected:
        var_research_scale.set(prison_labour)
    elif 'Education' in selected:
        var_research_scale.set(education)
    elif 'Land Expansion' in selected:
        var_research_scale.set(land_expansion)
    elif 'Contraband' in selected:
        var_research_scale.set(contraband)
    elif 'Policy' in selected:
        var_research_scale.set(policy)
    elif 'Armoury' in selected:
        var_research_scale.set(armoury)
    elif 'BodyArmour' in selected:
        var_research_scale.set(body_armour)
    elif 'Tazers' in selected and 'For Everyone' not in selected:
        var_research_scale.set(tazers)
    elif 'Tazers For Everyone' in selected:
        var_research_scale.set(tazers_for_everyone)
    elif 'Bank Loans' in selected:
        var_research_scale.set(bank_loans)
    elif 'Lower Taxes1' in selected:
        var_research_scale.set(lower_taxes_1)
    elif 'Lower Taxes2' in selected:
        var_research_scale.set(lower_taxes_2)
    elif 'Extra Grant' in selected:
        var_research_scale.set(extra_grant)
    elif 'Advanced Management' in selected:
        var_research_scale.set(advanced_management)
    elif 'Deathrow' in selected:
        var_research_scale.set(death_row)
    elif 'Permanent Punishment' in selected:
        var_research_scale.set(permanent_punishment)
    elif 'Remove Min Cell Size' in selected:
        var_research_scale.set(remove_min_cell_size)
    elif 'Reduce Execution Liability' in selected:
        var_research_scale.set(reduce_execution_liability)
    elif 'Legal Prep' in selected:
        var_research_scale.set(legal_prep)
    elif 'Legal Defense' in selected:
        var_research_scale.set(legal_defense)


#############
# Main Code #
#############
root = Tk()
root.title("Prison Architect -- sirNoolas -- Save editor")

mainframe = ttk.Notebook(root)

# adding Frames as pages for the ttk.Notebook
# first page: for explanation about program
doc_page = ttk.Frame(mainframe, padding="3 12")
ttk.Label(doc_page, text='This program can be used to edit prison architect save files.'
                         '\nWhen you edit a value (except when you type it), it is '
                         '\nautomatically saved to the save-folder which you chose when '
                         '\nstarting this program (when in doubt: press save anyway)\n'
                         '\nThis program was written by: sirNoolas'
                         '\nThe program was inspired by a similar program by fragmer, '
                         '\nwhich was originally written in C#. It can be found here: '
                         '\nhttp://forums.introversion.co.uk/viewtopic.php?f=42&t=50603&'
                         '\nsid=51d9d4228a7b0fae9b1f391c23dd054f\n'
                         '\nPlease always choose a new file as save-location; '
                         '\nbecause this program is not 100% save, and might corrupt your '
                         '\nsave-file.\n'
                         '\nPress the button to select files to read from and write to.'
                         '\nIn the dialog that opens first select the PA .prison save file'
                         '\n you want to edit, then select a file to save your changes to.').grid(column=1, row=1,
                                                                                                  columnspan=2,
                                                                                                  sticky=(W, N, E))

select_files_button = Button(doc_page, text='Select Files', command=select_files)
select_files_button.grid(column=2, row=2, sticky=(W, E, S))
mainframe.add(doc_page, text='About')

# second page, which would get widgets gridded into it
general_page = ttk.Frame(mainframe, padding="3 12")

#####################################################
# these are the checkboxes with the prison settings #
#####################################################
prison_settings_box = ttk.LabelFrame(general_page, text='Prison Settings')

# misconduct
var_misconduct = IntVar()
ttk.Checkbutton(prison_settings_box, text='Misconduct', variable=var_misconduct, command=gen_set).grid(
        column=1, row=1, sticky=(W, E))

# gangs
var_gangs = IntVar()
ttk.Checkbutton(prison_settings_box, text='Gangs', variable=var_gangs, command=gen_set).grid(
        column=1, row=2, sticky=(W, E))

# decay
var_decay = IntVar()
ttk.Checkbutton(prison_settings_box, text='Decay', variable=var_decay, command=gen_set).grid(
        column=1, row=3, sticky=(W, E))

# visibility
var_visibility = IntVar()
ttk.Checkbutton(prison_settings_box, text='Visibility', variable=var_visibility, command=gen_set).grid(
        column=1, row=4, sticky=(W, E))

# failure conditions
var_failure_conditions = IntVar()
ttk.Checkbutton(prison_settings_box, text='Failure Conditions', variable=var_failure_conditions,
                command=gen_set).grid(column=1, row=5, sticky=(W, E))

# events
var_events = IntVar()
ttk.Checkbutton(prison_settings_box, text='Events', variable=var_events, command=gen_set).grid(
        column=1, row=7, sticky=(W, E))

prison_settings_box.grid(column=1, row=1, sticky=W)

######################################################
# these are the checkboxes with the finance settings #
######################################################
finance_box = ttk.LabelFrame(general_page, text='Finance')

# Unlimited Funds
var_unlimited_funds = IntVar()
ttk.Checkbutton(finance_box, text='Unlimited funds', variable=var_unlimited_funds, command=gen_set).grid(
        column=1, row=1, columnspan=2, sticky=(W, E))

# Balance
var_balance = StringVar()
ttk.Label(finance_box, text='Balance ($)').grid(column=1, row=2, sticky=W)
balance_entry = Entry(finance_box, textvariable=var_balance)
balance_entry.grid(column=2, row=2, sticky=E)

# Bank Loan
var_bank_loan = StringVar()
ttk.Label(finance_box, text='Bank Loan ($)').grid(column=1, row=3, sticky=W)
Entry(finance_box, textvariable=var_bank_loan).grid(column=2, row=3, sticky=E)

# Credit Rating
var_credit_rating = StringVar()
ttk.Label(finance_box, text='Credit Rating').grid(column=1, row=4, sticky=W)
Entry(finance_box, textvariable=var_credit_rating).grid(column=2, row=4, sticky=E)

# Ownership
var_ownership = StringVar()
ttk.Label(finance_box, text='Ownership (%)').grid(column=1, row=5, sticky=W)
Spinbox(finance_box, from_=50, to=100.0, textvariable=var_ownership).grid(column=2, row=5, sticky=E)

finance_box.grid(column=2, row=1, sticky=E)

################
# Research Box #
################
research_box = ttk.LabelFrame(general_page, text='research')

combo_var = StringVar()
combo_var.set('Select...')
research_selector = ttk.Combobox(research_box, textvariable=combo_var, state='readonly')
research_selector.configure(values=('Maintainance', 'Security', 'Legal', 'Mental Health', 'Finance', 'Cctv',
                                    'Remote Access', 'Health', 'Cleaning', 'Grounds Keeping', 'Clone', 'Deployment',
                                    'Patrols', 'Dogs', 'Prison Labour', 'Education', 'Land Expansion', 'Contraband',
                                    'Policy', 'Armoury', 'Body Armour', 'Tazers', 'Tazers For Everyone', 'Bank Loans',
                                    'Lower Taxes 1', 'Tower Taxes 2', 'Extra Grant', 'Advanced Management', 'Death Row',
                                    'Permanent Punishment', 'Remove Min Cell Size', 'Reduce Execution Liability',
                                    'Legal Prep', 'Legal Defense'))
research_selector.grid(column=1, row=1, sticky=(W, E))
research_selector.bind('<<ComboboxSelected>>', combo_update)

var_research_scale = DoubleVar()
ttk.Label(research_box, text='%', textvariable=var_research_scale, width=4, state='readonly').grid(column=2, row=1, sticky=N)
research_scale = ttk.Scale(research_box, orient=HORIZONTAL, length=200, from_=0.0, to=100.0, variable=var_research_scale
                           , command=res_set)
research_scale.grid(column=3, row=1, sticky=E)

research_box.grid(column=1, row=2, columnspan=2, sticky=(W, E))

###############
# Save Button #
###############
var_save_result = StringVar()
save_result = ttk.Label(general_page, textvariable=var_save_result)
save_result.grid(column=1, row=3, columnspan=2, sticky=W)
Button(general_page, text='Save', command=validate_and_save).grid(column=2, row=3, sticky=E)

# END of finance

mainframe.pack(expand=1, fill="both")

###############
# final setup #
###############
#  init global variables for later use by several functions
save_file_path = None
maintainance = security = legal = mental_health = finance = cctv = remote_access = health = cleaning = \
    grounds_keeping = clone = deployment = patrols = dogs = prison_labour = education = land_expansion = contraband = \
    policy = armoury = body_armour = tazers = tazers_for_everyone = bank_loans = lower_taxes_1 = lower_taxes_2 = \
    extra_grant = advanced_management = death_row = permanent_punishment = remove_min_cell_size = \
    reduce_execution_liability = legal_prep = legal_defense = 0


root.mainloop()  # starts the gui loop
