Distance=int(input('Enter_distance_in_km : '))
Time=int(input('Enter_travel_hrs: '))
Oil=int(input('Enter_oil_in_liters: '))
Distance_travel_per_hr=Distance/Time
print(Distance_travel_per_hr)
Oil_per_hour=Oil/Time
print(Oil_per_hour)
Oil_per_hour=Oil/Time
Oil_consumed_per_km_hour=Distance_travel_per_hr/Oil_per_hour
print(Oil_consumed_per_km_hour)