import React from "react";
import {shortDescription,getMap} from "../utils/Utils"
import { motion } from 'framer-motion';

class Card extends React.Component{
    render(){

		let fav_check,basket_check;
		let favourites, basket;

		if (localStorage.favourites) {
			favourites = JSON.parse(localStorage.favourites)
			fav_check = (favourites.includes(this.props.id))}
		else fav_check = false

		if(localStorage.basket){
			basket = getMap(JSON.parse(localStorage.basket))
			basket_check = (basket.has(this.props.id))
		} 
			else basket_check = false

		let fav_name = (fav_check)? "Из избранного" : "В избранное"
		let basket_name = (basket_check)?"Из корзины" : "В корзину"

		let css_fav = (fav_check)? "btn btn-outline-danger mr-3":"btn btn-outline-primary mr-3"
		let css_basket = (basket_check)? "btn btn-danger mr-3":"btn btn-primary mr-3"
		
        return(
			<motion.div
                initial={{ opacity: 0, y: 50 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.5 }}
				whileHover={{ scale: 1.05 }}
                whileTap={{ scale: 0.95 }}
             	class="col-md-4 mb-4">
				<div class="card" data-id={this.props.id}>
					<img src={this.props.image} class="card-img-top"/>
					<div class="card-body">
						<h5 class="card-title">{this.props.name}</h5>
						<p class="card-text">{shortDescription(this.props.description)}</p>
						<p class="card-text">{this.props.price} руб</p>
						<div class="container mt-4">
							<div class="row">
								<a href={"/about/"+this.props.id} class="btn btn-outline-primary mr-3">Подробнее</a>
								{this.props.extra && (
                                    <>
								<a href="#" onClick={()=>this.props.addToFavourite(this.props.id)} class={css_fav}>{fav_name}</a>
								<a href="#" onClick={()=>this.props.addToBasket(this.props.id)} class={css_basket}>{basket_name}</a>
								</>
							)}
							</div>
						</div>
					</div>
				</div>
			</motion.div>
        )
    }
}

export default Card;