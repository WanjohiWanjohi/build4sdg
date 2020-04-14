# class Impact():

# 	def __init__(self, data):
# 		super(Impact, self).__init__()
# 		self.data = data
severe_impact = {}
o_impact = {}
data = {}

def  getdata(data = data):
	finaldata = {}
	
	if data():
		for key , value in  data.items():
			if isinstance(value , collections.Mapping):
				for seckeys , secvalues in value.items():
					finaldata[seckeys] = (secvalues)
			else:
				finaldata[key] = value
	else:
		pass

	return finaldata

def impact(getdata):
	if getdata():
		cases_reported = int(finaldata["reportedCases"])
		currentlyInfected = int(casesreported *10)
		o_impact[impact.__name__] = currentlyInfected
	else:
   		pass
	return currentlyInfected
def severeImpact(getdata):
	if getdata():
		int(finaldata["reportedCases"])
		currentlyInfected = casesreported * 50 
		severe_impact[severeImpact.__name__] = currentlyInfected
	return int(currentlyInfected)

##check the type of period and convert it
def convert_to_days(getdata):
	if getdata():

		period=data["periodType"], time=finaldata["timeToElapse"]
	
		if period == "days":
			timeToElapse = data["timetoElapse"]

		elif period =="weeks":
			time *= 7 

		elif period == "months":
			timeToElapse *= 30 
	else:
		pass

	return timeToElapse

def infectionsByRequestedTime(
	convert_to_days, impact ,severeImpact
	):
	if convert_to_days():
		time = int(timetoElapse)

		infection_gaps  = int(time / 3)

		totalrequested = int(severeImpact()* 2 ** infection_gaps)
		severe_impact[infectionsByRequestedTime.__name__] = totalrequested
		low_totalrequested = impact() * 2 ** infection_gaps
		o_impact[infectionsByRequestedTime.__name__] = low_totalrequested
	else: 
		pass

	return totalrequested , low_totalrequested

##assignment 2

def severeCasesByRequestedTime(infectionsByRequestedTime):
	if infectionsByRequestedTime():
		severeCases = int(0.15 * totalrequested)
		lowimpact = int(0.15* low_totalrequested)
		severe_impact[severeCasesByRequestedTime.__name__] = severeCases 
		o_impact[severeCasesByRequestedTime.__name__] = lowimpact
	else:
		pass
	return lowimpact , severeCases

def hospitalBedsByRequestedTime(severeCasesByRequestedTime , getdata ):
	if severeCasesByRequestedTime() and getdata():
		beds_available = int(data["totalHospitalBeds"]) 
		low_hospt_req = int((beds_available * 0.35) - lowimpact)
		severe_hospt_req = int((beds_available * 0.35) - severeCases)
		o_impact[hospitalBedsByRequestedTime.__name__] = low_hospt_req
		severe_impact[hospitalBedsByRequestedTime.__name__] = severe_hospt_req
	else:
		pass
		
	return low_hospt_req , severe_hospt_req

##challenge 3 
def casesForICUByRequestedTime (infectionsByRequestedTime):
	if infectionsByRequestedTime():
		low_ICU =  0.05 * low_totalrequested
		high_ICU = 0.05 * totalrequested
		o_impact[casesForICUByRequestedTime.__name__] = low_ICU
		severe_impact[casesForICUByRequestedTime.__name__] = high_ICU
	else:
		pass
	return high_ICU , low_ICU

def casesForVentilatorsByRequestedTime(infectionsByRequestedTime):
	#estimated number of severe positive cases that will require ventilators
	if infectionsByRequestedTime():
		high_ventilator =  int(0.02 * totalrequested)
		low_ventilator = int(0.02 * low_totalrequested)
		o_impact[casesForVentilatorsByRequestedTime.__name__] = low_ventilator
		severe_impact[casesForVentilatorsByRequestedTime.__name__] = high_ventilator

	else:
		pass

	return high_ventilator , low_ventilator


def dollarsInFlight(infectionsByRequestedTime , avgDailyIncomeinUSD , avgDailyIncomePopulation,getdata):
	if getdata():
		time = data["timeToElapse"]
		totalcases = impact(cases)
		totaldollars_high = [] 
		totaldollars_low = []
		for day in range(0 , time+1):

			if infectionsByRequestedTime():
				low_dollarsinfected = int( low_totalrequested* 0.65 * 1.5) / time
				high_dollarsinfected = int(totalrequested * 0.65 * 1.5) / time
				totaldollars_high.append(high_dollarsinfected)
				totaldollars_low.append(low_dollarsinfected)
				o_impact[dollarsInFlight.__name__] = low_dollarsinfected
				severe_impact[dollarsInFlight.__name__] = high_dollarsinfected

			else:
				pass

		total_severe = sum(totaldollars_low)
		total_impact = sum(totaldollars_high)
		avg_total_severe = total_severe / len(totaldollars_high)
		avg_total_impact = total_impact / len(totaldollars_low)

	return low_dollarsinfected, high_dollarsinfected , total_severe , total_impact , avg_total_severe , avg_total_impact
