# SCRIPT CHE CALCOLA E SCRIVE IN UN FILE I GIORNI DI FERIE E PERMESSI MATURATI
def days_accrued(p_hours):
    l_hours_day = 8
    # CALCOLO DEI GIORNI INTERI
    l_full_days = int(p_hours // l_hours_day)
    # CALCOLO LE ORE RIMANENTI
    l_remaining_hours = p_hours % l_hours_day
    # CALCOLO I MINUTI RIMANENTI
    l_remaining_minutes = round((l_remaining_hours % 1) * 60, 0)
    l_remaining_hours = int(l_remaining_hours)
    return l_full_days, l_remaining_hours, l_remaining_minutes

# INPUT DELLE ORE DI FERIE E PERMESSI MATURATI
g_accrued_holidays = float(input('ENTER HOURS FOR HOLIDAYS (ES: 66.77): '))
g_accrued_permits = float(input('ENTER HOURS FOR PERMITS (ES: 66.77): '))

# CALCOLO DEI GIORNI DI FERIE E PERMESSI MATURATI
g_accrued_holidays_days, g_accrued_holidays_hours, g_accrued_holidays_minutes = days_accrued(g_accrued_holidays)
g_accrued_permits_days, g_accrued_permits_hours, g_accrued_permits_minutes = days_accrued(g_accrued_permits)

# STAMPA DEI RISULTATI SUL TERMINALE
print(f'\nHOLIDAYS: {g_accrued_holidays_days} DAYS, {g_accrued_holidays_hours} HOURS, {g_accrued_holidays_minutes} MINUTES')
print(f'PERMITS: {g_accrued_permits_days} DAYS, {g_accrued_permits_hours} HOURS, {g_accrued_permits_minutes} MINUTES\n')

# SCRITTURA DEI RISULTATI IN UN FILE DI TESTO
with open('accrued_days.txt','w') as file:
    file.write(f'\nHOLIDAYS: {g_accrued_holidays_days} DAYS, {g_accrued_holidays_hours} HOURS, {g_accrued_holidays_minutes} MINUTES\n')
    file.write(f'PERMITS: {g_accrued_permits_days} DAYS, {g_accrued_permits_hours} HOURS, {g_accrued_permits_minutes} MINUTES\n')