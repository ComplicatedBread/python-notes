#Environmental descriptions in order

GREEN =  '\033[32m' #32m changes to green
RED = '\033[31m'    #31m red
BLUE = '\033[34m'   #34m blue
PURPLE = '\033[35m' #35m purple
WHITE = '\033[37m'  #37m white

from time import sleep
print(WHITE + "The glaring sun hits your eyes as you begin to stir awake. Looking around, you see a barren sandy landscape encompassing your vision") ; sleep(2.5)
print("In front of you stands several decrepit factories. Their chimneys looming like crooked spires over head") ; sleep(2.5)
print("Several questions are brought to your mind, 'who am I, why am I here and what is this place?'") ; sleep(2.5)
print("There appears to be nothing around for miles, which enticed one option. Enter the factory.") ; sleep(2.5)
print("You stand and walk to the nearest entrance of one building, it is silent besides the creaking of metal structures.") ; sleep(2.5)
print("You enter and are met with a corridor with 3 rooms leading off it.") ; sleep(2.5)
print(RED + "Which room do you enter?")

#CHOICE OPTIONS HERE

#1

from time import sleep
print(WHITE + "You decide to enter the first room, inside appeared to be an office.") ; sleep(2.5)
print("Lockers lined one wall, desks with strewn paper were scattered throughout the room, there also appeared to be old fashioned PC's") ; sleep(2.5)
print("On one table you spot a lanyard with a picture and name of an employee the face and name are scratched out with black marker") ; sleep(2.5)
print("Something about it was familiar you seem to vaguely remember interacting with someone once") ; sleep(2.5)
print("You leave the room and enter a large room which seemed to be the main area of the factory") ; sleep(2.5)

#2

from time import sleep
print(WHITE + "You enter the second room only to find it was a closet with cleaning supplies, nothing much here") ; sleep(2.5)
print("You decide to pick another room") ; sleep(2.5)

#3

from time import sleep
print(WHITE + "You enter the third room, the room was cast with shadows from the setting sun, from the ceiling hung hundreds of dead small animals by their necks swaying slightly in the breeze from the shattered windows") ; sleep(2.5)
print("On the walls were images of peoples faces painted distorted in a red substance along with tally marks") ; sleep(2.5)
print("You step backwards in horror the smell of decay was overwhelming, you quickly go through a door to the right") ; sleep(2.5)
print("You enter a large room that seemed to be the main area of the factory") ; sleep(2.5)

from time import sleep
print(WHITE + "The room contained alot of machinery 'the place appears to be a logging factory' you think judging the rusting saws and chopped tree trunks.") ; sleep(2.5)
print("Broken glass and rubbish littered the floor, you try to see a path past the machines but it was like a maze. The only way forward it seemed was to pass through them") ; sleep(2.5)
print("You start to climb over conveyor belts and metal pipes, there was the tinkling of glass being shifted suddenly to your right and a scratching sound like a sharp object on metal") ; sleep(2.5)
print("You freeze looking for the source of the sound but it all was silent now, you start to move forward again") ; sleep(2.5)
print("Suddenly theres a blaring horn sound and steam rises from the metal around you, the conveyor belt you are on clanks into life and starts drifting you towards a rotating saw") ; sleep(2.5)
print("There was a second conveyor belt next you, metal chains also passed over your head attached to a moving track on the roof") ; sleep(2.5)

print(RED + "how will you escape?")

#Choices

#1

from time import sleep
print(WHITE + "You jump onto the conveyor belt next to you thats going in the opposite direction but your feet go sideways under you and you are swept into a shredding machine") ; sleep(2.5)
print(RED + "YOU DIED CONGRATS") ; sleep(2.5)

#2
from time import sleep
print(WHITE + "You jump up and grab the next chain that passes over you and it swings to the right avoiding the saw") ; sleep(2.5)
print("You pass over clunking machinery looking for a place to jump off and spy a flat platform coming up on your left") ; sleep(2.5)
print("You swing back and forth on the chain timing it to swing left as the platform came up and landed but stumbled on it") ; sleep(2.5)
print("There was a ladder up to a balcony which seemed to be a second floor which u take") ; sleep(2.5)
#3
from time import sleep
print(WHITE + "You try to go back but the conveyor belt speeds up and you end up running in place and then you stumble and get dragged into the saw blades") ; sleep(2.5)
print(RED + "YOU DIED CONGRATS") ; sleep(2.5)

from time import sleep
print(WHITE + "Along the balcony theres 3 doors again") ; sleep(2.5)
print(RED + "Which room do you go in?") ; sleep(2.5)

#choices

#1
from time import sleep
print(WHITE + "You enter the first room on the row, inside is another office like room but with no tables on the walls lines photos in frames of people") ; sleep(2.5)
print("Alot of the images are crossed out in red or ripped with what seemed to be claw marks but there was one that was circled but undamaged") ; sleep(2.5)
print("It made you extremely uneasy since the person seemed so familiar, you leave the room") ; sleep(2.5)
print(RED + "Which room do you go in?") ; sleep(2.5)

#1 if you entered this room second after the bathroom
from time import sleep
print(WHITE + "You enter the first room on the row, inside is another office like room but with no tables on the walls lines photos in frames of people") ; sleep(2.5)
print("Alot of the images are crossed out in red or ripped with what seemed to be claw marks but there was one that was circled but undamaged") ; sleep(2.5)
print("You realise, looking closer at the image that it looked the same as the reflection you saw in the mirror") ; sleep(2.5)
print("You quickly leave not wanting to stay there any longer") ; sleep(2.5)
#Cant go in the same room twice, say you have already explored this room

#2 option - if you entered the first room
from time import sleep
print(WHITE + "You enter the second room which you find to be a bathroom, one wall was lined with sinks and mirrors and the other with cubicles") ; sleep(2.5)
print("You go over to a sink and look into a mirror, you realise that the person in the circled photo looked the same as you") ; sleep(2.5)
print("In the background, you see one of the cubicle doors open slightly and something peers out and you whip around to see nothing") ; sleep(2.5)
print("You leave the room quickly") ; sleep(2.5)

#2 option- not entered first room

from time import sleep
print(WHITE + "You enter the second room which you find to be a bathroom, one wall was lined with sinks and mirrors and the other with cubicles") ; sleep(2.5)
print("You go over to a sink and look into a mirror, you now know what you look like") ; sleep(2.5)
print("You decide not to check the cubicles because they probably have awful hygeine and thats a key horror way to get killed") ; sleep(2.5)

#3 option

from time import sleep
print(WHITE + "You enter the third room inside appeared to be a dining area with tables chairs and a kitchen, most were in shambles") ; sleep(2.5)
print("You wander in seeing if theres anything of interest, the kitchen area was completely dark. You look at an empty coffee mug sat on one of the only standing tables") ; sleep(2.5)
print("You approach it, feeling something familiar about it, you remember something, sitting here at this table with someone else their face blurred out but they were laughing and talking to you") ; sleep(2.5)
print("The memory made you feel happy") ; sleep(2.5)
print("You look out the window over the roofs and question why its been sunset for so long") ; sleep(2.5)
print("A clang suddenly rang out from the kitchen as something metal was dropped onto the tiled floor") ; sleep(2.5)
print("You jump startled by the sudden sound and peer into the kitchen from where your stood") ; sleep(2.5)
print("It was pitch black but you see movement as something crept forward the red light from the window illuminating it slightly") ; sleep(2.5)
print("you see a long bird skull like face with teeth, clawed hands covered its eye sockets its skin seemed to be falling off of it and looked rotten") ; sleep(2.5)
print("Thats all you see as you start bolting for the door and run hearing the creature scramble over tables behind you") ; sleep(2.5)
print("You run to the end of the balcony finding a ladder and climb down it and run through a door into a corridor") ; sleep(2.5)
print("You don't pay attention to the rotting walls or floor as you run, suddenly the floor starts to give way taking you with it and you fall into the dark depths") ; sleep(2.5)

#place something to split it up

from time import sleep
print(WHITE + "Luckily you land without injury, as the dust clears you find that you have fallen down into another level of the factory, a gaping black corridor stretches infront of you") ; sleep(2.5)
print("You stand up and look up at the hole in the ceiling, there was no way back up") ; sleep(2.5)
print("You hear what seems to be claws clicking on tiles above so you waste no time sprinting down the corridor which seemed to stretch forever") ; sleep(2.5)
print("You reach an end to the corridor and it splits into two") ; sleep(2.5)
print(RED + "Do you go left or right?") ; sleep(2.5)

#option left if you went to the first memory

from time import sleep
print(WHITE + "You turn left, at the end there is one wooden door.") ; sleep(2.5)
print("You pull it open inside is nearly pitch black but you can make out the shape of a lever on the wall, you pull it and lights flicker on") ; sleep(2.5)
print("The room is now observable, it appeared to be a storage room with boxes stacked against a wall and broken machinery parts scattered the floor, a single table sat under the hanging light") ; sleep(2.5)
print("On the table lay a cardboard box its lid open inside was a bunch of photographs, some documents and a scarf, you look through the photos you recognise yourself along with the person from the cafe") ; sleep(2.5)
print("You and the person both looked happy stood among what seemed to be workers at the factory, you realise that you must of worked here along with the other person, you question why you diddnt remember this and what happened?") ; sleep(2.5)
print("The other photos also contained the person and you, you were in every single one. In each you were interacting and looked joyful, in some photos the other person was wearing a scarf") ; sleep(2.5)
print("You remember that you gave them the scarf, you were clearly close with them") ; sleep(2.5)
print("You look at the scarf in the box, it is the same as the one in the pictures. You put it on wanting to keep it with you") ; sleep(2.5)
print("You check the papers next they looked official, a name appears that you remember from before on a lanyard along with a picture. It is the same person you saw in your memories") ; sleep(2.5)
print("It had all their information on it but then continued into 'fatal accident occured 5th of april involving this person via falling onto conveyor belt in line of logging saw...'") ; sleep(2.5)
print("You stop reading not wanting to read anymore as a dark memory fills your mind") ; sleep(2.5)
print("You were back in the main room of the factory on the balcony but everything looked unabandoned, there was the person stood next to the short barrier looking down at a machine and talking") ; sleep(2.5)
print("You see a cranes metal line carrying some sliced logs slowly moving your direction, suddenly theres the sound of breaking metal and the crane itself tips from the logs weight") ; sleep(2.5)
print("Before you can shout a warning the logs swing right into the balcony breaking part of it taking the person with it, you rush forward hand stretched out calling their name but it was too late you stop yourself before you fall") ; sleep(2.5)
print("You look down in horror as the person is carried down the conveyor belt clearly in no shape to move, you shout 'STOP THE CONVEYOR BELTS' but it's too late, the saw at the end slices them up into shreds, blood splattered the saw and flew into the air") ; sleep(2.5)
print("You snap back to where you were and nearly throw up, you feel awful. You leave the room") ; sleep(2.5)

#option left if you diddnt see first memory

from time import sleep
print(WHITE + "You turn left, at the end there is one wooden door.") ; sleep(2.5)
print("You pull it open inside is nearly pitch black but you can make out the shape of a lever on the wall, you pull it and lights flicker on") ; sleep(2.5)
print("The room is now observable, it appeared to be a storage room with boxes stacked against a wall and broken machinery parts scattered the floor, a single table sat under the hanging light") ; sleep(2.5)
print("On the table lay a cardboard box its lid open inside was a bunch of photographs, some documents and a scarf, you look through the photos you recognise yourself along with the person from the cafe") ; sleep(2.5)
print("You and the person both looked happy stood among what seemed to be workers at the factory, you realise that you must of worked here along with the other person, you question why you diddnt remember this and what happened?") ; sleep(2.5)
print("The other photos also contained the person and you, you were in every single one. In each you were interacting and looked joyful, in some photos the other person was wearing a scarf") ; sleep(2.5)
print("You remember that you gave them the scarf, you were clearly close with them") ; sleep(2.5)
print("You look at the scarf in the box, it is the same as the one in the pictures. You put it on wanting to keep it with you") ; sleep(2.5)
print("You check the papers next they looked official, a name appears along with a picture") ; sleep(2.5)
print("It had all their information on it but then continued into 'fatal accident occured 5th of april involving this person via falling onto conveyor belt in line of logging saw...'") ; sleep(2.5)
print("You stop reading not wanting to read anymore as a dark memory fills your mind") ; sleep(2.5)
print("You were back in the main room of the factory on the balcony but everything looked unabandoned, there was the person stood next to the short barrier looking down at a machine and talking") ; sleep(2.5)
print("You see a cranes metal line carrying some sliced logs slowly moving your direction, suddenly theres the sound of breaking metal and the crane itself tips from the logs weight") ; sleep(2.5)
print("Before you can shout a warning the logs swing right into the balcony breaking part of it taking the person with it, you rush forward hand stretched out calling their name but it was too late you stop yourself before you fall") ; sleep(2.5)
print("You look down in horror as the person is carried down the conveyor belt clearly in no shape to move, you shout 'STOP THE CONVEYOR BELTS' but it's too late, the saw at the end slices them up into shreds, blood splattered the saw and flew into the air") ; sleep(2.5)
print("You snap back to where you were and nearly throw up, you feel awful. You leave the room") ; sleep(2.5)

#need to break this one up more ^

#option right

from time import sleep
print(WHITE + "You turn right at the end there is a metal door with thin pipes on each side, you enter") ; sleep(2.5)
print("It was dark inside with a damp smell, you make out the shape of a switch on the wall and turn it on") ; sleep(2.5)
print("A dim light flickers on and exposes hulking metal boilers and pipes stretching through the room, at the far end is another door") ; sleep(2.5)
print("You go through the door and find yourself on a concrete platform over a stream, there was some light shining down from a metal grill in the ceiling") ; sleep(2.5)
print("It appeared to be a sewage system with three large tunnels branching off from the main area you are in") ; sleep(2.5)
print("You hear the familiar clicking of claws on tiles behind you and some ragged breathing") ; sleep(2.5)
print(RED + "Where do you go?") ; sleep(2.5)

#choice 1

from time import sleep
print(WHITE + "You run down some small stairs and go down the tunnel with the flowing stream") ; sleep(2.5)
print("The water sloshes around your feet as you run, you hear splashing behind you") ; sleep(2.5)
print("You turn a corner and find that a metal grid is blocking your escape you turn with your back against it") ; sleep(2.5)
print("You look around frantically for an escape but theres nothing you can do") ; sleep(2.5)
print("You stare at the direction you can hear the splashing from, the creature turned the corner, from the dim light you could see its full size") ; sleep(2.5)
print("It stood nearly as tall as the tunnel with large bone like spines sticking out from its back, it had long legs with talons like a birds") ; sleep(2.5)
print("It appeared to have two sets of arms one long pair and a shorter pair that were covering the eyes, it looked like it had died a while ago") ; sleep(2.5)
print("Its black skin hung loosely from jutting bone, it turned its head in your direction its jaws opened slightly drool dripping from its teeth") ; sleep(2.5)
print("It paused, breathing ragged. You stare at it in horror. It then lunged jaws open clearing the gap very quickly only to pause millimeters from you") ; sleep(2.5)
print("It tipped its head and one hand lifts from its eyes, which exposed an empty eye socket with flesh hanging from it, it seemed to be looking at the scarf") ; sleep(2.5)
print("You slowly take it off and hold it away from you, it seemed to follow your movement. You make a split second decision and throw the scarf to the side as far away as you could") ; sleep(2.5)
print("The creatures lunges after it and you bolt past it running back up the tunnel and go down the one on the right spotting a door you throw it open and enter") ; sleep(2.5)

#choice 2 first try 

from time import sleep
print(WHITE + "You run down some small stairs and go down a tunnel the was ahead of you, theres a door on one side but also a dead end to the tunnel") ; sleep(2.5)
print("You enter, inside is a barren room except for a lift with a metal cage like appearance") ; sleep(2.5)
print("You realise its a ticket back up to the surface do you go up to it, there is a metal grid door it appeared to be locked") ; sleep(2.5)
print("You look around but there was no sign of a key") ; sleep(2.5)
print("You leave the room in search of the key") ; sleep(2.5)
print("You hear sounds from the tunnel to the left so you decide to avoid it") ; sleep(2.5)
print("The only place left it the other tunnel") ; sleep(2.5)

#choice 2 if choice 1 was picked first

from time import sleep
print(WHITE + "Inside is a barren room except for a lift with a metal cage like appearance") ; sleep(2.5)
print("You realise its a ticket back up to the surface do you go up to it, there is a metal grid door it appeared to be locked") ; sleep(2.5)
print("You look around but there was no sign of a key") ; sleep(2.5)
print("Looks like you have to go back out") ; sleep(2.5)
print("You hear sounds from the tunnel to the left where you came from so you go down the other") ; sleep(2.5)

#choice 3 first try

from time import sleep
print(WHITE + "You run down some small stairs and go down a tunnel to the left") ; sleep(2.5)
print("You see a door on the right side, the tunnel was blocked by a metal grill that let water through but you wouldnt fit") ; sleep(2.5)
print("You go into the room, there were pipes on one side with valves and pressure readers, on the other was a table with files and paper") ; sleep(2.5)
print("On the paper you see something shiny, it's a key.") ; sleep(2.5)
print("You pick it up and decide to leave") ; sleep(2.5)

# when you have the key

from time import sleep
print(WHITE + "You go back to the lift room and put the key into the lock") ; sleep(2.5)
print("The door creaks open behind you, you turn and see the creatures long face peering through") ; sleep(2.5)
print("You quickly turn the key") ; sleep(2.5)
print("The creature forces its way through the door taking a chunk of the wall off since it was too big") ; sleep(2.5)
print("The door clicks open and you rush inside and slam the door closed behind you and frantically press the up button") ; sleep(2.5)
print("The creature dives at the metal doors shaking them and trying to fit its face and arms between the metal") ; sleep(2.5)
print("Thankfully the lift starts to move up, you stare at the creature as you go up, it appeared to have alot of scars criss crossing its body") ; sleep(2.5)
print("You notice it also had the scarf tied around one arm") ; sleep(2.5)
print("The lift climbs too high and it goes out of view, it concerns you as to why it was so interesting in the scarf and why it is chasing you so insistently") ; sleep(2.5)

#back in factory

from time import sleep
print(WHITE + "You exit the lift when it reaches the top floor and find that you are back in a factory again") ; sleep(2.5)
print("It appeared to be a bit different however, you leave the lifts room and find your again in the main room but at the highest platform") ; sleep(2.5)
print("You get annoyed, you question why this is happening and what it all means. All that you remembered earlier was pretty important however") ; sleep(2.5)
print("A screech echoes out through the factory, you look around and curse you spot a large shard of broken glass from a window on the floor and pick it up") ; sleep(2.5)
print("You decide its time to try and get out the building fast as you can, you spy the creature on the ground floor") ; sleep(2.5)
print("It also notices you and jumps latching onto the platform, you run through a door at the end which leads to some stairs and out onto the roof") ; sleep(2.5)
print("There was a ladder that led to a higher part of the roof so you start to climb it") ; sleep(2.5)
print("You reach the top, you hear a clanging sound and suddenly the roof splits open tiles and wood flying everywhere, the creature emerges screeching") ; sleep(2.5)
print(RED + "Do you:") ; sleep(2.5)

#a

from time import sleep
print(WHITE + "Try to dodge it and run away along the roof") ; sleep(2.5)

#b
print("Stand your ground and fight with the glass shard") ; sleep(2.5)

#c 
print("Go back down the ladder") ; sleep(2.5)

#choice a

print("You try to dodge it but slip on a tile and the creature grabs you with its talons and rips you apart") ; sleep(2.5)
print(RED + "YOU DIED") ; sleep(2.5)

#choice b

print(WHITE + "You stand your ground holding the glass") ; sleep(2.5)
print("The creature turns to you") ; sleep(2.5)
print("The sunset was in full swing gold light reflected off the glass into the creatures eye sockets blinding it") ; sleep(2.5)
print("It shook its head and tried to cover its eyes but looses its grip on the roof and slips falling backwards into the hole") ; sleep(2.5)
print("You peer down the hole and see it landed on one of the machines and you get an idea") ; sleep(2.5)
print("You rush back down to the main room from where you came") ; sleep(2.5)

#choice c

print("You try to go back down the ladder but the creature climbs across the roof and swipes at you knocking you off and you fall off the roof") ; sleep(2.5)
print(RED + "YOU DIED") ; sleep(2.5)

from time import sleep
print(WHITE + "You spy a control panel on a balcony across from you and make your way over while the creature stirs below") ; sleep(2.5)
print("You reach the control panel and turn on the machinery as the creature stands up and jumps up at the balcony holding onto it") ; sleep(2.5)
print("It tries to snap at you with its jaws while holding on") ; sleep(2.5)
print(RED + "Do you:") ; sleep(2.5)

#a
print(WHITE + "Jump past it's jaws and get to the other control panel") ; sleep(2.5)

#b
print("Try to kick its face till it falls") ; sleep(2.5)

#c 
print("Flee") ; sleep(2.5)

#choice a

print("You jump past the creature and reach another control panel and use it to control a crane that was carrying logs and swing it into the creature") ; sleep(2.5)
print("The logs hit the creature and part of the platform making that part collapse and the creature falls onto a conveyor belt") ; sleep(2.5)
print("The creature is carried thrashing towards a saw and is sliced to bits") ; sleep(2.5)

#chocie b

print("You try to kick it in the face and it grabs your leg in its teeth and eats you") ; sleep(2.5)
print(RED + "YOU DIED") ; sleep(2.5)

#choice c
print(WHITE + "You try to run and the creature climbs up and pounces on you") ; sleep(2.5)
print(RED + "YOU DIED") ; sleep(2.5)

# END

from time import sleep
print(WHITE + "You look at the place where the creature died feeling glad you are rid of it but it felt wrong too") ; sleep(2.5)
print("The bloodied parts of the creature suddenly start to move into smaller chunks and form human body parts, there is a severed head looking up at you") ; sleep(2.5)
print("It was the person from your memories") ; sleep(2.5)
print("You wake suddenly sweating and shaking where you lay and try to sit calm") ; sleep(2.5)
print("You turn the nightstand lamp on and look at a picture next to it") ; sleep(2.5)
print("It was you and your best friend who you worked with") ; sleep(2.5)
print("'Im sorry' you say") ; sleep(2.5)

print(RED + "END") ; sleep(2.5)