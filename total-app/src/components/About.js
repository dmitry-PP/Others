import React, { useEffect, useState,useContext } from "react";
import Footer from "./Footer";
import Header from "./Header";
import axios from "axios";
import "../static/about.css";
import { useParams } from "react-router-dom";
import { AppStateContext } from "../utils/Context";

import {getMap} from "../utils/Utils"


function About(){

        const { appendToBasket, appendToFavourites } = useContext(AppStateContext);

        const params = useParams();
        const productId = params.productId

        let fav_check,basket_check;
		let favourites, basket;

		if (localStorage.favourites) {
			favourites = JSON.parse(localStorage.favourites)
			fav_check = (favourites.includes(productId))}
		else fav_check = false

		if(localStorage.basket){
			basket = getMap(JSON.parse(localStorage.basket))
			basket_check = (basket.has(productId))
		} 
			else basket_check = false

		let fav_name = (fav_check)? "Удалить из избранного" : "Добавить в избранное"
		let basket_name = (basket_check)?"Удалить из корзины" : "Добавить в корзину"

		let css_fav = (fav_check)? "btn btn-outline-danger mr-2":"btn btn-outline-primary mr-2"
		let css_basket = (basket_check)? "btn btn-danger":"btn btn-primary"


        const [data, setData] = useState({})

        useEffect(()=> {
            axios.get('http://localhost:3001/products')
            .then(res=>{
                console.log(res)
                let product=res.data.find(elem=> elem.id == productId)
                setData(product)}
            )
            .catch(err=>console.log(err))
        },[productId])

        return(
			<main>
                <Header Main="" Catalog="" Favourite="" Basket="" About="active" Order=""/>
                <div class="container mt-5">
                    <div class="row ">
                        <div class="col-md-6 ">
                            <img src={data.image} alt="Изображение товара" class="img-fluid mb-3"/>
                            <h2>{data.name}</h2>
                            <div class="mb-3">
                                <p><strong>Белки:</strong> {data.squirrels} г</p>
                                <p><strong>Жиры:</strong> {data.fats} г</p>
                                <p><strong>Углеводы:</strong> {data.сarbohydrates} г</p>
                                <p><strong>Калорийность:</strong> {data.сalorieСontent} ккал</p>
                            </div>
                            <p><strong>Состав:</strong> {data.сomposition}</p>
                            <p><strong>Прочая информация:</strong> {data.info}</p>
                        </div>
                        <div class="col-md-6">
                            <div class="mb-3">
                                <h4>Описание товара</h4>
                                <p>{data.description}</p>
                                <h4>Цена: {data.price} руб</h4>
                            </div>

                            <div class="text-center mb-3">
                                <a class={css_fav} onClick={() => appendToFavourites(productId)}>{fav_name}</a>
                                <a class={css_basket} onClick={() => appendToBasket(productId)}>{basket_name}</a>
                            </div>
                        </div>
                    </div>
                </div>

                <Footer/>
            </main>
        )
    }


export default About;