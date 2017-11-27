// === Game Data ===
var gameData = {
	commandCounter : 0,
	gameOver : false,
	introText : 'You are Concordia Jones the paranormal investigator. As you have a third eye in the centre of your forehead, it\'s safe to say that you yourself are also paranormal.',
	outroText : 'Thanks For playing!',
	player : {
		currentLocation : 'Office',
		inventory : {},
	},
	map : {
		'Office' : {
			firstVisit : true,
			displayName : 'Your Office',
			description : 'This is your office. Office may be a strong word in light of the fact that it\'s actually a corner of your apartment that you\'ve crammed a desk and chairs into. A hot pink light shines through the window from the many brightly coloured signs of the neon district, illuminating the otherwise dim room. So tech noir.',
			interactables : {
				desk : { look : 'Covered in pages of notes you\'ve scrawled in order to feign an air of legitimacy.' },
				self : { look : 'You always wear your trench coat during work hours, indoors or outdoors. How else are people meant to correctly identify that you\'re a paranormal investigator?'},
				window : {
					look : 'You look out at the neon district. A whole district dedicated to the manufacture of neon signs. You briefly meditate on how that seems pretty reasonable and realistic.',
					use : 'You open the window. You think you can hear the dulcet tones of synthwave music in the warm air.'
				}
			},
			items : {
				helmet : {
					displayName : 'Miner Helmet',
					description : 'A trusty old miner helmet covered in minor dents. Still seems sturdy and the light works.',
					quantity : 1,
					hidden : true
				}
			},
			exits : {
				inside : {
					displayName : 'Inside',
					destination : 'Tunnel'
				}
			},
		},
		'Tunnel' : {
			firstVisit : true,
			displayName : 'Tunnel',
			description : 'It is dimly lit here and look much darker further back.',
			exits : {
				outside : {
					displayName : 'Outside',
					destination : 'MineEntrance'
				},
				deeper : {
					displayName : 'Deeper',
					destination : 'End'
				}
			}
		},
		'End' : {
			firstVisit : true,
			description : 'placeholder',
		}
	}
};

// === Game Actions ===
var gameActions = {

}

// === Necessary Exports ===
module.exports.gameData = gameData;
module.exports.gameActions = gameActions;

// === Helper Functions ===
