from app.models import db, Roster, Player, Franchise

rosterOne = [
    Roster(id="01", week="6"),
    Franchise(id="0001", name="Every Year's Runner up", abbr="EYR", roster_id= "01"),
    [
    ["player_id:11516", "roster_id: 01", "status: ROSTER"],
    ["player_id:12239", "roster_id: 01", "status: ROSTER"],
    ["player_id:12187", "roster_id: 01", "status: ROSTER"],
    ["player_id:11232", "roster_id: 01", "status: ROSTER"],
    ["player_id:10292", "roster_id: 01", "status: ROSTER"],
    ["player_id:13189", "roster_id: 01", "status: ROSTER"],
    ["player_id:10779", "roster_id: 01", "status: ROSTER"],
    ["player_id:14102", "roster_id: 01", "status: ROSTER"],
    ["player_id:13139", "roster_id: 01", "status: ROSTER"],
    ["player_id:14072", "roster_id: 01", "status: ROSTER"],
    ["player_id:12779", "roster_id: 01", "status: ROSTER"],
    ["player_id:13760", "roster_id: 01", "status: ROSTER"],
    ["player_id:13470", "roster_id: 01", "status: ROSTER"],
    ["player_id:14927", "roster_id: 01", "status: ROSTER"],
    ["player_id:14804", "roster_id: 01", "status: ROSTER"],
    ["player_id:14815", "roster_id: 01", "status: ROSTER"],
    ["player_id:14909", "roster_id: 01", "status: ROSTER"],
    ["player_id:12241", "roster_id: 01", "status: ROSTER"],
    ["player_id:13412", "roster_id: 01", "status: ROSTER"],
    ["player_id:13284", "roster_id: 01", "status: ROSTER"],
    ["player_id:14067", "roster_id: 01", "status: ROSTER"],
    ["player_id:12691", "roster_id: 01", "status: ROSTER"],
    ["player_id:14811", "roster_id: 01", "status: ROSTER"],
    ["player_id:13684", "roster_id: 01", "status: ROSTER"],
    ["player_id:13632", "roster_id: 01", "status: ROSTER"],
    ["player_id:12088", "roster_id: 01", "status: ROSTER"],
    ["player_id:13146", "roster_id: 01", "status: ROSTER"],
    ["player_id:12750", "roster_id: 01", "status: ROSTER"],
    ["player_id:14105", "roster_id: 01", "status: ROSTER"],
    ["player_id:14167", "roster_id: 01", "status: ROSTER"],
    ["player_id:14087", "roster_id: 01", "status: ROSTER"],
    ["player_id:13590", "roster_id: 01", "status: ROSTER"],
    ["player_id:15282", "roster_id: 01", "status: ROSTER"],
    ["player_id:15366", "roster_id: 01", "status: ROSTER"],
    ["player_id:15379", "roster_id: 01", "status: ROSTER"],
    ["player_id:13763", "roster_id: 01", "status: ROSTER"],
    ["player_id:15425", "roster_id: 01", "status: ROSTER"],
    ["player_id:13846", "roster_id: 01", "status: ROSTER"],
    ["player_id:10754", "roster_id: 01", "status: ROSTER"],
    ["player_id:10753", "roster_id: 01", "status: ROSTER"],
    ["player_id:13789", "roster_id: 01", "status: ROSTER"],
    ["player_id:15246", "roster_id: 01", "status: ROSTER"],
    ["player_id:12700", "roster_id: 01", "status: ROSTER"],
    ["player_id:10879", "roster_id: 01", "status: ROSTER"],
    ["player_id:13246", "roster_id: 01", "status: ROSTER"],
    ["player_id:*5848", "roster_id: 01", "status: ROSTER"],
    ["player_id:14808", "roster_id: 01", "status: INJURED_RESERVE"],
    ["player_id:13702", "roster_id: 01", "status: INJURED_RESERVE"],
]]

rosterTwo = [
    Roster(id="02", week="6"),
    Franchise(id="0002", name="Suspension Central", abbr="SC", roster_id= "02"),
    [    
    ["player_id:13610", "roster_id: 02", "status: ROSTER"],
    ["player_id:13622", "roster_id: 02", "status: ROSTER"],
    ["player_id:12930", "roster_id: 02", "status: ROSTER"],
    ["player_id:12788", "roster_id: 02", "status: ROSTER"],
    ["player_id:13646", "roster_id: 02", "status: ROSTER"],
    ["player_id:13116", "roster_id: 02", "status: ROSTER"],
    ["player_id:12610", "roster_id: 02", "status: ROSTER"],
    ["player_id:12686", "roster_id: 02", "status: ROSTER"],
    ["player_id:13277", "roster_id: 02", "status: ROSTER"],
    ["player_id:12768", "roster_id: 02", "status: ROSTER"],
    ["player_id:12287", "roster_id: 02", "status: ROSTER"],
    ["player_id:12741", "roster_id: 02", "status: ROSTER"],
    ["player_id:14138", "roster_id: 02", "status: ROSTER"],
    ["player_id:13606", "roster_id: 02", "status: ROSTER"],
    ["player_id:13747", "roster_id: 02", "status: ROSTER"],
    ["player_id:14171", "roster_id: 02", "status: ROSTER"],
    ["player_id:13249", "roster_id: 02", "status: ROSTER"],
    ["player_id:14122", "roster_id: 02", "status: ROSTER"],
    ["player_id:11680", "roster_id: 02", "status: ROSTER"],
    ["player_id:14870", "roster_id: 02", "status: ROSTER"],
    ["player_id:14798", "roster_id: 02", "status: ROSTER"],
    ["player_id:14896", "roster_id: 02", "status: ROSTER"],
    ["player_id:13322", "roster_id: 02", "status: ROSTER"],
    ["player_id:13447", "roster_id: 02", "status: ROSTER"],
    ["player_id:14226", "roster_id: 02", "status: ROSTER"],
    ["player_id:11956", "roster_id: 02", "status: ROSTER"],
    ["player_id:12987", "roster_id: 02", "status: ROSTER"],
    ["player_id:12742", "roster_id: 02", "status: ROSTER"],
    ["player_id:14218", "roster_id: 02", "status: ROSTER"],
    ["player_id:14260", "roster_id: 02", "status: ROSTER"],
    ["player_id:14143", "roster_id: 02", "status: ROSTER"],
    ["player_id:13299", "roster_id: 02", "status: ROSTER"],
    ["player_id:15238", "roster_id: 02", "status: ROSTER"],
    ["player_id:15346", "roster_id: 02", "status: ROSTER"],
    ["player_id:10413", "roster_id: 02", "status: ROSTER"],
    ["player_id:15409", "roster_id: 02", "status: ROSTER"],
    ["player_id:15361", "roster_id: 02", "status: ROSTER"],
    ["player_id:15385", "roster_id: 02", "status: ROSTER"],
    ["player_id:14073", "roster_id: 02", "status: ROSTER"],
    ["player_id:11671", "roster_id: 02", "status: ROSTER"],
    ["player_id:13723", "roster_id: 02", "status: ROSTER"],
    ["player_id:15040", "roster_id: 02", "status: ROSTER"],
    ["player_id:14127", "roster_id: 02", "status: ROSTER"],
    ["player_id:13765", "roster_id: 02", "status: ROSTER"],
    ["player_id:14159", "roster_id: 02", "status: ROSTER"],
    ["player_id:10729", "roster_id: 02", "status: ROSTER"],
    ["player_id:12652", "roster_id: 02", "status: INJURED_RESERVE"],
    ["player_id:13668", "roster_id: 02", "status: INJURED_RESERVE"],
]]

rosterThree = [
    Roster(id="03", week="6"),
    Franchise(id="0003", name="Tua-finity & Beyond", abbr="TIB", roster_id= "03"),
    [
    ["player_id:12745", "roster_id: 03", "status: ROSTER"],
    ["player_id:12231", "roster_id: 03", "status: ROSTER"],
    ["player_id:14163", "roster_id: 03", "status: ROSTER"],
    ["player_id:13230", "roster_id: 03", "status: ROSTER"],
    ["player_id:13223", "roster_id: 03", "status: ROSTER"],
    ["player_id:13251", "roster_id: 03", "status: ROSTER"],
    ["player_id:12176", "roster_id: 03", "status: ROSTER"],
    ["player_id:14225", "roster_id: 03", "status: ROSTER"],
    ["player_id:14247", "roster_id: 03", "status: ROSTER"],
    ["player_id:13236", "roster_id: 03", "status: ROSTER"],
    ["player_id:14974", "roster_id: 03", "status: ROSTER"],
    ["player_id:14778", "roster_id: 03", "status: ROSTER"],
    ["player_id:15082", "roster_id: 03", "status: ROSTER"],
    ["player_id:12658", "roster_id: 03", "status: ROSTER"],
    ["player_id:14184", "roster_id: 03", "status: ROSTER"],
    ["player_id:14858", "roster_id: 03", "status: ROSTER"],
    ["player_id:14081", "roster_id: 03", "status: ROSTER"],
    ["player_id:13319", "roster_id: 03", "status: ROSTER"],
    ["player_id:12225", "roster_id: 03", "status: ROSTER"],
    ["player_id:13216", "roster_id: 03", "status: ROSTER"],
    ["player_id:13153", "roster_id: 03", "status: ROSTER"],
    ["player_id:14873", "roster_id: 03", "status: ROSTER"],
    ["player_id:14170", "roster_id: 03", "status: ROSTER"],
    ["player_id:14186", "roster_id: 03", "status: ROSTER"],
    ["player_id:15240", "roster_id: 03", "status: ROSTER"],
    ["player_id:15284", "roster_id: 03", "status: ROSTER"],
    ["player_id:15239", "roster_id: 03", "status: ROSTER"],
    ["player_id:15331", "roster_id: 03", "status: ROSTER"],
    ["player_id:15287", "roster_id: 03", "status: ROSTER"],
    ["player_id:15272", "roster_id: 03", "status: ROSTER"],
    ["player_id:11760", "roster_id: 03", "status: ROSTER"],
    ["player_id:15292", "roster_id: 03", "status: ROSTER"],
    ["player_id:14845", "roster_id: 03", "status: ROSTER"],
    ["player_id:12625", "roster_id: 03", "status: ROSTER"],
    ["player_id:10271", "roster_id: 03", "status: ROSTER"],
    ["player_id:14085", "roster_id: 03", "status: ROSTER"],
    ["player_id:15334", "roster_id: 03", "status: ROSTER"],
    ["player_id:12711", "roster_id: 03", "status: ROSTER"],
    ["player_id:14923", "roster_id: 03", "status: ROSTER"],
    ["player_id:10261", "roster_id: 03", "status: ROSTER"],
    ["player_id:12317", "roster_id: 03", "status: ROSTER"],
    ["player_id:13700", "roster_id: 03", "status: ROSTER"],
    ["player_id:11150", "roster_id: 03", "status: ROSTER"],
    ["player_id:13810", "roster_id: 03", "status: ROSTER"],
    ["player_id:14558", "roster_id: 03", "status: ROSTER"],
    ["player_id:*9902",  "roster_id: 03", "status: ROSTER"],
    ["player_id:13290", "roster_id: 03", "status: INJURED_RESERVE"],
    ["player_id:14141", "roster_id: 03", "status: INJURED_RESERVE"],
]]

rosterFour = [
    Roster(id="04", week="6"),
    Franchise(id="0004", name="Brad", abbr="BRD", roster_id= "04"),
    [
    ["player_id:12647", "roster_id: 04", "status: ROSTER"],
    ["player_id:11317", "roster_id: 04", "status: ROSTER"],
    ["player_id:10775", "roster_id: 04", "status: ROSTER"],
    ["player_id:13129", "roster_id: 04", "status: ROSTER"],
    ["player_id:*9918",  "roster_id: 04", "status: ROSTER"],
    ["player_id:13115", "roster_id: 04", "status: ROSTER"],
    ["player_id:11644", "roster_id: 04", "status: ROSTER"],
    ["player_id:10697", "roster_id: 04", "status: ROSTER"],
    ["player_id:12630", "roster_id: 04", "status: ROSTER"],
    ["player_id:11244", "roster_id: 04", "status: ROSTER"],
    ["player_id:12752", "roster_id: 04", "status: ROSTER"],
    ["player_id:*9833",  "roster_id: 04", "status: ROSTER"],
    ["player_id:11228", "roster_id: 04", "status: ROSTER"],
    ["player_id:12676", "roster_id: 04", "status: ROSTER"],
    ["player_id:14168", "roster_id: 04", "status: ROSTER"],
    ["player_id:10266", "roster_id: 04", "status: ROSTER"],
    ["player_id:12678", "roster_id: 04", "status: ROSTER"],
    ["player_id:12767", "roster_id: 04", "status: ROSTER"],
    ["player_id:14889", "roster_id: 04", "status: ROSTER"],
    ["player_id:14841", "roster_id: 04", "status: ROSTER"],
    ["player_id:14834", "roster_id: 04", "status: ROSTER"],
    ["player_id:14136", "roster_id: 04", "status: ROSTER"],
    ["player_id:11316", "roster_id: 04", "status: ROSTER"],
    ["player_id:13377", "roster_id: 04", "status: ROSTER"],
    ["player_id:11769", "roster_id: 04", "status: ROSTER"],
    ["player_id:11772", "roster_id: 04", "status: ROSTER"],
    ["player_id:12688", "roster_id: 04", "status: ROSTER"],
    ["player_id:13607", "roster_id: 04", "status: ROSTER"],
    ["player_id:13307", "roster_id: 04", "status: ROSTER"],
    ["player_id:13108", "roster_id: 04", "status: ROSTER"],
    ["player_id:10267", "roster_id: 04", "status: ROSTER"],
    ["player_id:13630", "roster_id: 04", "status: ROSTER"],
    ["player_id:13304", "roster_id: 04", "status: ROSTER"],
    ["player_id:12447", "roster_id: 04", "status: ROSTER"],
    ["player_id:15241", "roster_id: 04", "status: ROSTER"],
    ["player_id:15257", "roster_id: 04", "status: ROSTER"],
    ["player_id:15373", "roster_id: 04", "status: ROSTER"],
    ["player_id:15362", "roster_id: 04", "status: ROSTER"],
    ["player_id:12611", "roster_id: 04", "status: ROSTER"],
    ["player_id:14956", "roster_id: 04", "status: ROSTER"],
    ["player_id:13880", "roster_id: 04", "status: ROSTER"],
    ["player_id:12218", "roster_id: 04", "status: ROSTER"],
    ["player_id:12637", "roster_id: 04", "status: ROSTER"],
    ["player_id:13688", "roster_id: 04", "status: ROSTER"],
    ["player_id:13623", "roster_id: 04", "status: ROSTER"],
    ["player_id:12629", "roster_id: 04", "status: ROSTER"],
    ["player_id:14800", "roster_id: 04", "status: INJURED_RESERVE"],
    ["player_id:13850", "roster_id: 04", "status: INJURED_RESERVE"],
]]

rosterFive = [
    Roster(id="05", week="6"),
    Franchise(id="0005", name="#beatinggoff", abbr="#BO", roster_id= "05"),
    [
    ["player_id:12677", "roster_id: 05", "status: ROSTER"],
    ["player_id:*9430",  "roster_id: 05", "status: ROSTER"],
    ["player_id:11678", "roster_id: 05", "status: ROSTER"],
    ["player_id:*7401",  "roster_id: 05", "status: ROSTER"],
    ["player_id:11382", "roster_id: 05", "status: ROSTER"],
    ["player_id:11757", "roster_id: 05", "status: ROSTER"],
    ["player_id:*9815",  "roster_id: 05", "status: ROSTER"],
    ["player_id:13273", "roster_id: 05", "status: ROSTER"],
    ["player_id:12175", "roster_id: 05", "status: ROSTER"],
    ["player_id:11657", "roster_id: 05", "status: ROSTER"],
    ["player_id:13713", "roster_id: 05", "status: ROSTER"],
    ["player_id:11721", "roster_id: 05", "status: ROSTER"],
    ["player_id:10277", "roster_id: 05", "status: ROSTER"],
    ["player_id:12650", "roster_id: 05", "status: ROSTER"],
    ["player_id:11938", "roster_id: 05", "status: ROSTER"],
    ["player_id:13696", "roster_id: 05", "status: ROSTER"],
    ["player_id:14059", "roster_id: 05", "status: ROSTER"],
    ["player_id:14079", "roster_id: 05", "status: ROSTER"],
    ["player_id:14149", "roster_id: 05", "status: ROSTER"],
    ["player_id:12263", "roster_id: 05", "status: ROSTER"],
    ["player_id:14210", "roster_id: 05", "status: ROSTER"],
    ["player_id:13614", "roster_id: 05", "status: ROSTER"],
    ["player_id:14850", "roster_id: 05", "status: ROSTER"],
    ["player_id:14852", "roster_id: 05", "status: ROSTER"],
    ["player_id:14783", "roster_id: 05", "status: ROSTER"],
    ["player_id:14877", "roster_id: 05", "status: ROSTER"],
    ["player_id:12301", "roster_id: 05", "status: ROSTER"],
    ["player_id:13813", "roster_id: 05", "status: ROSTER"],
    ["player_id:13690", "roster_id: 05", "status: ROSTER"],
    ["player_id:12152", "roster_id: 05", "status: ROSTER"],
    ["player_id:13775", "roster_id: 05", "status: ROSTER"],
    ["player_id:14905", "roster_id: 05", "status: ROSTER"],
    ["player_id:12234", "roster_id: 05", "status: ROSTER"],
    ["player_id:13154", "roster_id: 05", "status: ROSTER"],
    ["player_id:13699", "roster_id: 05", "status: ROSTER"],
    ["player_id:15237", "roster_id: 05", "status: ROSTER"],
    ["player_id:12184", "roster_id: 05", "status: ROSTER"],
    ["player_id:15349", "roster_id: 05", "status: ROSTER"],
    ["player_id:15355", "roster_id: 05", "status: ROSTER"],
    ["player_id:15404", "roster_id: 05", "status: ROSTER"],
    ["player_id:15301", "roster_id: 05", "status: ROSTER"],
    ["player_id:15297", "roster_id: 05", "status: ROSTER"],
    ["player_id:11293", "roster_id: 05", "status: ROSTER"],
    ["player_id:13620", "roster_id: 05", "status: ROSTER"],
    ["player_id:14250", "roster_id: 05", "status: ROSTER"],
    ["player_id:13959", "roster_id: 05", "status: ROSTER"],
    ["player_id:14799", "roster_id: 05", "status: INJURED_RESERVE"],
    ["player_id:15253", "roster_id: 05", "status: INJURED_RESERVE"],
]]

rosterSix = [
    Roster(id="06", week="6"),
    Franchise(id="0006", name="Hines Park Bumz", abbr="HPB", roster_id= "06"),
    [
    ["player_id:13138", "roster_id: 06", "status: ROSTER"],
    ["player_id:10768", "roster_id: 06", "status: ROSTER"],
    ["player_id:13156", "roster_id: 06", "status: ROSTER"],
    ["player_id:13163", "roster_id: 06", "status: ROSTER"],
    ["player_id:12150", "roster_id: 06", "status: ROSTER"],
    ["player_id:10816", "roster_id: 06", "status: ROSTER"],
    ["player_id:12626", "roster_id: 06", "status: ROSTER"],
    ["player_id:11886", "roster_id: 06", "status: ROSTER"],
    ["player_id:14223", "roster_id: 06", "status: ROSTER"],
    ["player_id:14071", "roster_id: 06", "status: ROSTER"],
    ["player_id:10703", "roster_id: 06", "status: ROSTER"],
    ["player_id:10973", "roster_id: 06", "status: ROSTER"],
    ["player_id:14836", "roster_id: 06", "status: ROSTER"],
    ["player_id:14844", "roster_id: 06", "status: ROSTER"],
    ["player_id:13772", "roster_id: 06", "status: ROSTER"],
    ["player_id:*9988",  "roster_id: 06", "status: ROSTER"],
    ["player_id:*9431",  "roster_id: 06", "status: ROSTER"],
    ["player_id:14412", "roster_id: 06", "status: ROSTER"],
    ["player_id:14857", "roster_id: 06", "status: ROSTER"],
    ["player_id:15281", "roster_id: 06", "status: ROSTER"],
    ["player_id:15288", "roster_id: 06", "status: ROSTER"],
    ["player_id:15283", "roster_id: 06", "status: ROSTER"],
    ["player_id:15351", "roster_id: 06", "status: ROSTER"],
    ["player_id:15242", "roster_id: 06", "status: ROSTER"],
    ["player_id:15387", "roster_id: 06", "status: ROSTER"],
    ["player_id:12476", "roster_id: 06", "status: ROSTER"],
    ["player_id:11247", "roster_id: 06", "status: ROSTER"],
    ["player_id:12616", "roster_id: 06", "status: ROSTER"],
    ["player_id:12238", "roster_id: 06", "status: ROSTER"],
    ["player_id:13675", "roster_id: 06", "status: ROSTER"],
    ["player_id:14328", "roster_id: 06", "status: ROSTER"],
    ["player_id:13133", "roster_id: 06", "status: ROSTER"],
    ["player_id:14162", "roster_id: 06", "status: ROSTER"],
    ["player_id:12628", "roster_id: 06", "status: ROSTER"],
    ["player_id:12349", "roster_id: 06", "status: ROSTER"],
    ["player_id:13204", "roster_id: 06", "status: ROSTER"],
    ["player_id:15271", "roster_id: 06", "status: ROSTER"],
    ["player_id:12817", "roster_id: 06", "status: ROSTER"],
    ["player_id:14221", "roster_id: 06", "status: ROSTER"],
    ["player_id:*9828",  "roster_id: 06", "status: ROSTER"],
    ["player_id:12831", "roster_id: 06", "status: ROSTER"],
    ["player_id:12773", "roster_id: 06", "status: ROSTER"],
    ["player_id:13268", "roster_id: 06", "status: ROSTER"],
    ["player_id:15029", "roster_id: 06", "status: ROSTER"],
    ["player_id:13382", "roster_id: 06", "status: ROSTER"],
    ["player_id:12828", "roster_id: 06", "status: ROSTER"],
    ["player_id:*8062",  "roster_id: 06", "status: INJURED_RESERVE"],
    ["player_id:15290", "roster_id: 06", "status: INJURED_RESERVE"],
]]

rosterSeven = [
    Roster(id="07", week="6"),
    Franchise(id="0007", name="Lines & Dimes", abbr="L&D", roster_id= "07"),
    [
    ["player_id:13214", "roster_id: 07", "status: ROSTER"],
    ["player_id:*9099",  "roster_id: 07", "status: ROSTER"],
    ["player_id:10276", "roster_id: 07", "status: ROSTER"],
    ["player_id:10738", "roster_id: 07", "status: ROSTER"],
    ["player_id:13231", "roster_id: 07", "status: ROSTER"],
    ["player_id:*9474",  "roster_id: 07", "status: ROSTER"],
    ["player_id:12151", "roster_id: 07", "status: ROSTER"],
    ["player_id:10700", "roster_id: 07", "status: ROSTER"],
    ["player_id:12217", "roster_id: 07", "status: ROSTER"],
    ["player_id:12181", "roster_id: 07", "status: ROSTER"],
    ["player_id:12718", "roster_id: 07", "status: ROSTER"],
    ["player_id:14835", "roster_id: 07", "status: ROSTER"],
    ["player_id:14840", "roster_id: 07", "status: ROSTER"],
    ["player_id:14802", "roster_id: 07", "status: ROSTER"],
    ["player_id:14782", "roster_id: 07", "status: ROSTER"],
    ["player_id:12386", "roster_id: 07", "status: ROSTER"],
    ["player_id:12734", "roster_id: 07", "status: ROSTER"],
    ["player_id:13245", "roster_id: 07", "status: ROSTER"],
    ["player_id:14842", "roster_id: 07", "status: ROSTER"],
    ["player_id:11679", "roster_id: 07", "status: ROSTER"],
    ["player_id:13707", "roster_id: 07", "status: ROSTER"],
    ["player_id:12785", "roster_id: 07", "status: ROSTER"],
    ["player_id:13298", "roster_id: 07", "status: ROSTER"],
    ["player_id:13201", "roster_id: 07", "status: ROSTER"],
    ["player_id:14918", "roster_id: 07", "status: ROSTER"],
    ["player_id:12656", "roster_id: 07", "status: ROSTER"],
    ["player_id:12764", "roster_id: 07", "status: ROSTER"],
    ["player_id:14197", "roster_id: 07", "status: ROSTER"],
    ["player_id:12795", "roster_id: 07", "status: ROSTER"],
    ["player_id:12620", "roster_id: 07", "status: ROSTER"],
    ["player_id:15329", "roster_id: 07", "status: ROSTER"],
    ["player_id:15259", "roster_id: 07", "status: ROSTER"],
    ["player_id:15350", "roster_id: 07", "status: ROSTER"],
    ["player_id:15255", "roster_id: 07", "status: ROSTER"],
    ["player_id:13919", "roster_id: 07", "status: ROSTER"],
    ["player_id:15378", "roster_id: 07", "status: ROSTER"],
    ["player_id:14992", "roster_id: 07", "status: ROSTER"],
    ["player_id:15275", "roster_id: 07", "status: ROSTER"],
    ["player_id:15480", "roster_id: 07", "status: ROSTER"],
    ["player_id:15263", "roster_id: 07", "status: ROSTER"],
    ["player_id:12952", "roster_id: 07", "status: ROSTER"],
    ["player_id:12275", "roster_id: 07", "status: ROSTER"],
    ["player_id:14928", "roster_id: 07", "status: ROSTER"],
    ["player_id:10308", "roster_id: 07", "status: ROSTER"],
    ["player_id:13192", "roster_id: 07", "status: ROSTER"],
    ["player_id:15293", "roster_id: 07", "status: ROSTER"],
    ["player_id:15250", "roster_id: 07", "status: INJURED_RESERVE"],
    ["player_id:11647", "roster_id: 07", "status: INJURED_RESERVE"],
]]

rosterEight = [
    Roster(id="08", week="6"),
    Franchise(id="0008", name="Storm of Bolts", abbr="SOB", roster_id= "08"),
    [
    ["player_id:13589", "roster_id: 08", "status: ROSTER"],
    ["player_id:13697", "roster_id: 08", "status: ROSTER"],
    ["player_id:13198", "roster_id: 08", "status: ROSTER"],
    ["player_id:13727", "roster_id: 08", "status: ROSTER"],
    ["player_id:12702", "roster_id: 08", "status: ROSTER"],
    ["player_id:11670", "roster_id: 08", "status: ROSTER"],
    ["player_id:12186", "roster_id: 08", "status: ROSTER"],
    ["player_id:13733", "roster_id: 08", "status: ROSTER"],
    ["player_id:13130", "roster_id: 08", "status: ROSTER"],
    ["player_id:13132", "roster_id: 08", "status: ROSTER"],
    ["player_id:12250", "roster_id: 08", "status: ROSTER"],
    ["player_id:11222", "roster_id: 08", "status: ROSTER"],
    ["player_id:11695", "roster_id: 08", "status: ROSTER"],
    ["player_id:*7836",  "roster_id: 08", "status: ROSTER"],
    ["player_id:12814", "roster_id: 08", "status: ROSTER"],
    ["player_id:12305", "roster_id: 08", "status: ROSTER"],
    ["player_id:14137", "roster_id: 08", "status: ROSTER"],
    ["player_id:14109", "roster_id: 08", "status: ROSTER"],
    ["player_id:13672", "roster_id: 08", "status: ROSTER"],
    ["player_id:14832", "roster_id: 08", "status: ROSTER"],
    ["player_id:14867", "roster_id: 08", "status: ROSTER"],
    ["player_id:14897", "roster_id: 08", "status: ROSTER"],
    ["player_id:13764", "roster_id: 08", "status: ROSTER"],
    ["player_id:14839", "roster_id: 08", "status: ROSTER"],
    ["player_id:12164", "roster_id: 08", "status: ROSTER"],
    ["player_id:*9853",  "roster_id: 08", "status: ROSTER"],
    ["player_id:12763", "roster_id: 08", "status: ROSTER"],
    ["player_id:11265", "roster_id: 08", "status: ROSTER"],
    ["player_id:13479", "roster_id: 08", "status: ROSTER"],
    ["player_id:11390", "roster_id: 08", "status: ROSTER"],
    ["player_id:13404", "roster_id: 08", "status: ROSTER"],
    ["player_id:11375", "roster_id: 08", "status: ROSTER"],
    ["player_id:13604", "roster_id: 08", "status: ROSTER"],
    ["player_id:12221", "roster_id: 08", "status: ROSTER"],
    ["player_id:13234", "roster_id: 08", "status: ROSTER"],
    ["player_id:13714", "roster_id: 08", "status: ROSTER"],
    ["player_id:14779", "roster_id: 08", "status: ROSTER"],
    ["player_id:15319", "roster_id: 08", "status: ROSTER"],
    ["player_id:13762", "roster_id: 08", "status: ROSTER"],
    ["player_id:15252", "roster_id: 08", "status: ROSTER"],
    ["player_id:15332", "roster_id: 08", "status: ROSTER"],
    ["player_id:14991", "roster_id: 08", "status: ROSTER"],
    ["player_id:12311", "roster_id: 08", "status: ROSTER"],
    ["player_id:14590", "roster_id: 08", "status: ROSTER"],
    ["player_id:13157", "roster_id: 08", "status: ROSTER"],
    ["player_id:14847", "roster_id: 08", "status: ROSTER"],
    ["player_id:10789", "roster_id: 08", "status: INJURED_RESERVE"],
    ["player_id:13364", "roster_id: 08", "status: INJURED_RESERVE"],
]]

rosterNine = [
    Roster(id="09", week="6"),
    Franchise (id="0009", name="Cobra Ky", abbr="CK", roster_id= "09"),
    [
    ["player_id:12701", "roster_id: 09", "status: ROSTER"],
    ["player_id:11640", "roster_id: 09", "status: ROSTER"],
    ["player_id:14056", "roster_id: 09", "status: ROSTER"],
    ["player_id:14104", "roster_id: 09", "status: ROSTER"],
    ["player_id:13680", "roster_id: 09", "status: ROSTER"],
    ["player_id:14123", "roster_id: 09", "status: ROSTER"],
    ["player_id:13706", "roster_id: 09", "status: ROSTER"],
    ["player_id:12985", "roster_id: 09", "status: ROSTER"],
    ["player_id:14887", "roster_id: 09", "status: ROSTER"],
    ["player_id:14838", "roster_id: 09", "status: ROSTER"],
    ["player_id:14797", "roster_id: 09", "status: ROSTER"],
    ["player_id:13737", "roster_id: 09", "status: ROSTER"],
    ["player_id:13252", "roster_id: 09", "status: ROSTER"],
    ["player_id:13427", "roster_id: 09", "status: ROSTER"],
    ["player_id:13743", "roster_id: 09", "status: ROSTER"],
    ["player_id:14148", "roster_id: 09", "status: ROSTER"],
    ["player_id:14903", "roster_id: 09", "status: ROSTER"],
    ["player_id:14075", "roster_id: 09", "status: ROSTER"],
    ["player_id:12140", "roster_id: 09", "status: ROSTER"],
    ["player_id:14875", "roster_id: 09", "status: ROSTER"],
    ["player_id:13674", "roster_id: 09", "status: ROSTER"],
    ["player_id:14908", "roster_id: 09", "status: ROSTER"],
    ["player_id:13635", "roster_id: 09", "status: ROSTER"],
    ["player_id:13717", "roster_id: 09", "status: ROSTER"],
    ["player_id:13131", "roster_id: 09", "status: ROSTER"],
    ["player_id:13128", "roster_id: 09", "status: ROSTER"],
    ["player_id:11675", "roster_id: 09", "status: ROSTER"],
    ["player_id:12801", "roster_id: 09", "status: ROSTER"],
    ["player_id:14157", "roster_id: 09", "status: ROSTER"],
    ["player_id:13593", "roster_id: 09", "status: ROSTER"],
    ["player_id:15256", "roster_id: 09", "status: ROSTER"],
    ["player_id:15289", "roster_id: 09", "status: ROSTER"],
    ["player_id:14892", "roster_id: 09", "status: ROSTER"],
    ["player_id:11728", "roster_id: 09", "status: ROSTER"],
    ["player_id:15034", "roster_id: 09", "status: ROSTER"],
    ["player_id:13671", "roster_id: 09", "status: ROSTER"],
    ["player_id:13488", "roster_id: 09", "status: ROSTER"],
    ["player_id:11225", "roster_id: 09", "status: ROSTER"],
    ["player_id:14147", "roster_id: 09", "status: ROSTER"],
    ["player_id:13777", "roster_id: 09", "status: ROSTER"],
    ["player_id:14978", "roster_id: 09", "status: ROSTER"],
    ["player_id:14180", "roster_id: 09", "status: ROSTER"],
    ["player_id:13716", "roster_id: 09", "status: ROSTER"],
    ["player_id:14518", "roster_id: 09", "status: ROSTER"],
    ["player_id:14926", "roster_id: 09", "status: ROSTER"],
    ["player_id:13770", "roster_id: 09", "status: ROSTER"],
    ["player_id:13710", "roster_id: 09", "status: INJURED_RESERVE"],
    ["player_id:14803", "roster_id: 09", "status: INJURED_RESERVE"],
]]

rosterTen = [
    Roster(id="10", week="6"),
    Franchise(id="0010", name="Fish Under Water", abbr="FUW", roster_id= "10"),
    [
    ["player_id:13113", "roster_id: 10", "status: ROSTER"],
    ["player_id:11314", "roster_id: 10", "status: ROSTER"],
    ["player_id:10260", "roster_id: 10", "status: ROSTER"],
    ["player_id:11349", "roster_id: 10", "status: ROSTER"],
    ["player_id:13629", "roster_id: 10", "status: ROSTER"],
    ["player_id:14080", "roster_id: 10", "status: ROSTER"],
    ["player_id:14057", "roster_id: 10", "status: ROSTER"],
    ["player_id:14208", "roster_id: 10", "status: ROSTER"],
    ["player_id:10272", "roster_id: 10", "status: ROSTER"],
    ["player_id:13208", "roster_id: 10", "status: ROSTER"],
    ["player_id:13306", "roster_id: 10", "status: ROSTER"],
    ["player_id:11742", "roster_id: 10", "status: ROSTER"],
    ["player_id:13726", "roster_id: 10", "status: ROSTER"],
    ["player_id:10783", "roster_id: 10", "status: ROSTER"],
    ["player_id:14899", "roster_id: 10", "status: ROSTER"],
    ["player_id:14780", "roster_id: 10", "status: ROSTER"],
    ["player_id:13424", "roster_id: 10", "status: ROSTER"],
    ["player_id:11674", "roster_id: 10", "status: ROSTER"],
    ["player_id:*9925", "roster_id: 10", "status: ROSTER"],
    ["player_id:11313", "roster_id: 10", "status: ROSTER"],
    ["player_id:11010", "roster_id: 10", "status: ROSTER"],
    ["player_id:12075", "roster_id: 10", "status: ROSTER"],
    ["player_id:11795", "roster_id: 10", "status: ROSTER"],
    ["player_id:13793", "roster_id: 10", "status: ROSTER"],
    ["player_id:13164", "roster_id: 10", "status: ROSTER"],
    ["player_id:13681", "roster_id: 10", "status: ROSTER"],
    ["player_id:12171", "roster_id: 10", "status: ROSTER"],
    ["player_id:14805", "roster_id: 10", "status: ROSTER"],
    ["player_id:14813", "roster_id: 10", "status: ROSTER"],
    ["player_id:14113", "roster_id: 10", "status: ROSTER"],
    ["player_id:13633", "roster_id: 10", "status: ROSTER"],
    ["player_id:13193", "roster_id: 10", "status: ROSTER"],
    ["player_id:11720", "roster_id: 10", "status: ROSTER"],
    ["player_id:14777", "roster_id: 10", "status: ROSTER"],
    ["player_id:11706", "roster_id: 10", "status: ROSTER"],
    ["player_id:15254", "roster_id: 10", "status: ROSTER"],
    ["player_id:15258", "roster_id: 10", "status: ROSTER"],
    ["player_id:15308", "roster_id: 10", "status: ROSTER"],
    ["player_id:15345", "roster_id: 10", "status: ROSTER"],
    ["player_id:15352", "roster_id: 10", "status: ROSTER"],
    ["player_id:15243", "roster_id: 10", "status: ROSTER"],
    ["player_id:15261", "roster_id: 10", "status: ROSTER"],
    ["player_id:10774", "roster_id: 10", "status: ROSTER"],
    ["player_id:13722", "roster_id: 10", "status: ROSTER"],
    ["player_id:14833", "roster_id: 10", "status: ROSTER"],
    ["player_id:13592", "roster_id: 10", "status: ROSTER"],
]]
list_of_rosters = [rosterOne, rosterTwo, rosterThree, rosterFour, rosterFive, rosterSix, rosterSeven, rosterEight, rosterNine, rosterTen]


def seed_rosters():
    for item in list_of_rosters:
        db.session.add(item[0])
        db.session.add(item[1])
        for plyr in item[-1]:
            print(plyr)
            first = plyr[0]
            pid = first[-5:]
            if pid[0] == "*":
                pid = pid[1:]    
            player = Player.query.filter_by(player_id=pid)
            second = plyr[1]
            rid = second[-2:]
            stat = plyr[2]
            sid = ""
            if stat == "status: ROSTER":
                sid = "ROSTER"
            elif stat == "status: INJURED_RESERVE":
                sid = "INJURED_RESERVE"
            print(player)
            setattr(player, "roster_id", rid)
            setattr(player, "status", sid)
    db.session.commit()

def undo_rosters():
    db.session.execute('TRUNCATE rosters RESTART IDENTITY CASCADE;')
    db.session.commit()

# def seed_franchises():
#     for item in list_of_rosters:
        

#     db.session.commit()
    
# def undo_franchises():
#     db.session.execute('TRUNCATE franchises RESTART IDENTITY CASCADE;')
#     db.session.commit()

# def seed_players_two():

        

            