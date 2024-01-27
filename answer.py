class answer:

  # get one argument, which is the result of pysolr.search
  def __init__(self, result):
    self.result = result

  def answer(self):
    
    documents = self.result.docs

    for document in documents:
        
        # make answer for EV cars
        if document['Name'][0] in ['EQA', 'EQB', 'EQE', 'EQE SUV']:
          print('For {o}\n Battery Capacity is {bc}kWh\n Max Torque is {tq}\n Drive Range is {dr}km\n Price is {p}euro'
                .format(o = document['Option'], bc = document['Battery_Capacity_kWh_'], tq = document['Torque_Nm_'],
                      dr = document['Drive_Range_Min_-_Max_km__'], p = document['Price_euro_']))
                

        # make answer for non-EV cars
        else:
          print('For {o}\n Max Torque is {tq}Nm\n Engine/Zylinder is {ez}\n Displacement is {dp}cm3\n Fuel Consumption is {fc}l/100km\n Co2 Emission is {co2}g/km\n Price is {p}euro'
                .format(o = document['Option'], tq = document['Torque_Nm_'], ez = document['Engine_Zylinder'],
                      dp = document['Displacement_cm3_'], fc = document['Fuel_Consumption_l_100_km_'], co2 = document['CO2_Emissions_g_km_'], p = document['Price_euro_']))