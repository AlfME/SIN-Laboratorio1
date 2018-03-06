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

ambulances = {"A1": {"x":hospitals["Antiguo Hospital"]["x"],		"y":hospitals["Antiguo Hospital"]["y"],		"g": 20,	"has_victim":False},
	      "A2": {"x":hospitals["Hospital Quironsalud Valencia"],	"y":hospitals["Hospital Quironsalud Valencia"], "g": 5,		"has_victim":False},
	      "A3": {"x": 39.4706400,					"y": -0.3780208,				"g": 5,		"has_victim":False}
	}

victims = {"V1" :	{"x":39.4815278,	"y":-0.3466096, "g": 10,	"treated":False},
	"V2" :		{"x":39.4706462,	"y":-0.3762518, "g": 30,	"treated":False},
	"V3" :		{"x":39.4691474,	"y":-0.3262902, "g": 25,	"treated":False}	
	}



#########################AUXILIARES###########################
def distance(lhs, rhs):
	diff_x = lhs["x"] - rhs["x"];
	diff_y = lhs["y"] - rhs["y"];
	return Math.sqrt(diff_x*diff_x + diff_y*diff_y);



#########################METHODS#############################
def save_the_victims(state, goal):
	#...



#########################OPERATORS##########################
def save_victim(state, goal):
	#...

def move_ambulance(state, goal):
	#...

def enter_ambulance(state, goal):
	#...

def exit_ambulance(state, goal):
	#...
	state.num_victims--;

def call_success(state, goal):
	#...
	print("Success!!");




#############################PYHOP############################
state1			= pyhop.State("state1");

state1.hospitals	= hospitals;
state1.ambulances	= ambulances;
state1.victims		= victims;
state1.num_victims	= len(victims);

goal1			= pyhop.Goal("goal1");
goal1.num_victims	= 0;

pyhop.declare_operators(choose_victim, move_ambulance, enter_ambulance, exit_ambulance);
pyhop.declare_method('save_the_victims', save_victim, call_success);
