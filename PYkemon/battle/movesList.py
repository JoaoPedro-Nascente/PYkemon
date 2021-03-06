from battle.Moves import moves
from battle.pokeTypeList import *
#all moves in one place
#moves(name, power, type, accuracy, pp, class)

bite = moves('bite', 60, dark, 100, 25, 'physical')
surf = moves('surf', 90, water, 100, 15, 'special')
outrage = moves('outrage', 120, dragon, 100, 10, 'physical')
hyperbeam = moves('hyper beam', 150, normal, 90, 5, 'special')
dragonclaw = moves('dragon claw', 80, dragon, 100, 15, 'physical')
flamethrower = moves('flamethrower', 90, fire, 100, 15, 'special')
megapunch = moves('mega punch', 80, normal, 85, 20, 'physical')
aerialace = moves('aerial ace', 60, flying, 100, 20, 'physical')
ember = moves('ember', 40, fire, 100, 25, 'special')
rockslide = moves('rock slide', 75, rock, 90, 10, 'physical')
megakick = moves('mega kick', 120, normal, 75, 5, 'physical')
inferno = moves('inferno', 100, fire, 50, 5, 'special')
thundershock = moves('thunder shock', 40, electric, 100, 30, 'special')
brickbreak = moves('brick break', 75, fighting, 100, 15, 'physical')
thief = moves('thief', 60, dark, 100, 25, 'physical')
thunderbolt = moves('thunderbolt', 90, electric, 100, 15, 'special')
#bulbasaur
tackle = moves('tackle', 40, normal, 100, 35, 'physical')
solarbeam = moves('solar beam', 120, grass, 100, 10, 'special')
vinewhip = moves('vine whip', 45, grass, 100, 25, 'physical')
bodyslam = moves('body slam', 85, normal, 100, 15, 'physical')
#squirtle
hydropump = moves('hydro pump', 110, water, 80, 5, 'physical')
watergun = moves('water gun', 40, water, 100, 20, 'physical')
skullbash = moves('skull bash', 130, normal, 100, 10, 'physical')

#introbot
armario = moves('armário', 90, introcomp, 100, 5, 'physical')
aula04 = moves('aula 04', 130, introcomp, 100, 5, 'special')
feedback = moves('feedback', 150, introcomp, 100, 5, 'special')
beberagua = moves('beber água', 0, introcomp, 100, 5, 'special')