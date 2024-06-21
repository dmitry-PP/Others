import React,{ useEffect, useState, useContext } from "react";
import axios from "axios";

import Footer from "./Footer";
import Header from "./Header";

import "../static/about.css";
import CardSettings from "./CardSettings";

import {AppStateContext} from "../utils/Context"



function Favourite(){

    const { appendToFavourites } = useContext(AppStateContext);
    console.log("local",localStorage.getItem("favourites"))
    let favourites = JSON.parse(localStorage.getItem("favourites"))

    const [products, setProducts] = useState([])
	useEffect(()=> {
		axios.get('http://localhost:3001/products')
		.then(res=>{
			setProducts(res.data.filter(elem=> favourites.includes(elem.id)))
		    }
		)
		.catch(err=>console.log(err))
		},[localStorage.favourites])
        

        return(
			<main>
                <Header Main="" Catalog="" Favourite="active" Basket="" About="" Order=""/>
                <div class="container mt-5">
                    <div class="row" id="favorite-items">
                        {
                            products.map((elem)=>{
                                return <CardSettings  rmFrom={appendToFavourites} Text="Удалить из избранного" price={elem.price} id={elem.id} name={elem.name} description={elem.description} image={elem.image}/>
                            })
                        }

                    </div>
                </div>
                <Footer/>
            </main>
        )
    
}

export default Favourite;