import axios from "axios";

function shortDescription(description, limit=100){
	if(description.length>=limit){
		return description.substring(0,limit-3)+'...'
	}
	return description
}


function getMap(obj){
	if(obj){
		return new Map(Object.entries(obj))
	}
	return new Map()
}


export {getMap,shortDescription}