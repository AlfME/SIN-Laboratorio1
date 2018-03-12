import pyhop
import math


#############################MODEL#####################################
hospitals = { "Antiguo Hospital":				{"x": 39.4694707,	"y": -0.3838572},
	"Hospital Quironsalud Valencia" :			{"x" : 39.4689241,	"y" : -0.3978476},
	"Ivo" :							{"x" : 39.4706468,	"y":-0.3988776},
	"Consorci Hospital General Universitari de Valencia": 	{"x": 39.4706468,	"y" : -0.3988776},
	 "Hospital Vithas Nisa Virgen del Consuelo" :		{"x": 39.4683278,	"y": -0.3934703},
	 "Hospital Casa de Salud" :				{"x":39.4693879,	"y":-0.3780208}
	 }

ambulances = {"A1": {"x":hospitals["Antiguo Hospital"]["x"],			"y":hospitals["Antiguo Hospital"]["y"],			"g": 20,	"has_victim":False,	"t": 0},
	      "A2": {"x":hospitals["Hospital Quironsalud Valencia"]["x"],	"y":hospitals["Hospital Quironsalud Valencia"]["y"],	"g": 5,		"has_victim":False,	"t": 0},
	      "A3": {"x": 39.4706400,						"y": -0.3780208,					"g": 5,		"has_victim":False,	"t": 0}
	}

victims = {"V1" :	{"x":39.4815278,	"y":-0.3466096, "g": 10,	"treated":False},
	"V2" :		{"x":39.4706462,	"y":-0.3762518, "g": 30,	"treated":False},
	"V3" :		{"x":39.4691474,	"y":-0.3262902, "g": 25,	"treated":False}	
	}



#########################AUXILIARES###########################
def distance(lhs, rhs):
	diff_x = lhs["x"] - rhs["x"];
	diff_y = lhs["y"] - rhs["y"];
	return math.sqrt(diff_x*diff_x + diff_y*diff_y);

def choose_victim(state):
	#tmp_list = list(p for p in state.victims.items() if p[1]["treated"] == False);
	#return max(tmp_list, key=lamfbda x: x[1]["g"]);
	most_g = 100000000;
	for p in state.victims.items():
		if(p[1]["treated"] == False):
			if(p[1]["g"] < most_g):
				current_victim = p;
				most_g = current_victim[1]["g"];
	return current_victim;

def choose_ambulance(state, current_victim):
	#return min(a for a in state.ambulances.items() if p[1]["has_victim"] == False and p[1]["g"] >= current_victim["g"], key=lambda x: x[1]["g"]);
	min_amb  = 10000000;
	current_amb = 0;

	for a in state.ambulances.items():
		if(a[1]["has_victim"] == False and current_victim[1]["g"] >=  a[1]["g"]):
			distamb = distance(a[1], current_victim[1]);
			if(distamb < min_amb):
				current_amb = a;
				min_amb = distamb;
	return current_amb;

def choose_hospital(state, v):
	max_distance = 10000000000;
	for h in state.hospitals.items():
		test_distance = distance(v[1], h[1]);
		if(test_distance < max_distance):
			max_distance = test_distance;
			current_hospital = h;
	return current_hospital

#########################METHODS#############################
def save_the_victims(state, goal):
	if (state.num_victims <= 0):
		return [('call_success', state, goal)];
	else:
		return [('save_victim', state, goal), ('save_the_victims', state, goal)];



#########################OPERATORS##########################
def save_victim(state, goal):
	if(state.num_victims <= 0):
		return False;
	else:
		current_victim = choose_victim(state);
		current_ambulance = choose_ambulance(state, current_victim);
		current_hospital = choose_hospital(state, current_victim);
		return [('move_ambulance', current_ambulance, current_victim[1]["x"], current_victim[1]["y"]), ('enter_ambulance', current_ambulance, current_victim), ('move_ambulance', current_ambulance, current_hospital[1]["x"], current_hospital[1]["y"]), ('exit_ambulance', current_ambulance, current_victim)];

def move_ambulance(state, a, x, y):
	tuple = {"x":x, "y":y};
	a[1]["t"] += distance(a[1], tuple);
	a[1]["x"] = x;
	a[1]["y"] = y;
	return state;

def enter_ambulance(state, a, v):
	a[1]["has_victim"] = True;
	return state;

def exit_ambulance(state, a, v):
	v[1]["treated"] = True;
	a[1]["has_victim"] = False;
	state.num_victims -= 1;
	return state;

def call_success(state, goal):
	for a in state.ambulances.items():
		print(a[0], ": ", a[1]["t"]);
	print("Success!!");

	if(state.num_victims <= 0):
		return [];
	else:
		return False;



#############################PYHOP############################
state1			= pyhop.State("state1");

state1.hospitals	= hospitals;
state1.ambulances	= ambulances;
state1.victims		= victims;
state1.num_victims	= len(victims);

goal1			= pyhop.Goal("goal1");
goal1.num_victims	= 0;

pyhop.declare_operators(move_ambulance, enter_ambulance, exit_ambulance);
pyhop.declare_methods('save_the_victims', save_victim, call_success);

pyhop.pyhop(state1,[('save_the_victims', goal1)], verbose=1);
