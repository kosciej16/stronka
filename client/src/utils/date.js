function newDateNoTime(x) {
	let ret = new Date()
	if (x) ret = new Date(x)
	ret.setHours(1)
	ret.setMinutes(0, 0, 0)
	return ret
}

function useTodayStrings(date_, options) {
	const date = newDateNoTime(date_)
	const today = newDateNoTime()
	if (date.getTime() == today.getTime()) return 'dziś'
	if (date.getTime() == today.addDays(1).getTime()) return 'jutro'
	if (date.getTime() == today.addDays(2).getTime()) return 'pojutrze'
	if (date.getTime() == today.addDays(-1).getTime()) return 'wczoraj'
	if (date.getTime() == today.addDays(-2).getTime()) return 'przedwczoraj'
	return date_.toLocaleDateString('pl-PL', options)
}

Date.prototype.addDays = function(days) {
    var date = new Date(this.valueOf());
    date.setDate(date.getDate() + days);
    return date;
}

export function getDateTimeString(time) {
	const options = { weekday: 'short', year: 'numeric', month: 'long', day: 'numeric' };
	const date = new Date(Date.parse(time + "Z"))
	return useTodayStrings(date, options)  + ", "  + date.toLocaleTimeString('pl-PL', {timeStyle: 'short'})
}

export function getDateStringShort(datetime) {
	const options = { year: 'numeric', month: 'numeric', day: 'numeric' };
	const date = new Date(Date.parse(datetime + "Z"))
	return useTodayStrings(date, options)
}

export function getTimeStringShort(datetime) {
	const date = new Date(Date.parse(datetime + "Z"))
	return date.toLocaleTimeString('pl-PL', {timeStyle: 'short'})
}

