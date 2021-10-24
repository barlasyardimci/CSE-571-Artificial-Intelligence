###################################################
##             ASU CSE 571 ONLINE                ##
##        Unit 3 Reasoning under Uncertainty     ##
##             Project Submission File           ##
##                 burglary.py                   ##
###################################################

###################################################
##                !!!IMPORTANT!!!                ##
##        This file will be auto-graded          ##
##    Do NOT change this file other than at the  ##
##       Designated places with your code        ##
##                                               ##
##  READ the instructions provided in the code   ##
###################################################

# Starting with defining the network structure
from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

def buildBN():

    #!!!!!!!!!!!!!!!  VERY IMPORTANT  !!!!!!!!!!!!!!!
    # MAKE SURE to use the terms "MaryCalls", "JohnCalls", "Alarm",
    # "Burglary" and "Earthquake" as the states/nodes of the Network.
    # And also use "burglary_model" as the name of your Bayesian model.
    ########-----YOUR CODE STARTS HERE-----########
    burglary_model = BayesianModel([('Burglary','Alarm'),
                                    ('Earthquake','Alarm'),
                                    ('Alarm','JohnCalls'),
                                    ('Alarm','MaryCalls')])

    cpd_burglary = TabularCPD(variable='Burglary', variable_card=2,
                            values = [[0.999],[0.001]])

    cpd_earthquake = TabularCPD(variable='Earthquake', variable_card=2,
                            values = [[0.998],[0.002]])

    cpd_alarm = TabularCPD(variable='Alarm', variable_card=2,
                            values = [[0.999, 0.71, 0.06, 0.05],
                                      [0.001, 0.29, 0.94, 0.95]],
                            evidence = ['Burglary', 'Earthquake'],
                            evidence_card=[2,2])
    
    cpd_johncalls = TabularCPD(variable='JohnCalls', variable_card=2,
                            values = [[0.95, 0.1],
                                      [0.05,0.9]],
                            evidence = ['Alarm'],
                            evidence_card=[2])

    cpd_marycalls = TabularCPD(variable='MaryCalls', variable_card=2,
                            values = [[0.99,0.3],
                                      [0.01, 0.7]],
                            evidence = ['Alarm'],
                            evidence_card=[2])
    
    
    burglary_model.add_cpds(cpd_burglary, cpd_earthquake, cpd_alarm, cpd_johncalls, cpd_marycalls)
    ########-----YOUR CODE ENDS HERE-----########
    
    # Doing exact inference using Variable Elimination
    burglary_infer = VariableElimination(burglary_model)

    ########-----YOUR MAY TEST YOUR CODE BELOW -----########
    ########-----ADDITIONAL CODE STARTS HERE-----########
    #print(burglary_model.check_model())
    #print(burglary_model.edges())
    #print(burglary_model.nodes())
    #print(burglary_model.get_cpds())
    #print(burglary_infer.query(variables=['JohnCalls'], evidence={'Earthquake': 0},joint=False)['JohnCalls'])
    #print(burglary_infer.query(variables=['MaryCalls'], evidence={'Burglary':1,'Earthquake': 0},joint=False)['MaryCalls'])
    #print(burglary_infer.query(variables=['MaryCalls'], evidence={'Burglary':1,'Earthquake': 1},joint=False)['MaryCalls'])
    #print(burglary_infer.query(variables=['MaryCalls'], evidence={'JohnCalls': 1},joint=False)['MaryCalls'])
    #print(burglary_infer.query(variables=['MaryCalls'], evidence={'JohnCalls': 1,'Burglary':0,'Earthquake': 0},joint=False)['MaryCalls'])
    ########-----YOUR CODE ENDS HERE-----########
    
    return burglary_infer
