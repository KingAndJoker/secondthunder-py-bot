const sharedVars = require('../data/variables');

function helpMessage(msg) {
  msg.delete( {timeout: 15000} );
  msg.channel.send(sharedVars.vars.helpMessage)
			.then(msg => {
				msg.delete({ timeout: 15000 });
			});
}

module.exports = {
	name: 'help',
	description: 'Returns all commands of bot',
	execute(msg) {
		helpMessage(msg);
	},
};