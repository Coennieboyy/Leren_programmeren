from help import *

RECEIPT_TEXT = '***** SPEELHAL ENTREE VOOR {personen:2} PERSONEN *****'
RESTART_TEXT = '\nBestelprocedure gestopt door invoerfout!\nHerstart de bestelprocedure!'
MAX_TICKETS = 30
MAX_VR_VIP_SEAT_TIME = 45
VR_VIP_SEAT_PRICE_PERIOD = 5
TICKET_PRICE = 7.50
VR_VIP_SEAT_PERIOD_PRICE = 0.37
COLA_PRICE = 2.10
POPCORN_PRICE = 2.89
VAT_CODE_H = 'H'
VAT_CODE_L = 'L'

print("SPEELHAL-ENTREE-KASSA")
answer = input_yes_no("Wilt u bestellen?(J/N)\n") 
if answer in NO_OPTIONS: 
  exit('Nu geen interesse? Tot ziens!')
else:
  print('Ik ga u nu vragen wat en hoeveel u wilt...')

nr_tickets = input_int("Hoeveel personen?\n")

answer = input_yes_no("Ook VR-VIP seats?(J/N)\n")
vr_vip_ordered = answer in YES_OPTIONS

if vr_vip_ordered:
  nr_vr_vip_seats = input_int("hoeveel VR-VIP seats?\n")
  vr_vip_seat_time = input_int("hoeveel minuten in de VR-VIP-seats?\n")
else:
  nr_vr_vip_seats = 0
  vr_vip_seat_time = 0

nr_cola = input_int("Hoeveel cola?\n")
nr_popcorn = input_int("Hoeveel popcorn?\n")

answer = input_yes_no("Wilt u een factuur met BTW specificatie?(J/N)\n")
vat_invoice = answer in YES_OPTIONS
if vat_invoice:
   company_name = input('Op welke bedrijfsnaam komt de factuur?\n').strip()
   if len(company_name) == 0:
     company_name = '........... (zelf invullen)'

total_tickets = round(nr_tickets * TICKET_PRICE,2)
vr_vip_seat_price = vr_vip_seat_time / VR_VIP_SEAT_PRICE_PERIOD * VR_VIP_SEAT_PERIOD_PRICE
total_vr_vip_seats = round(nr_vr_vip_seats * vr_vip_seat_price, 2)
total_cola = round(nr_cola * COLA_PRICE, 2)
total_popcorn = round(nr_popcorn * POPCORN_PRICE, 2)
total_all = total_tickets + total_vr_vip_seats + total_cola + total_popcorn

if vat_invoice:
  total_H = total_tickets + total_vr_vip_seats
  total_L = total_cola + total_popcorn
  total_vat_H = get_vat_from_amount_incl(total_H, VAT_CODE_H)
  total_vat_L = get_vat_from_amount_incl(total_L, VAT_CODE_L)
  total_vat = total_vat_H + total_vat_L

# ***************** OUTPUT *****************
receipt_text = RECEIPT_TEXT.format(personen = nr_tickets)
print(receipt_text+'\n')
if vat_invoice:
  print(f'Factuur voor: {company_name}')
else:
  print(f'Kassabon')\
  
print('-'*len(receipt_text))
print(f'Tickets                   {nr_tickets:2} x {TICKET_PRICE:2.2f} = {total_tickets:6.2f}')
print(f'VR-vip-seats  {vr_vip_seat_time:3} minuten {nr_vr_vip_seats:2} x {vr_vip_seat_price:2.2f} = {total_vr_vip_seats:6.2f}')
print(f'Cola                      {nr_cola:2} x {COLA_PRICE:2.2f} = {total_cola:6.2f}')
print(f'Popcorn                   {nr_popcorn:2} x {POPCORN_PRICE:2.2f} = {total_popcorn:6.2f}')
print('.'*len(receipt_text))
print(f'Totaal:                               {total_all:6.2f}')
print()
if vat_invoice:
  print(f'BTW Hoog                          {get_vat_perc("H")}% {total_vat_H:6.2f}')
  print(f'BTW Laag                          {get_vat_perc("L")}% {total_vat_L:6.2f}')
print('='*len(receipt_text))
print('Bedankt voor de bestelling, veel plezier!')