
# Check if airbags were deployed, then car was made after 1970
count_airbag = 0
list_airbag = []
for i in range(len(AIRBAG_DEPLOYED)):
  if AIRBAG_DEPLOYED[i] != 'None' and AIRBAG_DEPLOYED[i] != 'Unknown': # check if value is not None or Unknown
      if CLMT_VEH_YR[i] < 1970:
        count_airbag += 1 # add count
        list_airbag.append(i) # append index to list
print(count_airbag) 
print(list_airbag) 