image splash = "images/logo/KIBA.png"

# NVL characters are used for the phone texting
define mc_nvl = Character(persistent.kidMC, kind=nvl, image="nighten", callback=Phone_SendSound)
define girl_nvl = Character("Girl", kind=nvl, callback=Phone_ReceiveSound)

define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.3)

#########################################################################################################
#                                            CHAPTER 0                                                  #
#########################################################################################################
define oldMC = Character("Robert")
define myst_alternateMC = Character("???", color = "#1DDCB3")

##############################
# kidMC
##############################
#define persistent.kidMC = Character("Robert")
image kidMC shrugShoulders = "characters/kidMC/kidMC shrugShoulders.png"
image kidMC thinking = "characters/kidMC/kidMC thinking.png"
image kidMC defaultEmotion = "characters/kidMC/kidMC defaultEmotion.png"
image kidMC unfocused = "characters/kidMC/kidMC unfocused.png"
image kidMC serious = "characters/kidMC/kidMC serious.png"
image kidMC smiling = "characters/kidMC/kidMC smiling.png"
image kidMC sad = "characters/kidMC/kidMC sad.png"
image kidMC confused = "characters/kidMC/kidMC confused.png"
image kidMC surprised = "characters/kidMC/kidMC surprised.png"
image kidMC flustered = "characters/kidMC/kidMC flustered.png"

##############################
# alternateMC and MC
##############################
define mc = Character("Robert")
define alternateMC = Character("Robert (Alternate)", color = "#1DDCB3")
image mc mysterious = "characters/mc/mc mysterious.png"
#==============================================================================
image mc thinking = "characters/mc/mc thinking.png"
image mc defaultEmotion = "characters/mc/mc defaultEmotion.png"
image mc unfocused = "characters/mc/mc unfocused.png"
image mc smiling = "characters/mc/mc smiling.png"
image mc sad = "characters/mc/mc sad.png"
image mc confused = "characters/mc/mc confused.png"
image mc surprised = "characters/mc/mc surprised.png"
image mc flustered = "characters/mc/mc flustered.png"

image mc student defaultEmotion = "characters/mc/mc student defaultEmotion.png"
image mc student unfocused = "characters/mc/mc student unfocused.png"
image mc student smiling = "characters/mc/mc student smiling.png"
image mc student sad = "characters/mc/mc student sad.png"
image mc student confused = "characters/mc/mc student confused.png"
image mc student surprised = "characters/mc/mc student surprised.png"
image mc student flustered = "characters/mc/mc student flustered.png"

image mc casual tearyEyed = "characters/mc/mc casual tearyEyed.png"
image mc casual defaultEmotion = "characters/mc/mc casual defaultEmotion.png"
image mc casual unfocused = "characters/mc/mc casual unfocused.png"
image mc casual smiling = "characters/mc/mc casual smiling.png"
image mc casual sad = "characters/mc/mc casual sad.png"
image mc casual confused = "characters/mc/mc casual confused.png"
image mc casual surprised = "characters/mc/mc casual surprised.png"
image mc casual flustered = "characters/mc/mc casual flustered.png"



#########################################################################################################
#                                            CHAPTER 1                                                  #
#########################################################################################################
##############################
# Biological Mom and Dad
##############################
define biologicalMom = Character("Olivia (Mom)", color = "#8BC7CC")
image biologicalMom defaultEmotion = "characters/biologicalMom/biologicalMom defaultEmotion.png"
image biologicalMom unfocused = "characters/biologicalMom/biologicalMom unfocused.png"
image biologicalMom threateningSmile = "characters/biologicalMom/biologicalMom threateningSmile.png"

define biologicalDad = Character("Alfred (Dad)", color = "#FFBD31")
image biologicalDad thinking = "characters/biologicalDad/biologicalDad thinking.png"
image biologicalDad defaultEmotion = "characters/biologicalDad/biologicalDad defaultEmotion.png"
image biologicalDad unfocused = "characters/biologicalDad/biologicalDad unfocused.png"
image biologicalDad smiling = "characters/biologicalDad/biologicalDad smiling.png"
image biologicalDad sad = "characters/biologicalDad/biologicalDad sad.png"
image biologicalDad confused = "characters/biologicalDad/biologicalDad confused.png"
image biologicalDad surprised = "characters/biologicalDad/biologicalDad surprised.png"
image biologicalDad flustered = "characters/biologicalDad/biologicalDad flustered.png"

##############################
# Mike
##############################
define mike = Character("Mike", color = "#9EFF31")
image mike defaultEmotion = "characters/mike/mike defaultEmotion.png"
image mike unfocused = "characters/mike/mike unfocused.png"
image mike smiling = "characters/mike/mike smiling.png"
image mike sad = "characters/mike/mike sad.png"
image mike confused = "characters/mike/mike confused.png"
image mike surprised = "characters/mike/mike surprised.png"
image mike flustered = "characters/mike/mike flustered.png"

image mike suit defaultEmotion = "characters/mike/mike suit defaultEmotion.png"
image mike suit unfocused = "characters/mike/mike suit unfocused.png"

image mike casual defaultEmotion = "characters/mike/mike casual defaultEmotion.png"
image mike casual unfocused = "characters/mike/mike casual unfocused.png"

##############################
# Neighbor and Dad's Friend
##############################
define neighbor = Character("Neighbor", color = "#DCC79F")
image neighbor smiling= "characters/neighbor/neighbor smiling.png"

define dadFriend = Character("Jim (Dad's Friend)", color = "#DCC79F")

##############################
# Rich Dad
##############################
define richDad = Character("Benedict (Mike's Dad)", color = "#FF0044")
image richDad pointingOnHisHead = "characters/richDad/richDad pointingOnHisHead.png"
image richDad thinking = "characters/richDad/richDad thinking.png"
image richDad slyGrin = "characters/richDad/richDad pointingOnHisHead.png"
image richDad defaultEmotion = "characters/richDad/richDad defaultEmotion.png"
image richDad unfocused = "characters/richDad/richDad unfocused.png"
image richDad smiling = "characters/richDad/richDad smiling.png"
image richDad sad = "characters/richDad/richDad sad.png"
image richDad confused = "characters/richDad/richDad confused.png"
image richDad surprised = "characters/richDad/richDad surprised.png"
image richDad flustered = "characters/richDad/richDad flustered.png"

##############################
# Rich Dad Employees
##############################
define mrsMartin = Character ("Mrs. Martin", color = "#804D90")
image mrsMartin defaultEmotion = "characters/mrsMartin/mrsMartin defaultEmotion.png"
image mrsMartin unfocused = "characters/mrsMartin/mrsMartin unfocused.png"
image mrsMartin smiling = "characters/mrsMartin/mrsMartin smiling.png"
image mrsMartin sad = "characters/mrsMartin/mrsMartin sad.png"
image mrsMartin confused = "characters/mrsMartin/mrsMartin confused.png"
image mrsMartin surprised = "characters/mrsMartin/mrsMartin surprised.png"
image mrsMartin flustered = "characters/mrsMartin/mrsMartin flustered.png"


define comicDistributor = Character("Comic Distributor", color = "#DCC79F")
image comicDistributor defaultEmotion = "characters/neighbor/neighbor defaultEmotion.png"
image comicDistributor unfocused = "characters/neighbor/neighbor unfocused.png"
image comicDistributor smiling = "characters/neighbor/neighbor smiling.png"

##############################
# Extras
##############################
define kidMCAngelConscience = Character("Good Conscience", color = "#5394b9")
define kidMCDevilConscience = Character("Bad Conscience", color = "#9b1b1b")
image kidMCAngelConscience = "ch1/kidMCAngelConscience.png"
image kidMCAngelConscience unfocused= "ch1/kidMCAngelConscience unfocused.png"
image kidMCDevilConscience = "ch1/kidMCDevilConscience.png"
image kidMCDevilConscience unfocused = "ch1/kidMCDevilConscience unfocused.png"

##############################
# IMAGES FOR CHAPTER 1
##############################
image logBook = "ch1/logBook.png"
image mcShakeHands = "ch1/mcShakeHands.png"
image coinsOnOpenHands = "ch1/coinsOnOpenHands.png"



#########################################################################################################
#                                            CHAPTER 2                                                  #
#########################################################################################################
##############################
# Kim
##############################
define Kim = Character("Kim" , color="#68e6e8")
image Kim defaultEmotion = "characters/kim/kim defaultEmotion.png"
image Kim unfocused = "characters/kim/kim unfocused.png"
image Kim smiling = "characters/kim/kim smiling.png"
image Kim casual defaultEmotion = "characters/kim/kim casual defaultEmotion.png"
image Kim casual unfocused = "characters/kim/kim casual unfocused.png"
image Kim casual smiling = "characters/kim/kim casual smiling.png"

##############################
# John
##############################
define john = Character("John", color = "#9EFF31")
image john defaultEmotion = "characters/john/john defaultEmotion.png"
image john unfocused = "characters/john/john unfocused.png"
image john smiling = "characters/john/john smiling.png"
image john sad = "characters/john/john sad.png"

##############################
# John's Butler
##############################
define butler = Character('Butler', color="#68e6e8")
image butler defaultEmotion = "characters/butler/butler defaultEmotion.png"
image butler unfocused = "characters/butler/butler unfocused.png"


##############################
# Liam, Noah, Oliver, and William
##############################
define Liam = Character('Liam', color = "#DCC79F")
image Liam defaultEmotion = "characters/liam/liam defaultEmotion.png"
image Liam unfocused = "characters/liam/liam unfocused.png"
image Liam smiling = "characters/liam/liam smiling.png"

define Oliver = Character('Oliver', color = "#DCC79F")
image Oliver defaultEmotion = "characters/oliver/oliver defaultEmotion.png"
image Oliver unfocused = "characters/oliver/oliver unfocused.png"
image Oliver smiling = "characters/oliver/oliver smiling.png"

define William = Character('William', color = "#DCC79F")
image William defaultEmotion = "characters/william/william defaultEmotion.png"
image William unfocused = "characters/william/william unfocused.png"
image William smiling = "characters/william/william smiling.png"

##############################
# Husband and Wife (Ext.Story)
##############################
define wife = Character('Wife', color = "#DCC79F")
define husband = Character('Husband', color = "#DCC79F")
image husband focused = "characters/husband and wife/husband focused.png"
image wife focused = "characters/husband and wife/wife focused.png"
image husbandwife unfocused = "characters/husband and wife/husband and wife unfocused.png"
image husband solo = "characters/husband and wife/husband solo.png"
image wife solo = "characters/husband and wife/wife solo.png"

##############################
# School Teacher
##############################
define teacher = Character('Teacher Beth', color = "#DCC79F")
image teacher defaultEmotion = "characters/teacher/teacher defaultEmotion.png"
image teacher unfocused = "characters/teacher/teacher unfocused.png"

##############################
# Car Salesman
##############################
define salesman = Character('Saleswoman', color = "#DCC79F")
image salesman defaultEmotion= "characters/salesman/salesman defaultEmotion.png"
image salesman unfocused = "characters/salesman/salesman unfocused.png"
image salesman smiling = "characters/salesman/salesman smiling.png"

##############################
#IMAGES FOR CHAPTER 2
##############################
image envelope = "ch2/envelope.png"
image readInvitation = "ch2/readInvitation.png"
image casual readInvitation = "ch2/casual readInvitation.png"
image cashflowAsset = "ch2/cashFlowPatternOfAsset.png"
image cashflowLiability = "ch2/cashFlowPatternOfLiability.png"
image cashflowMiddleClass = "ch2/cashFlowMiddleClass.png"
image cashflowPoor = "ch2/cashFlowPoor.png"
image cashflowRich = "ch2/cashFlowRich.png"
image ancillaryExpenses = "ch2/ancillaryExpenses.png"
image poorDadCashFlow = "ch2/poorDadCashFlow.png"
image richDadCashFlow = "ch2/richDadCashFlow.png"
image richGetRicher = "ch2/richGetRicher.png"
image middleClassStruggles = "ch2/middleClassStruggles.png"
image signingADocument = "ch2/signingADocument.png"



#########################################################################################################
#                                            CHAPTER 3                                                  #
#########################################################################################################
define RayKroc = Character("Ray Kroc", color = "#6B7AB9")
image RayKroc defaultEmotion = "characters/ray kroc/rayKroc defaultEmotion.png"
image RayKroc unfocused = "characters/ray kroc/rayKroc unfocused.png"
image RayKroc smiling = "characters/ray kroc/rayKroc smiling.png"

define keith = Character("Keith", color = "#DCC79F")
image keith defaultEmotion = "characters/oliver/oliver defaultEmotion.png"
image keith unfocused = "characters/oliver/oliver unfocused.png"
image keith smiling = "characters/oliver/oliver smiling.png"

#########################################################################################################
#                                            CHAPTER 4                                                  #
#########################################################################################################
##############################
# Popular Girl
##############################
define PopularGirl = Character("Popular Girl", color = "#DCC79F")
image PopularGirl defaultEmotion = "characters/popular girl/PopularGirl defaultEmotion.png"
image PopularGirl unfocused = "characters/popular girl/PopularGirl unfocused.png"
image PopularGirl smiling = "characters/popular girl/PopularGirl smiling.png"

##############################
# Customer Service
##############################
define CustomerService = Character("Customer Service Clerk", color = "#DCC79F")
image CustomerService defaultEmotion = "characters/customer service/CustomerService defaultEmotion.png"
image CustomerService unfocused = "characters/customer service/CustomerService unfocused.png"

##############################
# Bank Employee
##############################
define Employee = Character("Bank Employee", color = "#DCC79F")
image Employee defaultEmotion = "characters/bank employee/Employee defaultEmotion.png"
image Employee unfocused = "characters/bank employee/Employee unfocused.png"
image Employee smiling = "characters/bank employee/Employee smiling.png"

##############################
#IMAGES FOR CHAPTER 4
##############################
image locationEmoji = "locationEmoji.png"
image oven = "ch4/oven.png"
image handsOnLaptop = "ch4/handsOnLaptop.png"



#########################################################################################################
#                                            CHAPTER 5                                                  #
#########################################################################################################
##############################
# Attorney
##############################
define Attorney = Character("Attorney", color = "#DCC79F")
image Attorney defaultEmotion = "characters/attorney/Attorney defaultEmotion.png"
image Attorney unfocused = "characters/attorney/Attorney unfocused.png"
image Attorney smiling = "characters/attorney/Attorney smiling.png"

image mcReadInvitation = "ch2/mc readInvitation.png"

##############################
# Sean
##############################
define Sean = Character("Sean", color = "#DCC79F")
image Sean defaultEmotion = "characters/sean/Sean defaultEmotion.png"
image Sean unfocused = "characters/sean/Sean unfocused.png"
image Sean smiling = "characters/sean/Sean smiling.png"
image Sean sad = "characters/sean/Sean sad.png"



#########################################################################################################
#                                            CHAPTER 6                                                  #
#########################################################################################################
##############################
# Mechanic
##############################
define mechanic = Character("Mechanic", color="#DCC79F")
image mechanic clean defaultEmotion = "characters/mechanic/mechanic clean defaultEmotion.png"
image mechanic clean unfocused = "characters/mechanic/mechanic clean unfocused.png"
image mechanic dirty defaultEmotion = "characters/mechanic/mechanic dirty defaultEmotion.png"
image mechanic dirty unfocused = "characters/mechanic/mechanic dirty unfocused.png"

##############################
# Mechanic
##############################
define writer = Character("Writer", color="#DCC79F")
image writer defaultEmotion = "characters/writer/writer defaultEmotion.png"
image writer unfocused = "characters/writer/writer unfocused.png"
image writer smiling = "characters/writer/writer smiling.png"
image writer confused = "characters/writer/writer confused.png"

##############################
# Jake
##############################
define jake = Character("Jake", color="#DCC79F")
image jake defaultEmotion = "characters/jake/jake defaultEmotion.png"
image jake unfocused = "characters/jake/jake unfocused.png"
image jake smiling = "characters/jake/jake smiling.png"

##############################
# IMAGES FOR QUESTIONNAIRE
##############################
image 8bitCorrect = "8bitCheck.png"
image 8bitWrong = "8bitWrong.png"